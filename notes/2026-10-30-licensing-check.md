# Licensing check before anything is reused or open-sourced

_2026-10-30_

Aldred: *"can we add a check to ensure that from a licensing perspective,
anything that we've quoted or taken out or whatever is something we can
use? And in the citations… make some kind of indication as to whether there
are any licensing restrictions… I just don't want to be in a situation
where… when we do open source this at some point, people become upset or I
find out that I've broken some rules somewhere."*

What this adds (good practice, not legal advice):

- **An audit of every file** (`docs/licensing.md`): each verbatim
  quotation with its length, each transcribed table, figure or list, each
  passage that may derive from Wikipedia or another share-alike source,
  and each dataset, tagged with the source's licence where determinable
  and a verdict: ok / attribute / shorten / remove. Fixes applied where
  the verdict is attribute or shorten; removals listed.
- **A standing rule** (in `CLAUDE.md`): citations and facts are free;
  equations may be restated; quotations stay short and attributed;
  tables and lists are transcribed only when the licence allows or are
  reduced to a description; Wikipedia-derived text is marked CC BY-SA;
  paywalled text is read, never reproduced; access controls are never
  circumvented.
- **A licence for the repo itself**, Aldred's call before open-sourcing:
  the usual pairing is CC BY 4.0 for text and notes, MIT or Apache-2.0
  for code.
