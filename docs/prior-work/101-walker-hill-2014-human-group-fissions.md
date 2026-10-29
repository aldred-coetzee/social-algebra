# Prior work 101: Walker and Hill 2014, human group fissions (the only human fission dataset candidate)

Direction: D593

Date: 2026-10-29. Kind: deep-read. **Outcome: the full text could not be read. It is paywalled and no open copy was found. Only the abstract was read, at the publisher page. Nothing in this file is a full-text [read], and nothing here may feed an equation.** The question D593 asks (what was measured, at what n, and could it test a split prediction) is only partly answerable from the abstract. The n is unknown. Do not cite any count of fissions from this file.

Tags: **[abs]** = the abstract read at the publisher page or an indexer; **[sa]** = secondary account; **[refs]** = the reference list as deposited at Crossref (a fact about what the paper cites, not about what it says).

## What was tried (routes, so the next reader does not repeat them)

- Crossref (OK): doi 10.1007/s12110-014-9209-0. Walker RS, Hill KR (2014), "Causes, Consequences, and Kin Bias of Human Group Fissions", *Human Nature* 25(4): 465-475; published online 2014-07-24; 61 references; 21 citing works at Crossref and 23 at OpenAlex. Crossref carries no abstract; it does carry the reference list.
- Springer page (link.springer.com/article/10.1007/s12110-014-9209-0), fetched by curl: HTTP 200, but the page says "This is a preview of subscription content" (39.95 EUR for the PDF). The abstract, the reference list and two figure thumbnails are public; the body text is not. The `/content/pdf/` URL returns the same HTML preview, not a PDF.
- Unpaywall: `is_oa false`, `oa_status closed`, no locations. OpenAlex: closed, `any_repository_has_fulltext false`, two locations (publisher DOI, PubMed 25056829), no PDF. Europe PMC: one record, abstract-level, `isOpenAccess N`.
- ASU Pure page: abstract only, no file. HRAF (Yale) document 909 and hypothesis 2896: abstract plus two coded hypotheses, with the evidence, societies, sample size and notes all absent. ResearchGate and CORE: 403. Academia.edu: Cloudflare challenge. Google Scholar "all versions": HTTP 429, not machine-reachable from here. Semantic Scholar API: 429 (in the D592 run; not retried). Two web searches (standard mode) returned no PDF. Author pages (Missouri anthropology CV, HG Cosmos researcher PDF) surfaced as search hits but are CVs, not the paper.
- Next routes for a human: an institutional login via the DOI; an emailed request to the first author (Walker, University of Missouri; corresponding author per Unpaywall); the ASU Hill lab. Neither was tried from here.

## 1. Walker and Hill 2014

**Citation.** Walker RS, Hill KR (2014). Causes, consequences, and kin bias of human group fissions. *Human Nature* 25(4): 465-475. doi 10.1007/s12110-014-9209-0 (Crossref-confirmed; resolves, HTTP 200).

**Abstract [abs], in substance, nearly verbatim.**
- Fissions of human communities have consequences for cultural and genetic variation and divergence through serial founder effects.
- "An ethnographic review shows that most human group fissions are fueled primarily by internal political conflict and secondarily by resource scarcity."
- Fissions lead to subgroups with higher relatedness than the original community, through kin-biased assortment, "the lineal effect", as found in other social animals. This matters because relatedness governs how strongly kin/group selection favours warfare, peacekeeping and other collective action.
- "Random individual assortment is not an appropriate null model for evaluating lineage assortment because nuclear families and extended households are expected to remain together," which by itself forces higher relatedness in smaller subgroups.
- They "develop a lineage assortment index where low values represent subgroups with coefficients of relatedness near those expected if nuclear and extended households had chosen to associate into random groupings."
- Two Ache village fissions (Paraguay) have a low index "not significantly different from zero as evaluated with controlled simulations". A Piaroa (Venezuela) fission has an index near unity, "a lineal fission that maximizes the relatedness of subgroups such as the perfect split of a lineage into sublineages."
- Conclusion: "previous discussions of fission have emphasized similarities among human studies and even other social mammals"; they "highlight the full range of potential kin bias in the formation of new communities". (Corrected 2026-10-30 against the PubMed abstract: the earlier paraphrase dropped "and even other social mammals".)

