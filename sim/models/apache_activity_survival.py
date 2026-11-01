"""Team-scale activity and survival on the Apache Incubator dataset: does the DISTRIBUTION of activity
across members predict graduation better than its mean, what changes with size n, and is there a
measurable analogue of a threshold cascade or of escalation (early-warning signals) in the series?

    cd sim
    ~/.local/bin/uv run python -m models.apache_activity_survival fetch    # once: ~1.2 GB, checks md5, git-ignored
    ~/.local/bin/uv run python -m models.apache_activity_survival build    # once: streams ~12 GB of CSV, about 2 minutes
    ~/.local/bin/uv run python -m models.apache_activity_survival report   # writes results/apache_activity_survival.md

Prior work and ledger.  docs/prior-work/117-modern-signed-and-split-datasets.md section 4.3 (the dataset,
counts, terms: L4623-L4633; the group-size counts L4626-L4627; labels L4628-L4632); models/02-our-claims.md
Claim 1 (a group's drive state is a distribution, not a mean; L1225 Granovetter's two crowds, L1831 the
threshold map); models/00-v0.md section 7 "Team" (a coupling term D2 goes if it adds no predictive gain
over individual dynamics D1 for who leaves) and section 8 item 5 (no guidance on sample size); the
early-warning side is docs/prior-work/27-measuring-drive-dynamics.md section I and
30-ecological-stability-resilience.md F3 (critical slowing down: Scheffer et al. 2009, van de Leemput et
al. 2014, Helmich et al. 2023: low specificity at the individual level).  The group-size ledger lines the
size question touches are L5779 (the return to a contribution decides the sign of the group-size effect)
and L5740 (community stability depends on turnover and size).  Ledger ids are grep-able in
docs/ledger.jsonl.

What this is.  A proxy test, never a refutation of the section 7 certificate (117 section 5.3): the
dataset records no anchoring w_i, no enemy weight E_i, no tie signs; its outcome is dissolution
(retired) against a success exit (graduated), not a split (L4632).  What it can measure is how
members' activity is distributed, how it moves in time, and how both relate to the outcome.

Privacy.  The raw files carry names and email addresses (L4623).  They are read once, as a stream, and
reduced to integer, project-local pseudonyms (a one-way hash with a per-build random salt that is
never stored, then a relabelling by first appearance).  Only counts per pseudonym per month leave
the build; no name, address or message text is kept anywhere, and nothing written to results/ names a
person.  The data directory is git-ignored (sim/data/README.md).

Conventions.  Month 0 is the calendar month in which the podling entered the Incubator (its
startdate in the ASF's own podlings.xml); a window [0, W) is the first W calendar months from it.
An "event" is a distinct commit (the commit file has one row per file touched; rows are grouped by
revision) or a message on a human list (every list except the automated ones, HUMAN_LIST_RULE) sent by
a pseudonym not flagged as a robot.  A "regular member" is a pseudonym with at least one event in at
least ceil(W/4) of the window's months (3 of 12; at least 2): a team is a window choice (117 section 5.2),
and "any event" counts a crowd (median 56 members at W = 12), not a team.  The outcome is graduated (1) or
retired (0) from podlings.xml; a landmark analysis at W keeps the podlings still incubating then (exit
month >= W), so that no feature can contain the exit.

What was fixed in advance, what changed after a first look, and every decision rule are written out
in results/apache_activity_survival.md (section 2); PRIMARY below holds the numbers.
"""

from __future__ import annotations

import argparse
import csv
import datetime
import hashlib
import io
import json
import math
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np

SIM = Path(__file__).resolve().parents[1]
DATA_DIR = SIM / "data" / "apache-incubator"
DERIVED = DATA_DIR / "derived"
RESULTS = SIM / "results" / "apache_activity_survival.md"
SEED = 20261101

# ------------------------------------------------------------------ the sources and their terms

ZENODO_RECORD = "https://zenodo.org/api/records/5637530"
FILES = {
    "commits_2021_update.zip": {
        "bytes": 156_231_855,
        "md5": "952ec9c66f1c2a96ddf3deab2e78f9e9",
        "sha256": "143dab8e9ef184b62b505615906578022118665b0f6dc9d7de36cc5df021ce8c",
        "member": "commits_full.csv",
    },
    "emails_2021_update.zip": {
        "bytes": 1_041_656_466,
        "md5": "ac716c35e7f160178e83ea9ae40fd4be",
        "sha256": "3be525e64893256bfab8128bc889c5e9829de1e1cfe16ef7602b6457dfc7b5fb",
        "member": "emails_full.csv",
    },
}
PODLINGS_URL = "https://incubator.apache.org/podlings.xml"
PODLINGS_FILE = "podlings.xml"
# Dataset project names that are a podling under a longer name in podlings.xml (checked by hand against the file:
# Empire-db and OpenOffice.org are podlings; the other unmatched names are not).
NAME_ALIASES = {"empire": "empire-db", "openoffice": "openofficeorg"}
# Counts 117 section 4.3 made from the same files (L4624, L4625); the build must reproduce them.
COUNTS_117 = {"commit_rows": 12_608_575, "commit_projects": 265, "email_rows": 2_161_558, "email_projects": 274}
USER_AGENT = "social-algebra-research/0.1"  # no identity beyond this string is ever sent

DATA_END = datetime.date(2021, 7, 31)  # last date in both files (L4624, L4625)
COMMITS_FIRST = datetime.date(2005, 1, 30)  # first date in the commit file (L4624): earlier podlings' first months have no commits
EMAILS_FIRST = datetime.date(2003, 4, 1)  # first date in the mail file (L4625)
VALID_FIRST = datetime.date(2002, 1, 1)  # headers carry wild dates; anything outside is dropped
EPOCH = datetime.date(1970, 1, 1)

# Mailing lists (pre-specified from the inventory of list names, before any outcome was looked at).  The
# automated lists carry machine-generated commit mail (flagged from_commit, L4625) and tracker, review and
# build traffic whose From address is nearly always a robot.  Every other list counts as human; the
# development list ("dev", "dev-xx", "xx-dev") is the subset used by the dev_messages measure.
HUMAN_LIST_RULE = (
    "every list except commits, issues, notifications, reviews, codereview, scm, cvs, svn, builds, agent "
    "and lists ending -commits, -issues, -notifications, -reviews, -builds"
)
_AUTOMATED_LIST = re.compile(
    r"^(commits|issues|notifications|reviews|codereview|scm|cvs|svn|builds|agent)$|[-._](commits|issues|notifications|reviews|builds)$"
)
_DEV_LIST = re.compile(r"^dev(-[a-z0-9]+)?$|[-._]dev$")
# Automated senders (pre-specified).  A pseudonym is flagged when the local part of its address or the
# display name that came with it matches a robot pattern; only the boolean is kept, never the text.  The
# display-name patterns are specific (JIRA's "Name (JIRA)", GitHub and GitBox relays, CI servers) because a
# generic word such as "Jenkins" or "Hudson" is also a surname.
_BOT_LOCAL_EXACT = re.compile(
    r"^(jenkins|hudson|jira|git|gitbox|asfgit|svn|noreply|no-reply|donotreply|do-not-reply|notifications?|commits?|"
    r"issues|builds?|ci|travis|bugzilla|bugs|gerrit|phabricator|reviewboard|reviews?|wikidiffs?|confluence|hadoopqa|"
    r"dev-help|actions?|nobody|root|www-data)$",
    re.I,
)
_BOT_LOCAL_TOKEN = re.compile(r"(^|[-._+0-9])(bot|buildbot|dependabot|git-wip|noreply|no-reply|renovate|snyk|sonar|codecov)([-._+0-9]|$)", re.I)
_BOT_NAME = re.compile(
    r"\(JIRA\)|\bJIRA\b|\bGitHub\b|\bGitBox\b|\basfgit\b|\bASF (subversion|git|infra)|\bApache (Jenkins|Hudson|Wiki|Git|Subversion|Gump)\b|"
    r"\bHadoop QA\b|\bbuild ?(bot|server)\b|\bReview ?Board\b|\bBugzilla\b|\bGerrit\b|\bPhabricator\b|\bTravis\b|"
    r"\bSonar|\bConfluence\b|\bwiki\b|\bbot\b|\bnotifications?\b|\bcommits?\b",
    re.I,
)
# Behavioural rule for relays that evade both patterns (applied per project when the panel is built):
# a pseudonym with at least RELAY_MIN human-list messages of which at least RELAY_REPLY are replies.
RELAY_MIN = 3000
RELAY_REPLY = 0.98


def is_bot_local(addr: str) -> bool:
    local = addr.split("@", 1)[0]
    return bool(_BOT_LOCAL_EXACT.search(local) or _BOT_LOCAL_TOKEN.search(local))


def is_bot(addr: str, name: str = "") -> bool:
    return is_bot_local(addr) or bool(name and _BOT_NAME.search(name))


def is_human_list(name: str) -> bool:
    return not _AUTOMATED_LIST.search(name.lower())


# ------------------------------------------------------------------ fetch

def _md5_of(path: Path, chunk: int = 1 << 22) -> str:
    h = hashlib.md5()
    with open(path, "rb") as f:
        while b := f.read(chunk):
            h.update(b)
    return h.hexdigest()


def _sha256_of(path: Path, chunk: int = 1 << 22) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while b := f.read(chunk):
            h.update(b)
    return h.hexdigest()


