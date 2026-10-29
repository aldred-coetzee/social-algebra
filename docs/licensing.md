# Licensing

Date: 2026-10-30

This is good practice, not legal advice. It records what was checked, so that nothing here surprises a reader or a rights holder when the repo is opened.

## Policy

Copied from the Licensing section of `CLAUDE.md`:

> Nothing goes into the repo that could not be reused when it is open-sourced. Citations, facts and numbers are free. Equations are restated, not copied with their surrounding text. Quotations are short and attributed. Tables, figure contents and lists are transcribed only when the source licence allows (say which licence) or are reduced to a description. Text derived from Wikipedia is marked as CC BY-SA. Paywalled text is read, never reproduced; access controls are never circumvented. Every dive records the licence of anything quoted or transcribed. The audit and per-file table live in `docs/licensing.md`; `notes/2026-10-30-licensing-check.md` has the why.

## Repo licence: choose before open-sourcing

| Option | Applies to | One line |
|---|---|---|
| CC BY 4.0 | Text, notes, models, diagrams | Anyone may reuse with attribution. It is the usual choice for written research. |
| CC BY-NC 4.0 | Text (alternative) | Also blocks commercial reuse. It is more restrictive and clashes with the CC0, CC BY and MIT sources we cite. |
| MIT | Code | Short and permissive. Needs only the copyright notice kept. |
| Apache-2.0 | Code | Like MIT, plus an explicit patent grant. Pick it if patents could matter. |

**CC BY-SA consequence.** Anything derived from Wikipedia stays CC BY-SA and keeps its attribution. If it is reused verbatim or adapted, the result must also be shared under CC BY-SA. It cannot be relicensed as plain CC BY or MIT. The clean fix is to rewrite such passages in our own words from primary sources, or to quarantine them and mark them. Our own repo licence only covers our own words. Quoted and restated third-party material keeps its owner's licence.

## Audit, 2026-10-30

### Totals

- 96 files audited: 93 prior-work dives, `synthesis.md` and `synthesis-brief.md`.
- Four files have nothing flagged at all (list at the end).
- Flagged items by verdict (itemised below, counted from the tables): remove 7, shorten about 32, attribute about 105, check about 185.
- Files with `paywalled_reproduced` true: 8. See below.
- Files with `circumvention` true: 1 (038). It is a method note, not retrieved text, but it must come out.
- **Global gap.** Almost every dive records no licence for what it quotes or transcribes. This is the rule's "every dive records the licence" requirement. It is not itemised row by row. The fix is a per-source licence column in a table. The `check` rows below are the specific items where something more than a missing record was found.
- **Short quotations are fine.** The great majority of quotations were under 60 words and attributed, and were verdict ok. They are not listed.

### Remove (7)

| File | Kind | Location | Source | Length | Licence | Reason |
|---|---|---|---|---|---|---|
| 038 | other | Line 89, section 5.3, "Readable copy" note | Bénabou & Tirole 2003 (RES) PDF at princeton.edu | n/a | Publisher copyright (OUP); author copy | A 403 was got past by fetching with a browser user-agent. That is circumventing an access control. Delete the method. Re-obtain the paper legitimately or drop the `[read]` tag on the Props list. |
| 052 | figure-content | 2.1, Fig. 1 legend quoted in full | Toates 2009, J. Sex Res. | ~70 words | Publisher copyright (T&F) | Verbatim legend from a paywalled journal. Replace with a description of the diagram. |
| 056 | quotation | §1 line 28, p. 431 block quote | Williams 2007, Annu. Rev. Psychol. | ~230 words | Publisher copyright (Annual Reviews) | Paywalled text at length. Paraphrase the three stages and cite the page. |
| 032 | quotation | §1 lines 31-41, "fear" explication | Wierzbicka 1999 p. 75, via Kitis | ~82 words | Publisher copyright (CUP) | Long passage from a paywalled book. Describe the prime structure in prose. |
| 030 | quotation | A3 line 47, Allesina & Tang 2012 abstract | Nature 483:205-208 | ~110 words | Publisher copyright (Nature) | Long verbatim abstract, paywalled. Paraphrase in one line. |
| 092 | quotation | Unconfirmed list, §1.4 homicide note | None found | ~9 words | Unknown | Unattributed and unverified, and the file says "do not use". Delete the quoted text. |
| 07 | quotation | §8 Thaler & Sunstein | House of Lords S&T Committee 2011 | 2 words ("precious little") | Parliamentary licence unchecked | The file says the phrase was not found in the report. Keep the paraphrase only. |

### Shorten (about 32)

