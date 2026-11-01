# sim/data/ -- local-use-only datasets

Nothing in this directory except this file is tracked: `sim/.gitignore` has `data/*` and `!data/README.md`.
A data file here is a local copy for running the tests. It is **never committed and never redistributed**
(the repo is meant to be open-sourced; see `CLAUDE.md`, Licensing). Tests that need a data file are skipped
with the fetch command in the reason when it is absent.

## newcomb/newfrat.dat -- Newcomb fraternity rank data (2026-10-31)

- **What.** The UCINET dataset "Newcomb Fraternity Networks": fifteen 17 x 17 sociomatrices NEWC0-NEWC15
  without NEWC9, DL full-matrix format. Each of 17 men ranks the other 16 for affect, 1 = first preference,
  no ties; ranks only, no signs. Study: Newcomb (1961), *The Acquaintance Process*; rank data as recorded by
  Nordlie (1958), PhD thesis, University of Michigan (neither read here).
- **Used by.** `sim/models/newcomb.py`, `sim/models/newcomb_report.py`, `sim/tests/test_newcomb_triads.py`,
  `sim/results/newcomb_n3.md`; also `sim/models/triad_rule_comparison.py` (its post hoc re-read of the Newcomb pattern,
  through `models.newcomb.load_ranks`, sha256-checked), its test and `sim/results/triad_rule_comparison.md` section 4.1
  (computed statistics only). Prior work: `docs/prior-work/104-newcomb-doreian-krackhardt-at-source.md`;
  ledger L4471-L4546.