def _download(url: str, dest: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as out:  # noqa: S310 (fixed https URLs)
        while b := r.read(1 << 20):
            out.write(b)


def fetch() -> None:
    """Download the two Zenodo zips (CC BY 4.0) and the ASF's podlings.xml (Apache-2.0) into the
    git-ignored data directory.  The zips are checked against Zenodo's md5 and the sizes in 117; nothing
    is extracted to disk (the build streams from the archive)."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    for name, meta in FILES.items():
        dest = DATA_DIR / name
        if dest.exists() and dest.stat().st_size == meta["bytes"] and _md5_of(dest) == meta["md5"]:
            print(f"ok (already here): {name}")
            continue
        print(f"downloading {name} ({meta['bytes']:,} bytes) ...", flush=True)
        _download(f"{ZENODO_RECORD}/files/{name}/content", dest)
        got = _md5_of(dest)
        if got != meta["md5"]:
            dest.unlink()
            raise SystemExit(f"md5 mismatch for {name}: {got} != {meta['md5']}; file removed")
        print(f"ok: {name} md5 {got} sha256 {_sha256_of(dest)}")
    pod = DATA_DIR / PODLINGS_FILE
    if not pod.exists():
        print("downloading podlings.xml (ASF Incubator status file; Apache-2.0) ...", flush=True)
        _download(PODLINGS_URL, pod)
    print(f"ok: {PODLINGS_FILE} sha256 {_sha256_of(pod)} ({pod.stat().st_size:,} bytes; the live file changes)")


# ------------------------------------------------------------------ labels: the ASF's own status file

def _ym(d: datetime.date) -> int:
    return d.year * 12 + d.month - 1


def load_podlings(path: Path | None = None) -> list[dict]:
    """Parse podlings.xml into names (name, resource, aliases), status, start, end.  Only these attributes
    are read, as sim/data/README.md records; the mentors, sponsors and free-text descriptions in the file
    are never touched."""
    root = ET.parse(path or (DATA_DIR / PODLINGS_FILE)).getroot()
    out = []
    for p in root:
        s, e = p.get("startdate"), p.get("enddate")
        names = {p.get("resource") or p.get("name", "").lower()}
        for alias in (p.get("resourceAliases") or "").replace(",", " ").split():
            names.add(alias.lower())
        names = {n.lower() for n in names if n}
        out.append(
            {
                "name": (p.get("name") or "").lower(),
                "keys": sorted(names | {(p.get("name") or "").lower()}),
                "status": p.get("status"),
                "start": datetime.date.fromisoformat(s) if s else None,
                "end": datetime.date.fromisoformat(e) if e else None,
            }
        )
    return out


# ------------------------------------------------------------------ build: stream the CSVs

_day_cache: dict[str, int] = {}


def _day(s: str) -> int:
    """'YYYY-MM-DD hh:mm:ss' -> days since 1970-01-01, or -1 for an unusable date."""
    d10 = s[:10]
    v = _day_cache.get(d10)
    if v is None:
        try:
            dt = datetime.date(int(d10[:4]), int(d10[5:7]), int(d10[8:10]))
            v = (dt - EPOCH).days if VALID_FIRST <= dt <= DATA_END + datetime.timedelta(days=31) else -1
        except ValueError:
            v = -1
        _day_cache[d10] = v
    return v


def _norm_email(s: str) -> str:
    s = s.strip().lower().strip("<>\"' ")
    if "@" in s:
        local, _, dom = s.partition("@")
        s = local.split("+", 1)[0] + "@" + dom
    return s


class _Pseudonymiser:
    """address -> 64-bit one-way hash under a per-build random salt (never stored)."""

    def __init__(self, salt: bytes):
        self.salt = salt
        self.cache: dict[str, int] = {}

    def __call__(self, email: str) -> int:
        h = self.cache.get(email)
        if h is None:
            h = int.from_bytes(hashlib.blake2b(email.encode("utf-8", "replace"), key=self.salt, digest_size=8).digest(), "little")
            self.cache[email] = h
        return h


def _open_csv(zip_path: Path, member: str):
    csv.field_size_limit(1 << 30)
    z = zipfile.ZipFile(zip_path)
    f = io.TextIOWrapper(z.open(member), encoding="utf-8", errors="replace", newline="")
    return z, csv.reader(f)


def _ingest_commits(salt: bytes, limit: int | None = None) -> dict:
    """One record per distinct (project, revision).  Person = author address if present, else the
    sender address (117 section 4.3)."""
    ps = _Pseudonymiser(salt)
    z, rd = _open_csv(DATA_DIR / "commits_2021_update.zip", FILES["commits_2021_update.zip"]["member"])
    hdr = next(rd)
    ix = {k: hdr.index(k) for k in ("project_name", "date", "sender_email", "author_email", "sender_name", "author_name", "loc",
                                    "ref_or_sha", "message_id", "commit_type")}
    projects: dict[str, int] = {}
    key_to_row: dict[tuple, int] = {}
    proj, day, person, nfiles, loc, svn, authk, bot = [], [], [], [], [], [], [], []
    rows = unknown_person = bad_date = malformed = 0
    nh = len(hdr)
    for rows, row in enumerate(rd, 1):
        if limit and rows > limit:
            rows -= 1
            break
        if len(row) < nh:
            malformed += 1
            continue
        p = projects.setdefault(row[ix["project_name"]], len(projects))
        rev = row[ix["ref_or_sha"]] or row[ix["message_id"]]
        k = (p, rev)
        j = key_to_row.get(k)
        try:
            l = int(float(row[ix["loc"]]))
        except ValueError:
            l = 0
        if j is not None:
            nfiles[j] += 1
            loc[j] += l
            continue
        d = _day(row[ix["date"]])
        a = _norm_email(row[ix["author_email"]])
        has_author = bool(a)
        nm = row[ix["author_name"]] if a else ""
        if not a:
            a = _norm_email(row[ix["sender_email"]])
            nm = row[ix["sender_name"]]
        if not a or d < 0:
            unknown_person += not a
            bad_date += d < 0
            continue
        key_to_row[k] = len(proj)
        proj.append(p); day.append(d); person.append(ps(a)); nfiles.append(1); loc.append(l)
        svn.append(row[ix["commit_type"]] == "svn"); authk.append(has_author); bot.append(is_bot(a, nm))
    z.close()
    return {
        "projects": list(projects),
        "proj": np.array(proj, np.int16), "day": np.array(day, np.int32), "person": np.array(person, np.uint64),
        "nfiles": np.array(nfiles, np.int32), "loc": np.array(loc, np.int64), "svn": np.array(svn, bool),
        "authk": np.array(authk, bool), "bot": np.array(bot, bool),
        "rows": rows, "unknown_person": unknown_person, "bad_date": bad_date, "malformed": malformed,
    }


def _ingest_emails(salt: bytes, limit: int | None = None) -> dict:
    ps = _Pseudonymiser(salt)
    z, rd = _open_csv(DATA_DIR / "emails_2021_update.zip", FILES["emails_2021_update.zip"]["member"])
    hdr = next(rd)
    ix = {k: hdr.index(k) for k in ("project_name", "list_name", "date", "message_id", "sender_email", "sender_name", "in_reply_to", "body",
                                    "from_commit")}
    projects: dict[str, int] = {}
    lists: dict[str, int] = {}
    list_counts: Counter = Counter()
    proj, day, person, lst, fromc, bot, blen = [], [], [], [], [], [], []
    mid, par = [], []
    rows = unknown_person = bad_date = malformed = 0
    nh = len(hdr)
    h8 = lambda s: int.from_bytes(hashlib.blake2b(s.encode("utf-8", "replace"), digest_size=8).digest(), "little")  # noqa: E731
    for rows, row in enumerate(rd, 1):
        if limit and rows > limit:
            rows -= 1
            break
        if len(row) < nh:
            malformed += 1
            continue
        p = projects.setdefault(row[ix["project_name"]], len(projects))
        ln = row[ix["list_name"]]
        li = lists.setdefault(ln, len(lists))
        list_counts[ln] += 1
        d = _day(row[ix["date"]])
        a = _norm_email(row[ix["sender_email"]])
        if not a or d < 0:
            unknown_person += not a
            bad_date += d < 0
            continue
        proj.append(p); day.append(d); person.append(ps(a)); lst.append(li)
        fromc.append(row[ix["from_commit"]] == "True"); bot.append(is_bot(a, row[ix["sender_name"]])); blen.append(len(row[ix["body"]]))
        mid.append(h8(row[ix["message_id"]].strip()) if row[ix["message_id"]] else 0)
        r = row[ix["in_reply_to"]].strip()
        par.append(h8(r) if r else 0)
    z.close()
    return {
        "projects": list(projects), "lists": list(lists), "list_counts": dict(list_counts),
        "proj": np.array(proj, np.int16), "day": np.array(day, np.int32), "person": np.array(person, np.uint64),
        "lst": np.array(lst, np.int16), "fromc": np.array(fromc, bool), "bot": np.array(bot, bool),
        "blen": np.array(blen, np.int32), "mid": np.array(mid, np.uint64), "par": np.array(par, np.uint64),
        "rows": rows, "unknown_person": unknown_person, "bad_date": bad_date, "malformed": malformed,
    }


def build(limit: int | None = None, workers: int = 2) -> None:
    """Stream both CSVs (in parallel), reduce to pseudonymised numeric arrays, write derived/*.npz and
    derived/meta.json.  Checks the row and project counts against 117's (L4624, L4625) unless `limit`
    is given (a smoke test)."""
    for name in FILES:
        if not (DATA_DIR / name).exists():
            raise SystemExit(f"{name} is absent: run `fetch` first")
    DERIVED.mkdir(parents=True, exist_ok=True)
    salt = os.urandom(16)
    with ProcessPoolExecutor(max_workers=workers) as ex:
        fc = ex.submit(_ingest_commits, salt, limit)
        fe = ex.submit(_ingest_emails, salt, limit)
        C, E = fc.result(), fe.result()
    # one project index for both files
    names = sorted(set(C["projects"]) | set(E["projects"]))
    pid = {n: i for i, n in enumerate(names)}
    cmap = np.array([pid[n] for n in C["projects"]], np.int16)
    emap = np.array([pid[n] for n in E["projects"]], np.int16)
    C["proj"] = cmap[C["proj"]]
    E["proj"] = emap[E["proj"]]
    (c_person, e_person), p_proj, p_local, p_bot = _relabel_two(C, E)
    np.savez_compressed(
        DERIVED / "commits.npz", proj=C["proj"], day=C["day"], person=c_person, nfiles=C["nfiles"], loc=C["loc"],
        svn=C["svn"], authk=C["authk"],
    )
    # reply parents: index of the parent message within the same file, or -1
    mid, par = E["mid"], E["par"]
    order = np.argsort(mid, kind="stable")
    ms = mid[order]
    pos = np.searchsorted(ms, par)
    pos[pos >= len(ms)] = 0
    found = (par != 0) & (ms[pos] == par)
    parent = np.where(found, order[pos], -1).astype(np.int32)
    parent[parent == np.arange(len(parent))] = -1
    np.savez_compressed(
        DERIVED / "emails.npz", proj=E["proj"], day=E["day"], person=e_person, lst=E["lst"], fromc=E["fromc"],
        blen=E["blen"], parent=parent, has_in_reply_to=(par != 0),
    )
    np.savez_compressed(DERIVED / "persons.npz", proj=p_proj, local=p_local, bot=p_bot)
    meta = {
        "built": datetime.date.today().isoformat(),
        "projects": names,
        "lists": E["lists"],
        "list_counts": E["list_counts"],
        "commit_rows": C["rows"], "commit_commits": int(len(C["proj"])),
        "commit_projects": len(set(C["projects"])), "commit_unknown_person": C["unknown_person"], "commit_bad_date": C["bad_date"], "commit_malformed": C["malformed"],
        "email_rows": E["rows"], "email_kept": int(len(E["proj"])),
        "email_projects": len(set(E["projects"])), "email_unknown_person": E["unknown_person"], "email_bad_date": E["bad_date"], "email_malformed": E["malformed"],
        "limit": limit,
        "human_list_rule": HUMAN_LIST_RULE,
    }
    (DERIVED / "meta.json").write_text(json.dumps(meta, indent=1))
    print(json.dumps({k: v for k, v in meta.items() if k not in ("projects", "lists", "list_counts")}, indent=1))
    if not limit:
        for k, exp in COUNTS_117.items():
            got = {"commit_rows": meta["commit_rows"] - meta["commit_malformed"], "commit_projects": meta["commit_projects"],
                   "email_rows": meta["email_rows"] - meta["email_malformed"], "email_projects": meta["email_projects"]}[k]
            print(f"  {k}: {got:,} (117: {exp:,}) {'OK' if got == exp else 'DIFFERS'}")


def _relabel_two(C: dict, E: dict):
    """Relabel both files' person hashes together (so the same address in the commit and the mail file
    gets the same local integer), and return the person table (project, local id, bot flag)."""
    P = np.concatenate([C["proj"], E["proj"]]).astype(np.int64)
    H = np.concatenate([C["person"], E["person"]])
    D = np.concatenate([C["day"], E["day"]]).astype(np.int64)
    B = np.concatenate([C["bot"], E["bot"]])
    order = np.lexsort((H, P))
    P1, H1, D1, B1 = P[order], H[order], D[order], B[order]
    newkey = np.ones(len(P1), bool)
    newkey[1:] = (P1[1:] != P1[:-1]) | (H1[1:] != H1[:-1])
    kid = np.cumsum(newkey) - 1
    nk = int(kid[-1]) + 1
    first_day = np.full(nk, np.iinfo(np.int64).max)
    np.minimum.at(first_day, kid, D1)
    bot_any = np.zeros(nk, bool)
    np.logical_or.at(bot_any, kid, B1)
    kp, kh = P1[newkey], H1[newkey]
    o2 = np.lexsort((kh, first_day, kp))
    kp2 = kp[o2]
    starts = np.r_[0, np.flatnonzero(kp2[1:] != kp2[:-1]) + 1]
    grp_start = np.repeat(starts, np.diff(np.r_[starts, nk]))
    local = np.empty(nk, np.int64)
    local[o2] = np.arange(nk) - grp_start
    row_local_sorted = local[kid]
    row_local = np.empty(len(P1), np.int64)
    row_local[order] = row_local_sorted
    nc = len(C["proj"])
    # person table in (project, local) order
    p_proj = kp[o2].astype(np.int16)
    p_local = local[o2].astype(np.int32)
    p_bot = bot_any[o2]
    return (row_local[:nc].astype(np.int32), row_local[nc:].astype(np.int32)), p_proj, p_local, p_bot


# ------------------------------------------------------------------ pure statistics (no data needed)

def gini(x) -> float:
    """Sample Gini coefficient of non-negative values: 0 = equal, (n-1)/n = one holds everything."""
    a = np.sort(np.asarray(x, float))
    n, s = len(a), a.sum()
    if n == 0 or s <= 0:
        return float("nan")
    return float(2.0 * (np.arange(1, n + 1) * a).sum() / (n * s) - (n + 1) / n)


def gini_corrected(x) -> float:
    """Gini rescaled by n/(n-1) so that 'one member holds everything' is 1 whatever n.  Needs n >= 2."""
    n = len(x)
    g = gini(x)
    return float(g * n / (n - 1)) if n >= 2 else float("nan")


def top_share(x, k: int) -> float:
    a = np.sort(np.asarray(x, float))[::-1]
    s = a.sum()
    return float(a[:k].sum() / s) if s > 0 else float("nan")


def norm_entropy(x) -> float:
    """Shannon entropy of the shares divided by ln n (1 = equal shares).  Needs n >= 2."""
    a = np.asarray(x, float)
    a = a[a > 0]
    n = len(a)
    if n < 2:
        return float("nan")
    p = a / a.sum()
    return float(-(p * np.log(p)).sum() / math.log(n))


def eff_number(x) -> float:
    """Effective number of contributors, exp(entropy): n if all equal, 1 if one holds everything."""
    a = np.asarray(x, float)
    a = a[a > 0]
    if len(a) == 0:
        return float("nan")
    p = a / a.sum()
    return float(math.exp(-(p * np.log(p)).sum()))


def theil(x) -> float:
    a = np.asarray(x, float)
    a = a[a > 0]
    if len(a) == 0:
        return float("nan")
    r = a / a.mean()
    return float((r * np.log(r)).mean())


def cv(x) -> float:
    a = np.asarray(x, float)
    return float(a.std(ddof=1) / a.mean()) if len(a) >= 2 and a.mean() > 0 else float("nan")


def shape_features(a) -> dict:
    """The shape block of the pre-specified model plus the extra measures used in the variations.
    `a` = per-member totals in the window (all >= 1)."""
    a = np.asarray(a, float)
    n, T = len(a), float(a.sum())
    return {
        "n": n, "T": T, "mean": T / n if n else float("nan"),
        "gini": gini_corrected(a), "top1": top_share(a, 1), "top3": top_share(a, 3),
        "entropy": norm_entropy(a), "effn": eff_number(a), "theil": theil(a), "cv": cv(a),
        "single": float((a == 1).mean()) if n else float("nan"),
    }


def exchangeable_gini(n: int, T: int, rng: np.random.Generator, draws: int = 2000) -> tuple[float, float]:
    """Mean and sd of the corrected Gini if T events were spread over n members by chance: every member
    gets one (so each is a member), the other T - n fall on members uniformly at random.  This is the
    'members are interchangeable' null; its Gini is not 0 because counts are lumpy."""
    if n < 2 or T < n:
        return float("nan"), float("nan")
    extra = rng.multinomial(T - n, np.full(n, 1.0 / n), size=draws) + 1
    g = np.array([gini_corrected(r) for r in extra])
    return float(g.mean()), float(g.std())


def auc_score(y, s) -> float:
    """P(score of a random positive > score of a random negative), ties one half (Mann-Whitney)."""
    from scipy.stats import rankdata

    y = np.asarray(y).astype(bool)
    n1, n0 = int(y.sum()), int((~y).sum())
    if n1 == 0 or n0 == 0:
        return float("nan")
    r = rankdata(s)
    return float((r[y].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def logit_fit(X: np.ndarray, y: np.ndarray, l2: float = 1.0, iters: int = 60) -> np.ndarray:
    """Ridge logistic regression by Newton steps; the intercept is not penalised.  X is used as given."""
    n, k = X.shape
    Xb = np.c_[np.ones(n), X]
    beta = np.zeros(k + 1)
    pen = np.eye(k + 1) * l2
    pen[0, 0] = 0.0
    for _ in range(iters):
        mu = 1.0 / (1.0 + np.exp(-np.clip(Xb @ beta, -30, 30)))
        g = Xb.T @ (mu - y) + pen @ beta
        H = (Xb * (mu * (1 - mu))[:, None]).T @ Xb + pen + 1e-9 * np.eye(k + 1)
        step = np.linalg.solve(H, g)
        beta -= step
        if np.max(np.abs(step)) < 1e-9:
            break
    return beta


def logit_predict(beta: np.ndarray, X: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(np.c_[np.ones(len(X)), X] @ beta, -30, 30)))


def _standardise(Xtr: np.ndarray, Xte: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    mu, sd = Xtr.mean(0), Xtr.std(0)
    sd = np.where(sd > 1e-12, sd, 1.0)
    return (Xtr - mu) / sd, (Xte - mu) / sd


def fold_ids(y: np.ndarray, k: int, rng: np.random.Generator, groups: np.ndarray | None = None) -> np.ndarray:
    """Stratified fold assignment (by y).  With `groups`, every group goes to one fold (the project)."""
    n = len(y)
    f = np.empty(n, int)
    if groups is None:
        for cls in (0, 1):
            idx = np.flatnonzero(y == cls)
            rng.shuffle(idx)
            f[idx] = np.arange(len(idx)) % k
        return f
    ug, inv = np.unique(groups, return_inverse=True)
    gy = np.zeros(len(ug))
    np.maximum.at(gy, inv, y)  # a group with any positive row counts as positive, for stratification
    gf = np.empty(len(ug), int)
    for cls in (0, 1):
        idx = np.flatnonzero(gy == cls)
        rng.shuffle(idx)
        gf[idx] = np.arange(len(idx)) % k
    return gf[inv]


def cv_oof(X: np.ndarray, y: np.ndarray, *, folds: int = 5, repeats: int = 20, l2: float = 1.0,
           seed: int = 0, groups: np.ndarray | None = None) -> np.ndarray:
    """Out-of-fold predicted probabilities, averaged over `repeats` random fold assignments.  Features
    are standardised on the training part of each fold."""
    X = np.asarray(X, float)
    if X.ndim == 1:
        X = X[:, None]
    y = np.asarray(y, float)
    acc = np.zeros(len(y))
    for r in range(repeats):
        rng = np.random.default_rng([seed, r])
        f = fold_ids(y, folds, rng, groups)
        for k in range(folds):
            te = f == k
            tr = ~te
            if te.sum() == 0 or len(np.unique(y[tr])) < 2:
                acc[te] += y[tr].mean() if tr.sum() else 0.5
                continue
            Xtr, Xte = _standardise(X[tr], X[te])
            acc[te] += logit_predict(logit_fit(Xtr, y[tr], l2), Xte)
    return acc / repeats


def cv_auc(X, y, **kw) -> float:
    return auc_score(y, cv_oof(X, y, **kw))


def logloss(y, p) -> float:
    p = np.clip(np.asarray(p, float), 1e-6, 1 - 1e-6)
    y = np.asarray(y, float)
    return float(-(y * np.log(p) + (1 - y) * np.log(1 - p)).mean())


def boot_auc(y, s, rng: np.random.Generator, B: int = 2000) -> tuple[float, float]:
    """95% percentile interval of the AUC of fixed scores, resampling positives and negatives separately."""
    y = np.asarray(y).astype(bool)
    pos, neg = np.flatnonzero(y), np.flatnonzero(~y)
    out = np.empty(B)
    for b in range(B):
        ix = np.r_[rng.choice(pos, len(pos)), rng.choice(neg, len(neg))]
        out[b] = auc_score(y[ix], np.asarray(s)[ix])
    return float(np.quantile(out, 0.025)), float(np.quantile(out, 0.975))


def boot_auc_diff(y, sa, sb, rng: np.random.Generator, B: int = 2000) -> tuple[float, float, float]:
    """Paired bootstrap of AUC(sa) - AUC(sb) on the same resampled units: (low, high, share of resamples > 0)."""
    y = np.asarray(y).astype(bool)
    sa, sb = np.asarray(sa), np.asarray(sb)
    pos, neg = np.flatnonzero(y), np.flatnonzero(~y)
    d = np.empty(B)
    for b in range(B):
        ix = np.r_[rng.choice(pos, len(pos)), rng.choice(neg, len(neg))]
        d[b] = auc_score(y[ix], sa[ix]) - auc_score(y[ix], sb[ix])
    return float(np.quantile(d, 0.025)), float(np.quantile(d, 0.975)), float((d > 0).mean())


def lr_test(Xbase: np.ndarray, Xfull: np.ndarray, y: np.ndarray) -> tuple[float, float, int]:
    """Likelihood-ratio test of nested logistic models (almost unpenalised): (statistic, p, df)."""
    from scipy.stats import chi2

    def dev(X):
        Z, _ = _standardise(X, X)
        b = logit_fit(Z, y, l2=1e-6)
        p = np.clip(logit_predict(b, Z), 1e-12, 1 - 1e-12)
        return -2.0 * float((y * np.log(p) + (1 - y) * np.log(1 - p)).sum())

    df = Xfull.shape[1] - Xbase.shape[1]
    stat = max(dev(Xbase) - dev(Xfull), 0.0)
    return stat, float(chi2.sf(stat, df)), df


def perm_gain(Xbase: np.ndarray, Xshape: np.ndarray, y: np.ndarray, *, perms: int, seed: int,
              folds: int = 5, repeats: int = 10, strata: np.ndarray | None = None, l2: float = 1.0) -> tuple[float, float, np.ndarray]:
    """Does the shape block add held-out AUC to the base block?  Returns (observed gain, one-sided p,
    permuted gains).  Null: the shape rows are unrelated to the outcome given the base columns; they are
    permuted across projects (within `strata` if given), which keeps the penalty for carrying useless
    columns in the null gain."""
    base_auc = cv_auc(Xbase, y, folds=folds, repeats=repeats, seed=seed, l2=l2)
    full_auc = cv_auc(np.c_[Xbase, Xshape], y, folds=folds, repeats=repeats, seed=seed, l2=l2)
    gain = full_auc - base_auc
    rng = np.random.default_rng([seed, 777])
    null = np.empty(perms)
    for b in range(perms):
        if strata is None:
            ix = rng.permutation(len(y))
        else:
            ix = np.arange(len(y))
            for s in np.unique(strata):
                m = np.flatnonzero(strata == s)
                ix[m] = rng.permutation(m)
        null[b] = cv_auc(np.c_[Xbase, Xshape[ix]], y, folds=folds, repeats=repeats, seed=seed, l2=l2) - base_auc
    p = float((1 + (null >= gain).sum()) / (perms + 1))
    return float(gain), p, null


def size_strata(n, k: int = 5) -> np.ndarray:
    """Quantile bins of team size, for the conditional form of perm_gain's null.  The free permutation also breaks
    the shape-size correlation (top-k shares fall with n, the Gini rises with it), so its null pays more for useless
    columns than the hypothesis 'shape adds nothing GIVEN size and mean' requires; permuting within size bins keeps
    most of that correlation.  Reported beside the pre-specified free permutation, never in its place (review 2026-11-01)."""
    n = np.asarray(n, float)
    q = np.quantile(n, np.linspace(0, 1, k + 1)[1:-1])
    return np.searchsorted(q, n, side="right")


# ------------------------------------------------------------------ early-warning statistics

def kendall_time(y) -> float:
    """Kendall tau-b between time (1..m, no ties) and y, ignoring NaN entries; NaN if fewer than 4 points."""
    y = np.asarray(y, float)
    y = y[~np.isnan(y)]
    m = len(y)
    if m < 4:
        return float("nan")
    d = np.sign(y[None, :] - y[:, None])  # d[i, j] = sign(y_j - y_i)
    iu = np.triu_indices(m, 1)
    S = d[iu].sum()
    n0 = m * (m - 1) / 2
    ties = (d[iu] == 0).sum()
    den = math.sqrt(n0 * (n0 - ties))
    return float(S / den) if den > 0 else float("nan")


def rolling_indicators(x, w: int, detrend: str = "linear") -> tuple[np.ndarray, np.ndarray]:
    """Lag-1 autocorrelation and standard deviation of the detrended series in each window of w points
    (window ending at e; NaN for e < w - 1 or a flat window).  detrend = 'linear' removes a straight line
    inside the window, the choice the slowing-down literature uses to keep a drifting mean from
    masquerading as memory (Dakos et al. 2012; 027 section I; L0512); 'mean' removes only the window mean."""
    x = np.asarray(x, float)
    E = len(x)
    ar1 = np.full(E, np.nan)
    sd = np.full(E, np.nan)
    if E < w or w < 4:
        return ar1, sd
    if detrend == "linear":
        A = np.c_[np.ones(w), np.arange(w, dtype=float)]
        df = w - 2
    else:
        A = np.ones((w, 1))
        df = w - 1
    M = np.eye(w) - A @ np.linalg.pinv(A)  # residual maker
    win = np.lib.stride_tricks.sliding_window_view(x, w)  # (E - w + 1, w)
    R = win @ M.T
    ss = (R**2).sum(1)
    lag = (R[:, :-1] * R[:, 1:]).sum(1)
    ok = ss > 1e-9
    a = np.full(len(ss), np.nan)
    a[ok] = lag[ok] / ss[ok]
    s_ = np.full(len(ss), np.nan)
    s_[ok] = np.sqrt(ss[ok] / df)
    ar1[w - 1 :] = a
    sd[w - 1 :] = s_
    return ar1, sd


def ews_taus(x, ref: int, w: int, L: int, detrend: str = "linear") -> tuple[float, float]:
    """Kendall tau of (AR1, SD) against time over the L windows ending at months ref-L .. ref-1, for a
    series x indexed from 0.  NaN if the series is too short (needs ref >= L + w - 1)."""
    if ref < L + w - 1 or ref > len(x):
        return float("nan"), float("nan")
    ar1, sd = rolling_indicators(np.asarray(x, float)[:ref], w, detrend)
    return kendall_time(ar1[ref - L : ref]), kendall_time(sd[ref - L : ref])


# ------------------------------------------------------------------ the panel: labels and monthly matrices

def ym_of_day(day) -> np.ndarray:
    """Days since 1970-01-01 -> calendar-month index (year * 12 + month - 1)."""
    return np.asarray(day).astype("datetime64[D]").astype("datetime64[M]").astype(np.int64) + 1970 * 12


def list_class(name: str) -> int:
    """0 automated (commit mail, tracker and review robots), 1 development list, 2 everything else human."""
    n = name.lower()
    if _AUTOMATED_LIST.search(n):
        return 0
    return 1 if _DEV_LIST.search(n) else 2


MEASURES = {
    # name: components (matrix names); `events` is the pre-specified combined measure
    "events": ("commits", "msg_human"),
    "commits": ("commits",),
    "files": ("files",),
    "loc": ("loc",),
    "messages": ("msg_human",),
    "dev_messages": ("msg_dev",),
    "all_messages": ("msg_all",),
    "events_all": ("commits", "msg_all"),
    "replies": ("reply_human",),
}


class Panel:
    """Labels from podlings.xml and, per project, dense person-by-month matrices of each activity count
    (months since the podling's start, 0 .. last month of the data).  Rows are project-local pseudonyms."""

    def __init__(self, derived: Path = DERIVED, cutoff: datetime.date = DATA_END, labels_as_of: datetime.date | None = None):
        self.cutoff = cutoff
        meta = json.loads((derived / "meta.json").read_text())
        self.meta = meta
        self.names: list[str] = meta["projects"]
        P = len(self.names)
        pods = load_podlings()
        key_to_pod: dict[str, int] = {}
        for i, pd in enumerate(pods):
            for k in pd["keys"]:
                key_to_pod.setdefault(k, i)
                key_to_pod.setdefault(re.sub(r"[^a-z0-9]", "", k), i)
        self.pod_index = np.full(P, -1)
        for p, nm in enumerate(self.names):
            key = NAME_ALIASES.get(nm.lower(), nm.lower())
            j = key_to_pod.get(key, key_to_pod.get(re.sub(r"[^a-z0-9]", "", key), -1))
            self.pod_index[p] = j
        self.matched = self.pod_index >= 0
        self.start_ym = np.full(P, -1, np.int64)
        self.end_ym = np.full(P, -1, np.int64)
        self.status = np.array(["unmatched"] * P, dtype=object)
        self.label = np.full(P, -1)  # 1 graduated, 0 retired, -1 not resolved by the cutoff
        asof = labels_as_of or cutoff
        for p in np.flatnonzero(self.matched):
            pd = pods[self.pod_index[p]]
            self.start_ym[p] = _ym(pd["start"])
            if pd["end"] is not None:
                self.end_ym[p] = _ym(pd["end"])
            self.status[p] = pd["status"]
            if pd["status"] in ("graduated", "retired") and pd["end"] is not None and pd["end"] <= asof:
                self.label[p] = 1 if pd["status"] == "graduated" else 0
        last_ym = _ym(DATA_END)
        self.n_months = np.where(self.matched, last_ym - self.start_ym + 1, 0)  # months 0 .. n_months-1 observed
        self.exit_m = np.where(self.label >= 0, self.end_ym - self.start_ym, 10**6)
        # persons
        pz = np.load(derived / "persons.npz")
        self.n_persons = np.bincount(pz["proj"].astype(np.int64), minlength=P)
        self.bot = [np.zeros(self.n_persons[p], bool) for p in range(P)]
        for pr, lo, b in zip(pz["proj"], pz["local"], pz["bot"]):
            self.bot[pr][lo] = b
        # matrices
        sizes = self.n_persons * self.n_months
        off = np.r_[0, np.cumsum(sizes)]
        self._off = off
        tot = int(off[-1])
        flat = {k: np.zeros(tot, np.float64) for k in ("commits", "files", "loc", "msg_human", "msg_dev", "msg_all", "reply_human")}
        cz = np.load(derived / "commits.npz")
        m = ym_of_day(cz["day"]) - self.start_ym[cz["proj"]]
        ok = self.matched[cz["proj"]] & (m >= 0) & (m < self.n_months[cz["proj"]])
        pr, pe, mm = cz["proj"][ok].astype(np.int64), cz["person"][ok].astype(np.int64), m[ok].astype(np.int64)
        idx = off[pr] + pe * self.n_months[pr] + mm
        flat["commits"] += np.bincount(idx, minlength=tot)
        flat["files"] += np.bincount(idx, weights=cz["nfiles"][ok], minlength=tot)
        flat["loc"] += np.bincount(idx, weights=cz["loc"][ok].astype(float), minlength=tot)
        self.commit_pre = np.bincount(cz["proj"][self.matched[cz["proj"]] & (m < 0)].astype(np.int64), minlength=P)
        ez = np.load(derived / "emails.npz")
        lc = np.array([list_class(n) for n in meta["lists"]])
        cls = lc[ez["lst"]]
        m = ym_of_day(ez["day"]) - self.start_ym[ez["proj"]]
        okm = self.matched[ez["proj"]] & (m >= 0) & (m < self.n_months[ez["proj"]]) & ~ez["fromc"]
        pr_all, pe_all, mm_all = ez["proj"].astype(np.int64), ez["person"].astype(np.int64), m.astype(np.int64)
        for name, sel in (
            ("msg_all", okm),
            ("msg_human", okm & (cls >= 1)),
            ("msg_dev", okm & (cls == 1)),
            ("reply_human", okm & (cls >= 1) & ez["has_in_reply_to"]),
        ):
            ix = off[pr_all[sel]] + pe_all[sel] * self.n_months[pr_all[sel]] + mm_all[sel]
            flat[name] += np.bincount(ix, minlength=tot)
        self._flat = flat
        self.email_pre = np.bincount(ez["proj"][self.matched[ez["proj"]] & (m < 0) & ~ez["fromc"]].astype(np.int64), minlength=P)
        self.mat: dict[str, list[np.ndarray | None]] = {}
        for k, v in flat.items():
            self.mat[k] = [
                v[off[p] : off[p + 1]].reshape(self.n_persons[p], self.n_months[p]) if self.matched[p] else None for p in range(P)
            ]
        # behavioural relay rule (see RELAY_MIN): automated mail relays that evade the address/name patterns
        self.relay_flagged = 0
        for p in np.flatnonzero(self.matched):
            tot = self.mat["msg_human"][p].sum(1)
            rep = self.mat["reply_human"][p].sum(1)
            relay = (tot >= RELAY_MIN) & (rep >= RELAY_REPLY * np.maximum(tot, 1)) & ~self.bot[p]
            self.relay_flagged += int(relay.sum())
            self.bot[p] = self.bot[p] | relay
        self._ez_parent = ez["parent"]
        self._derived = derived
        self._c = {"proj": cz["proj"], "day": cz["day"], "person": cz["person"]}
        self._e = {"proj": ez["proj"], "day": ez["day"], "person": ez["person"], "human": (cls >= 1) & ~ez["fromc"]}

    @classmethod
    def synthetic(cls, mats: dict, labels, exit_m, bots=None):
        """A panel built from hand-made person-by-month matrices (for tests): `mats` maps each matrix name
        (commits, files, loc, msg_human, msg_dev, msg_all, reply_human) to a list of arrays, one per project."""
        self = cls.__new__(cls)
        P = len(labels)
        self.names = [f"p{i}" for i in range(P)]
        self.matched = np.ones(P, bool)
        self.label = np.asarray(labels)
        self.exit_m = np.asarray(exit_m)
        self.start_ym = np.full(P, 2010 * 12)
        self.end_ym = self.start_ym + self.exit_m
        self.mat = mats
        self.n_months = np.array([mats["commits"][p].shape[1] for p in range(P)])
        self.n_persons = np.array([mats["commits"][p].shape[0] for p in range(P)])
        self.bot = bots if bots is not None else [np.zeros(n, bool) for n in self.n_persons]
        self.relay_flagged = 0
        return self

    # ---- accessors
    def resolved(self) -> np.ndarray:
        """Indices of projects matched to a podling and resolved (graduated or retired) by the cutoff."""
        return np.flatnonzero(self.matched & (self.label >= 0))

    def get(self, p: int, measure: str = "events", bots: str = "drop") -> np.ndarray:
        """Person-by-month matrix of `measure` for project p; bot rows zeroed if bots == 'drop'; if
        bots == 'top1' the single most active pseudonym of the project (by this measure) is zeroed too."""
        parts = MEASURES[measure]
        a = sum(self.mat[c][p] for c in parts)
        if bots in ("drop", "top1"):
            a = a * (~self.bot[p])[:, None]
        if bots == "top1" and a.shape[0]:
            a = a.copy()
            a[np.argmax(a.sum(1))] = 0
        return a

    def monthly_total(self, p: int, measure: str = "events", bots: str = "drop") -> np.ndarray:
        return self.get(p, measure, bots).sum(0)

    def _week0(self, p: int) -> datetime.date:
        y, m = divmod(int(self.start_ym[p]), 12)
        return datetime.date(y, m + 1, 1)

    def exit_week(self, p: int) -> int:
        """Week index (7-day bins from the first day of the start month) of the first day of the exit month."""
        y, m = divmod(int(self.end_ym[p]), 12)
        return (datetime.date(y, m + 1, 1) - self._week0(p)).days // 7

    def weekly_total(self, p: int, bots: str = "drop") -> np.ndarray:
        """Events (commits + human-list messages) per 7-day week from the first day of the start month to
        the end of the data; a finer series than the monthly matrices, for the early-warning variation."""
        s0 = (self._week0(p) - EPOCH).days
        nweeks = ((DATA_END - EPOCH).days - s0) // 7 + 1
        out = np.zeros(nweeks)
        keep = ~self.bot[p] if bots == "drop" else np.ones(self.n_persons[p], bool)
        for src in (self._c, self._e):
            m = src["proj"] == p
            if "human" in src:
                m &= src["human"]
            d, pe = src["day"][m].astype(np.int64), src["person"][m].astype(np.int64)
            ok = keep[pe] & (d >= s0)
            wk = (d[ok] - s0) // 7
            wk = wk[wk < nweeks]
            out += np.bincount(wk, minlength=nweeks)
        return out

    def window_totals(self, p: int, measure: str, lo: int, hi: int, *, bots: str = "drop", min_events: int = 1,
                      min_months: int = 1) -> np.ndarray:
        """Per-member totals of `measure` over months [lo, hi) for the members meeting the rule."""
        a = self.get(p, measure, bots)[:, lo:hi]
        tot = a.sum(1)
        act = (a > 0).sum(1)
        return tot[(tot >= min_events) & (act >= min_months) & (tot > 0)]


# ------------------------------------------------------------------ the pre-specified analysis

# Fixed before any outcome was looked at (descriptive looks at the label file, the list inventory and the
# lag between the last activity and the exit came first and are listed in the results file).
PRIMARY = {
    "W": 12,  # landmark: months after the podling's start; the features use months 0..W-1
    "measure": "events",  # distinct commits + human-list messages
    "bots": "drop",
    "min_events": 1,
    "min_months": "ceil(W/4), at least 2",  # a regular member: active in a quarter of the window's months (3 of 12)
    "min_n": 3,  # the shape block needs at least three members
    "base": ("ln_n", "ln_mean"),
    "shape": ("gini", "top1", "top3", "entropy"),
    "l2": 1.0,
    "folds": 5,
    "repeats": 20,
    "perms": 500,
    "boot": 2000,
    "ews_w": 6,
    "ews_L": 12,
    "growth_cut": math.log(1.5),
}
SIZE_BINS = ((1, 4), (5, 7), (8, 12), (13, 25), (26, 10**9))
SIZE_LABEL = {(1, 4): "1-4", (5, 7): "5-7", (8, 12): "8-12", (13, 25): "13-25", (26, 10**9): "26+"}


def landmark_table(panel: Panel, W: int = 12, measure: str = "events", bots: str = "drop", min_events: int = 1,
                   min_months: int | None = None, projects=None) -> dict:
    """One row per resolved project still in the Incubator at month W (exit month >= W), with the
    activity distribution in months [0, W) among the members meeting the rule (default: active in at
    least ceil(W/4) months, at least 2).  y = 1 if the podling graduated, 0 if it retired."""
    rows = []
    proj = panel.resolved() if projects is None else projects
    if min_months is None:
        min_months = regular_months(W)
    for p in proj:
        if panel.exit_m[p] < W:
            continue
        a = panel.window_totals(p, measure, 0, W, bots=bots, min_events=min_events, min_months=min_months)
        f = shape_features(a) if len(a) else {"n": 0, "T": 0.0, "mean": float("nan"), "gini": float("nan"), "top1": float("nan"),
                                              "top3": float("nan"), "entropy": float("nan"), "effn": float("nan"),
                                              "theil": float("nan"), "cv": float("nan"), "single": float("nan"),
                                              **{f"share{k}": 0.0 for k in range(1, 6)}}
        for k in range(1, 6):
            f[f"share{k}"] = (np.sort(a)[::-1][k - 1] / a.sum()) if len(a) >= k else 0.0
        ev = panel.monthly_total(p, measure, bots)[:W]
        h = W // 2
        f["growth"] = math.log((ev[h:].sum() + 1.0) / (ev[:h].sum() + 1.0))
        f["active_months"] = float((ev > 0).sum())
        f["mcv"] = float(ev.std(ddof=1) / ev.mean()) if ev.mean() > 0 and W > 1 else float("nan")
        f.update(p=int(p), y=int(panel.label[p]), exit_m=int(panel.exit_m[p]), year=float(panel.start_ym[p]) / 12.0 - 2003.0)
        rows.append(f)
    tab = {k: np.array([r[k] for r in rows], float) for k in rows[0]}
    with np.errstate(divide="ignore", invalid="ignore"):
        tab["ln_n"] = np.log(tab["n"])
        tab["ln_mean"] = np.log(tab["mean"])
        tab["ln_T"] = np.log(tab["T"])
    return tab


def _sel(tab: dict, mask) -> dict:
    return {k: v[mask] for k, v in tab.items()}


def _auc_raw(y, x) -> float:
    return auc_score(y, x)


def h1_analysis(tab: dict, *, seed: int = SEED, perms: int = PRIMARY["perms"], boot: int = PRIMARY["boot"],
                repeats: int = PRIMARY["repeats"], shape=PRIMARY["shape"], base=PRIMARY["base"], l2: float = PRIMARY["l2"],
                min_n: int = PRIMARY["min_n"]) -> dict:
    """Does the shape of the activity distribution predict graduation better than its mean?
    Four readings, each reported:  (a) the held-out AUC of each single feature;  (b) paired bootstrap of
    the difference between the best single shape feature and the mean;  (c) the held-out gain from adding
    the shape block to {size, mean}, with a permutation p;  (d) the nested likelihood-ratio test."""
    m = (tab["n"] >= min_n) & np.isfinite(tab["ln_mean"]) & np.isfinite(tab["gini"])
    t = _sel(tab, m)
    y = t["y"].astype(float)
    out: dict = {"N": int(len(y)), "grad": int(y.sum()), "ret": int(len(y) - y.sum()), "excluded_small": int((tab["n"] < min_n).sum()),
                 "excluded_small_ret": int(((tab["n"] < min_n) & (tab["y"] == 0)).sum())}
    Xb = np.c_[[t[c] for c in base]].T
    Xs = np.c_[[t[c] for c in shape]].T
    kw = dict(folds=PRIMARY["folds"], repeats=repeats, l2=l2, seed=seed)
    rng = np.random.default_rng([seed, 1])
    # (a) single features, held out (sign learned in the training folds)
    singles = {"size ln n": t["ln_n"], "mean ln(T/n)": t["ln_mean"], "total ln T": t["ln_T"]}
    for c in shape:
        singles[f"shape {c}"] = t[c]
    out["single"] = {}
    oof = {}
    for name, x in singles.items():
        s = cv_oof(x, y, **kw)
        oof[name] = s
        lo, hi = boot_auc(y, s, rng, boot)
        out["single"][name] = {"auc": auc_score(y, s), "lo": lo, "hi": hi, "raw_auc": _auc_raw(y, x)}
    # (b) best single shape feature vs the mean
    best = max((c for c in shape), key=lambda c: out["single"][f"shape {c}"]["auc"])
    out["best_shape"] = best
    lo, hi, pg = boot_auc_diff(y, oof[f"shape {best}"], oof["mean ln(T/n)"], rng, boot)
    out["diff_best_shape_vs_mean"] = {"diff": out["single"][f"shape {best}"]["auc"] - out["single"]["mean ln(T/n)"]["auc"], "lo": lo, "hi": hi, "p_gt0": pg}
    lo, hi, pg = boot_auc_diff(y, oof["shape gini"], oof["mean ln(T/n)"], rng, boot)
    out["diff_gini_vs_mean"] = {"diff": out["single"]["shape gini"]["auc"] - out["single"]["mean ln(T/n)"]["auc"], "lo": lo, "hi": hi, "p_gt0": pg}
    # (c) models
    s_base = cv_oof(Xb, y, **kw)
    s_full = cv_oof(np.c_[Xb, Xs], y, **kw)
    s_shape = cv_oof(Xs, y, **kw)
    s_mean = oof["mean ln(T/n)"]
    out["model"] = {}
    for name, s in (("size + mean", s_base), ("size + mean + shape", s_full), ("shape only", s_shape), ("mean only", s_mean)):
        lo, hi = boot_auc(y, s, rng, boot)
        out["model"][name] = {"auc": auc_score(y, s), "lo": lo, "hi": hi, "logloss": logloss(y, s)}
    lo, hi, pg = boot_auc_diff(y, s_full, s_base, rng, boot)
    gain, pperm, null = perm_gain(Xb, Xs, y, perms=perms, seed=seed, folds=PRIMARY["folds"], repeats=repeats, l2=l2)
    _, pperm_s, null_s = perm_gain(Xb, Xs, y, perms=perms, seed=seed, folds=PRIMARY["folds"], repeats=repeats, l2=l2, strata=size_strata(t["n"]))
    out["gain"] = {"diff": out["model"]["size + mean + shape"]["auc"] - out["model"]["size + mean"]["auc"], "lo": lo, "hi": hi, "p_gt0": pg,
                   "perm_gain": gain, "perm_p": pperm, "perm_null_mean": float(null.mean()), "perm_null_q95": float(np.quantile(null, 0.95)),
                   "perm_p_strat": pperm_s, "perm_null_mean_strat": float(null_s.mean())}
    lo, hi, pg = boot_auc_diff(y, s_shape, s_mean, rng, boot)
    out["shape_vs_mean_models"] = {"diff": out["model"]["shape only"]["auc"] - out["model"]["mean only"]["auc"], "lo": lo, "hi": hi, "p_gt0": pg}
    # (d) likelihood ratio
    stat, p, df = lr_test(Xb, np.c_[Xb, Xs], y)
    out["lr"] = {"stat": stat, "p": p, "df": df}
    # standardised coefficients of the full model (ridge), for the direction of each term
    Z, _ = _standardise(np.c_[Xb, Xs], np.c_[Xb, Xs])
    beta = logit_fit(Z, y, l2=l2)
    names = list(base) + list(shape)
    out["coef"] = {n: float(b) for n, b in zip(names, beta[1:])}
    # exchangeable-member reference: how concentrated would the same events be if members were interchangeable
    g_null = [exchangeable_gini(int(n), int(T), np.random.default_rng([seed, 2, i]), draws=300)[0] for i, (n, T) in enumerate(zip(t["n"], t["T"]))]
    out["gini_obs_median"] = float(np.median(t["gini"]))
    out["gini_null_median"] = float(np.nanmedian(g_null))
    out["_y"] = y
    return out


def size_analysis(tab: dict, *, seed: int = SEED, boot: int = 1000, repeats: int = 10, min_per_class: int = 5,
                  perm_halves: int = 200, boot_lr: int = 1000) -> dict:
    """What changes with n: per size range (members active in the window), the graduation rate, how
    concentrated the activity is, and how well concentration and the mean each separate the outcome."""
    n = tab["n"]
    out: dict = {"bins": []}
    rng = np.random.default_rng([seed, 3])
    for lo, hi in SIZE_BINS:
        m = (n >= lo) & (n <= hi)
        if m.sum() == 0:
            continue
        t = _sel(tab, m)
        y = t["y"]
        row = {"label": SIZE_LABEL[(lo, hi)], "N": int(m.sum()), "grad": int(y.sum()), "ret": int((1 - y).sum()),
               "rate": float(y.mean()), "median_mean": float(np.nanmedian(t["mean"])), "median_gini": float(np.nanmedian(t["gini"])) if lo >= 3 else float("nan"),
               "median_T": float(np.median(t["T"]))}
        k, N = int(y.sum()), len(y)
        z = 1.96
        ph = k / N
        den = 1 + z * z / N
        c = (ph + z * z / (2 * N)) / den
        hw = z * math.sqrt(ph * (1 - ph) / N + z * z / (4 * N * N)) / den
        row["wilson"] = (max(0.0, c - hw), min(1.0, c + hw))
        if min(row["grad"], row["ret"]) >= min_per_class:
            for name, x in (("auc_mean", t["ln_mean"]), ("auc_gini", t["gini"]), ("auc_T", t["ln_T"])):
                ok = np.isfinite(x)
                if ok.sum() >= 10 and len(np.unique(y[ok])) == 2:
                    a = auc_score(y[ok], x[ok])
                    pos, neg = np.flatnonzero(y[ok] == 1), np.flatnonzero(y[ok] == 0)
                    bs = []
                    for _ in range(boot):
                        ix = np.r_[rng.choice(pos, len(pos)), rng.choice(neg, len(neg))]
                        bs.append(auc_score(y[ok][ix], x[ok][ix]))
                    row[name] = (a, float(np.quantile(bs, 0.025)), float(np.quantile(bs, 0.975)))
        out["bins"].append(row)
    # size and concentration are mechanically linked; show the correlation and the interaction test
    m = (n >= 3) & np.isfinite(tab["gini"]) & np.isfinite(tab["ln_mean"])
    t = _sel(tab, m)
    from scipy.stats import spearmanr

    out["spearman_n_gini"] = tuple(float(v) for v in spearmanr(t["n"], t["gini"]))
    out["spearman_n_mean"] = tuple(float(v) for v in spearmanr(t["n"], t["mean"]))
    y = t["y"].astype(float)
    Xb = np.c_[t["ln_n"], t["ln_mean"], t["gini"]]
    Xi = np.c_[Xb, t["gini"] * t["ln_n"], t["ln_mean"] * t["ln_n"]]
    stat, p, df = lr_test(Xb, Xi, y)
    out["interaction_lr"] = {"stat": stat, "p": p, "df": df}
    # the 2-df test also holds mean x ln n; which term carries it (each given the other, 1 df)
    s_g, p_g, _ = lr_test(np.c_[Xb, t["ln_mean"] * t["ln_n"]], Xi, y)
    s_m, p_m, _ = lr_test(np.c_[Xb, t["gini"] * t["ln_n"]], Xi, y)
    out["interaction_gini_lr"] = {"stat": s_g, "p": p_g, "df": 1}
    out["interaction_mean_lr"] = {"stat": s_m, "p": p_m, "df": 1}
    # three checks on that p: a parametric bootstrap under the main-effects model (no reliance on the chi-square),
    # the Gini replaced by its rank, and ln T as the moderator in place of ln n
    Zm, _ = _standardise(Xb, Xb)
    pm = logit_predict(logit_fit(Zm, y, l2=1e-6), Zm)
    rngb = np.random.default_rng([seed, 4])
    sims = np.array([lr_test(Xb, Xi, (rngb.random(len(y)) < pm).astype(float))[0] for _ in range(boot_lr)])
    out["interaction_boot_p"] = float((1 + (sims >= stat).sum()) / (boot_lr + 1))
    from scipy.stats import rankdata

    gr = rankdata(t["gini"]) / len(y)
    Xr = np.c_[t["ln_n"], t["ln_mean"], gr]
    out["interaction_rank_p"] = lr_test(Xr, np.c_[Xr, gr * t["ln_n"], t["ln_mean"] * t["ln_n"]], y)[1]
    Xt = np.c_[t["ln_T"], t["ln_mean"], t["gini"]]
    out["interaction_lnT_p"] = lr_test(Xt, np.c_[Xt, t["gini"] * t["ln_T"], t["ln_mean"] * t["ln_T"]], y)[1]
    Z, _ = _standardise(Xi, Xi)
    beta = logit_fit(Z, y, l2=1e-3)
    out["interaction_coef"] = dict(zip(("ln_n", "ln_mean", "gini", "gini x ln_n", "ln_mean x ln_n"), [float(b) for b in beta[1:]]))
    # the sign of the concentration effect, small against large (split at the median n)
    med = float(np.median(t["n"]))
    out["split_median_n"] = med
    out["half_gain"] = {}
    for nm, mm in (("small", t["n"] <= med), ("large", t["n"] > med)):
        yy = y[mm]
        if min(yy.sum(), len(yy) - yy.sum()) >= 8:
            Xb_, Xs_ = np.c_[t["ln_n"][mm], t["ln_mean"][mm]], np.c_[[t[c][mm] for c in PRIMARY["shape"]]].T
            g_, p_, _ = perm_gain(Xb_, Xs_, yy, perms=perm_halves, seed=seed, repeats=repeats)
            out["half_gain"][nm] = {"N": int(mm.sum()), "ret": int((1 - yy).sum()), "gain": g_, "perm_p": p_,
                                    "auc_base": cv_auc(Xb_, yy, folds=5, repeats=repeats, seed=seed), "auc_full": cv_auc(np.c_[Xb_, Xs_], yy, folds=5, repeats=repeats, seed=seed)}
    for nm, mm in (("small", t["n"] <= med), ("large", t["n"] > med)):
        yy = y[mm]
        if min(yy.sum(), len(yy) - yy.sum()) >= 5:
            Zs, _ = _standardise(np.c_[t["ln_n"][mm], t["ln_mean"][mm], t["gini"][mm]], np.c_[t["ln_n"][mm], t["ln_mean"][mm], t["gini"][mm]])
            b = logit_fit(Zs, yy, l2=1.0)
            out[f"coef_gini_{nm}"] = float(b[3])
            out[f"auc_gini_{nm}"] = auc_score(yy, t["gini"][mm])
            out[f"N_{nm}"] = int(mm.sum())
    return out


def growth_analysis(tab: dict, cut: float = PRIMARY["growth_cut"]) -> dict:
    """Sustained growth against decline over the landmark window: the log ratio of events in the second
    half to the first.  Three classes; the graduation rate in each; Fisher/chi-square between classes."""
    from scipy.stats import fisher_exact

    g = tab["growth"]
    y = tab["y"]
    cls = np.where(g >= cut, "growth", np.where(g <= -cut, "decline", "steady"))
    out = {"cut": cut, "classes": {}}
    for c in ("growth", "steady", "decline"):
        m = cls == c
        out["classes"][c] = {"N": int(m.sum()), "grad": int(y[m].sum()), "ret": int((1 - y[m]).sum()), "rate": float(y[m].mean()) if m.sum() else float("nan")}
    a, b = out["classes"]["growth"], out["classes"]["decline"]
    if min(a["N"], b["N"]) > 0:
        out["fisher_growth_vs_decline"] = fisher_exact([[a["grad"], a["ret"]], [b["grad"], b["ret"]]])[1]
    out["auc_growth"] = auc_score(y, g)
    return out


def trajectory_classes(panel: Panel, measure: str = "events", bots: str = "drop", roll: int = 6, drop_last: int = 1) -> dict:
    """Retrospective description of each resolved project's whole pre-exit series (rolling mean of
    `roll` months, the last `drop_last` month(s) dropped because the exit process itself is mail).
    ended-at-peak: the final rolling mean is >= 80% of its maximum; decayed: <= 50%; collapsed: it stayed
    <= 20% of the maximum for the last 6 months."""
    rows = []
    for p in panel.resolved():
        ev = panel.monthly_total(p, measure, bots)[: max(panel.exit_m[p] - drop_last + 1, 0)]
        if len(ev) < roll + 6:
            continue
        r = np.convolve(ev, np.ones(roll) / roll, mode="valid")
        peak = r.max()
        if peak <= 0:
            continue
        end = r[-1]
        collapsed = bool((r[-6:] <= 0.2 * peak).all()) and r.argmax() < len(r) - 6
        cls = "collapsed" if collapsed else ("ended at peak" if end >= 0.8 * peak else ("decayed" if end <= 0.5 * peak else "in between"))
        rows.append((int(panel.label[p]), cls, len(ev), float(peak), float(end / peak)))
    out: dict = {"N": len(rows), "classes": {}}
    for c in ("ended at peak", "in between", "decayed", "collapsed"):
        sel = [r for r in rows if r[1] == c]
        g = sum(r[0] for r in sel)
        out["classes"][c] = {"N": len(sel), "grad": g, "ret": len(sel) - g}
    return out


def ews_table(panel: Panel, *, w: int = 6, L: int = 12, lag: int = 0, measure: str = "events", bots: str = "drop",
              transform: str = "log1p", detrend: str = "linear") -> dict:
    """Kendall tau of the rolling lag-1 autocorrelation and standard deviation against time over the L
    windows before the reference month (the administrative exit month minus `lag`)."""
    rows = []
    for p in panel.resolved():
        ref = int(panel.exit_m[p]) - lag
        ev = panel.monthly_total(p, measure, bots)
        x = np.log1p(ev) if transform == "log1p" else ev.astype(float)
        if ref < L + w - 1:
            continue
        ta, ts = ews_taus(x, ref, w, L, detrend)
        # the trend of the level itself over the same span, so a mean drifting down is visible
        lev = np.convolve(x[:ref], np.ones(w) / w, mode="valid")
        tl = kendall_time(lev[-L:]) if len(lev) >= L else float("nan")
        rows.append((int(p), int(panel.label[p]), ta, ts, tl, ref))
    return {k: np.array([r[i] for r in rows]) for i, k in enumerate(("p", "y", "tau_ar1", "tau_sd", "tau_level", "ref"))}


def ews_table_weekly(panel: Panel, *, w: int = 26, L: int = 52, lag: int = 0, bots: str = "drop", detrend: str = "linear") -> dict:
    """The same statistics on weekly counts (about four times the points of the monthly series), with the
    series ending `lag` weeks before the first day of the exit month."""
    rows = []
    for p in panel.resolved():
        ref = panel.exit_week(p) - lag
        if ref < L + w - 1:
            continue
        x = np.log1p(panel.weekly_total(p, bots))
        ta, ts = ews_taus(x, ref, w, L, detrend)
        lev = np.convolve(x[:ref], np.ones(w) / w, mode="valid")
        tl = kendall_time(lev[-L:]) if len(lev) >= L else float("nan")
        rows.append((int(p), int(panel.label[p]), ta, ts, tl, ref))
    return {k: np.array([r[i] for r in rows]) for i, k in enumerate(("p", "y", "tau_ar1", "tau_sd", "tau_level", "ref"))}


def ews_compare(t: dict, key: str, rng: np.random.Generator, boot: int = 1000) -> dict:
    """Retired against graduated on one indicator: AUC for 'retired' (higher indicator -> retired), the
    Mann-Whitney one-sided p, medians, and the share above 0.5 (a conventional alarm level)."""
    from scipy.stats import mannwhitneyu

    ok = np.isfinite(t[key])
    y = (t["y"][ok] == 0).astype(int)  # 1 = retired
    x = t[key][ok]
    if y.sum() < 3 or (1 - y).sum() < 3:
        return {"N": int(ok.sum())}
    a = auc_score(y, x)
    pos, neg = np.flatnonzero(y == 1), np.flatnonzero(y == 0)
    bs = [auc_score(y[ix], x[ix]) for ix in (np.r_[rng.choice(pos, len(pos)), rng.choice(neg, len(neg))] for _ in range(boot))]
    return {
        "N": int(ok.sum()), "ret": int(y.sum()), "grad": int((1 - y).sum()), "auc": a, "lo": float(np.quantile(bs, 0.025)), "hi": float(np.quantile(bs, 0.975)),
        "p_mwu": float(mannwhitneyu(x[y == 1], x[y == 0], alternative="greater").pvalue),
        "median_ret": float(np.median(x[y == 1])), "median_grad": float(np.median(x[y == 0])),
        "alarm_ret": float((x[y == 1] > 0.5).mean()), "alarm_grad": float((x[y == 0] > 0.5).mean()),
    }


def ews_time_matched(panel: Panel, *, w: int = 6, L: int = 12, lag: int = 0, measure: str = "events", bots: str = "drop",
                     min_null: int = 5, detrend: str = "linear") -> dict:
    """Within each project: where does the pre-exit tau sit among the taus at every earlier reference
    month whose L-month window does not overlap the pre-exit window?  u = fraction of those earlier taus
    that are lower (ties half).  No signal: u is uniform, mean 0.5.  Needs a long series."""
    rows = []
    for p in panel.resolved():
        ref = int(panel.exit_m[p]) - lag
        cand = np.arange(L + w - 1, ref - L + 1)
        if len(cand) < min_null:
            continue
        x = np.log1p(panel.monthly_total(p, measure, bots))[:ref]
        ar1, sd = rolling_indicators(x, w, detrend)
        obs = (kendall_time(ar1[ref - L : ref]), kendall_time(sd[ref - L : ref]))
        nul = np.array([[kendall_time(ar1[r - L : r]), kendall_time(sd[r - L : r])] for r in cand])
        u = []
        for j in (0, 1):
            col = nul[:, j]
            col = col[np.isfinite(col)]
            u.append(float(((col < obs[j]).sum() + 0.5 * (col == obs[j]).sum()) / len(col)) if len(col) >= min_null and np.isfinite(obs[j]) else float("nan"))
        rows.append((int(p), int(panel.label[p]), u[0], u[1]))
    return {k: np.array([r[i] for r in rows]) for i, k in enumerate(("p", "y", "u_ar1", "u_sd"))}


def ews_time_matched_weekly(panel: Panel, *, w: int = 26, L: int = 52, lag: int = 0, bots: str = "drop", min_null: int = 5,
                            detrend: str = "linear") -> dict:
    """The within-project comparison of `ews_time_matched` on weekly counts (needs about 2.5 years of series)."""
    rows = []
    for p in panel.resolved():
        ref = panel.exit_week(p) - lag
        cand = np.arange(L + w - 1, ref - L + 1)
        if len(cand) < min_null:
            continue
        x = np.log1p(panel.weekly_total(p, bots))[:ref]
        ar1, sd = rolling_indicators(x, w, detrend)
        obs = (kendall_time(ar1[ref - L : ref]), kendall_time(sd[ref - L : ref]))
        nul = np.array([[kendall_time(ar1[r - L : r]), kendall_time(sd[r - L : r])] for r in cand])
        u = []
        for j in (0, 1):
            col = nul[:, j]
            col = col[np.isfinite(col)]
            u.append(float(((col < obs[j]).sum() + 0.5 * (col == obs[j]).sum()) / len(col)) if len(col) >= min_null and np.isfinite(obs[j]) else float("nan"))
        rows.append((int(p), int(panel.label[p]), u[0], u[1]))
    return {k: np.array([r[i] for r in rows]) for i, k in enumerate(("p", "y", "u_ar1", "u_sd"))}


def _ar1_path(phi: np.ndarray, rng: np.random.Generator) -> np.ndarray:
    e = rng.normal(size=len(phi))
    x = np.zeros(len(phi))
    for t in range(1, len(phi)):
        x[t] = phi[t] * x[t - 1] + e[t]
    return x


def ews_power(w: int, L: int, *, rng: np.random.Generator, sims: int = 300, phi0: float = 0.3, phi1: float = 0.9,
              detrend: str = "linear") -> dict:
    """How well could this test see a true slowing down at this series length?  AR(1) noise whose
    coefficient rises from phi0 to phi1 over the last L + w months (the 'transition' cases) against a
    constant coefficient phi0 (the controls); the same detrending, window and Kendall statistic.  Reports
    the AUC of each indicator for telling the two apart and the share above the 0.5 alarm level in each."""
    burn, pre = 30, 6
    n = pre + L + w

    def one(phi_end: float) -> np.ndarray:
        phi = np.r_[np.full(burn + pre, phi0), np.linspace(phi0, phi_end, L + w)]
        return _ar1_path(phi, rng)[burn:]

    ta = np.array([ews_taus(one(phi1), n, w, L, detrend) for _ in range(sims)])
    tc = np.array([ews_taus(one(phi0), n, w, L, detrend) for _ in range(sims)])
    y = np.r_[np.ones(sims), np.zeros(sims)]
    out = {"w": w, "L": L}
    for j, nm in ((0, "ar1"), (1, "sd")):
        x = np.r_[ta[:, j], tc[:, j]]
        ok = np.isfinite(x)
        out[f"auc_{nm}"] = auc_score(y[ok], x[ok])
        out[f"alarm_tp_{nm}"] = float((ta[:, j] > 0.5).mean())
        out[f"alarm_fp_{nm}"] = float((tc[:, j] > 0.5).mean())
    return out


# ------------------------------------------------------------------ survival form, critical mass, member dynamics

def regular_months(W: int) -> int:
    """The primary member rule: active in at least a quarter of the window's months (3 of 12), at least 2."""
    return max(2, math.ceil(W / 4))


def hazard_table(panel: Panel, *, w: int = 6, h: int = 6, step: int = 3, t_min: int = 6, measure: str = "events",
                 bots: str = "drop", min_months: int = 2) -> dict:
    """Discrete-time survival form of the same question.  One row per project and origin month t (every
    `step` months from t_min while the podling is still in the Incubator, exit month >= t); features from
    the trailing window [t - w, t); outcomes: retires within the next h months, graduates within them."""
    rows = []
    for p in panel.resolved():
        em, lab = int(panel.exit_m[p]), int(panel.label[p])
        series = panel.monthly_total(p, measure, bots)
        for t in range(t_min, em + 1, step):
            lo = t - w
            a = panel.window_totals(p, measure, lo, t, bots=bots, min_months=min_months)
            n = len(a)
            ev = series[lo:t]
            half = w // 2
            rows.append({
                "p": p, "t": t, "n": n, "ln_n": math.log1p(n), "ln_mean": math.log1p(a.sum() / n) if n else 0.0,
                "gini": gini_corrected(a) if n >= 3 else 0.0, "top1": top_share(a, 1) if n >= 1 else 1.0,
                "top3": top_share(a, 3) if n >= 1 else 1.0, "entropy": norm_entropy(a) if n >= 2 else 0.0,
                "small": float(n < 3), "growth": math.log((ev[half:].sum() + 1.0) / (ev[:half].sum() + 1.0)),
                "ln_t": math.log(t), "y_ret": int(lab == 0 and em < t + h), "y_grad": int(lab == 1 and em < t + h),
            })
    return {k: np.array([r[k] for r in rows], float) for k in rows[0]}


def cluster_boot_auc_diff(y, sa, sb, groups, rng: np.random.Generator, B: int = 500) -> tuple[float, float, float]:
    """Paired bootstrap of AUC(sa) - AUC(sb) resampling whole projects (rows of one project stay together)."""
    y, sa, sb, groups = map(np.asarray, (y, sa, sb, groups))
    ug = np.unique(groups)
    idx = {g: np.flatnonzero(groups == g) for g in ug}
    d = []
    for _ in range(B):
        take = np.concatenate([idx[g] for g in rng.choice(ug, len(ug))])
        if y[take].sum() == 0 or y[take].sum() == len(take):
            continue
        d.append(auc_score(y[take], sa[take]) - auc_score(y[take], sb[take]))
    d = np.array(d)
    return float(np.quantile(d, 0.025)), float(np.quantile(d, 0.975)), float((d > 0).mean())


def hazard_analysis(tab: dict, *, seed: int = SEED, target: str = "y_ret", repeats: int = 5, boot: int = 400) -> dict:
    """Does adding the shape block to {size, mean, tenure} improve the held-out ranking of who retires (or
    graduates) within the next h months?  Folds hold out whole projects."""
    y = tab[target]
    g = tab["p"]
    base = np.c_[tab["ln_n"], tab["ln_mean"], tab["ln_t"], tab["small"]]
    shape = np.c_[tab["gini"], tab["top1"], tab["top3"], tab["entropy"]]
    kw = dict(folds=5, repeats=repeats, l2=1.0, seed=seed, groups=g)
    sb = cv_oof(base, y, **kw)
    sf = cv_oof(np.c_[base, shape], y, **kw)
    sg = cv_oof(np.c_[base, tab["growth"]], y, **kw)
    sfg = cv_oof(np.c_[base, shape, tab["growth"]], y, **kw)
    rng = np.random.default_rng([seed, 5])
    out = {"rows": int(len(y)), "projects": int(len(np.unique(g))), "events": int(y.sum()), "event_projects": int(len(np.unique(g[y == 1])))}
    for name, s in (("tenure+size+mean", sb), ("+ shape", sf), ("+ growth", sg), ("+ shape + growth", sfg)):
        out[name] = {"auc": auc_score(y, s), "logloss": logloss(y, s)}
    for name, (a, b) in (("shape gain", (sf, sb)), ("growth gain", (sg, sb)), ("shape+growth gain", (sfg, sb))):
        lo, hi, pg = cluster_boot_auc_diff(y, a, b, g, rng, boot)
        out[name] = {"diff": auc_score(y, a) - auc_score(y, b), "lo": lo, "hi": hi, "p_gt0": pg}
    return out


def step_vs_smooth(x, y, *, seed: int = SEED, folds: int = 5, repeats: int = 20, grid=np.arange(0.10, 0.901, 0.05)) -> dict:
    """Critical mass: is the graduation probability a smooth function of the early size x, or does it jump
    at a threshold (the group-level analogue of an ignition point, Claim 1.4)?  Compared on held-out
    log-loss and AUC; the step's cut is chosen on the training part of each fold from a quantile grid."""
    x = np.asarray(x, float)
    y = np.asarray(y, float)

    def fit_step(xt, yt):
        best = (-np.inf, None, None, None)
        for q in grid:
            c = np.quantile(xt, q)
            lo, hi = yt[xt < c], yt[xt >= c]
            if len(lo) < 5 or len(hi) < 5:
                continue
            p0, p1 = (lo.sum() + 1) / (len(lo) + 2), (hi.sum() + 1) / (len(hi) + 2)
            ll = lo.sum() * math.log(p0) + (len(lo) - lo.sum()) * math.log(1 - p0) + hi.sum() * math.log(p1) + (len(hi) - hi.sum()) * math.log(1 - p1)
            if ll > best[0]:
                best = (ll, c, p0, p1)
        return best

    acc = np.zeros(len(y))
    for r in range(repeats):
        rng = np.random.default_rng([seed, 11, r])
        f = fold_ids(y, folds, rng)
        for k in range(folds):
            te = f == k
            _, c, p0, p1 = fit_step(x[~te], y[~te])
            acc[te] += np.where(x[te] >= c, p1, p0)
    s_step = acc / repeats
    s_smooth = cv_oof(x, y, folds=folds, repeats=repeats, l2=1.0, seed=seed)
    ll, c, p0, p1 = fit_step(x, y)
    return {"step_logloss": logloss(y, s_step), "smooth_logloss": logloss(y, s_smooth), "step_auc": auc_score(y, s_step),
            "smooth_auc": auc_score(y, s_smooth), "cut": float(c), "p_below": float(p0), "p_above": float(p1),
            "n_below": int((x < c).sum()), "n_above": int((x >= c).sum()), "base_logloss": logloss(y, np.full(len(y), y.mean())),
            "oof_step": s_step}


def member_panel(panel: Panel, *, measure: str = "events", bots: str = "drop", min_members: int = 5, t_min: int = 3) -> dict:
    """Member-month rows for the D1 against D2 comparison (models/00-v0.md section 7, 'Team': does the
    coupling term add anything over individual dynamics for who stays active?).  A member is eligible in
    month t once she has been active in two distinct months up to t.  y = active in month t + 1.
    Own history (D1): active now, last month and the month before, the share of her months since her
    first that were active, her tenure, her volume now.  Others (D2): the share of the other eligible
    members active now and last month, and their volume now.  The exit month is dropped (it is mail
    about the exit)."""
    rows = []
    for p in panel.resolved():
        A = panel.get(p, measure, bots)
        em = int(panel.exit_m[p])
        last = em - 1  # the last month used as an outcome
        if last <= t_min + 1:
            continue
        A = A[:, : last + 1]
        act = A > 0
        if act.sum() == 0:
            continue
        first = np.where(act.any(1), act.argmax(1), 10**6)
        cum = np.cumsum(act, 1)
        for t in range(t_min, last):
            elig = (cum[:, t] >= 2)
            ne = int(elig.sum())
            if ne < min_members:
                continue
            ids = np.flatnonzero(elig)
            a0, a1 = act[ids, t], act[ids, t - 1]
            a2 = act[ids, t - 2]
            tot_now = A[ids, t].sum()
            n_act = int(a0.sum())
            n_act1 = int(a1.sum())
            denom = max(ne - 1, 1)
            s_other = (n_act - a0.astype(float)) / denom
            s_other1 = (n_act1 - a1.astype(float)) / denom
            v_other = np.log1p(tot_now - A[ids, t])
            rate = cum[ids, t] / (t - first[ids] + 1.0)
            ten = np.log1p(t - first[ids])
            vol = np.log1p(A[ids, t])
            y = act[ids, t + 1]
            for j in range(len(ids)):
                rows.append((p, t, ne, a0[j], a1[j], a2[j], rate[j], ten[j], vol[j], s_other[j], s_other1[j], v_other[j], y[j]))
    names = ("p", "t", "ne", "a0", "a1", "a2", "rate", "ten", "vol", "s", "s1", "v", "y")
    return {k: np.array([r[i] for r in rows], float) for i, k in enumerate(names)}


def d1_d2_analysis(tab: dict, *, seed: int = SEED, repeats: int = 3, boot: int = 300) -> dict:
    """Held-out comparison, whole projects held out: D1 (own history) against D1 + D2 (the others'
    activity), and against D1 + D2 with a quadratic term (a threshold-like response)."""
    y = tab["y"]
    g = tab["p"]
    d1 = np.c_[tab["a0"], tab["a1"], tab["a2"], tab["rate"], tab["ten"], tab["vol"]]
    d2 = np.c_[tab["s"], tab["s1"], tab["v"]]
    d2q = np.c_[d2, tab["s"] ** 2]
    kw = dict(folds=5, repeats=repeats, l2=1.0, seed=seed, groups=g)
    s1 = cv_oof(d1, y, **kw)
    s12 = cv_oof(np.c_[d1, d2], y, **kw)
    s12q = cv_oof(np.c_[d1, d2q], y, **kw)
    rng = np.random.default_rng([seed, 9])
    out = {"rows": int(len(y)), "projects": int(len(np.unique(g))), "base_rate": float(y.mean())}
    for name, s in (("D1", s1), ("D1 + D2", s12), ("D1 + D2 + s^2", s12q)):
        out[name] = {"auc": auc_score(y, s), "logloss": logloss(y, s)}
    for name, (a, b) in (("D2 gain", (s12, s1)), ("quadratic gain", (s12q, s12))):
        lo, hi, pg = cluster_boot_auc_diff(y, a, b, g, rng, boot)
        out[name] = {"diff": auc_score(y, a) - auc_score(y, b), "lo": lo, "hi": hi, "p_gt0": pg,
                     "dlogloss": logloss(y, b) - logloss(y, a)}
    Z, _ = _standardise(np.c_[d1, d2], np.c_[d1, d2])
    beta = logit_fit(Z, y, l2=1.0)
    out["coef"] = dict(zip(("a0", "a1", "a2", "rate", "tenure", "volume", "s_others", "s_others_lag", "v_others"), [float(b) for b in beta[1:]]))
    # response curve: the share of members active next month, by decile of the others' active share now
    q = np.quantile(tab["s"], np.linspace(0, 1, 11))
    q[-1] += 1e-9
    curve = []
    for lo, hi in zip(q[:-1], q[1:]):
        m = (tab["s"] >= lo) & (tab["s"] < hi)
        curve.append((float(tab["s"][m].mean()), float(y[m].mean()), float(s1[m].mean()), int(m.sum())))
    out["curve"] = curve
    small = tab["ne"] <= 10
    for nm, m in (("small teams (<=10 eligible)", small), ("larger (>10)", ~small)):
        if m.sum() > 500 and 0 < y[m].mean() < 1:
            sub1 = cv_oof(d1[m], y[m], **{**kw, "groups": g[m]})
            sub12 = cv_oof(np.c_[d1, d2][m], y[m], **{**kw, "groups": g[m]})
            out[nm] = {"rows": int(m.sum()), "d1_auc": auc_score(y[m], sub1), "d12_auc": auc_score(y[m], sub12),
                       "dlogloss": logloss(y[m], sub1) - logloss(y[m], sub12)}
    return out

# ------------------------------------------------------------------ variations

def hanley_se(auc: float, n1: int, n0: int) -> float:
    """Hanley and McNeil's standard error of an AUC (a scale for 'is this difference within noise')."""
    a = min(max(auc, 0.5), 0.999)
    q1, q2 = a / (2 - a), 2 * a * a / (1 + a)
    return math.sqrt((a * (1 - a) + (n1 - 1) * (q1 - a * a) + (n0 - 1) * (q2 - a * a)) / (n1 * n0))


def quick_eval(tab: dict, *, shape=PRIMARY["shape"], extra=(), controls=(), min_n: int = PRIMARY["min_n"], repeats: int = 10,
               seed: int = SEED, l2: float = PRIMARY["l2"], perms: int = 0, perms_strat: int = 0) -> dict:
    cols = ["ln_n", "ln_mean", *shape, *extra, *controls]
    m = (tab["n"] >= min_n)
    for c in cols:
        m &= np.isfinite(tab[c])
    if m.sum() < 30 or len(np.unique(tab["y"][m])) < 2:
        return {"N": int(m.sum())}
    t = _sel(tab, m)
    y = t["y"].astype(float)
    kw = dict(folds=5, repeats=repeats, l2=l2, seed=seed)
    Xb = np.c_[[t[c] for c in ("ln_n", "ln_mean", *controls)]].T
    Xs = np.c_[[t[c] for c in shape]].T if shape else np.zeros((len(y), 0))
    Xe = np.c_[[t[c] for c in extra]].T if extra else np.zeros((len(y), 0))
    out = {"N": int(len(y)), "ret": int((1 - y).sum()), "grad": int(y.sum())}
    out["auc_size"] = cv_auc(t["ln_n"], y, **kw)
    out["auc_mean"] = cv_auc(t["ln_mean"], y, **kw)
    out["auc_base"] = cv_auc(Xb, y, **kw)
    if shape:
        out["auc_shape"] = cv_auc(Xs, y, **kw)
        out["auc_full"] = cv_auc(np.c_[Xb, Xs], y, **kw)
        out["gain"] = out["auc_full"] - out["auc_base"]
        out["auc_best_single_shape"] = max(cv_auc(t[c], y, **kw) for c in shape)
        # a shape column with no variation cannot add anything (e.g. the one-event share among regular members, all of
        # whom have at least regular_months(W) events): such a row is reported but is not a test
        out["degenerate"] = bool(np.all(Xs.std(0) < 1e-12))
        if perms:
            out["perm_p"] = perm_gain(Xb, Xs, y, perms=perms, seed=seed, repeats=repeats, l2=l2)[1]
        if perms_strat:
            out["perm_p_strat"] = perm_gain(Xb, Xs, y, perms=perms_strat, seed=seed, repeats=repeats, l2=l2, strata=size_strata(t["n"]))[1]
    if extra:
        out["auc_extra"] = cv_auc(np.c_[Xb, Xe], y, **kw)
        out["auc_all"] = cv_auc(np.c_[Xb, Xs, Xe], y, **kw)
    out["se"] = hanley_se(out["auc_base"], out["grad"], out["ret"])
    if "gini" in t:
        Xa = np.c_[t["ln_n"], t["ln_mean"], t["gini"]]
        Xi = np.c_[Xa, t["gini"] * t["ln_n"], t["ln_mean"] * t["ln_n"]]
        out["int_p"] = lr_test(Xa, Xi, y)[1]
    return out


def variations(panel: Panel, *, seed: int = SEED, repeats: int = 10, perms: int = 0) -> list[dict]:
    """One factor at a time around the primary specification: window, activity measure, bot handling,
    member rule, which shape measures, regularisation, dynamics terms.  Each row is the held-out AUC of
    size, mean, size + mean, and size + mean + shape for that variant.  A row whose shape-gain test is the
    primary's own (same table, block and penalty) carries same_as_primary, so a family-wise correction counts
    that test once; the dynamics rows' own result is auc_extra (growth added to size and mean)."""
    rows = []

    def add(group, label, tab, dup=False, **kw):
        r = quick_eval(tab, repeats=repeats, seed=seed, perms=perms, **kw)
        r.update(group=group, label=label, same_as_primary=bool(dup))
        rows.append(r)

    W0 = PRIMARY["W"]
    prim = landmark_table(panel, W0, min_months=regular_months(W0))
    add("primary", "W=12, events, bots dropped, member = active in >= 3 months", prim)
    for W in (3, 6, 9, 12, 18, 24):
        add("window", f"W={W} (member: >= {regular_months(W)} active months)", landmark_table(panel, W, min_months=regular_months(W)), dup=W == W0)
    for meas in ("events", "commits", "messages", "dev_messages", "replies", "files", "events_all"):
        add("activity measure", meas, landmark_table(panel, W0, measure=meas, min_months=regular_months(W0)), dup=meas == PRIMARY["measure"])
    for b in ("drop", "keep", "top1"):
        add("bots", {"drop": "flagged robots dropped (primary)", "keep": "robots kept", "top1": "robots dropped and the project's single most active pseudonym dropped"}[b],
            landmark_table(panel, W0, bots=b, min_months=regular_months(W0)), dup=b == PRIMARY["bots"])
    for label, mm, me in (("any event (participants)", 1, 1), ("active in >= 2 months", 2, 1), ("active in >= 3 months (primary)", 3, 1),
                          ("active in >= 6 months (half the window)", 6, 1), ("at least 5 events", 1, 5)):
        add("member rule", label, landmark_table(panel, W0, min_months=mm, min_events=me), dup=(mm, me) == (regular_months(W0), 1))
    for label, shp in (("Gini only", ("gini",)), ("top-1 share only", ("top1",)), ("top-3 share only", ("top3",)), ("entropy only", ("entropy",)),
                       ("effective number only", ("effn",)), ("Theil only", ("theil",)), ("coefficient of variation only", ("cv",)),
                       ("share of one-event members only", ("single",)), ("all four (primary)", PRIMARY["shape"])):
        add("shape measure", label, prim, shape=shp, dup=shp == PRIMARY["shape"])
    add("shape measure", "profile of the five largest shares", prim, shape=("share1", "share2", "share3", "share4", "share5"))
    add("shape measure", "profile of the five largest shares + effective number", prim, shape=("share1", "share2", "share3", "share4", "share5", "effn"))
    for l2 in (0.01, 0.1, 1.0, 10.0):
        add("regularisation", f"ridge l2 = {l2}", prim, l2=l2, dup=l2 == PRIMARY["l2"])
    early = [p for p in panel.resolved() if panel.start_ym[p] // 12 <= 2012]
    late = [p for p in panel.resolved() if panel.start_ym[p] // 12 >= 2013]
    add("era", "podlings started 2003-2012", landmark_table(panel, W0, projects=early))
    add("era", "podlings started 2013-2021", landmark_table(panel, W0, projects=late))
    add("era", "start year added to size and mean", prim, controls=("year",))
    add("dynamics", "adds growth over the window (second half against first)", prim, extra=("growth",), dup=True)
    add("dynamics", "adds growth and monthly variability", prim, extra=("growth", "mcv"), dup=True)
    return rows


def grid_family(vr: list[dict]) -> list[int]:
    """Indices of the distinct, informative shape-gain tests in the variation grid: the family a correction runs over.
    Rows that repeat the primary's test, and rows whose shape column is constant, are left out (review 2026-11-01:
    the first version corrected over all 42 rows, 9 of them one test and 1 a constant)."""
    return [i for i, r in enumerate(vr) if "perm_p" in r and not r.get("same_as_primary") and not r.get("degenerate")]


def _variant_table(panel: Panel, r: dict) -> tuple[dict, dict]:
    """Rebuild the landmark table and the quick_eval keywords of a variation row from its label."""
    W0 = PRIMARY["W"]
    g, lb = r["group"], r["label"]
    mm = regular_months(W0)
    kw: dict = {}
    if g == "window":
        W = int(lb.split("=")[1].split(" ")[0])
        return landmark_table(panel, W, min_months=regular_months(W)), kw
    if g == "activity measure":
        return landmark_table(panel, W0, measure=lb, min_months=mm), kw
    if g == "bots":
        b = "keep" if lb.startswith("robots kept") else ("top1" if "single most active" in lb else "drop")
        return landmark_table(panel, W0, bots=b, min_months=mm), kw
    if g == "member rule":
        table = {"any event (participants)": (1, 1), "active in >= 2 months": (2, 1), "active in >= 3 months (primary)": (3, 1),
                 "active in >= 6 months (half the window)": (6, 1), "at least 5 events": (1, 5)}[lb]
        return landmark_table(panel, W0, min_months=table[0], min_events=table[1]), kw
    if g == "shape measure":
        shp = {"Gini only": ("gini",), "top-1 share only": ("top1",), "top-3 share only": ("top3",), "entropy only": ("entropy",),
               "effective number only": ("effn",), "Theil only": ("theil",), "coefficient of variation only": ("cv",),
               "share of one-event members only": ("single",), "all four (primary)": PRIMARY["shape"],
               "profile of the five largest shares": ("share1", "share2", "share3", "share4", "share5"),
               "profile of the five largest shares + effective number": ("share1", "share2", "share3", "share4", "share5", "effn")}[lb]
        return landmark_table(panel, W0, min_months=mm), {"shape": shp}
    if g == "regularisation":
        return landmark_table(panel, W0, min_months=mm), {"l2": float(lb.split("=")[1])}
    if g == "era":
        if lb.startswith("podlings started 2003"):
            return landmark_table(panel, W0, projects=[q for q in panel.resolved() if panel.start_ym[q] // 12 <= 2012]), kw
        if lb.startswith("podlings started 2013"):
            return landmark_table(panel, W0, projects=[q for q in panel.resolved() if panel.start_ym[q] // 12 >= 2013]), kw
        return landmark_table(panel, W0, min_months=mm), {"controls": ("year",)}
    return landmark_table(panel, W0, min_months=mm), kw


def _refine_variant_p(panel: Panel, r: dict, seed: int, perms: int = 2000) -> float:
    tab, kw = _variant_table(panel, r)
    shape = kw.get("shape", PRIMARY["shape"])
    t = _sel(tab, (tab["n"] >= PRIMARY["min_n"]) & np.all([np.isfinite(tab[c]) for c in ["ln_n", "ln_mean", *shape, *kw.get("controls", ())]], axis=0))
    y = t["y"].astype(float)
    ctrl = kw.get("controls", ())
    return perm_gain(np.c_[[t[c] for c in ("ln_n", "ln_mean", *ctrl)]].T, np.c_[[t[c] for c in shape]].T, y, perms=perms, seed=seed, repeats=10,
                     l2=kw.get("l2", PRIMARY["l2"]))[1]


LEAD_MEASURES = ("messages", "dev_messages", "replies")
LEAD_WINDOWS = (6, 9, 12, 18)


def gini_vs_mean(tab: dict, *, seed: int = SEED, repeats: int = 10, boot: int = 1000) -> dict:
    """Held-out AUC of the Gini alone, the mean alone and size alone, and the paired bootstrap of Gini minus mean."""
    m = (tab["n"] >= PRIMARY["min_n"]) & np.isfinite(tab["gini"]) & np.isfinite(tab["ln_mean"])
    t = _sel(tab, m)
    y = t["y"].astype(float)
    kw = dict(folds=5, repeats=repeats, l2=PRIMARY["l2"], seed=seed)
    sg, sm, sn = cv_oof(t["gini"], y, **kw), cv_oof(t["ln_mean"], y, **kw), cv_oof(t["ln_n"], y, **kw)
    lo, hi, pg = boot_auc_diff(y, sg, sm, np.random.default_rng([seed, 31]), boot)
    return {"N": int(len(y)), "ret": int((1 - y).sum()), "gini": auc_score(y, sg), "mean": auc_score(y, sm), "size": auc_score(y, sn),
            "diff": auc_score(y, sg) - auc_score(y, sm), "lo": lo, "hi": hi, "raw_gini": auc_score(y, t["gini"])}


def cond_shape_coefs(tab: dict, features=("gini", "top1", "top3", "entropy", "theil"), *, seed: int = SEED, boot: int = 300) -> dict:
    """Standardised logistic coefficient of each shape measure when added alone to {ln n, ln mean}, with a
    percentile bootstrap interval: the direction of the shape effect at a given size and mean."""
    m = (tab["n"] >= PRIMARY["min_n"]) & np.isfinite(tab["gini"]) & np.isfinite(tab["ln_mean"])
    t = _sel(tab, m)
    y = t["y"].astype(float)
    rng = np.random.default_rng([seed, 41])
    out = {}
    for f in features:
        X = np.c_[t["ln_n"], t["ln_mean"], t[f]]
        Z, _ = _standardise(X, X)
        b = logit_fit(Z, y, l2=1e-3)[3]
        bs = []
        for _ in range(boot):
            ix = rng.integers(0, len(y), len(y))
            if y[ix].sum() in (0, len(y)):
                continue
            Zi, _ = _standardise(X[ix], X[ix])
            bs.append(logit_fit(Zi, y[ix], l2=1e-3)[3])
        out[f] = (float(b), float(np.quantile(bs, 0.025)), float(np.quantile(bs, 0.975)))
    return out


def lead_conversation(panel: Panel, *, seed: int = SEED, perms: int = 300, repeats: int = 10, boot: int = 1000) -> dict:
    """The lead that came out of the variation grid: the activity measures that are list conversation alone
    (no commits) show a shape gain that the combined measure does not.  Re-examined across windows, eras and
    robot handling, with the Gini against the mean.  Found by searching, so its p-values are not confirmatory.
    Each row also carries the within-size-quintile permutation p (size_strata), and the development-list cell at
    12 months is split at its median size (post hoc)."""
    early = [p for p in panel.resolved() if panel.start_ym[p] // 12 <= 2012]
    late = [p for p in panel.resolved() if panel.start_ym[p] // 12 >= 2013]
    rows, gm, cc = [], {}, {}
    kw = dict(repeats=repeats, seed=seed, perms=perms, perms_strat=perms)
    for meas in LEAD_MEASURES:
        for W in LEAD_WINDOWS:
            r = quick_eval(landmark_table(panel, W, measure=meas), **kw)
            rows.append(r | {"measure": meas, "kind": "window", "label": f"W={W}", "W": W})
        for nm, sub in (("started 2003-2012", early), ("started 2013-2021", late)):
            r = quick_eval(landmark_table(panel, 12, measure=meas, projects=sub), **kw)
            rows.append(r | {"measure": meas, "kind": "era", "label": nm, "W": 12})
        for b, nm in (("keep", "robots kept"), ("top1", "robots and the most active pseudonym dropped")):
            r = quick_eval(landmark_table(panel, 12, measure=meas, bots=b), **kw)
            rows.append(r | {"measure": meas, "kind": "bots", "label": nm, "W": 12})
        for W in (12, 18):
            tabw = landmark_table(panel, W, measure=meas)
            gm[(meas, W)] = gini_vs_mean(tabw, seed=seed, repeats=repeats, boot=boot)
            cc[(meas, W)] = cond_shape_coefs(tabw, seed=seed, boot=min(boot, 300))
    tabd = landmark_table(panel, 12, measure="dev_messages")
    tabd = _sel(tabd, (tabd["n"] >= PRIMARY["min_n"]) & np.isfinite(tabd["ln_mean"]) & np.isfinite(tabd["gini"]))
    med = float(np.median(tabd["n"]))
    halves = {"median_n": med}
    for nm, mm in (("small", tabd["n"] <= med), ("large", tabd["n"] > med)):
        sub = _sel(tabd, mm)
        halves[nm] = quick_eval(sub, repeats=repeats, seed=seed, perms=perms) | {"raw_gini": auc_score(sub["y"], sub["gini"])}
    return {"rows": rows, "gini_vs_mean": gm, "cond_coef": cc, "halves": halves}


def coverage_check(panel: Panel, W: int = PRIMARY["W"], *, seed: int = SEED, repeats: int = 10, perms: int = 200) -> dict:
    """The commit file starts 2005-01-30 and the mail file 2003-04-01 (L4624, L4625): a podling whose landmark window
    starts before February 2005 has no commits for some or all of it, so its n is too small.  Counts them, and re-runs
    the primary and the development-list lead without them (review 2026-11-01)."""
    first_c, first_e = _ym(COMMITS_FIRST) + 1, _ym(EMAILS_FIRST)  # first fully covered month of each file
    tab = landmark_table(panel, W)
    cm = landmark_table(panel, W, measure="commits")
    start = panel.start_ym[tab["p"].astype(int)]
    part = start < first_c
    out = {"W": W, "at_risk": int(len(tab["y"])), "short": int(part.sum()), "short_grad": int(tab["y"][part].sum()),
           "short_ret": int((1 - tab["y"][part]).sum()), "short_mail": int((start < first_e).sum()),
           "committers_short": float(np.median(cm["n"][part])) if part.any() else float("nan"),
           "committers_rest": float(np.median(cm["n"][~part]))}
    out["primary_rest"] = quick_eval(_sel(tab, ~part), repeats=repeats, seed=seed, perms=perms)
    d = landmark_table(panel, W, measure="dev_messages")
    out["lead_rest"] = quick_eval(_sel(d, ~np.isin(d["p"], tab["p"][part])), repeats=repeats, seed=seed, perms=perms)
    return out


def descriptives(panel: Panel) -> dict:
    """Counts for the data section: nothing here names a person."""
    res = panel.resolved()
    out = {
        "projects_in_files": len(panel.names), "matched": int(panel.matched.sum()), "unmatched": [n for n, m in zip(panel.names, panel.matched) if not m],
        "resolved": int(len(res)), "graduated": int((panel.label[res] == 1).sum()), "retired": int((panel.label[res] == 0).sum()),
        "persons": int(panel.n_persons.sum()), "robot_pseudonyms": int(sum(b.sum() for b in panel.bot)), "relay_added": int(panel.relay_flagged),
    }
    tot = {k: sum(float(panel.mat[k][p].sum()) for p in np.flatnonzero(panel.matched)) for k in ("commits", "msg_human", "msg_all")}
    bot = {k: sum(float((panel.mat[k][p] * panel.bot[p][:, None]).sum()) for p in np.flatnonzero(panel.matched)) for k in tot}
    out["activity_total"] = tot
    out["activity_robot_share"] = {k: bot[k] / tot[k] for k in tot}
    dur = {lab: np.array([panel.exit_m[p] for p in res if panel.label[p] == lab]) for lab in (0, 1)}
    out["exit_month_quantiles"] = {("graduated" if lab else "retired"): np.quantile(v, [0.25, 0.5, 0.75]).tolist() for lab, v in dur.items()}
    post = tot_ev = 0.0
    lag0 = {0: 0, 1: 0}
    cnt = {0: 0, 1: 0}
    for p in res:
        ev = panel.monthly_total(p, "events", "drop")
        em = int(panel.exit_m[p])
        tot_ev += ev.sum()
        post += ev[em + 1 :].sum()
        nz = np.flatnonzero(ev[: em + 1])
        cnt[int(panel.label[p])] += 1
        lag0[int(panel.label[p])] += int(len(nz) > 0 and nz[-1] == em)
    out["by_era"] = []
    for lo, hi in ((2003, 2008), (2009, 2011), (2012, 2014), (2015, 2018), (2019, 2021)):
        ps = [p for p in res if lo <= panel.start_ym[p] // 12 <= hi]
        out["by_era"].append({"label": f"{lo}-{hi}", "N": len(ps), "grad": int(sum(panel.label[p] == 1 for p in ps)), "ret": int(sum(panel.label[p] == 0 for p in ps))})
    out["share_events_after_exit_month"] = float(post / tot_ev)
    out["last_active_is_exit_month"] = {("graduated" if k else "retired"): (lag0[k], cnt[k]) for k in (0, 1)}
    return out


def model_forms(tab: dict, *, seed: int = SEED, repeats: int = 20, min_n: int = PRIMARY["min_n"], boot: int = 2000) -> dict:
    """The primary window under different model forms, same projects, same folds: held-out AUC and
    log-loss for each, and each form's AUC minus that of size alone with a paired bootstrap of the fixed
    predictions.  The Hanley-McNeil s.e. is the uncertainty of one AUC; two forms scored on the same
    podlings differ by far less, so a difference is read against the paired interval, not against the s.e."""
    cols = ["ln_n", "ln_T", "ln_mean", *PRIMARY["shape"], "growth"]
    m = tab["n"] >= min_n
    for c in cols:
        m &= np.isfinite(tab[c])
    t = _sel(tab, m)
    y = t["y"].astype(float)
    S = np.c_[[t[c] for c in PRIMARY["shape"]]].T
    forms = {
        "size (ln n)": np.c_[t["ln_n"]],
        "total activity (ln T)": np.c_[t["ln_T"]],
        "mean per member (ln T/n)": np.c_[t["ln_mean"]],
        "size + mean": np.c_[t["ln_n"], t["ln_mean"]],
        "size + mean + shape (primary)": np.c_[t["ln_n"], t["ln_mean"], S],
        "shape only": S,
        "size + growth": np.c_[t["ln_n"], t["growth"]],
        "size + mean + growth": np.c_[t["ln_n"], t["ln_mean"], t["growth"]],
        "size + mean + shape + growth": np.c_[t["ln_n"], t["ln_mean"], S, t["growth"]],
        "size + Gini + Gini x size": np.c_[t["ln_n"], t["gini"], t["gini"] * t["ln_n"]],
        "size + mean + Gini + Gini x size + mean x size": np.c_[t["ln_n"], t["ln_mean"], t["gini"], t["gini"] * t["ln_n"], t["ln_mean"] * t["ln_n"]],
    }
    out = {"N": int(len(y)), "ret": int((1 - y).sum()), "grad": int(y.sum()), "forms": {}}
    kw = dict(folds=5, repeats=repeats, l2=PRIMARY["l2"], seed=seed)
    oof = {}
    for name, X in forms.items():
        sc = cv_oof(X, y, **kw)
        oof[name] = sc
        out["forms"][name] = {"auc": auc_score(y, sc), "logloss": logloss(y, sc), "se": hanley_se(auc_score(y, sc), int(y.sum()), int((1 - y).sum()))}
    st = step_vs_smooth(t["ln_n"], y, seed=seed, repeats=repeats)
    oof["step on size (cut chosen in training folds)"] = st["oof_step"]
    out["forms"]["step on size (cut chosen in training folds)"] = {"auc": st["step_auc"], "logloss": st["step_logloss"],
                                                                  "se": hanley_se(st["step_auc"], int(y.sum()), int((1 - y).sum()))}
    rng = np.random.default_rng([seed, 51])
    ref = oof["size (ln n)"]
    for name, sc in oof.items():
        if name != "size (ln n)":
            lo, hi, _ = boot_auc_diff(y, sc, ref, rng, boot)
            out["forms"][name]["vs_size"] = (auc_score(y, sc) - auc_score(y, ref), lo, hi)
    out["null_logloss"] = logloss(y, np.full(len(y), y.mean()))
    out["step"] = st
    st2 = step_vs_smooth(t["ln_T"], y, seed=seed, repeats=repeats)
    out["step_T"] = st2
    return out


def run_all(panel: Panel | None = None, *, fast: bool = False, seed: int = SEED, log=print) -> dict:
    """Everything the report needs.  `fast` shrinks permutations, bootstraps and repeats (for tests)."""
    panel = panel or Panel()
    perms, boot, reps = (60, 300, 6) if fast else (PRIMARY["perms"], PRIMARY["boot"], PRIMARY["repeats"])
    R: dict = {"fast": fast, "seed": seed, "perms": perms, "boot": boot, "repeats": reps}
    R["desc"] = descriptives(panel)
    log("descriptives done")
    W = PRIMARY["W"]
    tab = landmark_table(panel, W)
    R["tab_counts"] = {"at_risk": int(len(tab["y"])), "grad": int(tab["y"].sum()), "ret": int((1 - tab["y"]).sum()),
                       "n_quantiles": np.quantile(tab["n"], [0.1, 0.25, 0.5, 0.75, 0.9]).tolist(),
                       "n_lt3": int((tab["n"] < 3).sum()), "n0": int((tab["n"] == 0).sum()), "n0_ret": int(((tab["n"] == 0) & (tab["y"] == 0)).sum()),
                       "n_lt3_ret": int(((tab["n"] < 3) & (tab["y"] == 0)).sum())}
    tab_any = landmark_table(panel, W, min_months=1)
    R["tab_any_counts"] = {"n_quantiles": np.quantile(tab_any["n"], [0.1, 0.25, 0.5, 0.75, 0.9]).tolist()}
    R["h1"] = h1_analysis(tab, seed=seed, perms=perms, boot=boot, repeats=reps)
    R["h1_participants"] = h1_analysis(tab_any, seed=seed, perms=perms, boot=boot, repeats=reps)
    log("H1 done")
    R["size"] = size_analysis(tab, seed=seed, boot=max(300, boot // 2), repeats=reps, perm_halves=30 if fast else 300, boot_lr=100 if fast else 1000)
    R["size_participants"] = size_analysis(tab_any, seed=seed, boot=max(300, boot // 2), repeats=reps, perm_halves=30 if fast else 300, boot_lr=100 if fast else 1000)
    R["growth"] = growth_analysis(tab)
    R["trajectories"] = trajectory_classes(panel)
    R["forms"] = model_forms(tab, seed=seed, repeats=reps, boot=boot)
    R["coverage"] = coverage_check(panel, W, seed=seed, repeats=4 if fast else 10, perms=20 if fast else 200)
    log("size, growth, forms, coverage done")
    # early warning
    rng = np.random.default_rng([seed, 21])
    R["ews"] = []
    for (w, L, lag, det) in ((6, 12, 1, "linear"), (6, 12, 0, "linear"), (6, 12, 3, "linear"), (6, 18, 1, "linear"), (9, 18, 1, "linear"),
                             (12, 24, 1, "linear"), (6, 12, 1, "mean"), (9, 18, 1, "mean")):
        t = ews_table(panel, w=w, L=L, lag=lag, detrend=det)
        row = {"w": w, "L": L, "lag": lag, "detrend": det, "N": int(len(t["y"])), "ret": int((t["y"] == 0).sum()), "grad": int((t["y"] == 1).sum())}
        for key in ("tau_ar1", "tau_sd", "tau_level"):
            row[key] = ews_compare(t, key, rng, boot=max(300, boot // 2))
        R["ews"].append(row)
    R["ews_weekly"] = []
    for (w, L, lag) in ((26, 52, 0), (26, 52, 4), (26, 52, 8), (13, 26, 4)):
        t = ews_table_weekly(panel, w=w, L=L, lag=lag)
        row = {"w": w, "L": L, "lag": lag, "detrend": "linear", "N": int(len(t["y"])), "ret": int((t["y"] == 0).sum()), "grad": int((t["y"] == 1).sum())}
        for key in ("tau_ar1", "tau_sd", "tau_level"):
            row[key] = ews_compare(t, key, rng, boot=max(300, boot // 2))
        R["ews_weekly"].append(row)
    R["ews_time_matched"] = {}
    for (w, L, lag) in ((6, 12, 1), (6, 12, 0)):
        R["ews_time_matched"][(w, L, lag)] = ews_time_matched(panel, w=w, L=L, lag=lag)
    R["ews_time_matched_weekly"] = {(26, 52, lag): ews_time_matched_weekly(panel, w=26, L=52, lag=lag) for lag in (0, 4)}
    sims = 100 if fast else 400
    R["ews_power"] = [ews_power(w, L, rng=np.random.default_rng([seed, 22, w, L]), sims=sims, detrend=det)
                      | {"detrend": det, "unit": unit} for (w, L, unit, dets) in ((6, 12, "months", ("linear", "mean")), (9, 18, "months", ("linear", "mean")),
                                                                             (12, 24, "months", ("linear", "mean")), (26, 52, "weeks", ("linear", "mean")),
                                                                             (13, 26, "weeks", ("linear",))) for det in dets]
    log("EWS done")
    # survival form and member dynamics
    ht = hazard_table(panel)
    R["hazard"] = {tgt: hazard_analysis(ht, seed=seed, target=tgt, repeats=3 if fast else 5, boot=200 if fast else 400) for tgt in ("y_ret", "y_grad")}
    mp = member_panel(panel)
    R["d1d2"] = d1_d2_analysis(mp, seed=seed, repeats=1 if fast else 3, boot=150 if fast else 300)
    log("hazard and member dynamics done")
    R["lead"] = lead_conversation(panel, seed=seed, perms=30 if fast else 300, repeats=4 if fast else 10, boot=200 if fast else 1000)
    log("lead done")
    R["variations"] = variations(panel, seed=seed, repeats=4 if fast else 10, perms=20 if fast else 200)
    if not fast:  # a finer permutation count for the variants that look nominally significant, so the family-wise step has resolution
        tabs = {}
        for r in R["variations"]:
            if r.get("perm_p", 1.0) <= 0.06:
                r["perm_p_200"] = r["perm_p"]
                r["perm_p"] = _refine_variant_p(panel, r, seed)
    log("variations done")
    # Holm over the variation grid's distinct tests for the lead's headline cell (dev_messages, W = 12)
    vr = R["variations"]
    idx = grid_family(vr)
    holm = dict(zip(idx, _holm([vr[i]["perm_p"] for i in idx])))
    R["lead_holm"] = next(holm[i] for i in idx if vr[i]["group"] == "activity measure" and vr[i]["label"] == "dev_messages")
    R["grid_family_size"] = len(idx)
    # pre-specified decisions, computed once
    g = R["h1"]["gain"]
    R["decisions"] = {
        "H1_gain": bool(g["diff"] > 0 and g["perm_p"] < 0.05),
        "H1_gini_vs_mean": bool(R["h1"]["diff_gini_vs_mean"]["lo"] > 0),
        "size_interaction": bool(R["size"]["interaction_lr"]["p"] < 0.05),
        "ews_ar1": bool(R["ews"][0]["tau_ar1"].get("auc", 0.5) > 0.5 and R["ews"][0]["tau_ar1"].get("p_mwu", 1) < 0.05),
        "ews_sd": bool(R["ews"][0]["tau_sd"].get("auc", 0.5) > 0.5 and R["ews"][0]["tau_sd"].get("p_mwu", 1) < 0.05),
        "growth": bool(R["growth"].get("fisher_growth_vs_decline", 1) < 0.05),
        "d2": bool(R["d1d2"]["D2 gain"]["diff"] > 0.01),
        "step_preferred": bool(R["forms"]["step"]["step_logloss"] < R["forms"]["step"]["smooth_logloss"]),
    }
    lead12 = next(r for r in R["lead"]["rows"] if r["measure"] == "dev_messages" and r["label"] == "W=12")
    R["decisions"]["lead_conversation"] = bool(lead12.get("gain", 0) > 0 and lead12.get("perm_p", 1) < 0.05)
    return R


# ------------------------------------------------------------------ the report

def _p(p: float) -> str:
    return "< 0.001" if p < 0.001 else (f"{p:.3f}" if p < 0.1 else f"{p:.2f}")


def _sg(x: float, d: int = 3) -> str:
    """Signed number; a value that rounds to zero prints as +0.000, never -0.000."""
    v = round(float(x), d)
    return f"{(0.0 if v == 0 else v):+.{d}f}"


def _pv(p: float) -> str:
    return "p < 0.001" if p < 0.001 else f"p = {_p(p)}"


def _ci(d: dict, key: str = "auc", digits: int = 3) -> str:
    return f"{d[key]:.{digits}f} [{d['lo']:.{digits}f}, {d['hi']:.{digits}f}]"


def _pct(x: float) -> str:
    return f"{100 * x:.0f}%"


def _holm(ps: list[float]) -> list[float]:
    """Holm-Bonferroni adjusted p-values, in the input order."""
    m = len(ps)
    order = np.argsort(ps)
    adj = np.empty(m)
    run = 0.0
    for rank, i in enumerate(order):
        run = max(run, (m - rank) * ps[i])
        adj[i] = min(1.0, run)
    return adj.tolist()


def _time_matched_family(R: dict) -> list[dict]:
    """Every within-project (time-matched) test the results table prints, with Holm over that family."""
    from scipy.stats import wilcoxon

    rows = []
    for unit, tmx in (("m", R["ews_time_matched"]), ("w", R["ews_time_matched_weekly"])):
        for key, t in tmx.items():
            for lab, nm in ((0, "retired"), (1, "graduated")):
                for ind in ("u_ar1", "u_sd"):
                    u = t[ind][(t["y"] == lab) & np.isfinite(t[ind])]
                    if len(u) >= 8:
                        rows.append({"unit": unit, "key": key, "group": nm, "ind": ind, "n": len(u), "mean_u": float(u.mean()),
                                     "p": float(wilcoxon(u - 0.5).pvalue)})
    for r, h in zip(rows, _holm([r["p"] for r in rows])):
        r["holm"] = h
    return rows


def write_report(R: dict, panel: Panel, path: Path = RESULTS) -> str:
    L: list[str] = []
    add = L.append
    D, h1, hp = R["desc"], R["h1"], R["h1_participants"]
    sz, gr, tr, fm = R["size"], R["growth"], R["trajectories"], R["forms"]
    d12, haz, dec = R["d1d2"], R["hazard"], R["decisions"]
    e0 = R["ews"][0]
    met = json.loads((DERIVED / "meta.json").read_text())
    today = datetime.date.today().isoformat()

    add("# Apache Incubator: team-scale activity and survival, against Claim 1's \"state is a distribution\", the size question and the early-warning signals")
    add("")
    add(f"_Generated {today} by `uv run python -m models.apache_activity_survival report` (seed {R['seed']}; {R['perms']} permutations, {R['boot']} bootstrap draws, "
        f"{R['repeats']} cross-validation repeats). Code: `sim/models/apache_activity_survival.py`; checks: `sim/tests/test_apache_activity_survival.py`. "
        "Ledger ids: the dataset L4623-L4633 (file 117 section 4.3) and L4666 (how 117's counts were made, its sections 0 and 8); Claim 1 and the cascade map L1225, L1831; size L5779, L5740; "
        "early warning L0512, L0527, L0547, L3057, L1404-L1406; individual dynamics L5742, L4367, L5764. Results are computed statistics only: no name, "
        "address or message text is kept anywhere in the repo, and the data files are local-use-only (`sim/data/README.md`)._")
    add("")
    add("**What we are trying to achieve (one line).** An algebra of drives, of persons and of groups, composed into an equation set usable to predict or "
        "steer outcomes at the membership, group and crowd scales, sensitive to group size, composition and definition (`CLAUDE.md`, 2026-10-29).")
    add("")
    add("**What was tested.** On the Apache Incubator sustainability dataset (CC BY 4.0), a proxy for the team-scale half of `models/00-v0.md` section 7. "
        "Per podling: per-member activity (distinct commits and human mailing-list messages) month by month, the number of regular members n, and the outcome "
        "(graduated or retired, from the ASF's own status file). Three questions. **(1)** Does the *distribution* of activity across members "
        "(concentration: Gini, top-k share, entropy; the shape, not the mean) predict graduation better than the *mean* activity, the spirit of Claim 1 "
        "(`models/02-our-claims.md` 1.1: a group's state is a distribution, because no summary of it fixes the outcome, L1225)? **(2)** What changes with n "
        "(Aldred's size question)? **(3)** Is there a measurable analogue of a threshold cascade or of escalation in the activity series: sustained growth against "
        "collapse, a critical mass, and the early-warning signals of 027 and 030 (rising lag-1 autocorrelation and variance before retirement, L0512, L0527)? "
        "It is a **proxy**: the dataset records no anchoring w_i, no enemy weight E_i and no tie signs, and its outcome is dissolution against a success exit, "
        "not a split (L4632; 117 section 5.3), so nothing here can refute the section 7 certificate.")
    add("")

    # ------------------------------------------------------------------ verdict
    add("## Verdict")
    add("")
    g = h1["gain"]
    s_mean = h1["single"]["mean ln(T/n)"]
    s_size = h1["single"]["size ln n"]
    s_gini = h1["single"]["shape gini"]
    dg = h1["diff_gini_vs_mean"]
    add("**In short.**")
    add("")
    L12 = {(r["measure"], r["label"]): r for r in R["lead"]["rows"]}
    ld12, ld18 = L12[("dev_messages", "W=12")], L12[("dev_messages", "W=18")]
    ldE, ldL = L12[("dev_messages", "started 2003-2012")], L12[("dev_messages", "started 2013-2021")]
    ldK = L12[("dev_messages", "robots kept")]
    gm12, gm18 = R["lead"]["gini_vs_mean"][("dev_messages", 12)], R["lead"]["gini_vs_mean"][("dev_messages", 18)]
    vera = {r["label"]: r for r in R["variations"] if r["group"] == "era"}
    add(f"- *(1) For the pre-specified measure (commits plus list messages) the shape of the activity distribution, added to team size and mean activity, does not predict graduation: not supported. "
        f"For list conversation alone there is a lead.* At the first-year landmark "
        f"({h1['N']} podlings with at least 3 regular members, {h1['grad']} graduated and {h1['ret']} retired) the held-out AUC for graduation is {s_size['auc']:.2f} for size alone and {s_mean['auc']:.2f} for the mean activity per member; "
        f"adding the four shape measures to size and mean changes it by {_sg(g['diff'])} (bootstrap 95% interval {_sg(g['lo'])} to {_sg(g['hi'])}; permutation {_pv(g['perm_p'])}, within size quintiles {_pv(g['perm_p_strat'])}; likelihood-ratio {_pv(h1['lr']['p'])}). "
        f"The Gini coefficient alone separates the outcome no better than the mean does ({s_gini['auc']:.2f} against {s_mean['auc']:.2f}; difference {dg['diff']:+.2f}, "
        f"95% {dg['lo']:+.2f} to {dg['hi']:+.2f}). Shape-only models reach {h1['model']['shape only']['auc']:.2f}, because top-3 share and Gini move with n. "
        f"The mean per member is not told apart from chance ({s_mean['auc']:.2f}, interval {s_mean['lo']:.2f} to {s_mean['hi']:.2f}; {vera['podlings started 2003-2012']['auc_mean']:.2f} in the podlings started 2003-2012, "
        f"{vera['podlings started 2013-2021']['auc_mean']:.2f} in the later ones); size is. "
        f"**The lead:** counting only messages on the development lists (no commits), the Gini alone beats the mean by {gm12['diff']:+.2f} AUC (95% {gm12['lo']:+.2f} to {gm12['hi']:+.2f}) and the shape block adds "
        f"{_sg(ld12['gain'], 3)} AUC to size and mean (permutation {_pv(ld12['perm_p'])}; within size quintiles {_pv(ld12['perm_p_strat'])}), rising to {_sg(ld18['gain'], 3)} at 18 months ({_pv(ld18['perm_p'])}; {_pv(ld18['perm_p_strat'])}): "
        "conversation carried by a few voices goes with graduation. "
        f"It came out of a grid of {len(R['variations'])} variants ({R['grid_family_size']} distinct tests) and does not survive a correction over them (Holm p = {R['lead_holm']:.2f} at 12 months); it is absent in podlings started 2003-2012 "
        f"(gain {_sg(ldE['gain'], 2)}, {_pv(ldE['perm_p'])}) and present in those started 2013-2021 ({_sg(ldL['gain'], 2)}, {_pv(ldL['perm_p'])}), and it vanishes when automated senders are kept "
        f"({_sg(ldK['gain'], 3)}). A lead to test on podlings after 2021 with the rule written first, not a finding (section 7.4).")
    ih, ig, imn = sz["interaction_lr"], sz["interaction_gini_lr"], sz["interaction_mean_lr"]
    hg = sz.get("half_gain", {})
    bret = [b["ret"] for b in sz["bins"] if "auc_gini" in b]
    fx = fm["forms"]["size + Gini + Gini x size"]["vs_size"]
    add(f"- *(2) Size is the predictor, and the association of concentration with graduation changes with it: supported.* The graduation rate climbs with the number of regular members: "
        + ", ".join(f"{b['label']} members {_pct(b['rate'])} ({b['grad']}/{b['N']})" for b in sz["bins"])
        + f". The pre-specified shape-by-size interaction is significant (likelihood-ratio {_pv(ih['p'])} on 2 df), and the Gini x size term carries it (1 df, {_pv(ig['p'])}; the mean x size term {_pv(imn['p'])}); "
        f"held out, size + Gini + Gini x size beats size alone by {_sg(fx[0])} AUC (paired 95% {_sg(fx[1])} to {_sg(fx[2])}; the best of {len(fm['forms'])} forms, so biased upward). Where the association sits is post hoc: above the median size "
        f"(n > {sz['split_median_n']:.0f}) the Gini has a raw AUC of {sz.get('auc_gini_large', float('nan')):.2f} for graduation"
        + (f" ({hg['large']['N']} podlings, {hg['large']['ret']} retired)" if "large" in hg else "")
        + f", at or below it {sz.get('auc_gini_small', float('nan')):.2f}; the per-band AUCs rest on {min(bret)} to {max(bret)} retired projects per band.")
    pw0 = next(r for r in R["ews_power"] if r["unit"] == "months" and r["detrend"] == "linear" and r["w"] == 6)
    wk0 = R["ews_weekly"][0]
    pww = next(r for r in R["ews_power"] if r["unit"] == "weeks" and r["detrend"] == "linear" and r["w"] == 26)
    tmf = _time_matched_family(R)
    tm_sd = next(r for r in tmf if r["unit"] == "w" and r["key"] == (26, 52, 0) and r["group"] == "retired" and r["ind"] == "u_sd")

    add(f"- *(3) Growth against collapse is visible and predictive; a critical-mass step and early-warning signals are not found.* First-year activity up by half or more: {_pct(gr['classes']['growth']['rate'])} graduate "
        f"({gr['classes']['growth']['grad']}/{gr['classes']['growth']['N']}); down by a third or more: {_pct(gr['classes']['decline']['rate'])} ({gr['classes']['decline']['grad']}/{gr['classes']['decline']['N']}; Fisher {_pv(gr['fisher_growth_vs_decline'])}). "
        f"A smooth rise of graduation with early size beats a jump at a critical mass (held-out log-loss {fm['step']['smooth_logloss']:.3f} against {fm['step']['step_logloss']:.3f}). "
        f"Monthly early-warning statistics do not separate retirement from graduation (autocorrelation AUC {e0['tau_ar1']['auc']:.2f}, variance {e0['tau_sd']['auc']:.2f}), **but they could not have**: in simulation they detect a true slowing down with AUC "
        f"{pw0['auc_ar1']:.2f} and {pw0['auc_sd']:.2f}. Weekly series do have power ({pww['auc_ar1']:.2f} in simulation); there the data give {wk0['tau_ar1']['auc']:.2f} ({wk0['tau_ar1']['lo']:.2f} to {wk0['tau_ar1']['hi']:.2f}) for autocorrelation and "
        f"{wk0['tau_sd']['auc']:.2f} for variance; within retired projects the variance trend sits at {tm_sd['mean_u']:.2f} of the project's own history (nominal {_pv(tm_sd['p'])}, "
        f"one of {len(tmf)} within-project tests, Holm {_p(tm_sd['holm'])}): if anything decay, not slowing down. "
        f"The level trend discriminates strongly (AUC {1 - e0['tau_level']['auc']:.2f} for graduation).")
    add(f"- *Individual dynamics carry the member-level signal; a mean-field coupling term adds nothing material.* Whether a member is active next month is predicted with AUC {d12['D1']['auc']:.2f} by her own history alone "
        f"(D1: persistence, rate, tenure, volume); adding the share of the other members active now (D2) gains {d12['D2 gain']['diff']:+.4f} AUC "
        f"({d12['D2 gain']['lo']:+.4f} to {d12['D2 gain']['hi']:+.4f}), and a quadratic term for a threshold-like response gains {d12['quadratic gain']['diff']:+.4f}. v0 section 7's rule "
        "(\"if D2 adds no predictive gain over D1 for who leaves, the coupling term goes\") is met only for this proxy: D2 here is the others' activity share, not tie-based coupling "
        "(who replies to whom, 117 section 5.3), and the outcome is next month's activity, not departure. On that reading the dyad finding of 098 (partner term near zero beside inertia, L4367) "
        "reappears at team scale; the tie-based test has not been run.")
    add("")
    add("**Status.**")
    add("")
    add(f"- *Not supported (and bounded):* that concentration, entropy or top-k share of commits plus messages, added as a block, add held-out information about graduation beyond team size and mean activity ({g['lo']:+.3f} to {g['hi']:+.3f} AUC); "
        "that the mean activity per member predicts the outcome; that graduation turns on a critical early size (step against smooth); that the others' activity share adds to a member's own for staying active.")
    add(f"- *Supported:* that the number of regular members predicts graduation (AUC {s_size['auc']:.2f}); that sustained growth against decline in the first year separates the outcomes; "
        f"that the association of concentration with graduation changes with size (interaction {_pv(ih['p'])}, carried by the Gini x size term, {_pv(ig['p'])}); that a member's own recent activity predicts her next month (AUC {d12['D1']['auc']:.2f}).")
    add("- *Not found, with limits:* early-warning signals of the slowing-down kind before retirement: absent on monthly series (which have no power) and on weekly series (which would have caught a strong signal), "
        "so any such signal here is weaker than a rise of the lag-1 coefficient from 0.3 to 0.9. The retirement date is administrative, which blurs the reference point.")
    lh = R["lead"]["halves"]
    add("- *Lead, unconfirmed:* that the concentration of list conversation (messages without commits, automated senders removed) adds to size and mean, in the later half of the sample and at windows of 9 months or more; "
        f"its point estimate is larger in the larger projects (development lists at 12 months: {_sg(lh['large']['gain'])} above the median of {lh['median_n']:.0f} members, {lh['large']['ret']} retired, against "
        f"{_sg(lh['small']['gain'])} at or below it; post hoc). Found in the variation grid, not surviving a correction over it, to be tested on new podlings with a rule written first.")
    add("- *Undecided:* whether concentration matters in large projects specifically (a post hoc subgroup, see section 4); anything about thresholds, which this data cannot identify.")
    add("")
    add("**What an activity-first outcome could be fitted to here, and what cannot.**")
    add("")
    add("*Could be fitted:* (a) the team's size and the level and trend of its monthly activity, against exit (graduated or retired): size AUC "
        f"{s_size['auc']:.2f}, size plus growth {fm['forms']['size + growth']['auc']:.2f}, and the six-month retirement hazard from tenure, size and mean {haz['y_ret']['tenure+size+mean']['auc']:.2f}; "
        f"(b) a member's own persistence, the set-point-and-inertia form D1, for staying active (AUC {d12['D1']['auc']:.2f}), which is the activity-first analogue of v0's D1; "
        f"(c) a size-conditional concentration rule, as a Gini x size interaction term (held out {_sg(fx[0])} AUC over size alone), with concentration going with graduation in the larger projects; where it changes sign "
        "is post hoc and its mechanism is not in the data; "
        "(d) possibly, a conversation-concentration term (list messages without commits, robots removed), which is a lead for the later podlings and not a result.")
    add("")
    add("*Cannot be fitted:* (a) any main effect of the *distribution* of commits plus messages beyond size and mean (its interaction with size is (c) above); (b) a mean-field coupling term (the others' activity share) beyond a member's own, "
        "while the tie-based D2 has not been tried; (c) a threshold or critical-mass cascade: "
        "thresholds are not observed (activity is an outcome of the thresholds, and an aggregate entry curve does not identify them: read as thresholds, the order in which members first appear gives a uniform distribution by construction), and the step-against-smooth test prefers smooth; "
        "(d) an early-warning rule of the slowing-down kind: the monthly series are too short for the indicators to work even when the signal is present, and the weekly ones, which would catch a strong signal, show none; (e) drives, tie signs, enemy weights E_i or anchoring w_i, "
        "none of which the data record; (f) a split: the outcome is dissolution against success, and the exit date is administrative "
        f"({D['last_active_is_exit_month']['retired'][0]} of {D['last_active_is_exit_month']['retired'][1]} retired projects, and {D['last_active_is_exit_month']['graduated'][0]} of {D['last_active_is_exit_month']['graduated'][1]} graduated ones, show activity in the exit month itself, "
        "so a quiet spell before a retirement is not visible as a gap and the exit month's mail is at least partly about the exit; the messages were not read, by design); (g) causation: activity is both a cause and a symptom of the outcome.")
    add("")

    # ------------------------------------------------------------------ 1 data
    add("## 1. Data and terms")
    add("")
    add("- **Dataset.** Yin, Zhang, Xuan, Filkov, *Apache Software Foundation Incubator Project Sustainability Dataset*, version 1.1 (updated June 2021), Zenodo, "
        "doi:10.5281/zenodo.5637530, **CC BY 4.0** (open access; 117 section 4.3, L4623). Papers: Yin, Zhang, Xuan, Filkov 2021, MSR data showcase, doi:10.1109/msr52588.2021.00081; "
        "Yin, Chen, Xuan, Filkov 2021, ESEC/FSE, doi:10.1145/3468264.3468563. Credit as CC BY requires; the only change is aggregation (counts per pseudonym per month).")
    add("- **Files.** `commits_2021_update.zip` (156,231,855 bytes, md5 `952ec9c66f1c2a96ddf3deab2e78f9e9`, sha256 `143dab8e9ef184b62b505615906578022118665b0f6dc9d7de36cc5df021ce8c`) and "
        "`emails_2021_update.zip` (1,041,656,466 bytes, md5 `ac716c35e7f160178e83ea9ae40fd4be`, sha256 `3be525e64893256bfab8128bc889c5e9829de1e1cfe16ef7602b6457dfc7b5fb`); "
        "md5s match the Zenodo record. Streamed from the archives; nothing is extracted to disk; git-ignored under `sim/data/apache-incubator/`.")
    add(f"- **The build reproduces 117's counts.** {met['commit_rows'] - met['commit_malformed']:,} commit rows from {met['commit_projects']} projects (117: 12,608,575; 265) and "
        f"{met['email_rows'] - met['email_malformed']:,} messages from {met['email_projects']} projects (117: 2,161,558; 274), once {met['commit_malformed']} and {met['email_malformed']} short CSV records are set aside "
        f"(they have fewer fields than the header and cannot be assigned to a project). The commit file is one row per file touched; rows are grouped by revision into {met['commit_commits']:,} distinct commits.")
    add("- **Labels.** The Zenodo record has no label file (L4628). Labels come from the ASF's own `podlings.xml` (`https://incubator.apache.org/podlings.xml`, fetched 2026-11-01, "
        "sha256 `98f0b33016c850b6ee9fdb6d623c20c4116fefd5f1619ab35dcf2c152ffcb541`, 253,042 bytes; licensed to the ASF under the Apache License 2.0 in its header): status "
        "(graduated, retired, current), start date and end date per podling. Only those attributes are read. "
        f"{D['matched']} of the {D['projects_in_files']} project names in the files match a podling; the {len(D['unmatched'])} that do not "
        f"({', '.join(D['unmatched'])}) have no podling of that name in the file (old top-level projects that were never podlings, and `pubscribe`) and are left out; two names were matched by an explicit alias table "
        "(`empire` is Empire-db, `openoffice` is OpenOffice.org). "
        f"All {D['resolved']} matched projects are resolved by the data end, so a later cut-off for the labels changes nothing: "
        f"**{D['graduated']} graduated and {D['retired']} retired**: the MSR paper's 269 labelled projects (L4628), and against the APEX paper's 273 = 211 + 62 (L4629) six fewer graduated and two more retired (the labels of those papers are not on the Zenodo record, so the difference is not explained).")
    q = D["exit_month_quantiles"]
    add(f"- **Time.** Month 0 is the podling's start month. The exit month (graduation or retirement) has quartiles {q['graduated'][0]:.0f}, {q['graduated'][1]:.0f}, {q['graduated'][2]:.0f} for graduated "
        f"and {q['retired'][0]:.0f}, {q['retired'][1]:.0f}, {q['retired'][2]:.0f} for retired podlings. The files cover the incubation only: {100 * D['share_events_after_exit_month']:.1f}% of events fall after the exit month. "
        f"The last month with any activity is the exit month itself for {D['last_active_is_exit_month']['graduated'][0]}/{D['last_active_is_exit_month']['graduated'][1]} graduated and "
        f"{D['last_active_is_exit_month']['retired'][0]}/{D['last_active_is_exit_month']['retired'][1]} retired projects: the exit process (votes, resolutions, retirement threads) plausibly accounts for some of that mail (the messages were not read), so the last month may be contaminated by the outcome; "
        "the early-warning windows stop before it (section 5.3).")
    cv_ = R["coverage"]
    add(f"- **Coverage.** The commit file starts on 2005-01-30 and the mail file on 2003-04-01 (L4624, L4625). Of the {cv_['at_risk']} podlings at risk at month {cv_['W']}, {cv_['short']} "
        f"({cv_['short_grad']} graduated, {cv_['short_ret']} retired) started before February 2005, so some or all of their first-year commits are missing (median regular committers {cv_['committers_short']:.0f}, "
        f"against {cv_['committers_rest']:.0f} for the rest; {cv_['short_mail']} also started before the mail file). Without them: size AUC {cv_['primary_rest']['auc_size']:.3f}, shape gain {_sg(cv_['primary_rest']['gain'])} "
        f"({_pv(cv_['primary_rest']['perm_p'])}), interaction {_pv(cv_['primary_rest']['int_p'])}; the development-list lead {_sg(cv_['lead_rest']['gain'])} ({_pv(cv_['lead_rest']['perm_p'])}). Nothing turns on them.")
    add("- **Era.** Outcomes by start year of the podling (graduated / retired): "
        + "; ".join(f"{e['label']}: {e['grad']} / {e['ret']}" for e in D["by_era"])
        + ". The Incubator's practice changed over these years, and magnitudes here are era-bound (`models/00-v0.md` 0.6); section 7 splits at 2012 and adds the start year as a control.")
    ar = D["activity_robot_share"]
    add(f"- **Pseudonyms and robots.** {D['persons']:,} addresses become project-local integers (a one-way hash with a per-build random salt that is never stored, then relabelled by first appearance); "
        f"{D['robot_pseudonyms']:,} are flagged as automated (JIRA, GitHub and CI relays, commit-notification senders and the like, by address or display-name pattern, and {D['relay_added']} by a behavioural relay rule). "
        f"They carry {_pct(ar['commits'])} of commit events but {_pct(ar['msg_human'])} of the messages on human lists: most \"dev\" traffic in this dataset is tracker mail. Human lists are every list except "
        f"commits, issues, notifications, reviews and the like (`HUMAN_LIST_RULE`).")
    add("- **Privacy.** The raw files carry names and addresses (L4623). They were read once, as a stream. The derived arrays hold integers only (`derived/*.npz`, `meta.json`: project and list names, counts); "
        "no name, address or text is in the repo, this file or the tests' output (a test scans this file for the at-sign of an address).")
    add("")

    # ------------------------------------------------------------------ 2 method
    add("## 2. Method")
    add("")
    add("- **Unit and landmark.** A podling is at risk at month W if it is still in the Incubator then (exit month >= W). Features come from months 0 to W-1 only, so nothing from the exit leaks in. "
        f"Primary W = 12: {R['tab_counts']['at_risk']} podlings at risk ({R['tab_counts']['grad']} graduated, {R['tab_counts']['ret']} retired); the {D['resolved'] - R['tab_counts']['at_risk']} that exit earlier "
        "are in the survival form (section 6).")
    add("- **Activity.** An *event* is a distinct commit or a message on a human list sent by a non-automated pseudonym. A *regular member* is active (at least one event) in at least a quarter of the window's months "
        f"(3 of 12). The shape block needs at least 3 regular members ({R['tab_counts']['n_lt3']} podlings have fewer). Median n = {R['tab_counts']['n_quantiles'][2]:.0f} "
        f"(quartiles {R['tab_counts']['n_quantiles'][1]:.0f} and {R['tab_counts']['n_quantiles'][3]:.0f}); with the looser *any-event* rule the median is {R['tab_any_counts']['n_quantiles'][2]:.0f}, a crowd rather than a team.")
    add("- **Shape and mean.** From the per-member totals a_i in the window: n; mean = T/n; the Gini coefficient rescaled by n/(n-1); the top-1 and top-3 shares; the entropy of the shares over ln n. Variations add the effective number, "
        "Theil, the coefficient of variation, the share of one-event members, and the profile of the five largest shares.")
    add("- **Models and scores.** Ridge logistic regression (penalty 1 on standardised inputs; intercept free), five-fold stratified cross-validation repeated "
        f"{R['repeats']} times, predictions averaged over repeats, AUC of the out-of-fold predictions for *graduation*. Intervals are percentile bootstraps of those fixed predictions (positives and negatives resampled "
        "separately); the standard error of Hanley and McNeil gives the scale for variants. The survival form and the member panel hold out whole podlings.")
    add(f"- **The nulls.** (1) *Shape adds nothing given size and mean*: the shape rows are permuted across podlings ({R['perms']} times), which keeps the penalty for carrying useless columns; p is the share of permuted gains at least the observed one. "
        "A free permutation also breaks the shape-size correlation that the hypothesis keeps (top-k shares fall with n, the Gini rises with it), so its null is not quite the hypothesis's; "
        f"the p from permuting within size quintiles, which keeps most of that correlation, is shown beside it (for the primary the two nulls' mean gains are {h1['gain']['perm_null_mean']:+.4f} and "
        f"{h1['gain']['perm_null_mean_strat']:+.4f}), as is a nested likelihood-ratio test. "
        "(2) *Members are interchangeable*: the same events spread by chance over the same number of members give a Gini of "
        f"{h1['gini_null_median']:.2f} (median); the observed median is {h1['gini_obs_median']:.2f}, so activity is far more concentrated than chance, as in every contribution system. "
        "(3) *Early warning*: the retired against graduated contrast, a within-project comparison against the same project's earlier windows, and a simulation of a true slowing down for power. "
        "(4) *Coupling*: the held-out gain of D2 over D1, with the cluster bootstrap over podlings. (5) *Critical mass*: step against smooth, on held-out log-loss.")
    add("- **Pre-specified, and what was looked at first.** Fixed before any outcome relation was computed: the unit and landmark, the activity measure, the human-list rule, the robot patterns, the shape block, "
        "the model and scoring, the decision rules (gain > 0 with permutation p < 0.05; Gini against mean by the paired bootstrap; shape-by-size interaction p < 0.05; early warning by the one-sided "
        "Mann-Whitney test on monthly series, 6-month windows, 12 windows, lag 1; growth by Fisher's test; D2 by a gain above 0.01 AUC; step against smooth). Descriptive looks that came first and did not involve the outcome relation: the list inventory, the label counts "
        "and exit-month distribution, the lag between the last activity and the exit, the robot-share and the top senders' behaviour. **Two changes after a first look.** (i) A first run at W = 12 used *any event* as "
        "the member rule; its median n was 56, a crowd, so the member rule became \"regular\" (3 of 12 months). The same printout showed raw AUCs, so this change was not outcome-blind; "
        f"the any-event rule is reported in full in section 7 (gain {hp['gain']['diff']:+.3f}, permutation {_pv(hp['gain']['perm_p'])}), and gives the same answer. (ii) The first build flagged robots by address only; "
        "after seeing that its top senders were relays it gained display-name patterns and the relay rule (no outcome involved). The monthly early-warning grid (eight configurations) was explored before the (6, 12, lag 1) design was named primary, "
        "and the weekly series (four configurations) was added after the monthly power simulation showed that the monthly test had no power, so their p-values are descriptive, not confirmatory. "
        "The survival form, the step-against-smooth comparison and the D1/D2 panel were each run once in exploration (same code, fewer resamples) before this run; "
        "after seeing those runs the code gained the detrending option, the weekly series, the era split and the robustness checks of the size interaction, and nothing in the definitions was changed. "
        "The conversation lead of section 7.4 came out of the variation grid of section 7.2, which is a search, and was then re-examined (windows, eras, robots) on the same data. "
        "Added at review (2026-11-01), after every result here had been seen, and so checks rather than tests: the permutation within size quintiles, the one-term split of the size interaction, "
        "the paired comparison of model forms with size alone, the coverage check of section 1, the lead by size half, and the counting of each distinct test once in the corrections.")
    add("")

    # ------------------------------------------------------------------ 3 H1
    add("## 3. Does the distribution beat the mean? (question 1)")
    add("")
    add(f"Primary specification: W = 12, events, robots dropped, regular members, n >= 3: {h1['N']} podlings ({h1['grad']} graduated, {h1['ret']} retired); {h1['excluded_small']} with fewer than 3 regular members are left out "
        f"({h1['excluded_small_ret']} of them retired).")
    add("")
    add("**Single features, held out** (the sign is learned in the training folds; \"raw AUC\" fixes the orientation, above 0.5 meaning a higher value goes with graduation):")
    add("")
    add("| feature | held-out AUC for graduation [95%] | raw AUC |")
    add("|---|---|---|")
    for k, v in h1["single"].items():
        add(f"| {k} | {_ci(v)} | {v['raw_auc']:.3f} |")
    add("")
    add("**Models, held out:**")
    add("")
    add("| model | AUC [95%] | log-loss |")
    add("|---|---|---|")
    for k, v in h1["model"].items():
        add(f"| {k} | {_ci(v)} | {v['logloss']:.3f} |")
    add("")
    gp = h1["gain"]
    add(f"- *Gain from adding the shape block to size and mean:* {gp['diff']:+.4f} AUC (paired bootstrap {gp['lo']:+.4f} to {gp['hi']:+.4f}); permutation {_pv(gp['perm_p'])} "
        f"(the permuted gains average {gp['perm_null_mean']:+.4f}, 95th percentile {gp['perm_null_q95']:+.4f}); permuted within size quintiles {_pv(gp['perm_p_strat'])}; "
        f"likelihood-ratio statistic {h1['lr']['stat']:.2f} on {h1['lr']['df']} df, {_pv(h1['lr']['p'])}. "
        f"**Decision rule: {'met' if dec['H1_gain'] else 'not met'}.**")
    add(f"- *Gini against mean, the pre-specified single comparison:* held-out AUC {h1['single']['shape gini']['auc']:.3f} against {h1['single']['mean ln(T/n)']['auc']:.3f}; paired difference {dg['diff']:+.3f} "
        f"({dg['lo']:+.3f} to {dg['hi']:+.3f}). **{'Met' if dec['H1_gini_vs_mean'] else 'Not met'}.** The best of the four shape features (`{h1['best_shape']}`) differs from the mean by "
        f"{h1['diff_best_shape_vs_mean']['diff']:+.3f} ({h1['diff_best_shape_vs_mean']['lo']:+.3f} to {h1['diff_best_shape_vs_mean']['hi']:+.3f}); it was picked as the best of four on the same predictions, so that figure is biased upward.")
    add(f"- *Shape alone against mean alone, as models:* {h1['shape_vs_mean_models']['diff']:+.3f} ({h1['shape_vs_mean_models']['lo']:+.3f} to {h1['shape_vs_mean_models']['hi']:+.3f}). "
        "Shape \"beats\" the mean in this narrow sense, but the shape measures carry n (top-k share and Gini move with it; section 4), and once size is in the model they add nothing.")
    add("- *Standardised coefficients of the full ridge model:* " + ", ".join(f"{k} {v:+.2f}" for k, v in h1["coef"].items()) + ". Size carries the signal.")
    add("")
    add("**Reading for Claim 1.** Claim 1 is about the *threshold* distribution of a cascade law: no summary of it fixes the equilibrium (L1225, L1831). Activity is not thresholds. This test asks the weaker, measurable question "
        f"whether the distribution of *engagement* carries outcome information the mean does not, once the group's size is known, and on these {h1['N']} podlings, for commits plus messages, it does not. For the conversation alone it may (section 7.4). That is not a refutation or a support of Claim 1 (thresholds are unobserved here): "
        "the engagement shape is not a free predictor of success, and where it is one, the measure matters.")
    add("")

    # ------------------------------------------------------------------ 4 size
    add("## 4. What changes with n (question 2)")
    add("")
    add("n is the number of regular members in the first year. Size ranges follow the scales of v0 (a team is 8 to 12). Graduation rate with a 95% Wilson interval, and the raw (in-sample) AUC of each "
        "quantity for graduation *within* the band, with a bootstrap interval, where the band has at least 5 of each outcome. "
        f"{R['tab_counts']['n0']} podlings with no regular member at all ({R['tab_counts']['n0_ret']} of them retired) belong to no band:")
    add("")
    add("| n | podlings | graduated / retired | graduation rate [95%] | median events per member | median Gini | AUC of Gini | AUC of mean | AUC of total |")
    add("|---|---|---|---|---|---|---|---|---|")
    for b in sz["bins"]:
        def cell(k):
            return _ci({"auc": b[k][0], "lo": b[k][1], "hi": b[k][2]}, digits=2) if k in b else "-"
        add(f"| {b['label']} | {b['N']} | {b['grad']} / {b['ret']} | {_pct(b['rate'])} [{_pct(b['wilson'][0])}, {_pct(b['wilson'][1])}] | {b['median_mean']:.0f} | "
            f"{'-' if math.isnan(b['median_gini']) else format(b['median_gini'], '.2f')} | {cell('auc_gini')} | {cell('auc_mean')} | {cell('auc_T')} |")
    add("")
    add(f"- *Size is linked to concentration and to the mean:* Spearman rho between n and the Gini = {sz['spearman_n_gini'][0]:+.2f} ({_pv(sz['spearman_n_gini'][1])}); between n and events per member = "
        f"{sz['spearman_n_mean'][0]:+.2f}. Larger projects are more concentrated and busier per member, which is why a shape-only model looks good and a size-aware one does not need it.")
    bd5 = next((b for b in sz["bins"] if b["label"] == "5-7"), None)
    nb_auc = sum(1 for b in sz["bins"] for k in ("auc_gini", "auc_mean", "auc_T") if k in b)
    rev = (f"{bd5['N']} podlings ({bd5['grad']} / {bd5['ret']}), its interval reaches {bd5['auc_gini'][2]:.2f}, and it is one of {nb_auc} within-band AUCs, so chance is not excluded."
           if bd5 is not None and "auc_gini" in bd5 else "too few podlings for an AUC.")
    add(f"- *The shape-by-size interaction (pre-specified):* adding Gini x ln n and mean x ln n to {{ln n, ln mean, Gini}} improves the likelihood by {ih['stat']:.1f} on {ih['df']} df, {_pv(ih['p'])} (parametric bootstrap under the main-effects model, 1,000 draws: p = {sz['interaction_boot_p']:.4f}; "
        f"with the Gini replaced by its rank {_pv(sz['interaction_rank_p'])}; with ln T as the moderator {_pv(sz['interaction_lnT_p'])}). "
        f"The 2-df test also holds mean x ln n; taken one at a time, each given the other, Gini x ln n gives {sz['interaction_gini_lr']['stat']:.1f} on 1 df ({_pv(sz['interaction_gini_lr']['p'])}) "
        f"and mean x ln n {sz['interaction_mean_lr']['stat']:.1f} ({_pv(sz['interaction_mean_lr']['p'])}), so the concentration term carries it. "
        "Standardised coefficients: " + ", ".join(f"{k} {v:+.2f}" for k, v in sz["interaction_coef"].items()) + ". "
        f"Split at the median size ({sz['split_median_n']:.0f}; a post hoc split): at or below it the Gini coefficient is {sz.get('coef_gini_small', float('nan')):+.2f} (standardised, ridge) with raw AUC {sz.get('auc_gini_small', float('nan')):.2f} "
        f"({sz.get('N_small', 0)} podlings); above it {sz.get('coef_gini_large', float('nan')):+.2f} with AUC {sz.get('auc_gini_large', float('nan')):.2f} ({sz.get('N_large', 0)} podlings). "
        "In the larger projects a concentrated core goes with graduation; in the smaller ones concentration is uninformative. This is the form of L5779 (the sign of a group-size effect depends on a return) and L5740 "
        "(stability depends on turnover and size): a *sign flag that is a setting operand*, as `models/00-v0.md` 0.6 rule 5 already requires, here with n as the moderator. The mechanism is not in the data. Part of the weaker association at small n may be estimation noise (a Gini from five members is a noisy "
        "measure of concentration, which attenuates an effect rather than reversing it); attenuation alone would not give the reversal in the 5 to 7 band, but that band holds " + rev)
    for nm in ("small", "large"):
        if nm in hg:
            hh = hg[nm]
            add(f"- *Shape gain within the {nm} half (post hoc):* {hh['N']} podlings, {hh['ret']} retired; AUC {hh['auc_base']:.3f} for size + mean and {hh['auc_full']:.3f} with shape: gain {hh['gain']:+.3f}, permutation {_pv(hh['perm_p'])}.")
    sp = R["size_participants"]
    add(f"- *With the looser any-event rule* (members = anyone who posted or committed once, a crowd): the interaction {_pv(sp['interaction_lr']['p'])}, "
        f"graduation rate by band " + ", ".join(f"{b['label']}: {_pct(b['rate'])}" for b in sp["bins"]) + ".")
    bd = {b["label"]: b for b in sz["bins"]}
    team = bd.get("8-12")
    if team:
        def _excl(b, k):
            return k in b and (b[k][2] < 0.5 or b[k][1] > 0.5)
        sep = [lab for lab in ("5-7", "8-12", "13-25", "26+") if lab in bd and _excl(bd[lab], "auc_gini")]
        txt = (f"- *The team band.* At 8 to 12 regular members the graduation rate is {_pct(team['rate'])} ({team['grad']}/{team['N']}), "
               f"and at 5 to 7 it is {_pct(bd['5-7']['rate'])} ({bd['5-7']['grad']}/{bd['5-7']['N']}): retirement is about as likely as graduation. "
               f"In the 8 to 12 band the Gini has AUC {team['auc_gini'][0]:.2f} ({team['auc_gini'][1]:.2f} to {team['auc_gini'][2]:.2f}), the mean {team['auc_mean'][0]:.2f}, the total {team['auc_T'][0]:.2f}: "
               "none separates the outcomes there. ")
        if sep:
            txt += ("The within-band Gini intervals exclude 0.5 in: " + ", ".join(f"{lab} (AUC {bd[lab]['auc_gini'][0]:.2f})" for lab in sep)
                    + f". A reversal of sign from the smallest bands to the largest is what the interaction says; the bands with an AUC hold {min(b['ret'] for b in sz['bins'] if 'auc_gini' in b)} to "
                    f"{max(b['ret'] for b in sz['bins'] if 'auc_gini' in b)} retired podlings each, so it is a pattern to test, not a result.")
        add(txt)
    add("")

    # ------------------------------------------------------------------ 5 cascade
    add("## 5. Cascade and escalation analogues (question 3)")
    add("")
    add("### 5.1 Sustained growth against decline, over the first year")
    add("")
    add("The log ratio of events in months 6 to 11 to those in months 0 to 5 (each plus one). Growth is a ratio of at least 1.5, decline of at most 2/3 (`growth_cut`, fixed in advance).")
    add("")
    add("| first-year trajectory | podlings | graduated / retired | graduation rate |")
    add("|---|---|---|---|")
    for c in ("growth", "steady", "decline"):
        v = gr["classes"][c]
        add(f"| {c} | {v['N']} | {v['grad']} / {v['ret']} | {_pct(v['rate'])} |")
    add("")
    add(f"Growth against decline: Fisher {_pv(gr['fisher_growth_vs_decline'])}; the log ratio as a single predictor has AUC {gr['auc_growth']:.2f} for graduation. **{'Met' if dec['growth'] else 'Not met'}.** "
        f"It adds little once size is known ({fm['forms']['size + growth']['auc']:.3f} for size + growth against {fm['forms']['size (ln n)']['auc']:.3f} for size), plausibly because growing projects are the ones that recruit.")
    add("")
    add("### 5.2 The whole pre-exit series (retrospective, not a predictor)")
    add("")
    add("Rolling six-month mean of events, last month dropped (the exit's own mail). *Ended at peak*: the final rolling mean is at least 80% of its maximum; *decayed*: at most 50%; *collapsed*: at most 20% of the "
        "maximum for the last six months; *in between*: otherwise.")
    add("")
    add("| trajectory | podlings | graduated / retired |")
    add("|---|---|---|")
    for c, v in tr["classes"].items():
        add(f"| {c} | {v['N']} | {v['grad']} / {v['ret']} |")
    add("")
    gtot = sum(v["grad"] for v in tr["classes"].values())
    rtot = sum(v["ret"] for v in tr["classes"].values())
    pk = tr["classes"]["ended at peak"]["grad"] + tr["classes"]["in between"]["grad"]
    dc = tr["classes"]["decayed"]["ret"] + tr["classes"]["collapsed"]["ret"]
    add(f"{_pct(pk / gtot)} of the graduated projects ended at or near their peak (or in between), and {_pct(dc / rtot)} of the retired ones decayed or collapsed; "
        f"collapse alone is {tr['classes']['collapsed']['ret']} of the {tr['classes']['collapsed']['N']} collapsed projects retiring. That is a description of the series in hindsight, and the exit is partly the reason for it.")
    add("")
    add("### 5.3 Early-warning signals before retirement")
    add("")
    add("Series: ln(1 + events) per month. Rolling window w, linear detrending inside the window (or only mean removal), lag-1 autocorrelation (AR1) and standard deviation (SD) per window; "
        "Kendall's tau of each against time over the L windows before the reference month. The series used ends at the month *before* the reference month, and the reference month is the exit month minus *lag*: "
        "lag 0 drops the exit month (the exit's own mail), lag 1 also the month before it, lag 3 the three before that. Retired podlings are the \"transition\" cases; graduated ones are the contrast "
        "(graduation is also an exit, and not a fold bifurcation). AUC is for *retired* (a higher tau means retired); the alarm share counts tau > 0.5; p is one-sided Mann-Whitney.")
    add("")
    add("| w | L | lag | detrend | podlings (retired / graduated) | AR1: AUC [95%], p, alarm retired / graduated | SD: AUC [95%], p, alarm retired / graduated | level trend: AUC for retired |")
    add("|---|---|---|---|---|---|---|---|")
    n_lt = {"ar1": 0, "sd": 0}
    n_tot = 0
    for r in R["ews"] + R["ews_weekly"]:
        a_, s_, lv = r["tau_ar1"], r["tau_sd"], r["tau_level"]
        if "auc" not in a_:
            continue
        n_tot += 1
        n_lt["ar1"] += a_["p_mwu"] < 0.05
        n_lt["sd"] += s_["p_mwu"] < 0.05
        unit = "w" if r in R["ews_weekly"] else "m"
        add(f"| {r['w']}{unit} | {r['L']}{unit} | {r['lag']} | {r['detrend']} | {r['N']} ({r['ret']} / {r['grad']}) | {_ci(a_, digits=2)}, {_p(a_['p_mwu'])}, {_pct(a_['alarm_ret'])} / {_pct(a_['alarm_grad'])} | "
            f"{_ci(s_, digits=2)}, {_p(s_['p_mwu'])}, {_pct(s_['alarm_ret'])} / {_pct(s_['alarm_grad'])} | {lv['auc']:.2f} |")
    add("")
    add(f"- The rows with *m* are monthly series, the rows with *w* weekly series (a variation added after the power check below). The primary monthly design is the first row (w = 6, L = 12, lag 1). "
        f"**Autocorrelation: {'met' if dec['ews_ar1'] else 'not met'}; variance: {'met' if dec['ews_sd'] else 'not met'}** (one-sided Mann-Whitney p < 0.05). "
        f"Over all {n_tot} configurations, {n_lt['ar1']} reach p < 0.05 for autocorrelation and {n_lt['sd']} for variance; {2 * n_tot} tests were run, so {0.05 * 2 * n_tot:.1f} such values are expected by chance, and the grid was explored before the primary was named.")
    add("- Alarms at tau > 0.5 are about as common among graduated projects as among retired ones: the poor specificity of Helmich et al. 2023 (L0547, L3057: rising autocorrelation before 89% of transitions and before 62.5% of non-transitions) "
        "appears here as low sensitivity together with no separation.")
    add("- The *level* trend, which is the growth-or-collapse signal, separates the groups strongly and in the expected direction (last column: AUC for retired far below 0.5, so graduated projects trend up). "
        "Slowing-down statistics are built to be independent of such a drift; here the drift is the information and the slowing-down statistics are not.")
    add("")
    add("**Within-project time-matched comparison** (monthly, w = 6, L = 12; weekly, w = 26, L = 52). For each project, where does the pre-exit tau sit among the taus at every earlier reference month whose window does not overlap? "
        "u is the share of those earlier taus below the observed one (0.5 under no signal). Only podlings with at least 5 non-overlapping earlier references qualify (long series).")
    add("")
    add("| design | group | indicator | podlings | mean u | Wilcoxon p (two-sided) | Holm p (over these rows) |")
    add("|---|---|---|---|---|---|---|")
    for r in tmf:
        add(f"| w={r['key'][0]}{r['unit']}, L={r['key'][1]}{r['unit']}, lag {r['key'][2]} | {r['group']} | {'AR1' if r['ind'] == 'u_ar1' else 'SD'} | {r['n']} | {r['mean_u']:.3f} | "
            f"{_p(r['p'])} | {_p(r['holm'])} |")
    add("")
    add("**Power: could these tests have seen a true slowing down?** Simulated AR(1) series whose coefficient rises from 0.3 to 0.9 over the last L + w points, against constant 0.3, passed through the same windows, detrending and Kendall statistic "
        "(noise sd fixed, so the variance rises too). AUC for telling them apart, and the share above tau 0.5 in each:")
    add("")
    add("| series | w | L | detrend | AUC (AR1) | AUC (SD) | alarm AR1: slowing / flat | alarm SD: slowing / flat |")
    add("|---|---|---|---|---|---|---|---|")
    for r in R["ews_power"]:
        add(f"| {r['unit']} | {r['w']} | {r['L']} | {r['detrend']} | {r['auc_ar1']:.2f} | {r['auc_sd']:.2f} | {_pct(r['alarm_tp_ar1'])} / {_pct(r['alarm_fp_ar1'])} | {_pct(r['alarm_tp_sd'])} / {_pct(r['alarm_fp_sd'])} |")
    add("")
    pm = next(r for r in R["ews_power"] if r["unit"] == "months" and r["detrend"] == "linear" and r["w"] == 6)
    pwk = next(r for r in R["ews_power"] if r["unit"] == "weeks" and r["detrend"] == "linear" and r["w"] == 26)
    w0 = R["ews_weekly"][0]
    add(f"At the monthly series lengths this dataset allows (a podling lives {q['graduated'][1]:.0f} to {q['retired'][1]:.0f} months at the median) the statistics barely separate a true critical slowing down from none "
        f"(AUC {pm['auc_ar1']:.2f} for autocorrelation, {pm['auc_sd']:.2f} for variance at 6 and 12), with either detrending, so the monthly null says nothing. At weekly resolution (26-week windows, 52 windows) the same simulated signal is "
        f"caught with AUC {pwk['auc_ar1']:.2f} (autocorrelation) and {pwk['auc_sd']:.2f} (variance), and there the data give {w0['tau_ar1']['auc']:.2f} ({w0['tau_ar1']['lo']:.2f} to {w0['tau_ar1']['hi']:.2f}) and "
        f"{w0['tau_sd']['auc']:.2f} ({w0['tau_sd']['lo']:.2f} to {w0['tau_sd']['hi']:.2f}) for retired against graduated: the upper ends are far below the simulated strength. "
        "A slowing down as strong as that one (the lag-1 coefficient rising from 0.3 to 0.9 in the year before the exit) is therefore not there; a weaker one cannot be excluded, and the retirement date is administrative, "
        "so the reference point is blurred. Pull-request latency or issue turnaround, which have a recovery time built in, would be a better series than counts.")
    add(f"Within the retired projects' own histories (weekly, lag 0; {tm_sd['n']} long series) the variance trend before the exit sits at {tm_sd['mean_u']:.2f} of the project's earlier windows "
        f"(Wilcoxon {_pv(tm_sd['p'])}, nominal: the weekly design came after the power check, and over the {len(tmf)} within-project rows above Holm gives {_p(tm_sd['holm'])}). "
        "If real, variance falls before retirement, as it does when activity decays towards zero: the opposite of critical slowing down.")
    add("")
    add("### 5.4 A critical mass: step against smooth")
    add("")
    st = fm["step"]
    add(f"The group-level analogue of an ignition point (Claim 1.4): does the graduation probability jump at a threshold in early size? The step model chooses its cut on the training folds from the 10th to 90th "
        f"percentile of ln n; the smooth model is a logistic in ln n. Held-out log-loss: base rate {fm['null_logloss']:.3f}, smooth {st['smooth_logloss']:.3f}, step {st['step_logloss']:.3f}; AUC {st['smooth_auc']:.3f} against {st['step_auc']:.3f}. "
        f"The best cut on all the data is {np.exp(st['cut']):.0f} regular members ({_pct(st['p_below'])} graduate below, {_pct(st['p_above'])} above; {st['n_below']} and {st['n_above']} podlings). "
        f"On total activity ln T the two are {'tied' if abs(fm['step_T']['step_logloss'] - fm['step_T']['smooth_logloss']) < 0.005 else 'not tied'} ({fm['step_T']['step_logloss']:.3f} against {fm['step_T']['smooth_logloss']:.3f}). **{'Step preferred' if dec['step_preferred'] else 'Smooth preferred'}.** "
        "There is no ignition point to find in this sample: more regular members means more graduation, steadily.")
    add("")
    add("### 5.5 Individual dynamics (D1) against coupling (D2), for who stays active")
    add("")
    add(f"A member-month panel: {d12['rows']:,} rows from {d12['projects']} podlings; a member is eligible once active in two distinct months, the outcome is activity in the next month (base rate {_pct(d12['base_rate'])}), "
        "whole podlings are held out. **D1** is her own state: active now, last month and the month before, the share of her months since her first that were active (her set point), her tenure and her volume now. "
        "**D2** adds the share of the *other* eligible members active now and last month and their volume now.")
    add("")
    add("| model | AUC | log-loss |")
    add("|---|---|---|")
    for k in ("D1", "D1 + D2", "D1 + D2 + s^2"):
        add(f"| {k} | {d12[k]['auc']:.4f} | {d12[k]['logloss']:.4f} |")
    add("")
    add(f"D2 gain: {d12['D2 gain']['diff']:+.4f} AUC ({d12['D2 gain']['lo']:+.4f} to {d12['D2 gain']['hi']:+.4f}; cluster bootstrap over podlings), log-loss {d12['D2 gain']['dlogloss']:+.4f}. "
        f"Quadratic term: {d12['quadratic gain']['diff']:+.4f} AUC. **{'D2 adds' if dec['d2'] else 'D2 adds nothing material'}** (rule: a gain above 0.01). "
        "Standardised coefficients: " + ", ".join(f"{k} {v:+.2f}" for k, v in d12["coef"].items()) + ". "
        "The interval excludes 0 because the gain, though tiny, recurs across podlings; it is a thousandth of the AUC. Own volume and own rate dominate.")
    for nm in ("small teams (<=10 eligible)", "larger (>10)"):
        if nm in d12:
            v = d12[nm]
            add(f"- {nm}: {v['rows']:,} rows; AUC {v['d1_auc']:.3f} for D1, {v['d12_auc']:.3f} with D2; log-loss change {v['dlogloss']:+.4f}.")
    add("")
    add("The response curve (members active next month against the others' active share now, by decile) rises steadily, and the D1-only prediction rises with it almost exactly: the share of others active is mostly "
        "the average of the members' own states, which D1 already holds. No knee appears.")
    add("")
    add("| mean share of others active | active next month (observed) | D1-predicted | rows |")
    add("|---|---|---|---|")
    for c in d12["curve"]:
        add(f"| {c[0]:.2f} | {c[1]:.3f} | {c[2]:.3f} | {c[3]:,} |")
    add("")
    add("Caveat that cuts the other way from the usual one: the others' share is a project-month quantity that all members share, so it is confounded with common shocks (a release, a holiday), which would *inflate* the apparent coupling. "
        "That the gain is still negligible makes the null stronger, not weaker. It does not make coupling absent: monthly counts are a coarse channel for what 098 measured per six seconds.")
    add("")

    # ------------------------------------------------------------------ 6 survival form
    add("## 6. The survival form: retirement and graduation within the next six months")
    add("")
    hz = haz["y_ret"]
    hg_ = haz["y_grad"]
    add(f"One row per podling and origin month (every third month from month 6 while still incubating), features from the trailing six months, outcome: retires (or graduates) within the next six months; "
        f"{hz['rows']:,} rows from {hz['projects']} podlings, {hz['events']} retirement events in {hz['event_projects']} podlings and {hg_['events']} graduation events in {hg_['event_projects']}. "
        f"Whole podlings are held out; intervals are cluster bootstraps over podlings. Tenure (ln of the origin month) is in the base because graduates leave early (median {q['graduated'][1]:.0f} months) "
        f"and retirees late ({q['retired'][1]:.0f}).")
    add("")
    add("| outcome within 6 months | tenure + size + mean | + shape | + growth | + shape + growth | shape gain [95%] | growth gain [95%] |")
    add("|---|---|---|---|---|---|---|")
    for lab, h in (("retires", hz), ("graduates", hg_)):
        add(f"| {lab} | {h['tenure+size+mean']['auc']:.3f} | {h['+ shape']['auc']:.3f} | {h['+ growth']['auc']:.3f} | {h['+ shape + growth']['auc']:.3f} | "
            f"{h['shape gain']['diff']:+.3f} [{h['shape gain']['lo']:+.3f}, {h['shape gain']['hi']:+.3f}] | "
            f"{h['growth gain']['diff']:+.3f} [{h['growth gain']['lo']:+.3f}, {h['growth gain']['hi']:+.3f}] |")
    add("")
    add("The conclusion of section 3 holds in the survival form: the shape of the distribution adds a few thousandths of AUC to the six-month retirement ranking, with an interval that includes zero, and nothing to the graduation ranking. "
        f"What does the work is tenure, size and the mean ({hz['tenure+size+mean']['auc']:.2f} for retirement, {hg_['tenure+size+mean']['auc']:.2f} for graduation).")
    add("")

    # ------------------------------------------------------------------ 7 variations
    add("## 7. Variations")
    add("")
    add("### 7.1 The primary window under different model forms")
    add("")
    add(f"Same {fm['N']} podlings ({fm['grad']} graduated, {fm['ret']} retired), same folds; held-out AUC for graduation, its Hanley-McNeil standard error (the uncertainty of that one AUC), log-loss "
        f"(base rate {fm['null_logloss']:.3f}), and the AUC minus that of size alone with a paired bootstrap of the fixed predictions: two forms scored on the same podlings differ by far less than either s.e., "
        "so a difference is read against the paired interval.")
    add("")
    add("| model form | AUC | s.e. | log-loss | minus size alone [paired 95%] |")
    add("|---|---|---|---|---|")
    ranked = sorted(fm["forms"].items(), key=lambda kv: -kv[1]["auc"])
    for k, v in ranked:
        vs = v.get("vs_size")
        cell_vs = "-" if vs is None else f"{_sg(vs[0])} [{_sg(vs[1])}, {_sg(vs[2])}]"
        add(f"| {k} | {v['auc']:.3f} | {v['se']:.3f} | {v['logloss']:.3f} | {cell_vs} |")
    best_k, best_v = ranked[0]
    sep_up = [k for k, v in ranked if "vs_size" in v and v["vs_size"][1] > 0]
    sep_dn = [k for k, v in ranked if "vs_size" in v and v["vs_size"][2] < 0]
    add("")
    nosize = [k for k in fm["forms"] if "size" not in k]
    add(f"**Best fit by held-out AUC: {best_k}** ({best_v['auc']:.3f}, against {fm['forms']['size (ln n)']['auc']:.3f} for plain size). "
        + (f"The forms whose paired interval against size alone lies above zero: {', '.join(sep_up)}. " if sep_up else "No form's paired interval against size alone lies above zero. ")
        + f"They were picked from {len(ranked)} forms on the same predictions, the interaction forms were added because the size interaction was tested, and the paired intervals hold the predictions fixed "
        "(they leave out the variation from refitting), so any such edge is biased upward: it backs the interaction of section 4 and is not a separate finding. The forms without size are "
        + ", ".join(f"{k} ({fm['forms'][k]['auc']:.2f})" for k in nosize)
        + ": the shape block recovers most of size's signal because its members move with n, and the mean per member has almost none. "
        + ("The step on size is the worst of the size-based forms and is below size alone. " if "step on size (cut chosen in training folds)" in sep_dn else "The step on size is the worst of the size-based forms. ")
        + f"By held-out log-loss the three best are {', '.join(k for k, _ in sorted(fm['forms'].items(), key=lambda kv: kv[1]['logloss'])[:3])}.")
    add("")
    add("### 7.2 Window, activity measure, robots, member rule, shape measure, regularisation, dynamics (one factor at a time)")
    add("")
    add("Held-out AUC (10 repeats) for graduation of size, mean, size + mean, size + mean + shape; the shape gain with its permutation p (200 draws) and Holm-adjusted p across the "
        "distinct shape-gain tests in this table (a row that repeats the primary's test says so and is counted once; a row whose shape column is constant is no test); the p of the shape-by-size interaction (Gini).")
    add("")
    vr = R["variations"]
    gain_idx = grid_family(vr)
    holm = dict(zip(gain_idx, _holm([vr[i]["perm_p"] for i in gain_idx])))
    ndup = sum(1 for r in vr if r.get("same_as_primary"))
    ndeg = sum(1 for r in vr if r.get("degenerate"))

    def _holm_cell(i, r):
        if r.get("same_as_primary"):
            return "= primary"
        if r.get("degenerate"):
            return "constant"
        return _p(holm[i]) if i in holm else "-"
    add("| factor | variant | podlings (retired) | size | mean | size + mean | + shape | gain | perm p | Holm p | interaction p |")
    add("|---|---|---|---|---|---|---|---|---|---|---|")
    for i, r in enumerate(vr):
        if "auc_base" not in r:
            add(f"| {r['group']} | {r['label']} | {r['N']} | too few | | | | | | | |")
            continue
        add(f"| {r['group']} | {r['label']} | {r['N']} ({r['ret']}) | {r['auc_size']:.3f} | {r['auc_mean']:.3f} | {r['auc_base']:.3f} | {r.get('auc_full', float('nan')):.3f} | "
            f"{r.get('gain', float('nan')):+.3f} | {_p(r['perm_p']) if 'perm_p' in r else '-'} | {_holm_cell(i, r)} | {_p(r['int_p']) if 'int_p' in r else '-'} |")
    add("")
    gains = [(vr[i]["gain"], vr[i]["label"], vr[i]["group"], vr[i]["perm_p"], holm[i]) for i in gain_idx]
    top = sorted(gains, reverse=True)[:3]
    nsig = sum(1 for i in gain_idx if vr[i]["perm_p"] < 0.05)
    sig_h = [f"{vr[i]['group']}: {vr[i]['label']}" for i in gain_idx if holm[i] < 0.05]
    add(f"- *Shape gain across the grid:* {len(vr)} rows hold {len(gain_idx)} distinct tests (the primary's own test recurs in {ndup + 1} rows and is counted once; {ndeg} row has a constant shape column: "
        f"the one-event share is 0 for every regular member, who has at least {regular_months(PRIMARY['W'])} events). {nsig} have a raw permutation p below 0.05 "
        f"({len(sig_h)} after Holm; p-values under 0.06 were re-run with 2,000 permutations). The largest gains are "
        + "; ".join(f"{g_:+.3f} ({gr_}: {lb})" for g_, lb, gr_, _, _ in top)
        + f". The median gain is {np.median([g_[0] for g_ in gains]):+.3f}. With {len(gain_idx)} correlated tests a few nominal p-values below 0.05 are expected by chance; "
        "the variants with a nominal gain are the three message-based measures and the 18-month window, which section 7.4 follows up; "
        + (f"after Holm over this grid only {', '.join(sig_h)} remain." if sig_h else "none of them survives the Holm correction over this grid."))
    dyn = [r for r in vr if r["group"] == "dynamics" and "auc_extra" in r]
    if dyn:
        add("- *Dynamics:* the two dynamics rows repeat the primary's shape test; their own result is the held-out AUC with the term added to size and mean: "
            + "; ".join(f"{r['label']}: {r['auc_extra']:.3f} (with the shape block too, {r['auc_all']:.3f})" for r in dyn)
            + f", against {vr[0]['auc_base']:.3f} for size and mean alone.")
    # the interaction test is unpenalised and uses only ln n, ln mean and the Gini, so every row on the same table is one test
    ints = [(r["label"], r["group"], r["int_p"], (r["N"], r["ret"], round(r["int_p"], 12))) for r in vr if "int_p" in r]
    seen, dints = set(), []
    for lb, g_, p_, k_ in ints:
        if k_ not in seen:
            seen.add(k_)
            dints.append((lb, g_, p_))
    nonsig = [f"{g_}: {lb}" for lb, g_, p_ in dints if p_ >= 0.05]
    nprim = sum(1 for *_, k_ in ints if k_ == ints[0][3])
    add(f"- *The shape-by-size interaction:* p < 0.05 in {sum(1 for _, _, p_ in dints if p_ < 0.05)} of the {len(dints)} distinct tables ({nprim} of the {len(ints)} rows use the primary's table, "
        "and the shape measures, the penalty and the added terms do not enter this unpenalised test). It is absent (p >= 0.05) for: " + "; ".join(nonsig)
        + ". These are the commit-only measures (few podlings have three regular committers), the shortest window, the two extreme member rules (anyone, and half the window's months) and the variant with robots kept.")
    both = [r for r in vr if "auc_base" in r]
    spread = max(max(r["auc_base"], r.get("auc_full", 0)) - r["auc_size"] for r in both)
    best_base = max(both, key=lambda r: r["auc_base"])
    best_full = max((r for r in vr if "auc_full" in r), key=lambda r: r["auc_full"])
    wbest = max((r for r in vr if r["group"] == "window"), key=lambda r: r["auc_size"])
    add(f"- *Which variant fits best:* by size + mean, `{best_base['group']}: {best_base['label']}` ({best_base['auc_base']:.3f}); by size + mean + shape, `{best_full['group']}: {best_full['label']}` ({best_full['auc_full']:.3f}). "
        f"In no row does size + mean or size + mean + shape beat size alone by more than {spread:.3f} AUC: the number of people active early is the predictor, however it is counted. "
        f"The best window for size is `{wbest['label']}` ({wbest['auc_size']:.3f}); later windows keep only the longer-lived podlings and fall in AUC.")
    era = {r["label"]: r for r in vr if r["group"] == "era"}
    if len(era) == 3:
        a_, b_, c_ = era["podlings started 2003-2012"], era["podlings started 2013-2021"], era["start year added to size and mean"]
        add(f"- *Era (drift):* size AUC {a_['auc_size']:.3f} for podlings started 2003-2012 ({a_['N']} podlings, {a_['ret']} retired) and {b_['auc_size']:.3f} for those started 2013-2021 ({b_['N']}, {b_['ret']}); "
            f"shape gain {a_.get('gain', float('nan')):+.3f} and {b_.get('gain', float('nan')):+.3f}; with the start year added to size and mean the AUC goes from {vr[0]['auc_base']:.3f} to {c_['auc_base']:.3f} "
            f"and the shape gain is {c_.get('gain', float('nan')):+.3f}. "
            + ("The size effect and the absence of a shape effect hold in both eras." if min(a_["auc_size"], b_["auc_size"]) > 0.65 and max(abs(a_.get("gain", 0)), abs(b_.get("gain", 0))) < 0.03
               else "The two eras differ; read the rows."))
    add("")
    add("### 7.3 The any-event (crowd) reading of question 1")
    add("")
    add(f"With every pseudonym who did anything counted as a member ({hp['N']} podlings, {hp['ret']} retired): size AUC {hp['single']['size ln n']['auc']:.3f}, mean {hp['single']['mean ln(T/n)']['auc']:.3f}, "
        f"Gini {hp['single']['shape gini']['auc']:.3f}; shape gain {hp['gain']['diff']:+.3f} (permutation {_pv(hp['gain']['perm_p'])}); likelihood ratio {_pv(hp['lr']['p'])}. The same answer.")
    add("")

    # ------------------------------------------------------------------ 8 caveats
    add("### 7.4 A lead: the concentration of conversation")
    add("")
    add("In the grid of 7.2 the three measures that count list messages only (all human lists, the development list, replies) show a larger shape gain than the combined measure, which adds commits. "
        f"This is the one place where the distribution of activity beats its mean. It is a **lead, not a result**: it came out of a search over {len(R['variations'])} variants, and the table below re-examines it on the same data, so its p-values "
        "are descriptive. Held-out AUC for graduation, 10 repeats; permutation p from 300 draws (so 0.003 is the floor), free and within size quintiles (the second keeps the shape-size correlation, section 2):")
    add("")
    add("| measure | variant | podlings (retired) | size | size + mean | + shape | gain | perm p | perm p within size quintiles |")
    add("|---|---|---|---|---|---|---|---|---|")
    for r in R["lead"]["rows"]:
        if "auc_base" not in r:
            continue
        add(f"| {r['measure']} | {r['label']} | {r['N']} ({r['ret']}) | {r['auc_size']:.3f} | {r['auc_base']:.3f} | {r['auc_full']:.3f} | {_sg(r['gain'])} | {_p(r['perm_p'])} | "
            f"{_p(r['perm_p_strat']) if 'perm_p_strat' in r else '-'} |")
    add("")
    add("The Gini alone against the mean alone (held out; paired bootstrap of the difference):")
    add("")
    add("| measure | window | podlings (retired) | Gini | mean | size | Gini minus mean [95%] | raw AUC of the Gini |")
    add("|---|---|---|---|---|---|---|---|")
    for (meas, W), v in R["lead"]["gini_vs_mean"].items():
        add(f"| {meas} | {W} | {v['N']} ({v['ret']}) | {v['gini']:.3f} | {v['mean']:.3f} | {v['size']:.3f} | {v['diff']:+.3f} [{v['lo']:+.3f}, {v['hi']:+.3f}] | {v['raw_gini']:.3f} |")
    add("")
    wrows = [r for r in R["lead"]["rows"] if r["kind"] == "window" and "gain" in r]
    pos = sum(1 for r in wrows if r["gain"] > 0)
    wp = [r["perm_p"] for r in wrows]
    wh = _holm(wp)
    ws = [r["perm_p_strat"] for r in wrows if "perm_p_strat" in r]
    wsh = _holm(ws) if ws else []
    add(f"- *Across windows:* the gain is positive in {pos} of {len(wrows)} measure-by-window cells ({min(r['gain'] for r in wrows):+.3f} to {max(r['gain'] for r in wrows):+.3f}); {sum(1 for p_ in wp if p_ < 0.05)} have a raw permutation p below 0.05 and "
        f"{sum(1 for p_ in wh if p_ < 0.05)} after Holm over these {len(wrows)} cells"
        + (f" (within size quintiles: {sum(1 for p_ in ws if p_ < 0.05)} and {sum(1 for p_ in wsh if p_ < 0.05)})" if ws else "")
        + f". The gain grows with the window (the long windows keep only the longer-lived podlings: {min(r['N'] for r in wrows if r['W'] == 18)} to {max(r['N'] for r in wrows if r['W'] == 18)} at 18 months).")
    cc = R["lead"]["cond_coef"]
    add("- *Direction, at a given size and mean:* the standardised logistic coefficient of each concentration measure when added alone to {ln n, ln mean}, with a bootstrap 95% interval "
        "(positive: more of it goes with graduation). The raw AUCs of the top-k shares are below 0.5 only because they fall with n; given n they point the other way.")
    add("")
    add("| measure | window | Gini | top-1 share | top-3 share | Theil | entropy |")
    add("|---|---|---|---|---|---|---|")
    for (meas, W), c in cc.items():
        add(f"| {meas} | {W} | " + " | ".join(f"{c[f][0]:+.2f} [{c[f][1]:+.2f}, {c[f][2]:+.2f}]" for f in ("gini", "top1", "top3", "theil", "entropy")) + " |")
    add("")
    sign = {"gini": 1, "top1": 1, "top3": 1, "theil": 1, "entropy": -1}
    same = sum(1 for c in cc.values() for f, sg_ in sign.items() if sg_ * c[f][0] > 0)
    excl = sum(1 for c in cc.values() for f in sign if c[f][1] > 0 or c[f][2] < 0)
    tot_ = len(cc) * len(sign)
    add(f"{same} of the {tot_} coefficients point to concentrated conversation going with graduation (a positive Gini, top-k share and Theil, a negative entropy), and {excl} of the {tot_} intervals exclude zero. "
        "They are not independent confirmations: three overlapping measures, two nested windows and five correlated shape measures on the same podlings.")
    lh = R["lead"]["halves"]
    add("")
    add(f"- *Size (post hoc):* split at its median ({lh['median_n']:.0f} members), the development-list gain at 12 months is {_sg(lh['small']['gain'])} at or below it "
        f"({lh['small']['N']} podlings, {lh['small']['ret']} retired; {_pv(lh['small']['perm_p'])}; raw Gini AUC {lh['small']['raw_gini']:.2f}) and {_sg(lh['large']['gain'])} above it "
        f"({lh['large']['N']}, {lh['large']['ret']} retired; {_pv(lh['large']['perm_p'])}; raw Gini AUC {lh['large']['raw_gini']:.2f}): larger in the larger projects, as the combined measure's interaction in section 4 is, "
        "on few retired podlings.")
    add("")
    eras = {(r["measure"], r["label"]): r for r in R["lead"]["rows"] if r["kind"] == "era"}
    add("- *Era:* " + "; ".join(f"{m_}: gain {_sg(eras[(m_, 'started 2003-2012')]['gain'], 2)} for podlings started 2003-2012 ({_pv(eras[(m_, 'started 2003-2012')]['perm_p'])}) and {_sg(eras[(m_, 'started 2013-2021')]['gain'], 2)} for 2013-2021 ({_pv(eras[(m_, 'started 2013-2021')]['perm_p'])})" for m_ in LEAD_MEASURES)
        + ". Two cohorts of about a hundred podlings each and 20 to 26 retired: the contrast is itself within noise, and the gain sits in the later half. A possible reason, not tested: in 2013-2021 more of the discussion had moved to trackers and pull requests, so the list is a smaller and more selective channel. The lead may then measure workflow (how much of the conversation still sits on the list) rather than group structure.")
    bk = {(r["measure"], r["label"]): r for r in R["lead"]["rows"] if r["kind"] == "bots"}
    add("- *Robots:* " + "; ".join(f"{m_}: {_sg(bk[(m_, 'robots kept')]['gain'])} with robots kept, {_sg(bk[(m_, 'robots and the most active pseudonym dropped')]['gain'])} with the most active pseudonym also dropped" for m_ in LEAD_MEASURES)
        + ". The effect needs the automated mail removed, which is what the human distribution is; but it also shrinks when the most active human voice goes, so it rests on the top of the distribution.")
    cmt = next(r for r in R["variations"] if r["group"] == "activity measure" and r["label"] == "commits")
    ev = {r["label"]: r for r in R["variations"] if r["group"] == "window" and r["label"].startswith(("W=12", "W=18"))}
    ev12 = next(v for k, v in ev.items() if k.startswith("W=12"))
    ev18 = next(v for k, v in ev.items() if k.startswith("W=18"))
    add(f"- *Why the combined measure shows less:* commits alone show no gain ({_sg(cmt.get('gain', float('nan')))}), and the combined count sums two different distributions (many people with a few commits; a few voices on the list). "
        f"The combined measure's gain is {_sg(ev12['gain'])} at 12 months and {_sg(ev18['gain'])} at 18 ({_pv(ev18['perm_p']) if 'perm_p' in ev18 else 'p not computed'}). "
        "Whether a pooled measure should be the algebra's activity variable is the question this lead raises.")
    add(f"- *Multiplicity:* Holm over the {R['grid_family_size']} distinct tests of 7.2 gives p = {R['lead_holm']:.2f} for the development-list cell at 12 months; Holm over the {len(wrows)} cells above does the rest. Neither is the right correction for a search whose size is not known; "
        "the honest reading is that the lead is nominally strong, consistent in sign across windows and measures, era-dependent and not confirmed.")
    add("- *What would confirm it.* Podlings that started after July 2021 (their lists are public), a rule written first (development-list messages, automated senders removed, W = 12 and 18, Gini, top-3 share and entropy added to size and mean, "
        "gain above 0.02 AUC with a one-sided permutation p below 0.05), and the same code. The era dependence says to expect it only if the later podlings resemble 2013-2021.")
    add("")
    add("## 8. What this test cannot say")
    add("")
    add("- **A proxy for the team half of section 7, not the test.** The outcome is dissolution against a success exit (L4632); no tie signs, no anchoring, no enemy weights. Whatever happens here, the certificate (kappa(G) >= 2 and w_i > 2E_i) is not touched.")
    add("- **The Incubator is an institution.** Mentors, reviews and the Board decide exits; retirement is often an administrative closing of a project that went quiet long before, and the graduation date is a vote. Both leave their mail in the last month.")
    cm = next(r for r in R["variations"] if r["group"] == "activity measure" and r["label"] == "commits")
    add(f"- **Activity is not effort.** Commits count revisions, not work; messages on human lists miss the discussion that happens in the tracker (the robots carry {_pct(D['activity_robot_share']['msg_human'])} of the messages on those lists, "
        f"and the human comments on them arrive under the robot's address). Commits alone leave {cm['N']} podlings with three regular committers against {h1['N']} for events, and show no shape gain ({cm.get('gain', float('nan')):+.3f}).")
    add("- **Identity.** One pseudonym per address: a person with two addresses is two members, and a committer who posts from a private address is not joined to her commits. This inflates n and lowers concentration, probably more for long-lived projects.")
    add("- **\"Team\" is a window choice** (117). The rule used, active in a quarter of the window's months, is arbitrary; section 7 varies it: the size effect is stable across the rules, the interaction is not.")
    add(f"- **Small numbers.** {h1['ret']} retired podlings in the primary analysis, fewer in later windows and in size bands; intervals are wide, and the {len(R['variations'])} variants are exploratory. The per-band AUCs in section 4 and the within-half gains are post hoc.")
    add(f"- **Selection.** The files hold podlings that resolved by mid-2021 (the dataset is conditioned on the label), so the \"at risk\" group at month 12 is conditioned on having lasted that long and on being resolved; the {D['resolved'] - R['tab_counts']['at_risk']} podlings that exited earlier are in section 6 only. Podlings still incubating in 2021 are absent, so the retired fraction ({D['retired'] / D['resolved']:.0%}) is that of a closed cohort.")
    add("- **Reflexivity.** The sustainability papers and the Incubator's own reporting use activity measures like these; a podling that knows it is monitored may produce activity for the monitors. Not tested.")
    add("- **Early warning needs finer data and a collapse date.** Section 5.3: the monthly series are too short for the indicators; the weekly ones have power only against a strong signal; the exit date is not the collapse date; the level trend swamps the indicators.")
    add("")
    add("## Reproduce")
    add("")
    add("    cd sim")
    add("    ~/.local/bin/uv run python -m models.apache_activity_survival fetch    # once; checks md5, writes to git-ignored data/apache-incubator/")
    add("    ~/.local/bin/uv run python -m models.apache_activity_survival build    # once; about 3 minutes; derived/ holds integers only")
    add("    ~/.local/bin/uv run python -m models.apache_activity_survival report   # rewrites this file (about 12 minutes; a ## Review section is kept)")
    add("    ~/.local/bin/uv run pytest tests/test_apache_activity_survival.py")
    text = "\n".join(L) + "\n"
    # a review appended by hand ("## Review (date)" to the end of the file) is kept when the file is regenerated
    if path.exists():
        old = path.read_text()
        k = old.find("\n## Review (")
        if k >= 0:
            text += old[k:]
    path.write_text(text)
    return text


# ------------------------------------------------------------------ command line

def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("fetch", help="download the Zenodo zips and podlings.xml (git-ignored); verifies md5")
    b = sub.add_parser("build", help="stream the CSVs into pseudonymised numeric arrays (derived/)")
    b.add_argument("--limit", type=int, default=None, help="smoke test: only the first N rows of each file")
    sub.add_parser("report", help="run the analysis and write results/apache_activity_survival.md")
    sub.add_parser("rewrite", help="rewrite the results file from the saved numbers of the last report run (text edits only)")
    args = ap.parse_args(argv)
    if args.cmd == "fetch":
        fetch()
    elif args.cmd == "build":
        build(limit=args.limit)
    elif args.cmd == "report":
        if not (DERIVED / "meta.json").exists():
            raise SystemExit("derived/ is absent: run `fetch` and `build` first")
        import pickle

        panel = Panel()
        R = run_all(panel)
        (DERIVED / "last_run.pkl").write_bytes(pickle.dumps(R))  # numbers only; git-ignored with the rest of data/
        write_report(R, panel)
        print(f"wrote {RESULTS}")
    elif args.cmd == "rewrite":
        import pickle

        R = pickle.loads((DERIVED / "last_run.pkl").read_bytes())
        write_report(R, Panel())
        print(f"rewrote {RESULTS} from derived/last_run.pkl")
    return 0


if __name__ == "__main__":
    sys.exit(main())