**What is NOT in the abstract and so is not known here.** The index formula (the abstract names it but gives no equation, so none is transcribed); how many fissions the ethnographic review covered and in which societies; the sizes (n) of the original and daughter groups; the number of Ache and Piaroa fissions beyond the "two" and "a"; the simulation design and its p-values; how "internal political conflict" and "resource scarcity" were coded and how the percentages split; whether a fission's cause was coded from the ethnographer's account or from the participants' stated reasons.

**HRAF coding [sa, from the HRAF eHRAF hypotheses database, not from the paper].** Two hypotheses are coded "Supported", test type "comparison of percentages", significance and coefficient unknown, both at p. 471: (1) fissions occur mainly through internal political conflict and secondarily resource scarcity; (2) fission along kin lines is common. HRAF lists the sources as eHRAF World Cultures and the *Encyclopedia of World Cultures*; I take "the *Encyclopedia of World Cultures*" to appear because the paper's reference list cites O'Leary et al. (1994) (the entry is in **[refs]**). This is a third party's reading of the paper and is [sa]; the "comparison of percentages" label suggests the cause claim rests on a tally of cases, not an inferential test, but that is an inference from a database label, not from the text.

**What the reference list shows [refs] (what the evidence base is, not what the paper concludes).** The ethnographic cases are drawn from monographs and book chapters, not from event-level time series. Cited case sources include Chagnon on Yanomamö village fissioning (1975, 1976, 1979), Smouse, Vitzthum and Neel 1981 on random versus lineal fission among the Yanomama, Kaplan 1975 on the Piaroa, Hill and Hurtado 1996 on the Ache, Olsen 1976 and 1987 on Hutterite colony fission, Whiteley 1988 and 2008 and Levy 1992 and Titiev 1972 on the Oraibi (Hopi) split, Turner 1957 (*Schism and Continuity*), Oliver 1955 and Keesing 1978 (Solomon Islands), Maybury-Lewis 1967 (Shavante), Matta 1970, Melatti 1970, Verswijver 1992, Silva 2009 (Waimiri-Atroari), Goodenough 1951 (Truk), and the Mbuti, Semai (Fix 1975), Xilixana (Early and Peters 2000) and Makuna (Århem 1981) monographs. Carneiro 1987, "Village splitting as a function of population size", is cited and is the one reference titled as a size law. Hill et al. 2011 (*Science* 331: 1286) on hunter-gatherer co-residence is cited. Animal fission papers: elephants (Archie et al. 2006), rhesus macaques (Chepko-Sade and Olivier 1979; Melnick and Kidd 1983), baboons (Van Horn et al. 2007), gorillas (Nsubuga et al. 2008), Cape ground squirrels (Waterman 2002), bats (Metheny et al. 2008), prairie dogs (Hoogland 1995). Wright 1922 and Hamilton 1964 supply the relatedness coefficient and the inclusive-fitness logic. This shows the paper is a synthesis of documented cases, with genealogical data for a small subset (the ones where relatedness could be computed: Ache, Piaroa, and the Yanomama literature), which is consistent with the abstract's "two Ache" and "a Piaroa" case studies.

**Their vocabulary.** Fission, subgroup, community, lineal effect, kin-biased assortment, lineage assortment index, serial founder effect, coefficient of relatedness, null model, extended household.

**Drives/operands [abs].** None are drives. The operands are communities (households, lineages) and the coefficient of relatedness r among members. The causes are named at the level of social facts: "internal political conflict" and "resource scarcity". The paper offers no motivation variable for individuals. (Whether the full text says anything about why individual households choose a side is unknown.)

