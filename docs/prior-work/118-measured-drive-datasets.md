# 118. Public datasets with a pre-measured drive and group play

Date: 2026-11-01. Scope: one dataset suitable for the measured-drive test, verified from metadata only. No data downloaded. No email address sent to any service.

## Result in one line

No dataset found that has BOTH an individually measured drive (SVO etc.) AND more than one group size with open per-participant data. The best single-group-size match is Szekely et al. (2021). The best multi-group-size dataset (Diederich et al.) has no drive measure that I could confirm.

## Chosen: Szekely et al. 2021 (single group size, SVO slider)

- Paper (Crossref record): Aron Szekely, Francesca Lipari, Alberto Antonioni, Mario Paolucci, Angel Sanchez, Luca Tummolini, Giulia Andrighetto. "Evidence from a long-term experiment that collective risks change social norms and promote cooperation". Nature Communications 12, 5452 (2021-09-15). DOI 10.1038/s41467-021-25734-w. Article licence CC BY 4.0.
- Data: OSF project https://osf.io/wvgk9 (DOI 10.17605/osf.io/wvgk9), public. Files listed via OSF API: full.csv (4.5 MB), full.dta, Raw data.zip, behavioral_types.xlsx, analysis.do, norm_strength.do, figures.do, import.do, folders "Experiment code" and "R code". Download e.g. https://osf.io/download/ra9ex/ (full.csv); existence of the listing confirmed, files not fetched.
- Licence: the article is CC BY 4.0. The OSF project's own licence field is null (no licence set). The paper's data statement says the data "have been deposited" there, so reuse is "data available" with attribution, not an explicit data licence.
- n: 286 recruited, 284 analysed. 28 rounds over 30 days.
- Group size: 6 only (reshuffled every round; temporary size differences from inactive or excluded players). Not two sizes.
- Drive measure: Social Value Orientation slider measure (Murphy et al. 2011), elicited on day 1 before the 28 game rounds, with other trait tests.
- Per-round outcomes: contribution (0-100 endowment), threshold (300) reached / loss, payoff, empirical and normative expectations, personal normative beliefs (every round); conditional contributions in rounds 1, 5, 10, 14, 15, 19, 24, 28; punishment on day 30.
- Group membership: the paper states there were no identifiers visible to players. Whether full.csv carries a group id per round is NOT confirmed.

## Runner-up: Diederich, Goeschl, Waichman 2016 (multiple group sizes, no confirmed drive)

- Crossref: Johannes Diederich, Timo Goeschl, Israel Waichman. "Group size and the (in)efficiency of pure public good provision". European Economic Review, 2016. DOI 10.1016/j.euroecorev.2016.03.001.
- Data: heiDATA DOI 10.11588/DATA/10069 (also Mendeley Data 8s3nys36rj). Stata/TSV/PDF per b2find record.
- 1,110 subjects, linear public goods game, groups of 10, 40, 100. Useful for the size dimension; no individually measured drive found.

## Could NOT confirm

- Any dataset with SVO/inequity/risk measure plus 2+ group sizes (searched Harvard Dataverse, Zenodo, OSF via API and web search; several APIs returned nothing for narrow queries).
- Variable names in Szekely full.csv (group id, SVO score, round).
- Explicit data licence on the OSF project.
- Diederich licence, codebook, and any trait measure.
- Whether CoDa exposes individual-level data: only study-level descriptions found.
- Not checked: Cartwright, Xue, Chai (Economic Inquiry, ICPSR doi:10.3886/E207422V1; keywords public good, SVO; no files listed in Dataverse harvest, group sizes unknown). Bouman and Dijkstra 2025 (DOI 10.1177/10434631251369684, N=120, groups of 5, six rounds, SVO triple-dominance) is too small and its data statement was not seen.

## Validation log

- Web search (3 queries) on public goods / SVO / group size / CoDa: surfaced candidates; no claims taken from search text without a later check, except Diederich design (groups 10/40/100, n=1110) which is from the b2find summary and is not independently verified.
- Harvard Dataverse search API `"social value orientation" AND "public good"`: returned Cartwright/Xue/Chai ECIN package, fileCount 0.
- Zenodo API, two narrow queries: total 0. Broader query: 19 records, none with SVO plus group size; Pereda/Capraro/Sanchez 10.5281/zenodo.2565197 (CC BY 4.0, group size field, no SVO).
- OSF API nodes filter title/description: 0 results.
- Harvard Dataverse search `"group size" "public goods" ...`: 15 hits; none meets criteria (Marshall and Paler, Lebanon, 713 participants, doi:10.7910/DVN/SWYQ26, noted, not examined).
- https://www.nature.com/articles/s41467-021-25734-w: redirected to an auth page, not read.
- https://pmc.ncbi.nlm.nih.gov/tools/idconv/... : PMC8443614. https://pmc.ncbi.nlm.nih.gov/articles/PMC8443614/ : read; source of n, group size, SVO, outcomes, data statement, CC BY 4.0.
- Europe PMC REST: HTTP 503.
- https://api.crossref.org/works/10.1038/s41467-021-25734-w : OK, title/authors/date/licence as above.
- https://api.crossref.org/works/10.1177/10434631251369684 : OK, Bouman and Dijkstra, CC BY 4.0.
- https://api.crossref.org/works?query.bibliographic=... : OK, 10.1016/j.euroecorev.2016.03.001, authors as above.
- https://research.rug.nl/... (Bouman and Dijkstra): N=120, groups of 5, 6 rounds; no data statement shown.
- https://api.osf.io/v2/nodes/wvgk9/ : public true, licence null, created 2018-04-25.
- https://api.osf.io/v2/nodes/wvgk9/files/osfstorage/ : 10 items listed above.

## Licences of quoted and transcribed material (2026-11-01)

- Szekely et al. (2021), Nature Communications 12, 5452: CC BY 4.0 (Crossref record). Used as citation and described facts (sample sizes, design, measures); no text quoted.
- Szekely et al. OSF project (osf.io/wvgk9): the project's licence field is null (no licence set); the article's data statement says the data are deposited there. Only the file listing was read; no data was downloaded for this file. (A later fetch of full.csv sits git-ignored under sim/data/szekely2021; not committed.)
- Diederich, Goeschl & Waichman (2016), Eur. Econ. Rev., and its heiDATA / Mendeley Data records: licence not determined; publisher copyright presumed. Described from a b2find summary (design only); no data downloaded.
- Pereda, Capraro & Sanchez (Zenodo 10.5281/zenodo.2565197): CC BY 4.0 as listed; cited only. Cartwright, Xue & Chai, Bouman & Dijkstra (2025, CC BY 4.0 per Crossref) and Marshall & Paler: cited only; data not examined.
- No Wikipedia-derived text is used in this file. No email address or contact detail appears in this file.