| File | Kind | Location | Source | Length | Licence | Reason |
|---|---|---|---|---|---|---|
| 045 | quotation | s.2, Troyer's printed equation, code block | Troyer 2004, AAAI SS-04-02 | ~75 tokens | Unrecorded | Verbatim displayed equation. Restate in our own notation or describe the term set. |
| 052 | quotation | 1.2, first Siviy quotation | Siviy 2016, Behaviour 153 | ~98 words | Publisher copyright (Brill) | Over 60 words. Keep the isolation-hours clause and paraphrase the rest. |
| 059 | table | 5.1, Cook et al. 1995 Table 1 | J. Family Psychol. | 7x7, 42 cells | Publisher copyright (APA) | Full transcription. Describe the key contrasts and cite the table. |
| 065 | table | 2.3, Table 3 and Table 7 coefficients | Smith, Seger & Mackie 2007 | 24 values | Publisher copyright (APA) | Numbers are free. The table layout is not. Describe as ranges. |
| 066 | list | L40, Granovetter's eight examples | Granovetter 1978, AJS | 8 items | Publisher copyright (UCP) | Replace with a one-line description. |
| 06 | list | Belbin, 8 team roles | Belbin 1981 | 8 items | Publisher copyright (Heinemann) | A full category list. Describe it and cite Belbin. |
| 06 | list | Bales IPA, 12 categories and 6 problems | Bales 1950, ASR | 12 + 6 | Publisher copyright | A full coding scheme. Describe it. |
| 081 | quotation | Cross-checks, Helbing impatience passage | Helbing, Farkas & Vicsek 2000 (arXiv) | ~63-65 words | arXiv licence unrecorded | Over the limit and spliced from several sentences. Paraphrase and cite the equation. |
| 084 | table | §4, Leskovec Table 3 triad counts | Leskovec et al. 2010a (CHI) | 12 cells | ACM; arXiv licence unstated | Reduce to prose values. |
| 084 | table | §5, Facchetti results table | Facchetti et al. 2011, PNAS | 3x4 | PNAS copyright (not CC) | Reduce to prose figures. |
| 084 | table | §6, Estrada & Benzi Table 1 | arXiv:1406.2132 | 3x7 | arXiv licence unstated; APS | Reduce to the values used. |
| 088 | quotation | 2.2, blockquote on husband's threshold | Gottman, Swanson & Murray 1999 | 72 words | Publisher copyright (APA) | Over the limit. Keep the F and direction sentence. |
| 088 | quotation | 3.4, FAQ passage | Gottman Institute FAQ | ~65 words | Website, no licence | Keep "a source of confusion" and the 93.6% clause. |
| 090 | quotation | §2 line 51, first Yue & Zelazo passage | arXiv:2411.05933v3 | ~70 words | arXiv licence unrecorded | Three sentences joined by an ellipsis. Keep one. |
| 091 | table | §1, Bettencourt Table 1 exponents | PNAS 2007 | ~15 rows | Publisher copyright | Reduce to a description or cite single values. |
| 093 | quotation | §1 line 57, Merton | Merton 1948, Antioch Rev. | ~47 words | Publisher copyright | Keep "This is peculiar to human affairs". Cut the rest. |
| 093 | figure-content | §8 line 277, Soros Figure 4 stages | Soros 2013, JEM | 10 stages | Unknown | Describe the sequence and cite the figure. |
| 094 | quotation | §3, Gelman block quote | Gelman et al. arXiv:2011.01808 | ~62 words | arXiv licence unrecorded | Borderline. Keep the 16-word sentence only. |
| 11 | quotation | §14, Bratman definition (paywalled_reproduced true) | Bratman 1993, Ethics | ~50 words | Publisher copyright (UCP/JSTOR) | Tracks the published wording closely. Restate in our notation. |
| 12 | list | A1, Propp's 31 functions | Propp, Morphology of the Folktale | 31 items | Publisher copyright; CC BY-SA via Wikipedia | Describe ("31 functions in spheres") and cite. |
| 12 | list | A1, Propp's 7 roles | as above | 7 items | as above | Reduce to a description. |
| 12 | list | C1 validation note, OCC 22 emotion types | Ortony, Clore & Collins 1988 | 22 items | CUP copyright | Replace with the grouping. |
| 30 | quotation | D2, Rohr et al. abstract | Science 345:1253497 | ~64 words | Publisher copyright | Keep the "structural stability" clause. |
| 30 | quotation | F3, Scheffer et al. 2009 abstract | Nature 461:53-59 | ~74 words | Publisher copyright (Nature) | Cut to a phrase or paraphrase. |
| 32 | quotation | §1, Wierzbicka fear explication | as in Remove | ~82 words | CUP copyright | Also shorten, per above. |
| 34 | table | §2, DeYoung CB5T seven-row table, Notes column quotes | DeYoung 2015, JRP | 7 rows | Elsevier; preprint unstated | Replace quoted Table 1 fragments with prose. |
| 35 | list | §6, "Example BCTs" | Michie et al. 2013 | ~16 items | Springer unless OA | Reduce to a description and 2-3 examples. |
| 38 | list | 5.3, Props 1-8 | Bénabou & Tirole 2003 | 8 props, ~170 words | RES/OUP copyright | One line each in our words. The `[read]` copy is also the Remove item. |
| 39 | list | §10, RAND Table S.1 | RAND RR-2341 | 29 factors, 61 subfactors | RAND terms unrecorded | Describe (5 levels, 3 categories, 29 factors). Keep only the few used. |

### Attribute (about 105)

#### Wikipedia-derived: mark CC BY-SA, or rewrite from primary sources

| File | Location | Source | Length | Reason |
|---|---|---|---|---|
| 01 | §1 line 15, Blockmodeling claim | Wikipedia "Blockmodeling" | one claim | Cite as CC BY-SA. |
| 02 | §10 Héran, "What is established" | Wikipedia François Héran (and Universalis) | ~45 words | Mark as derived, or rewrite. |
| 03 | L38 ACT: two quoted phrases | Wikipedia Affect control theory | 6 and 4 words | Mark CC BY-SA. |
| 03 | L145 Expectation states | Wikipedia | 10 words | Mark CC BY-SA. |
| 03 | L18 Fiske scale mapping; L200 Fararo | Wikipedia (paraphrase) | ~40 and ~15 words | Mark CC BY-SA. |
| 045 | L43, L130, L161 | Wikipedia ACT article | 1 sentence, 2 URLs, 1 item | Mark CC BY-SA, or cite primary. |
| 04 | §3 Searle gloss; §11 Arrow | Wikipedia Social ontology; Social Choice and Individual Values | 1 sentence; 1 bullet | Mark CC BY-SA or reword. |
| 05 | §8 Voter model, ~2 sentences | Wikipedia | ~2 sentences | Rewrite or mark. |
| 060 | §5 structural-balance definition; §4 [std] Kuramoto and MSF bullets | Unattributed, encyclopaedic | ~30 and ~60 words | Attribute to primaries or rewrite. |
| 061 | §5 Kelso reduced equation, k_c, mapping | Scholarpedia (believed CC BY-NC-SA 3.0, unverified) | ~6 results | The NC-SA term may conflict with a permissive licence if prose is copied. Verify and record. |
| 06 | Role theory definitions; Merton role-set paragraph | Unnamed; Wikipedia | 2 defs; ~40 words | Mark CC BY-SA or cite Merton. |
| 07 | §2 Ashby, §3 Beer/Cybersyn, §5 Urban Dynamics, §7 Mechanism design, §9 Sugarscape, §12 Cliodynamics | Wikipedia pages | ~25-120 words each | Mark CC BY-SA or rewrite from primaries. |
| 084 | §8 Caplow, §9 Simmel, §9 Burt, §9 Bowen | Search summaries, possibly Wikipedia | ~40-120 words | Cite primaries or mark. |
| 08 | Items 1, 8, 10, 12, 16, 17, 19, 23, 25 | Wikipedia pages (named in each Source line) | not measurable | Mark each CC BY-SA. |
| 10 | Entries 3, 6, 15, 16, 17, 19 | Wikipedia (Selectorate, Veto player, Reciprocity, Rite of passage, Cultural theory of risk, Politeness theory) | ~2-3 sentences each | Mark CC BY-SA or cite primaries. |
| 11 | §1 forms of sociation; §4, §8, §9, §16, §17, §19, §20 | Wikipedia pages | ~20-60 words each | Mark CC BY-SA. |
| 11 | §6 AGIL function/subsystem/medium rows | Wikipedia "AGIL paradigm" | 4 rows | Mark or cite Parsons 1968. |
| 12 | A1-A4 role and actant lists and prose | Wikipedia (Morphology, Actantial model, Semiotic square, Actant, 36 Situations) | ~30-80 words per entry | Mark CC BY-SA. A2 Greimas 6 actants and A3 Souriau 6 forces likewise. |
| 13 | Bateson, Watzlawick, Haley, Genogram, Yalom, Coercive persuasion, Cialdini, Ellul, Staircase, Asch/Milgram, Janis, social engineering | Wikipedia pages | sections; lists of 5-12 items | Mark CC BY-SA. Quoted phrases at lines 42, 75, 78, 86 need inline attribution. |
| 15 | §14 24-row Plutchik dyad table; opposite names | Wikipedia "Plutchik's wheel of emotions" | 24 rows; 4 names | Mark CC BY-SA. |
| 16 | §1 Hull, §1 Spence | Wikipedia (cited) | 1 citation each | Mark or cite primaries. |
| 17 | D1 Panksepp framing; C3 Girard; B3 Preparedness | Wikipedia | ~30-35 words each | Mark or reword. |
| 19 | Whole §1 PSI; L17 drive list; L17-20 quotes | Wikipedia Psi-theory | ~1,000 words; 7 items; 8, 4, 5, 6 words | Mark the whole section CC BY-SA. |
| 14 | Relation algebra definition | Possibly Wikipedia | ~30 words | Reword from Maddux 2006 or mark. |
| 40 | Max-plus and Maslov dequantisation | Possibly Wikipedia | ~150 words | Reword from primaries or mark. |
| 42 | §3 parental investment definition | Possibly Wikipedia | ~30 words | Cite Trivers 1972 directly. |
| 39 | §2 Kahn ladder (44 rungs, 7 groups) | Possibly Wikipedia | ~60 words | Check, then mark or rewrite from Kahn. |

