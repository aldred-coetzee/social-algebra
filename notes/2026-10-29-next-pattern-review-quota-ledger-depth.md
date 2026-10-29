# next-pattern's review: quota guard, ledger, depth, test the hypothesis

_2026-10-29. Received after Aldred asked whether the coordinator was
validating the approach; it had not been consulted since the first
synthesis._

Verdict: method sound, records exemplary. Six changes, applied from the
batch after iteration 1 (iteration 1 was not restarted):

1. **Quota guard.** Everything runs on Aldred's subscription, and the usage
   limit is shared by every session on the box, including the phone
   sessions he uses daily. A ~120-agent batch repeated back to back can
   exhaust the weekly limit and lock every session, which fails exactly
   when he is travelling (it already stopped seven validators mid-flight on
   the night of 2026-10-28/29). Until Aldred sets a number: **one batch per
   day**, Sonnet for dives, **Haiku** for cross-checks and DOI audits, Opus
   only for validation of load-bearing claims, and each batch ends with a
   ten-line report rather than auto-starting the next. **This overrides
   Aldred's "don't wait for me between batches" until he answers**
   next-pattern's question about the cap; his answer wins.
2. **Convergence ledger** (`docs/ledger.md`, `docs/ledger.jsonl`): one line
   per claim; a cluster closes when a batch adds fewer than one new claim
   per five directions; deep enough when every cluster is closed and every
   load-bearing claim is `read`.
3. **Depth over breadth.** Deep-reads of the sources the equation set will
   lean on run before further surveys. `read` only if the agent read the
   primary text; paywalled stays `sa`, never a secondary dressed as read.
4. **Validation of content**, not only existence: validators open the
   source for load-bearing claims; next-pattern audits twenty random ledger
   claims every third batch.
5. **Test the hypothesis.** "Drives as primitives" is Aldred's working
   hypothesis. Every dive ends with two fixed questions: *does this
   tradition reduce to a drive basis, and which of its content does not?*
   and *what outcome does it actually predict or control, and how well, out
   of sample?* The second feeds `empirical-result` lines; the equation set
   has no scoring criterion until the target outcomes are named, which is a
   question for Aldred.
6. **Model.** This session moved to Fable 5.1 (Aldred ran `/model fable`
   the same hour; the project pin applies on restart). Validators stay on
   Opus.