**Operators / equations.** The lineage assortment index is defined in the paper; its form is not available to me. The abstract states its endpoints only: 0 = the relatedness expected if intact households associated at random; near 1 = a lineage splitting into sublineages. **No equation transcribed. Tag: none. The index cannot be used.** The only formal content I can state is the abstract's own contrast between two null models (random individuals versus random intact households), which is a method point and not a dynamic.

**Theorems or derived predictions.** None stated in the abstract. The implicit prediction is descriptive: subgroup mean relatedness exceeds parent-group mean relatedness (the lineal effect), and the size of the excess depends on how far households, not individuals, are the units of assortment. There is no stated rule of the form "a group of size n with property X splits when Y".

## What changes with GROUP SIZE and COMPOSITION

- **Size.** The abstract says nothing about a size threshold, and I could not read the body. The only size-related fact I can report is a design point from the abstract: a smaller subgroup built of intact households has higher relatedness by construction, so the null expectation of r depends on subgroup size and household size distribution. Carneiro 1987, which the paper cites, is titled as village splitting as a function of population size, and Chagnon 1975 as limits to local group size and fissioning; those titles are in [refs] only. What either found is not known from this task. Do not use a Yanomamö "splits at about 100 people" figure from memory; it was not verified here and is [sa] at best.
- **Composition.** This is where the abstract is strong: composition (which households and lineages are in the group) is the determinant of how the group splits, in two named regimes (household-random, as the Ache; lineage-aligned, as the Piaroa).

## SCALE and consent

- **Scale of every empirical result.** Group scale, entirely: a community fissions into daughter communities. Membership-scale decisions (which household goes where) are the micro event inside it, but the paper's quantities (r, the index) are computed on the whole split, not on individual stay/leave choices as a function of a stated individual variable. The cause claim ("internal political conflict") is group-scale and categorical.
- **Consent or manipulation.** Not applicable in the sense asked: there is no intervention. These are naturally occurring splits recorded by ethnographers. Nothing was steered; the paper is observational.

## Could it test a split prediction? (D593's question)

On the evidence reachable: **partly, and only for one kind of prediction.**
- It could test a prediction about **who ends up with whom** (kin structure of the daughter groups), using its index and the genealogies behind the Ache, Piaroa and Yanomama cases, if the genealogies or the index code can be obtained. That is a composition prediction.
- It cannot, as far as the abstract shows, test **when** a group splits (a threshold in n, cohesion, or conflict) because the cases are reviewed after the fact, no matched non-splitting groups are mentioned in the abstract, and no time series of a drive or tension variable is mentioned. A split-timing prediction needs both splitters and stayers, which the abstract does not describe. This is the absence that matters most and it is stated from the abstract only; the full text may contain a comparison I cannot see.
- n is unknown. With "two" Ache fissions and "a" Piaroa fission as the quantitative cases, the quantitative n is plausibly very small (single digits) but that is the abstract's wording, not a count; the review may cover more cases qualitatively.

## Does it reduce to a drive basis?

From the abstract only, so provisional. Of this tradition's content:
- **Does not reduce, at the level stated:** the cause categories ("internal political conflict", "resource scarcity") are group-scale events and resource conditions, not drives of persons. The paper offers no individual-level drive variable (fear, desire, status-seeking) for choosing a side. A drive reading would have to be supplied from outside, for example grievance or rivalry as a driver of political conflict, and nothing here tests that.
- **Does not reduce:** the kin-assortment structure. Households staying together and lineages splitting along descent lines is a structure (a partition constraint on who can be separated), not a drive. A drive basis would have to represent it as an attachment or care coupling that binds nuclear households, which is a modelling choice the paper does not make.
- **Might reduce, untested:** kin-biased assortment can be read as a bonding drive (care or loyalty toward relatives) in an inclusive-fitness frame (Hamilton 1964 is cited). That is the paper's theoretical backdrop for why r matters, not a derivation from drives; whether the full text frames it that way is unknown.
- Net: for the working hypothesis "drives as primitives", this source offers **no support and no refutation**. It supplies a composition constraint (intact households, descent lines) the algebra's split operator would have to respect, whatever its primitives.