#### Unnamed or second-hand sources: name them, or drop the quotation marks

| File | Location | Quoted text | Length | Reason |
|---|---|---|---|---|
| 01 | §1 line 15, Lorrain & White definition | Search result, unquoted | 21 words | Name the source and quote it, or paraphrase. |
| 02 | §6 Read abstracts | Unnamed abstract | 15 words | Name the abstract. |
| 02 | §11 | Unnamed review of Maranda | 11 words | Cite the review. |
| 02 | §3 | "one table of contents" | 5 words | Give the catalogue URL. |
| 03 | L38 | "derived with calculus" | 3 words | Name the source or drop the marks. |
| 04 | §15 Shapley | "defined by a set of axioms" | 6 words | Name which page. |
| 048 | §1 | "basin of attraction is quite large" | 6 words | Add "Reverdy & Koditschek say". |
| 048 | §1 | "no inherent bias for either underlying task" | 7 words | Name the source. |
| 053 | §1 | Maier "Abstract's original claim" | 5 words | Name the work. |
| 053 | §4 | "generic or model-agnostic" | 3 words | Name the source or drop. |
| 055 | §3a | "rarely exceeds 80 individuals" | 4 words | Name Henrich et al. as the quoting source. |
| 056 | Exists list | "identical pattern" | 2 words | Name Woo 2014. |
| 057 | §3 | "that appear to be legitimate" | 5 words | Attribute to the summary or drop. |
| 059 | §5.3; §8 | "This is the model's version of negative outweighs positive."; "Triumph of negative over positive" | 4 and 6 words | Name the source or make it our label. |
| 064 | s1 Drives/operands | Kramer quote with a statistic | 9 words | Add an inline citation. |
| 066 | L73 Wheeler; L119 Kuran p. 53; L195 academia.edu | Quotes via Granovetter / Brummitt / unidentified abstract | 19, 9, 12 words | Keep the chain ("quoted in …"). Say "identity unconfirmed" for the abstract. |
| 06 | §10 Heider folk formula; §6 Berne | Marks without source; secondary TA wording | 15 and 8 words | Name the source, or paraphrase. |
| 07 | §2 "Necessary, not sufficient."; §5 "predictions" | Unnamed | 3 and 1 words | Name or drop. |
| 075 | §3 Bigsby coding definitions | In running prose, no attribution | 4 and 13 words | Attribute explicitly. |
| 077 | §1 | "the cue was followed by a shock for the demonstrator" | 10 words | Name Lindström 2019 in the sentence. |
| 080 | §2.1 | "four horsemen" | 2 words | Cite Gottman. |
| 083 | L260 | Two phrases credited to "the authors" of two papers | 9 and 7 words | Pin each to its paper. |
| 084 | §9 Bowen | "empirical studies … focus on the negative effects of triangulation" | ~11 words | Name the review. |
| 085 | L119 Olfati-Saber & Murray; L150-152 Altafini 2012 | Quotes with only a section heading | 15 words; ~60 across 7 fragments | Add inline cites. Record CC BY for Altafini. |
| 087 | L40 Moody & White | "This conception scales…" | 21 words | Add inline cite. |
| 089 | §2 | Narodnaya Volya quote | 10 words | Cite Kuran 1989 sec. 4.3. |
| 08 | Item 19 reviewer; Item 6 "mid-to-late 2020s"; line 293 owner phrase | Unnamed | 6, 3, 3 words | Name or drop. |
| 091 | §4 Kao & Couzin; §6c "one blog" | Quote without inline cite; unnamed blog | 19 and 3 words | Name both. |
| 093 | §4 Goodhart 1975; §6c Mendler-Dünner 2024 | Second-hand chains | 19 and 18 words | Write "quoted in Manheim & Garrabrant" and "in Hardt & Mendler-Dünner 2025 §7". |
| 11 | §9 "definition of the situation"; §17 "伐交" renderings | Term; unnamed translators | 4 and 3 words | Name Thomas/Blumer and the translator. |
| 12 | B3 Ensemble sentence; B2 CiF phrase; A4 Polti terms | No inline source | 24, 9, 2 and 4 words | Name the source inline. |
| 14 | 8a Hewitt | Quoted characterisation | 18 words | Attribute to Hewitt 1973 or paraphrase. |
| 16 | §7 "if any factor is zero, motivation is zero"; §11 "feeling right"; §13 K&G | Unnamed or no inline cite | 8, 2, 17 words | Name sources. |
| 24 | §9 "shared mindset"; §12 "66 studies, 92% positive" | Unnamed secondary | 2 and 5 words | Name or drop. |
| 26 | §9 rasa sutra | Sanskrit quote, no reference | ~4 words | Add chapter, verse and edition. |
| 28 | D3 Abrams & Strogatz | "roughly constant across cultures" | 4 words | Add inline cite. |
| 31 | §1 | "ready to go" | 3 words | Attribute or drop. |
| 32 | §3 | "little empirical proof" (a Finnish study) | 3 words | Name the study. |
| 33 | Tomasello "motivation to share psychological states"; White 1959 effectance definition | No inline cite; unread source | 8 and 19 words | Attribute or paraphrase. |
| 35 | §6 BCT definition | Michie et al. 2013, no inline cite | 19 words | Name the source. |
| 37 | §5 Ginges 2007 | Quote with no inline name | 27 words | Name in the sentence. |
| 39 | Unconfirmed "a player may be less likely…", "reduces population pressure on land"; Section 11 "never did the research" | No source | 13, 6, 4 words | Remove unless a source is found. |
| 40 | §1a VSL phrase; §9a "each competitor wins in turn"; §6 "the most urgent drive wins" | No inline cite / our own gloss | 4, 5, 5 words | Attribute, or drop the marks. |
| 41 | D4 | "trust is built slowly and lost quickly" | 7 words | Aphorism without source. |
| 42 | §4 | "winner effects modest, loser effects stronger" | 6 words | No source exists. Drop the marks and keep it under Unconfirmed. |