- **Fetch.** `cd sim && ~/.local/bin/uv run python -m models.newcomb_report fetch` (stdlib `urllib`; refuses
  any download whose sha256 differs from the one below; sends no identity beyond urllib's default agent).
- **Source URL actually used.**
  `https://web.archive.org/web/20241004180913id_/http://vlado.fmf.uni-lj.si/pub/networks/data/UciNet/newfrat.dat`
  -- the Internet Archive's public snapshot (raw bytes, `id_`) of the original distribution
  `http://vlado.fmf.uni-lj.si/pub/networks/data/UciNet/newfrat.dat` (Batagelj & Mrvar's Pajek datasets,
  "UCINET IV datasets"; listing page `.../UciNet/UciData.htm#newfrat`). The original host timed out from the
  box on 2026-10-31 (curl exit 28, twice), so the public archive copy was used; no login, paywall or access
  control was involved. The snapshot of 2021-04-21 (`20210421135101`) is byte-identical.
- **Size / checksum.** 13,702 bytes; sha256
  `884537cbb60cf6c9c8e3cea3fa2d9f4a54fef8981b28151e65d65c5d89d43b46`.
- **Independent cross-check (2026-10-31).** `data/fraternity.rda` of the R package `networkdata`
  (`github.com/schochastics/networkdata`, 7,809 bytes, sha256
  `8c5c1c8fa86ca3f76a50430d62206f96f82a9a502c80361c2b51e805bdcc8439`; list of 15 igraph objects, edge
  attribute `rank`) holds exactly the same 15 x 17 x 17 ranks, compared cell by cell with a throwaway
  stdlib reader. That file was not kept. The UCI Network Data Repository page
  (`networkdata.ics.uci.edu/netdata/html/Newcomb.html`) is R documentation only (it describes 14 networks,
  the odd one out against the 15 here, ledger L4543) and was not used for data.
- **Terms.** None are stated by the UCINET/Pajek listing (the archived page was searched for any copyright,
  licence or permission text). The UCI mirror's documentation says the data are CC BY-NC-ND 2.5 "if the
  source does not specify otherwise"; the `networkdata` MIT licence covers the package, not the data
  (L4539-L4542). Absence of a stated licence is not a grant, so the file is treated as **not licensed for
  redistribution**: local use only, git-ignored, not copied into any committed file, and no recoded
  (signed) matrix is stored either (a recode is an adaptation, which ND would bar distributing, L4544).
  Computed statistics -- counts, test statistics, p-values -- are published in `sim/results/` with
  attribution. If the file itself must ever ship, ask the UCINET authors (Borgatti, Everett, Freeman) or
  Batagelj & Mrvar.
- **Credit when publishing results from it.** Newcomb (1961); Nordlie (1958); UCINET (Borgatti, Everett &
  Freeman 1992), distributed via Batagelj & Mrvar (2006), Pajek datasets,
  `http://vlado.fmf.uni-lj.si/pub/networks/data/`.

## wiki-rfa/wiki-RfA.txt.gz -- SNAP "Wikipedia Requests for Adminship (with text)" (2026-11-01)

- **What.** Every vote cast in English Wikipedia's requests for adminship from 2003 through May 2013:
  198,275 records of SRC (voter), TGT (candidate), VOT (-1 oppose, 0 neutral, 1 support), RES (outcome of the
  election, -1 rejected / 1 accepted), YEA (year the election started), DAT (time of the vote) and TXT (the voter's
  comment, wiki markup), in blank-line-separated blocks. Compiled by West, Paskov, Leskovec & Potts (2014).
- **Used by.** `sim/models/wikirfa.py`, `sim/models/wikirfa_report.py`, `sim/tests/test_wikirfa_conversion.py`,
  `sim/results/wikirfa_conversion.md`; also `sim/models/triad_rule_comparison.py`,
  `sim/tests/test_triad_rule_comparison.py`, `sim/results/triad_rule_comparison.md` (which read this file in place and
  never fetch it); and `sim/models/crowd_gate_wikirfa.py`, `sim/tests/test_crowd_gate_wikirfa.py`,
  `sim/results/crowd_gate_wikirfa.md` (the crowd gate: it reads this file in place, parses it with its own loader that
  skips the comments, and has a `fetch` that is used only if the file is absent); and `sim/models/sign_registry_battery.py`,
  its test and `sim/results/sign_registry_battery.md` (the sign-registry battery: same terms, its own comment-skipping
  loader, `fetch wiki` only if absent; added at review 2026-11-01). Prior work:
  `docs/prior-work/117-modern-signed-and-split-datasets.md` section 3.3; ledger L4561-L4564, L4855.
- **Fetch.** `cd sim && ~/.local/bin/uv run python -m models.wikirfa_report fetch` (stdlib `urllib`; refuses any
  download whose sha256 differs from the one below; sends no identity beyond urllib's default agent).
- **Source URL.** `https://snap.stanford.edu/data/wiki-RfA.txt.gz` (page `https://snap.stanford.edu/data/wiki-RfA.html`),
  a plain public download: no login, paywall or access control; the site's `robots.txt` disallows only course-video
  directories.
- **Size / checksum.** 14,936,383 bytes (50,110,991 uncompressed; `Last-Modified` 2018-07-10); sha256
  `88d53196fb2564a2e20286dbba818832f718cc352bb181a2101d23d2556f0862`. Counts re-made on 2026-11-01 match 117:
  198,275 records, 144,451 support / 41,176 oppose / 12,648 neutral, per-year totals, 11,380 distinct user names (117's
  "named voters", L4562; but 10,416 of them vote and 964 are candidates who never do, recounted 2026-11-01), 1,661
  records with an empty voter field; also found here: 9,367 records without a time and one with an impossible one
  (hour 31), three month names with slips (`Mya`, `Julu`, `Janry`), and 18 elections carrying both outcome labels (15 as
  a complete copy).
- **Terms.** None stated on the dataset page (read 2026-11-01: it asks for a citation of West et al. 2014 and says
  nothing on use or redistribution). Its "License" link is the SNAP software BSD licence, which covers code. The
  comments are Wikipedia text, licensed CC BY-SA 4.0 / GFDL (117 section 3.3). Research use of a public download is
  not forbidden by anything stated, so it is used **locally only**: git-ignored, never committed, never
  redistributed; the comments are skipped at parse time and never stored; names are replaced by integers on load
  and never written out. Computed statistics (counts, rates, p-values) are published in `sim/results/`.
- **Credit when publishing results from it.** West, R., Paskov, H. S., Leskovec, J. & Potts, C. (2014), Exploiting
  social network structure for person-to-person sentiment analysis, *TACL* 2: 297-310,
  doi:10.1162/tacl_a_00184 (DOI resolved at Crossref by 117); the SNAP collection, `https://snap.stanford.edu/data/`.

## bitcoin/soc-sign-bitcoinotc.csv.gz and soc-sign-bitcoinalpha.csv.gz -- SNAP Bitcoin OTC and Alpha trust networks (2026-11-01)

- **What.** Who-trusts-whom ratings among traders on two Bitcoin platforms: lines `SOURCE,TARGET,RATING,TIME`
  (rater, ratee, integer rating -10 to +10, Unix time with a fractional part), sorted by time. OTC: 35,592 ratings
  among 5,881 nodes, 2010-11-08 to 2016-01; Alpha: 24,186 among 3,783, 2010-11-08 to 2016-01.
- **Used by.** the same three files, and `sim/models/triad_rule_comparison.py` with its test and results (which read
  these files in place and never fetch them); `sim/models/gate_reciprocity_bitcoin.py`, its `_report.py`, test and
  `sim/results/gate_reciprocity_bitcoin.md` (the reciprocity-gate test); `sim/models/sign_registry_battery.py`, its test
  and `sim/results/sign_registry_battery.md` (in place; `fetch otc alpha` only if absent; added at review 2026-11-01); 117
  section 3.4, ledger L4567-L4580.
- **Fetch.** the same command; sha256 is checked before anything is written. The Bitcoin files alone:
  `cd sim && ~/.local/bin/uv run python -m models.gate_reciprocity_bitcoin_report fetch`. Both local files were compared
  byte for byte with a fresh download from the source URLs on 2026-11-01 and are identical. Time resolution (found while
  testing the reciprocity gate): OTC times are sub-second; **Alpha's are whole days** (04:00 or 05:00 UTC), so 7,323 of its
  10,062 reciprocated pairs carry one timestamp and cannot be ordered.
- **Source URLs.** `https://snap.stanford.edu/data/soc-sign-bitcoinotc.csv.gz` and
  `https://snap.stanford.edu/data/soc-sign-bitcoinalpha.csv.gz` (pages `.../soc-sign-bitcoin-otc.html`,
  `.../soc-sign-bitcoin-alpha.html`); public downloads, no access control.
- **Size / checksum.** OTC 397,258 bytes (`Last-Modified` 2017-10-06), sha256
  `6424ac981dad3a019f697fc1b9fcd85c19d8d9f039797758e9ffb6fea100c373`; Alpha 149,480 bytes (2017-10-06), sha256
  `3a178611b9c2f39c9a0dc75936f28557317f1733319b49da4838232b3757cd76`. Counts match 117: 32,029 / 3,563 positive /
  negative and 22,650 / 1,536; no zero rating; no ordered pair rated twice.
- **Terms.** None stated on either page (read 2026-11-01); the pages ask users to cite the two papers below. Treated
  as not licensed for redistribution: local use only, git-ignored, not copied into any committed file; computed
  statistics only in `sim/results/`.
- **Credit when publishing results from it.** Kumar, S., Spezzano, F., Subrahmanian, V. S. & Faloutsos, C. (2016),
  Edge weight prediction in weighted signed networks, *ICDM*, doi:10.1109/ICDM.2016.0033; Kumar, S., Hooi, B.,
  Makhija, D., Kumar, M., Faloutsos, C. & Subrahmanian, V. S. (2018), REV2: fraudulent user prediction in rating
  platforms, *WSDM*, doi:10.1145/3159652.3159729 (both DOIs resolved at Crossref by 117).

## apache-incubator/ -- Apache Software Foundation Incubator Project Sustainability Dataset, and the ASF's podlings.xml (2026-11-01)

- **What.** Two zip files holding one CSV each: `commits_2021_update.zip` (`commits_full.csv`, 4.5 GB uncompressed; one row
  per file touched by a commit; 12,608,575 rows from 265 projects, 2005-2021) and `emails_2021_update.zip`
  (`emails_full.csv`, 7.8 GB; 2,161,558 mailing-list messages with bodies and reply links from 274 projects,
  2003-2021); plus `podlings.xml`, the ASF Incubator's own status file (status, start and end date of every podling),
  which supplies the graduated/retired labels because the Zenodo record has none (117 section 4.3, ledger L4623-L4633).
  **The raw files carry the names and email addresses of public mailing-list participants.**
- **Used by.** `sim/models/apache_activity_survival.py`, `sim/tests/test_apache_activity_survival.py`,
  `sim/results/apache_activity_survival.md`.
- **Fetch and build.** `cd sim && ~/.local/bin/uv run python -m models.apache_activity_survival fetch` (stdlib `urllib`;
  checks each zip's md5 against Zenodo's and removes a file that differs; sends only the user agent
  `social-algebra-research/0.1`), then `... build` (about 2 minutes). The build streams both archives (nothing is
  extracted to disk), reduces every address to a project-local integer (a one-way hash under a random per-build salt that
  is never stored, then renumbered by first appearance) and writes `data/apache-incubator/derived/*.npz` and `meta.json`:
  integer and boolean arrays, plus project and list names. No name, address or message text is kept anywhere.
- **Source URLs.** Zenodo record `https://zenodo.org/api/records/5637530` (doi:10.5281/zenodo.5637530, version 1.1,
  CC BY 4.0, open access); files at `.../files/commits_2021_update.zip/content` and `.../files/emails_2021_update.zip/content`;
  labels from `https://incubator.apache.org/podlings.xml` (fetched 2026-11-01; the live file changes).
- **Size / checksum.** `commits_2021_update.zip` 156,231,855 bytes, md5 `952ec9c66f1c2a96ddf3deab2e78f9e9`, sha256
  `143dab8e9ef184b62b505615906578022118665b0f6dc9d7de36cc5df021ce8c`; `emails_2021_update.zip` 1,041,656,466 bytes, md5
  `ac716c35e7f160178e83ea9ae40fd4be`, sha256 `3be525e64893256bfab8128bc889c5e9829de1e1cfe16ef7602b6457dfc7b5fb`; the md5s
  are Zenodo's own. `podlings.xml` as fetched: 253,042 bytes, sha256
  `98f0b33016c850b6ee9fdb6d623c20c4116fefd5f1619ab35dcf2c152ffcb541`. The build reproduces 117's counts exactly once 562
  and 7 short CSV records (fewer fields than the header) are set aside.
- **Terms.** The Zenodo record is **CC BY 4.0** (DataCite and the Zenodo API both say so): reuse with attribution, the
  only change here being aggregation. `podlings.xml` carries the ASF's Apache License 2.0 header; only status, dates and
  names of podlings are read, never the mentor lists. The zips and the CSV rows stay local and git-ignored; the open licence
  does not settle the privacy of the people in the files, so no person is named or addressed in any committed file, and
  `sim/results/` holds counts, AUCs and p-values only (a test scans for an `@`).
- **Credit when publishing results from it.** Yin, L., Zhang, Z., Xuan, Q. & Filkov, V. (2021), *Apache Software Foundation
  Incubator Project Sustainability Dataset* (version 1.1) [data set], Zenodo, doi:10.5281/zenodo.5637530, CC BY 4.0, and
  the paper of the same title, *2021 IEEE/ACM 18th International Conference on Mining Software Repositories*,
  doi:10.1109/msr52588.2021.00081; for the forecasting context, Yin, L., Chen, Z., Xuan, Q. & Filkov, V. (2021),
  Sustainability forecasting for Apache incubator projects, *ESEC/FSE*, doi:10.1145/3468264.3468563 (DOIs resolved at
  Crossref and DataCite 2026-11-01); the labels are The Apache Software Foundation's `podlings.xml`.

## bluesky/networks_to_share.zip -- BlueTempNet, temporal follow and block networks of Bluesky (2026-11-01)

- **What.** Jeong, Jiang, Tan, Bernard & Liu (2024), "Descriptor: a temporal multi-network dataset of social interactions
  in Bluesky Social (BlueTempNet)": four GEXF files in one zip (`graph_dimension1_to_share.gexf` 65 MB, the feed-creator
  follow/block graph; `graph_dimension2_to_share.gexf` 1.15 GB, the feed-member graph; `graph_dimension3_to_share.gexf`
  100 MB, member-feed joins; `multi_graph_to_share.gexf` 1.6 GB). Each signed edge carries `sign` (+1 follow, -1 block)
  and `time` (ISO, to the millisecond), 2023-05-11 to 2024-05-11. Node ids are field-level encrypted by the authors; no
  attempt was made to decode them.
- **Used by.** `sim/models/sign_registry_battery.py`, `sim/tests/test_sign_registry_battery.py`,
  `sim/results/sign_registry_battery.md`: only `graph_dimension1_to_share.gexf` (298,058 signed records: 273,696 follow,
  24,362 block, matching 117 section 3.6, ledger L4595; 24 self-loops dropped), streamed from the zip without extracting it.
  The metadata zip (`metadata_to_share.zip`, 24.6 MB) was not fetched. Prior work: 117 section 3.6, L4593-L4598, L4663.
- **Fetch.** `cd sim && ~/.local/bin/uv run python -m models.sign_registry_battery fetch bsky` (stdlib `urllib`; refuses
  any download whose sha256 differs from the one below; sends no identity beyond urllib's default agent).
- **Source URL.** `https://media.githubusercontent.com/media/ujeong1/BlueTempNet-IEEE-DATA-2024/main/data/networks_to_share.zip`,
  the public Git LFS endpoint of the authors' own repository (`github.com/ujeong1/BlueTempNet-IEEE-DATA-2024`; the files
  there are LFS pointers: oid `360839bf...` for this one, 221,305,868 bytes). No login, subscription or access control is
  involved on this route; IEEE DataPort (doi:10.21227/yrsy-ee91), which does require a subscription, was not used.
- **Size / checksum.** 221,305,868 bytes; sha256 `360839bfc6f7e4e8642ec207917c1401f2f665aa63478d3c3ff5fee5b6a9cf23`
  (equal to the LFS pointer's oid, checked on download 2026-11-01).
- **Terms.** DataCite lists CC BY 4.0 for the DataPort record (117 section 3.6); the GitHub repository carries no licence
  file (the API reports none) and its README asks users of the data or code to cite the paper. Taken as: citation
  required, redistribution not assumed (the GitHub copy has no licence of its own), so local use only: git-ignored, never
  committed, never redistributed. Computed statistics only in `sim/results/`.
- **Credit when publishing results from it.** Jeong, U., Jiang, B., Tan, Z., Bernard, H. R. & Liu, H. (2024), Descriptor: A
  Temporal Multi-network Dataset of Social Interactions in Bluesky Social (BlueTempNet), *IEEE Data Descriptions* 1:
  71-79, doi:10.1109/IEEEDATA.2024.3474640 (resolved at Crossref by 117).

## sign_registry_battery_cache/ -- computed statistics, not data (2026-11-01)

`sim/data/sign_registry_battery_cache/{wiki,otc,alpha,bsky}.json` hold the per-site statistics that
`python -m models.sign_registry_battery compute SITE` writes and `report` reads (coefficients, AUCs, intervals, null
replicates; no edge, user or text). They sit here only because this directory is git-ignored; they can be deleted and
regenerated. The same module reads the wiki-RfA and Bitcoin files above in place, and fetches them with
`fetch wiki otc alpha` if they are absent (sha256-checked).