## What does it predict or control, and how well?

- **Predicts:** nothing prospectively. It is a retrospective synthesis. The outcome it characterises is the genealogical composition of daughter groups, and (by tally) the cause of fission. No out-of-sample test is described in the abstract. No effect sizes, other than the two index endpoints, are reported there. The Ache result is "not significantly different from zero" against a simulation null; that is a significance statement on two cases, not an effect size, and the p-value is unknown.
- **Controls:** nothing. No intervention.
- **Replications:** none known. 23 citing works at OpenAlex; I did not read any of them, so I cannot say whether any applied the index to new fissions.
- **Failures:** the lineal effect is presented as general ("as found for other social animals") yet the paper's own cases span the whole range, from no excess over the household null (Ache) to the maximum (Piaroa). So the paper's own result is that kin bias is **not** a constant; it is not a predictor of any single split without further variables, and the abstract names none.

## Unconfirmed

- The index formula and its units, and whether it is computed from r among individuals or among households.
- The number and identity of fissions reviewed; the fraction attributed to political conflict versus resource scarcity; how causes were coded.
- Group sizes before and after each fission.
- Whether any non-splitting comparison communities appear.
- Whether the paper states any size or cohesion threshold, or cites one from Carneiro 1987 or Chagnon 1975.
- Whether genealogical data for the Ache, Piaroa or Yanomama cases are published in usable form.
- Whether the lineage assortment index has been used since.

## Ledger recommendation

Keep 083's line 284 as it stands in substance: "no human group-fission dataset with a tested rule" is **not** overturned, and not confirmed either. The Walker and Hill abstract now read at source shows the paper tests a kin-composition index against a simulation null on two or three cases; it does not show a timing rule. Change the tag from "not read, [sa]" to "abstract read [abs]; full text paywalled". D593 should stay open until the full text is obtained through a library or from the author. Nothing from this file may enter v0's split operator as a parameter.

## Validation log (2026-10-30)

Re-checked against Crossref, Unpaywall, OpenAlex, PubMed (PMID 25056829, abstract text) and the HRAF document 909 and hypothesis 2896 pages; two further web searches for an open copy found none.

- ✎ Walker RS, Hill KR (2014), *Human Nature* 25(4): 465-475, doi 10.1007/s12110-014-9209-0: existence, authors, title, volume, pages, online date 2014-07-24, 61 references and 21 Crossref citations all confirmed; Unpaywall and OpenAlex still `closed`, no repository copy, so the full text remains unread and every non-abstract claim stays [sa]. Abstract bullets re-checked word for word against PubMed and accurate, except the conclusion bullet, which dropped "and even other social mammals"; fixed in place.
- ✓ HRAF coding [sa]: both hypotheses, "Supported", p. 471, samples eHRAF World Cultures and the *Encyclopedia of World Cultures*; hypothesis 2896 lists test type "Comparison of percentages", significance and coefficient UNKNOWN, no sample size. Matches the file.
- ✓ Reference-list claims [refs]: every work named in that paragraph appears in the Crossref-deposited list with the stated author and year (Carneiro 1987 "Village splitting as a function of population size", in Donald (ed.) *Themes in ethnology and culture history*; Chagnon 1975 "Genealogy, solidarity, and relatedness: limits to local group size and patterns of fissioning in an expanding population", *Yearbook of Physical Anthropology* 19: 95-110; O'Leary et al. 1994 *Encyclopedia of World Cultures*). All 26 DOIs in the list resolve at Crossref with matching first author (Archie, Nsubuga and Hunley are dated 2005/2007/2007 at Crossref by online-first date against 2006/2008/2008 in print; not an error).
- No fabrications found; nothing removed; no claim upgraded to [read], because only the abstract and metadata were read. Nothing here may feed an equation.

Sources opened: 6 (Crossref record with reference list, Unpaywall, OpenAlex, PubMed abstract, HRAF document 909, HRAF hypothesis 2896), plus 26 Crossref DOI lookups for the reference list.

Verdict: the file is accurate and honest about its limits; its one error was a trimmed quotation in the abstract summary, now fixed. The paper is confirmed closed-access with no open copy, so the index formula, the number of fissions reviewed and the cause tally remain unknown, and the ledger recommendation (abstract read, full text paywalled, D593 open) stands.

## Cross-checks (2026-10-30)

Searched the prior-work directory for this paper's authors, title words, equations and numbers: Walker, Hill, fission, Carneiro, Chagnon, Hamilton, relatedness, lineage, Piaroa, Hutterite, Olsen, Hill et al. 2011 (*Science* 331: 1286). Files with real overlap: 083 (merge, split and fission), 091 (group size, Hutterites, Zhou et al. 2005), 08 (Carneiro), 09 (Hamilton's rule) and 29 (fission-fusion). No equation is stated in this file, so none is cross-checked.