### Check (about 185)

| File | Kind | Location | Source | Length | Licence | Reason |
|---|---|---|---|---|---|---|
| 01 | list | Harrison White section, vocabulary and chapter titles (line 199) | White 2008, Identity and Control | ~11 terms + titles | PUP copyright | Transcribed from a contents page, not the text. Reduce or confirm. |
| 01 | other | Padgett Florentine data, §4 line 63 | Padgett families dataset | n/a | Not stated | Record the dataset licence before any data is reproduced. |
| 01 | other | Lorrain & White PDF link, ucilnica.fri.uni-lj.si; Borgatti & Everett archive link; vdoc.pub mention | Unofficial copies of paywalled papers | links | Unknown | Cite DOIs. Remove the links and the mirror mention. |
| 02 | table | White 1963 six axioms, §4 line 47 | White 1963 (from memory) | 6 items | Prentice-Hall | Reduce to a description with citation. |
| 02 | list | nLab kinship definition (lines 27, 55) | nLab | ~8 and ~3 items | nLab licence unchecked | Restate in our wording. |
| 03 | other | Lefebvre formalism (L55, L62-64, L68) | Bulitko arXiv:math/0205325; Tarasenko arXiv:1011.3397 | formulas | arXiv licence unrecorded | Record the arXiv licences. |
| 03 | other | Emerson 1962 full text from umsl.edu | ASR | full read | ASA/JSTOR | Record the copy's provenance. |
| 043 | other | §8 line 265, small-gain paragraph | Unsourced | 1 paragraph | Unknown | Cite Jiang, Teel & Praly 1994, or confirm our wording. |
| 045 | list | s.2, 29 enumerated terms | Hoey et al. eq. 3 / Heise 2007 | 29 items | arXiv unrecorded | Describe rather than list. |
| 045 | other | s.3 formula block (eq. 46, 49) | Hoey et al.; Heise 2007 | ~60 tokens | arXiv; publisher | Near-transcription. Restate. |
| 045 | table | s.5 EPA dictionaries, 14 rows | affectcontroltheory.org hub | 14 rows | Hub licence unknown | Record or reduce. |
| 045 | dataset | Indiana 2003; West Germany 1989; actdata (CC0) vs Interact (noncommercial); 16 unopened dictionaries | Heise / Francis / Schneider | counts | Not stated; "noncommercial research only" | The CC0 package and the noncommercial guide sit uneasily. Check before redistributing. Do not add the 16 unchecked sets. |
| 046 | quotation | Revelle 2008 CTA draft: L41, L57, L59, L78, L79, L90-93, L123/L261 | Revelle (unpublished) | 8-19 words each | No licence | Record the licence, or paraphrase. |
| 046 | quotation | Revelle & Condon 2015 draft: L93, L125, L147 | Author draft | 8-29 words | "Please do not cite without…" header | Check the published JRP version, or paraphrase. |
| 046 | table | L38-48, 9-row vocabulary table | Revelle Table 1 + others | 9 rows | No licence | Record or reduce to prose. |
| 046 | other | Blankenship 1995 (Springer), Slade & Rush 1991 (interruptions.net) | Two full papers | read | Publisher copyright | Slade & Rush copy is unofficial. Record access route. |
| 047 | quotation | Pezzulo et al. 2015 (L172 x2, L173); Smith, Friston & Whyte 2022 (L181) | PMC copies | 9-13 words | PMC licence unrecorded | Confirm and record. |
| 049 | dataset | Hartgerink meta-analysis data (location unverified) | PLOS ONE | n/a | Unknown | Read the OSF/Figshare licence before use. |
| 049 | other | Magee & Galinsky; Verduyn & Lavrijsen PDFs | Paywalled-type journals | full texts | Publisher | Access route unrecorded. |
| 04 | other | ATL prose (Wikipedia cited) | Wikipedia | n/a | CC BY-SA if derived | Check for copied wording. |
| 04 | other | Goguen-Burstall institutions sentence | nLab | 1 sentence | Unchecked | Close paraphrase. Attribute or reword. |
| 050 | table | Pedersen et al. Table 3, 15 correlations + 6 fit stats | PLoS ONE e109394 | 21 values | CC BY 4.0 (default, unverified) | Record CC BY, or reduce. |
| 050 | dataset | Pick et al. 2022, N = 15,915 | Sci Data | summary | Unverified | Record the dataset licence. |
| 050 | other | PMC browser check, Nature paywall, empty OSF preprint | Marengo | n/a | n/a | State that the check was not worked around. |
| 051 | other | Study 1 writing prompt, ~22 words, unquoted | Greenberg et al. 1994 via ML4 | ~22 words | APA | Reduce to a description, or quote with attribution. |
| 051 | other | Pyszczynski et al. 2015 abstract paraphrase | Elsevier | ~19 words | Elsevier | Close to the abstract. Reword. |
| 051 | other | Three hypotheses and §6 standard account | Unsourced | ~40 words | Unknown | Attach a source or mark as ours. |
| 052 | quotation | 2.3, Blyuss & Kyrychko, two sentences | Chaos 33(4) | 14 and 19 words | AIP | Wording from a garbled summarising fetch. Verify against the PDF. |
| 052 | quotation | 4.2, "proof-of-study" | Veldhuis et al. 2020 | ~6 words | MDPI (verify) | The title says "proof-of-concept". A likely misquote. |
| 052 | other | Toates 2009 read from a course-page upload | J. Sex Res. | full read | T&F | Provenance unverified. |
| 053 | other | Huys et al. equations "transcribed from the PDF text" | NeurIPS 2008 | 5 equations | NeurIPS | Relabel "restated" and confirm. |
| 053 | wikipedia-text | CSD, fold bifurcation, eigenvalue | Unsourced | ~40-60 words | Possibly CC BY-SA | Name the source or mark. |
| 053 | dataset | Wichers & Groot data | JOPD 10.5334/jopd.29 | 1,478 / 239 days | Not recorded | Record. |
| 054 | quotation | Bench & Lench 2019 abstract fragments | Emotion | 13, 7, 4 words | APA | File calls it a paraphrase. Verify or remove the marks. |
| 054 | quotation | Wilson et al. 2014 "two-thirds of men…" | Science | 9 words | Science | Unverified. Remove the marks or verify. |
| 054 | table | MAC 4x2 table | Westgate 2018 dissertation | 8 cells | Not stated | Describe in prose. |
| 054 | dataset | Westgate internal meta-analysis | Dissertation | 14 studies, N = 1,364 | Not stated | Unpublished data. Record the licence. |
| 054 | other | Springer / Routledge PDF routes | Danckert; Bieleke | n/a | Publisher | Record how they were obtained. |
| 055 | quotation | Henrich & Gil-White abstract paraphrase, unquoted | Evolution & Human Behavior | ~24 words | Elsevier | Reword, or quote and attribute. |
| 055 | quotation | Magee & Galinsky definitions (L147) | Acad. Manag. Annals | 15 and 8 words | AoM | Source PDF provenance unrecorded. |
| 055 | dataset | BHPS (86,679 obs.); an unnamed German panel (7,812 people) | Boyce 2010; Di Tella 2010 | figures | UK Data Service restricted; unknown | Name the panel. Record terms. |
| 055 | other | Three saved mirror PDFs | Anderson; Henrich & Gil-White; Magee & Galinsky | 3 copies | Publisher | Confirm none is committed. |
| 056 | dataset | Neurosynth base rates | Neurosynth | ~6 figures | Not recorded | Record the licence. |
| 056 | other | Williams 2007 PDF route; Hartgerink and Eisenberger copies; Williams 2009 and Leary attempts | Various | n/a | Publisher | Record routes. |
| 058 | other | Gould 2000 paragraph | ASR abstract | ~110 words | SAGE | Check it is not lifted from the abstract. |
| 058 | other | Gould 2003 blurb; Cooney 1998 description | UCP; NYU Press | 1-2 sentences | Publisher | Confirm our wording. |
| 058 | other | A `curl -k` attempt, blocked | Publisher sites | n/a | n/a | Note it as a blocked attempt. |
| 059 | table | Gottman, Swanson & Murray 1999 Tables 1 and 2 | J. Family Psychol. | 5x5; ~12 values | APA | Reduce to values used. |
| 059 | list | SPAFF code weights | as above | 16 items | APA | Describe and give the scale range. |
| 059 | other | Dynamical-systems glossary | Unsourced | ~150 words | Possibly CC BY-SA | Confirm our wording. |
| 059 | quotation | Cumulative quoting across 4.4-4.5, section 5 | Three papers | ~200 words total | APA; T&F | Heavy. Trim lines 71 and 136. |
| 05 | list | Castellano et al., 10 terms | RMP 2009 | 10 terms | APS | May mirror the subject index. |
| 05 | other | Weidlich: Dover description of three parts | Publisher blurb | 3 parts | Publisher | Restate. |
| 05 | dataset | Fernandez-Gracia 2014 US county data | Referenced | n/a | Not stated | Record if copied. |
| 060 | dataset | figshare "Conflict Model of Actors Network" | Fernández-Rosales 2015 | not opened | Not checked | Check before reuse. |
| 061 | list | Ferrer & Steele 2010 slides, four model labels | CILVR slides | 4 labels | Not stated | Describe. |
| 061 | dataset | Klump twin study; rties example data | Hu et al. 2014; CRAN | summaries | Unknown | Record. |
| 061 | other | Helm et al. 2012; Steele & Ferrer 2011 abstract paraphrases | Emotion; MBR | 2-3 sentences | APA; T&F | Confirm not word-for-word. |
| 061 | other | Kelso page fetched with the expired TLS certificate ignored | Scholarpedia | n/a | n/a | Record the override, or re-read via a valid route. |
| 062 | quotation | Yoshida & Man 2024, five quotation groups (L36-43, L196, L282) | arXiv 2412.12103 | 3-18 words | arXiv unrecorded | Record the licence once. |
| 062 | quotation | "altruism narrows but does not close the gap" | Bergstrom, Blume & Varian 1986 (unopened) | 8 words | n/a | Not a verified quote. Remove the marks. |
| 063 | quotation | H&K 2002 (L44) | JASSS | ~24 words | Unrecorded | Record. |
| 063 | list | "Specialisations, all verbatim" | H&K 2002 | 4 items | Unrecorded | Relabel "restated". |
| 063 | quotation | Bosse 2015 via search summary; abstract paraphrase (L179) | Cognitive Computation | few words | Springer | Second-hand. Confirm route. |
| 063 | table / dataset | Parsegov C1, C2 matrices; W row; F&J 1999 profiles | arXiv:1505.04920; H&K | 8 numbers; 4 numbers | Unrecorded | Record the licences. |
| 063 | list | Properties I-IV | H&K 2002 | 4 items | Unrecorded | Record. |
| 064 | table | Kramer Results, 4x6 | PNAS | 24 cells | NAS; PMC | Record or reduce. |
| 064 | list | Fowler & Christakis tie results | BMJ | 6 items | OA, unrecorded | Record or reduce. |
| 064 | dataset | Framingham; Twitter gardenhose | FHS; Ferrara & Yang | 4,739; 3,800 | Access-controlled; Twitter terms | Record the terms. |
| 064 | other | Kramer read from a Stanford copy | PNAS | n/a | Unknown | Cite the PMC copy. |
| 065 | table | Pizarro Table 3 | Front. Psychol. | 10x5 | Probably CC BY | Confirm and record. |
| 065 | other | Access routes for Mackie, Goldenberg, Smith, Kuppens | APA; SAGE; Elsevier | n/a | Publisher | Record routes. |
| 066 | quotation | Thron & Jackson "no critical crowd size" | via file 068 | 6 words | Unknown | Verify at source. |
| 066 | quotation | Quote of sibling file 18 | Internal | ~19 words | n/a | Paraphrase or cite by name. |
| 066 | other | Copies: gwern.net scan, NYU, JSTOR, rasmusen.org | Granovetter; Watts; Rasmusen | n/a | Publisher | Record provenance. |
| 067 | quotation | Epstein PNAS "tip" sentence | PMC128592 | 22 words | PNAS | Line 8 says PMC was behind a browser check, yet later lines say it was read. Resolve, or drop the dependent claims. |
| 068 | table | Agent rule (Table 1); run settings (Table 2) | Epstein 2002 | 2 rows; ~20 values | PNAS | Restate in prose. |
| 068 | list | Variable names (~17); Ormazábal phase classes (~9) | Epstein; PRE | lists | PNAS; PRE | Record or describe. |
| 068 | dataset | ACLED riot-size data | Thron & Jackson | n/a | ACLED terms | Record if used. |
| 06 | list | Rusbult & Van Lange six dimensions | Annu. Rev. Psychol. 2003 | 6 items | Annual Reviews | Names not retrieved from the paper. |
| 06 | figure-content | Collins IR model, 4 + 4 elements | Collins 2004 p. 48 | 8 items | PUP | Listed from the figure. |
| 06 | other | Berne three rules | Secondary TA material | ~70 words | Grove Press | Close paraphrase. Restate. |
| 070 | list | Moulder et al. nine signals | ICMI '22 | 9 items | CC BY (secondary claim) | Confirm at the DOI page. |
| 071 | dataset | Kern et al. full text, provenance | Anim. Behav. | n/a | Elsevier | Record the route. |
| 072 | list | CoMSES five mechanisms | Smaldino replica page | ~110 words | AFL-3.0 covers code only | Shorten to one sentence. |
| 072 | table | PNAS 2013 methods equations "transcribed from equation images" | PMC3799307 | 7 lines | PNAS | Restate in our notation. |
| 072 | other | PMC browser check; pnas.org 403 | n/a | n/a | n/a | State no bypass was used. |
| 073 | wikipedia-text | Young / KMR standard content, Blume etc. | Unsourced | ~130 words | Possibly CC BY-SA | Confirm our wording. |
| 073 | other | Roos PDF is author-hosted; Young and KMR URL guessing | OBHDP; Econometrica | n/a | Publisher | Do not repeat the URL guessing. |
| 074 | wikipedia-text | Kalman/PBH and Gramian opening paragraphs | Unsourced | ~90 words | Possibly CC BY-SA | Confirm wording. |
| 075 | table | Within-study contrasts, 15 rows | Bigsby & Albarracín, OSF h9fyd | 15 rows | node_license null | Reduce to a description. |
| 075 | dataset | OSF h9fyd (157 d-rows); OSF wcxvg (1,450 cases) | as above; Kaspar & Keller | summary stats | None stated | Ask the authors or keep derived numbers only. |
| 076 | dataset | OpenNeuro ds003242; OSF F9CRU, CF2RT, s8xk9; preregistrations cwg9e, 6ynt3 | Tomova 2020; Stijovic 2023 | n/a | Not verified | Check each licence field. |
| 076 | other | Lee, Chen & Tye abstract paraphrase | Cell | ~30 words | Elsevier | Check it is not near-verbatim. |
| 077 | quotation | Golkar 2015 (2 and 20 words); Olsson 2020 (14 words) | Biol Lett; NRN | 36 words | Not open access | Record licences. |
| 077 | dataset | OSF xfe72 CSV | Lindström 2019 | 461 kB | Not recorded | Record before any refit is committed. |
| 077 | other | Reached text after reCAPTCHA / 403 | Golkar; PNAS SI | n/a | n/a | Confirm only public routes were used. |
| 078 | quotation | Dejonckheere data statement (21 words, read after a paywall redirect); EMOTE abstract (12 words) | Nature Hum. Behav.; PsyArXiv | 33 words | Unrecorded | Re-read from an open copy or paraphrase. |
| 078 | table | 12-row OSF node table | OSF nodes | 12 rows | Null/opaque | Reduce to citations. |
| 078 | dataset | Dejonckheere OSF zm6uw (2 of 15 open); EMOTE eb7rt | OSF | n/a | None declared | Reuse terms not read. |
| 079 | dataset | Hudson Bay lynx and hare; Lafit clinical data | Fasel; Lafit | 21 points; n/a | Not stated | Record. |
| 07 | quotation | Wiener's thesis (18 words) | via Wikipedia | 18 words | Book; CC BY-SA | Confirm against the book or paraphrase. |
| 07 | list | Komov's 11 elements | Thomas 2004 | 11 items | T&F | From memory. Check or describe. |
| 07 | wikipedia-text | Nudge definition; Lanchester prose | Nudge; Lanchester's laws | 25; 60 words | CC BY-SA | Check and attribute. |
| 080 | other | FLP design sentence | Vernon-Feagans 2013 | ~35 words | Unrecorded | Close to the abstract. |
| 080 | dataset | pairfam ZA5678; FLP; Early Years of Marriage; Fragile Families; Gottman lab data | Various | n/a | Terms unread | Record before use. |
| 081 | other | Helbing eqs. 1-4 headed "transcribed" | arXiv cond-mat/0009448 | 4 equations | arXiv unrecorded | Relabel "restated". |
| 082 | table | Nizamani Table 1 params | Physica A | 8 rows | Elsevier | Record or reduce. |
| 082 | figure-content | Eqs. 1-11 "as printed" | arXiv 1310.0731 | 11 equations | Elsevier | Restate in our notation. |
| 083 | table / list | Hill Table 1 (5 values); Baez Theorem 3 (6 equations) | Biol. Lett.; TAC | small | Unchecked | Verify. Keep as facts or describe. |
| 083 | dataset | Palla 2007 co-authorship and phone records; Niwa fisheries; Zachary; Axelrod & Bennett 1939 | Various | summaries | Unknown | Record. Do not redistribute. |
| 083 | other | Aureli 2008 from a JSTOR scan on eva.mpg.de | Curr. Anthropol. | n/a | Paywalled | Record provenance. |
| 084 | dataset | Epinions, Slashdot, Wikipedia elections (SNAP), Facchetti networks, Kirkley IR + freshman class, Askarisichani, Doreian & Krackhardt | Various | summaries | Not stated | Wikipedia elections is derived from CC BY-SA content. Record the rest. |
| 084 | other | C&H 1956 from a sitpor.org repost; Facchetti PDF from the Wayback Machine | Psychol. Rev.; PNAS | n/a | Publisher | Cite the DOI. Confirm the free window. |
| 085 | table | Dörfler & Bullo Theorem 4.1 (3 conditions, 4 consequences) | SIAM / arXiv:1011.3878 | 7 items | SIAM; arXiv unrecorded | Say which parts are quoted. |
| 085 | other | Acebrón "publisher-layout copy"; Strogatz course PDF | RMP; Physica D | n/a | Publisher | Record provenance. |
| 086 | quotation | Leonard SI wording although the SI was unread (12 words); L198 vs L142 mismatch; Dyer (31); Pinkoviezky (17); Couzin abstract (18) | PNAS; Science; PRE | short | Publisher | Verify at source. L198 and L142 disagree. |
| 086 | figure-content | Couzin Fig. 2B caption sentence | Science | ~38 words | AAAS | Check wording. |
| 086 | dataset | Couzin fish trials; baboon GPS | Couzin; Strandburg-Peshkin | stats | Unknown | Record before fitting. |
| 086 | other | Conradt & Roper 2005 from a "third-party copy" | TREE | full review | Elsevier | Record or reread. |
| 087 | wikipedia-text | Menger's theorem paragraph | Unsourced | ~60 words | Possibly CC BY-SA | Reword. |
| 087 | dataset | Add Health (12 schools); Mizruchi 1980; Mathieu 2015 | Various | stats | DUA; unknown; APA | Record terms. |
| 087 | other | ASR via a Wayback copy; "JSTOR-stamped" pages; 403 and cookie-wall attempts | Moody & White; others | n/a | Publisher; eScholarship CC BY | Cite the CC BY eScholarship copy. |
| 088 | table | Nine-row model table; Table 1 values | Gottman & Levenson 2000; GSM 1999 | 9 rows; ~10 pairs | Wiley/NCFR; APA | Reduce to the values used. |
| 088 | other | Scanned PDFs, source not stated | Family Process; JMF; JFP | n/a | Publisher | Record per PDF. |
| 089 | table | Chenoweth 2020 bin table, 8x3 | Carr Center DP | 8 rows | Unrecorded | Reduce to the figures in the text. |
| 089 | table | Kuran Table 1 values | Public Choice | 6 values | Springer | State in prose. |
| 089 | list / dataset | Carnegie Global Protest Tracker fields, bins and data | Carnegie Endowment | ~11 labels; 1,054 entries | All rights reserved | No reuse licence. Descriptive only. |
| 089 | dataset | SCAD and ARCHIGOS; Spanish 15-M Twitter data | Chenoweth & Belgioioso; González-Bailón | large | Not recorded | Check before use. |
| 089 | other | Granovetter and Kuran read from gwern.net copies | AJS; Public Choice | n/a | Publisher | Record the clean route. |
| 08 | other | Princeton blurbs for Turchin books | Publisher | n/a | PUP | Confirm our wording. |
| 08 | dataset | Seshat (414 polities); Breiger & Pattison Florentine; ICPSR 8872; NetLogo replica | Various | n/a | Not stated | Record. |
| 091 | quotation | Dunbar 1993 unedited preprint (4 + 1 + 1 quotes) | BBS | 3-17 words | Not recorded | Check each against the BBS text. |
| 091 | quotation | Zhou 2005 (16 and 9 words); Centola 2018 accepted manuscript (13, 11, 14, 13, 17, 9, 14 words) | Proc R Soc B; Science | short | Not recorded | Verify against the published versions. |
| 091 | table | Dunbar Table 1 | BBS preprint | 3 classes | Not recorded | Verify. |
| 091 | dataset | Bettencourt; Arcaute (8,850 wards); Dunbar (36 genera); Zhou; Lindenfors; Centola (194 subjects); Isaac et al. | Various | stats | Not recorded | Record. |
| 091 | other | PMC bot-check, alternative copies read | n/a | n/a | n/a | State no bypass. |
| 092 | quotation | Bates & Gupta "completely indistinguishable" | Intelligence 60 | 2 words | Elsevier | The file's own correction says the paper doesn't contain it. |
| 092 | list | Cox et al. eight Ostrom principles, 14 items | Ecol. Soc. 15(4) | 14 items | Unrecorded | Describe. |
| 092 | quotation | Agrawal & Chhatre quoted via Cox | World Dev. | 23 words | Elsevier | Verify at source. |
| 092 | quotation | OECD four capitals | How's Life? 2020 | 4 categories | OECD terms | Unread (403). Describe. |
| 092 | dataset | Correlates of War; Cirillo & Taleb 565 conflicts; Eisner homicide; Cox 77 cases | Various | stats | Not recorded | Record. |
| 092 | other | Woolley, Edmondson, Bates, Graf copies | Various | n/a | Publisher | Rights unverified. |
| 093 | other | Perdomo "verbatim in substance" header; Kaggle dataset | arXiv:2002.06673; Kaggle | n/a | Unrecorded | Relabel "restated". Record the Kaggle licence. |
| 093 | quotation | MacKenzie 2003 (L252-255, L261) | Soc. Stud. Sci. | ~5-36 words | Sage | Which copy was read is inconsistent. Resolve first. |
| 093 | other | Merton 1948 via a pbworks re-host of a JSTOR scan | Antioch Rev. | n/a | Unlicensed copy | Cite the JSTOR DOI. |
| 09 | quotation / list | Hinde "levels of social complexity" (unread); Trivers 5-item list; Hinde blurb list; Hinde biography | Man; QRB; blurb | short | Publisher | Verify, restate, or source. |
| 09 | other | Third-party copies linked: energia.mta.hu, pdodds, moodle2.units.it, Princeton and CMU course pages | Maynard Smith; Hamilton; Nowak; Couzin; NEJM | 6 links | Unauthorised redistribution possible | Cite DOIs and drop the links. |
| 10 | other | Akerlof & Kranton PDF; Feder reprint scan | QJE; Yale UP | n/a | Publisher | Record access routes. |
| 11 | other | Wolff 1950 via archive.org | Free Press | n/a | In copyright | Note it was consulted, not reproduced. |
| 12 | list / other | FIPA 22 acts; FIPA SL formulas; Carminati abstract paraphrase | FIPA; arXiv:2308.16017 | 22; 2; ~45 words | Unrecorded | Record or reduce. |
| 12 | other | Hosted IEEE and CogSci PDFs | McCoy; Evans & Short; Lehnert | n/a | Publisher | Provenance. |
| 13 | quotation / list | Minuchin caption (unread); Bowen's eight; Lifton eight via Hassan; McCauley twelve; Janis eight (source unrecorded) | Various | short lists | Unknown | Names only. Cite primaries. |
| 13 | figure-content | Minuchin key glyphs, from memory | Nichols & Schwartz | 7 | Publisher | Keep marked unverified. |
| 14 | list | ANSI/INCITS 359-2004 function names | Paid standard | ~17 | ANSI | Describe the groups. |
| 15 | table / other | Plutchik Table 1.3 eight blends; chapter access route | Academic Press 1980 | 8 entries | Publisher | Record or describe. |
| 16 | wikipedia-text | Approach-avoidance conflict types; Lewin's equation | Wikipedia | 4 descriptions; 1 equation | CC BY-SA | Compare, then attribute. |
| 17 | other | Anderson et al. 2015; Keltner et al. 2003 | Paywalled APA | ~15-20 words each | APA | Confirm our wording. |
| 18 | quotation | ASCRIBE expansion | Hoogendoorn 2010 | 9 words | Springer | Verify or drop. |
| 18 | other | Turchin equations from a secondary excerpt | Unidentified | 2 equations | Unknown | Name the excerpt. |
| 19 | table | EMA Table 2 rule list, partial | Marsella & Gratch 2009 | ~6 rules | Elsevier | Describe the rule types. |
| 20 | other | Murray via archive.org; Rinaldi via JSTOR; Gottman 2003 via a lab copy; IIASA blog; Kelso | Various | n/a | Publisher; CC BY-NC-SA (unverified) | Record routes and licences. |
| 20 | dataset | NFVS (528); Oregon Youth Study (85) | Heyman; Kim | counts | Not recorded | Record. |
| 21 | quotation | "behind hurts more than ahead" | No source | 5 words | n/a | Drop the marks or attribute. |
| 22 | other | Tomova 2020; Walum 2016 full-text route | Nat. Neurosci.; Biol. Psychiatry | n/a | Publisher | Record. |
| 23 | list / other | Helbing and Jaques and Hughes equations; Epstein 7 states | arXiv | 6 formulas; 7 items | Unrecorded | Restate. |
| 23 | dataset | Lux & Marchesi return series; Tsai crowd video | Nature; AAMAS | n/a | Unidentified | Name and record. |
| 23 | other | Cimpeanu 2025 route | JRSI | n/a | Unrecorded | Record. |
| 24 | list / other | Steiner, Klandermans, Gurr, Jasper, Hackman (unread books) | Various | 3-5 items each | Publisher | Describe. |
| 24 | other | Varmann 2023 access | ERSP | numbers | T&F | Record. |
| 25 | list | Roos 8-step procedure | OBHDP | 8 steps | Elsevier | Keep as restatement. |
| 25 | dataset | WVS; HRAF eHRAF page | n/a | n/a | Not stated; subscription | Record access. |
| 26 | quotation | Descartes (Bennett translation); Aristotle (Rhys Roberts); Stoic quote via a summarising fetch | Various | 9-28 words | Translations unstated | Check licence and wording. |
| 26 | list | Stoic subspecies (~30) | DL 7.111-114 | ~30 items | PD (Yonge) | Verify. |
| 26 | quotation | Herbart prose | SEP | ~150 words | SEP copyright | Rewrite from primaries. |
| 26 | wikipedia-text | Abhidharma and Natyashastra recall | Unsourced | 2 paragraphs | Unknown | Check against primaries. |
| 30 | wikipedia-text | F1-F3 standard accounts | Unsourced | 3 paragraphs | Possibly CC BY-SA | Confirm. |
| 30 | dataset | Kossakowski 2017 | JOPD 5:29 | 1,478 | Not recorded | Record. |
| 31 | wikipedia-text | "Standard account" passages | Unsourced | n/a | Possibly CC BY-SA | Check four-questions wording. |
| 32 | list / wikipedia-text | 65 NSM primes; definitional prose | Wikipedia NSM table | 65 items | CC BY-SA | Mark, or use the Griffith chart. |
| 32 | dataset | CLICS, Warriner, NRC VAD | n/a | n/a | Not verified | Record before use. |
| 32 | other | Kitis PDF provenance | Kitis | n/a | Unknown | If paywalled, the fear quotation must go (see Remove). |
| 33 | quotation | "two signs of one error term" (our wording); "about a third" (unverified) | Gubler & Bischof; Tronick | 10, 8 words | Erlbaum; Child Dev. | Quote the chapter exactly, or drop the marks. |
| 33 | list | Gubler & Bischof ~21 terms | Erlbaum chapter | 21 | OA scan unrecorded | Describe. |
| 33 | figure-content | Teaching-material crossing rates | Untraceable | 3 numbers | Unknown | Remove or source. |
| 33 | other | Pinquart / Waters abstract paraphrases; Strange Situation prose | T&F; Wiley | ~60 words | Publisher | Reword. |
| 34 | list | RDoC constructs | NIMH | ~40 | Probably PD | Record. |
| 35 | list | 16 BCT cluster names (from memory) | Michie 2013 | 16 | Springer | Verify, or reduce. |
| 36 | other | Theorem 1 lead-in sentence; Gul & Pesendorfer hosted copy | Econometrica | ~20 words | Publisher | Confirm our phrasing. Cite the DOI. |
| 37 | list | Ginges stimulus wordings | PNAS 2007 | 3 + 4 + 3 | Unrecorded | Describe. |
| 38 | figure-content | Lazear & Rosen section I | JPE | 10 equations + paragraph | UCP | Restate; record access. |
| 38 | table | Adams 2x2 | Standard account | 4 cells | Unknown | Prose. |
| 38 | wikipedia-text | Herzberg lists | Standard account | 9 items | Possibly CC BY-SA | Check. |
| 38 | other | Deci 1999; Gneezy & Rustichini 2000b access | Paywalled | stats | Publisher | Record. |
| 39 | quotation | Pape "Denial can work…" | Cornell UP, via search summary | 14 words | CUP | Verify; add page. |
| 39 | table | Kydd & Walter Figure 1, 5x4 | Int. Security 31(1) | 5 rows | MIT Press | Describe. |
| 39 | wikipedia-text | "audience cost"; "security dilemma" | Standard | <25 words each | Possibly CC BY-SA | Reword. |
| 39 | other | Abstract paraphrases (Powell, Fearon, Zagare & Kilgour, Levy); Spiller copy; RAND via IA | Various | 2-4 sentences | Publisher | Restate; cite DOIs. |
| 40 | quotation | Arcak 2007 quote from a seminar abstract | IEEE TAC | 21 words | Unknown | Paraphrase. |
| 41 | other | Rousseau et al. trust definition, unquoted | AMR 23 | 22 words | AoM | Quote with marks or reword. |
| 42 | other | Bonabeau 1995 abstract sentence, unquoted | Physica A | ~35 words | Elsevier | Quote or reword. |
| 42 | dataset | Murray & Schaller 230 regions; Hartgerink data | JCCP; PLoS ONE | counts | Not recorded | Record. |
| syn | other | Phrases at lines 63 and 67; Seshat; nLab restatement | n/a | n/a | n/a | Confirm they are ours. Check nLab's licence. |

