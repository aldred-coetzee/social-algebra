# Research before models; uv per project

_2026-10-29_

Aldred: *"Carry on, go deeper. Not sure why we are building models before
completing research though, and we should be using venv and uv so
different projects can use what they need."*

- **Research comes first.** The `sim/` build (reproducing published results
  as tests) was stopped the same hour. My reason for starting it early was
  that reproducing a published result is a way of *validating* an equation
  in the survey: a reproduction that fails can expose a misread equation.
  That stands as an option for the validation step, but modelling proper
  waits until the research iterations are done. Partial, uncommitted files
  under `sim/` were left untracked.
- **Per-project environments with uv.** No project relies on system Python
  packages. `uv` is installed for user `aldred` via Debian's `pipx`
  (`~/.local/bin/uv`, 0.13.6). When `sim/` resumes it gets its own
  `pyproject.toml` and `uv`-managed `.venv`. The Debian `python3-numpy`,
  `python3-scipy`, `python3-pytest` and `python3-venv` packages installed
  earlier that day (with gcc/g++ pulled in as dependencies) are not used
  by this project; removing them is Aldred's call, since the box is shared.