### Agreements

- 083 line 284 and line 312 name Walker and Hill 2014 as the nearest candidate for a tested human fission rule, tagged `[sa]` and not read. That matches this file's verdict: no human fission rule is confirmed or overturned. 083 line 284 still says "Not read"; per the ledger recommendation above, the tag should become "abstract read [abs]". Not edited here, since only this file may be changed.
- Hamilton's rule: 09 (operators, about line 67) gives r b > c and k > 1/r; 29 E-section gives rb > c. 101 cites Hamilton 1964 for inclusive fitness and states no rule. No conflict.
- 091 line 213 says no empirical human fission size law exists "in what I read". 101's abstract gives a composition index, not a size law, so both can stand.
- 091 line 88: Hutterites split around 150 (Dunbar citing Hardin 1988; mean 106.9 over 51 Schmedenleut communities). 101 cites Olsen 1976 and 1987 on Hutterite colony fission but gives no size. Same case domain, no shared number, no contradiction.
- Zhou, Sornette, Hill and Dunbar 2005 (091 section 3b; 09 §E4) is a different paper from Walker and Hill 2014. No shared number.
- No other file cites Chagnon, Smouse, Kaplan, Hill and Hurtado 1996, or Carneiro 1987.

### Same name, different people or works (do not merge)

- Hill, K. R. (this paper, and Hill et al. 2011 *Science*) is not Hill, R. A. (Zhou et al. 2005 in 091 and 09). The Hill et al. 2008 *Proc Roy Soc B* taxon-ratio paper in 083 is a third work.
- Walker, R. S. (this paper) is not Walker, J. M. (Isaac, Walker and Williams 1994, 091), Walker, D. (Milner, Parrow and Walker 1992, 04), Walker, A. M. (046) or Walker et al. 2004 (30).
- Carneiro 1987, "Village splitting as a function of population size" (cited here), is not Carneiro 1970, "A theory of the origin of the state" (08 §23).
- "Fission" here is a community splitting into daughter communities. In 29 E2 and 083 §3 it is the fission-fusion variable (party membership over time, Aureli et al. 2008). Same word, different object.

### Contradiction (not resolved)

- 083 line 284 describes this paper as "a cross-cultural review of fissions with a kin-assortment index tested on Ache and Piaroa fissions, per the search summary" (tag `[sa]`). This file's abstract tag [abs] says "ethnographic review", does not say "cross-cultural", and says the Ache index is compared with controlled simulations while the Piaroa case is a single lineal fission. The validation log above does not settle the wording. Both claims are recorded; **unresolved** until the full text is read.

Sources checked here: the files named above, read by grep and targeted line reads. No new external source was opened.