### Files with `paywalled_reproduced` true

- 052: Toates Fig. 1 legend (~70 words, Taylor & Francis).
- 056: Williams 2007 block quote (~230 words).
- 065: Smith, Seger & Mackie 2007 coefficient tables (APA).
- 11: Bratman 1993 definition (~50 words).
- 30: Allesina & Tang 2012 abstract (~110 words).
- 32: Wierzbicka 1999 fear explication (~82 words).
- 42: Bonabeau 1995 abstract sentence, unquoted (~35 words).
- 088: Gottman, Swanson & Murray 72-word block, plus the nine-row model table from Gottman & Levenson 2000.

### Files with `circumvention` true

- 038: a 403 on a Bénabou & Tirole PDF was got past by fetching with a browser user-agent. The note in the file must be removed (see Remove). The dependent Props list must be re-sourced.

### Files with nothing flagged

- 044 (all items verdict ok)
- 27
- 29
- synthesis-brief.md (no items)

Several other files, such as 047, 048, 069 and 072, were flagged only for missing licence records. That gap is the global one noted above.

## Fixes applied, 2026-10-30

One Sonnet agent per flagged file (92 files, commit 22fbac5): 8 removals
(including the access-control workaround note in 038, with its two
dependent `[read]` tags downgraded), 27 shortenings, 172 attributions
(mostly CC BY-SA marks on Wikipedia-derived wording), 375 licence records
for items whose verdict was check. Every file now ends with "Licences of
quoted and transcribed material". The whole-corpus DOI audit was re-run
after the edits: 2,125 DOIs, none newly broken; the eight that do not
resolve are extraction artefacts or DOIs the files themselves disclaim as
unused, except one completed by hand (065, the OUP volume).

Still open: the licence of most quoted sources is "not determined;
publisher copyright presumed" — safe under short-quotation use, but a
future pass could confirm open-access licences (eLife, PLOS, PNAS open
articles, arXiv) where they exist.
