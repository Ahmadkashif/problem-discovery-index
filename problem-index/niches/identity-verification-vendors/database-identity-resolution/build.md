# Resolving the People Records Miss

**Niche:** [[niches/identity-verification-vendors/database-identity-resolution/profile|Database Identity Resolution]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The check works well for people with a decade at one address and poorly for everyone else, which is a description of who gets excluded.
**Tags:** #graph-theory #bayesian-inference #evaluation-metrics #confidence-intervals #data-integration #k-nearest-neighbors #gradient-boosting #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to confirm that a claimed identity exists and belongs to this person from records that were never built for the purpose — and whoever resolves thin-file and frequently-moving populations best serves the people everyone else cannot see.

## The Problem
Database identity resolution works by finding corroborating records. A person with a long credit history, a stable address and a phone in their own name resolves easily. A recent arrival, a young adult, someone who moves annually, someone in shared or informal housing, someone whose phone is on a family plan, or someone who has deliberately minimised their data footprint resolves poorly or not at all. The check returns no record, the application fails, and the reason is that the sources were built for credit marketing rather than for identity.

## Why Nobody Has Built This
Coverage was inherited from whatever data was commercially available, so the population served was determined by the sources rather than chosen — and nobody was accountable for the people those sources never contained. Thin-file resolution is genuinely hard and commercially unattractive, since the excluded population is by definition less profitable. Failure reasons are not distinguished, so the gap is invisible. And no customer has demanded coverage reporting.

## What to Build
Broaden the sources and distinguish the failures. Separate "no record found" from "record found and contradicted", which is the core because they are entirely different situations and are currently the same result — one is a coverage gap and the other is a genuine discrepancy. Report coverage by population characteristics — tenure, mobility, age, housing type — since that is where the exclusion lives and it is measurable today. Incorporate sources that reach thin-file populations, including utility, rental, employment, education and government-adjacent records where lawful. Model the confidence of a resolution rather than returning a binary, as a weak match and no match are different and deserve different treatment. Use the relationship graph, because a person with few records of their own may be connected to well-documented ones in ways that corroborate. Handle name and address variation properly, since transliteration, compound surnames, informal addresses and recent moves are a large share of failures and are a solvable linkage problem. Offer a documented alternative path when the record genuinely does not exist, as a person cannot conjure a credit file. Measure resolution rate by population and target improvement where it is lowest. Keep the data governance explicit, since assembling more sources about people is exactly the practice that requires care. And publish coverage honestly, because a customer choosing a vendor for an underserved population currently has no basis to.

## Target Customer
Data and product leadership, institutions serving thin-file and newly arrived populations, financial inclusion policy functions, and data suppliers whose coverage gaps are unmeasured.

## Impact If Built
Coverage was inherited from commercially available sources, so the population served was determined rather than chosen. Distinguishing a coverage gap from a contradiction, and reporting resolution by tenure and mobility, makes the exclusion visible and addressable.
