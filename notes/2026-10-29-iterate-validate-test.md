# Many iterations, rigorous validation, models to test the equations

_2026-10-29_

Aldred: *"Carry on with research; I expect several iterations of this, 100s
of research directions and dives before we attempt to synthesise. I also
expect rigorous validation and cross checking of all stated findings with
validated links. We also need to construct models that we can use to test
our equations."*

Decisions taken with him the same day:

- **Scale: workflow batches.** Each iteration is a multi-agent workflow:
  dives in parallel, a separate validation agent per dive, a cross-check of
  new findings against the existing files, then commit. A research map
  (`docs/research-map.md`) lists every direction with its status, so
  coverage is visible and nothing is silently dropped. No synthesis until
  he says the research is deep enough.
- **Validation:** every stated finding carries a link that has been
  resolved (DOI at doi.org/Crossref, or a stable URL that was fetched), and
  every file gets its second pass and validation log. A corpus audit
  re-resolves every DOI and compares title and authors with the citing line.
  Contradictions between files are logged, not silently resolved.
- **Code is now in scope**: Python, in this repo, under `sim/`. Aldred
  approved it, which changes the brief's original "no code". The first job
  of `sim/` is to **reproduce published results** from validated equations
  (as regression tests), so that later the equation set can be tested
  against the literature and then against open data.
