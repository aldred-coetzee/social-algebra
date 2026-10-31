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
  `sim/results/newcomb_n3.md`. Prior work: `docs/prior-work/104-newcomb-doreian-krackhardt-at-source.md`;
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
