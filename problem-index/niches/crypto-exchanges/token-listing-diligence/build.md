# The Assessment That Learns From Outcomes

**Niche:** [[niches/crypto-exchanges/token-listing-diligence/profile|Token Listing Diligence]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Exchanges have listed thousands of assets and watched hundreds fail, and no listing framework has ever been calibrated against that record.
**Tags:** #gradient-boosting #graph-theory #survival-analysis #evaluation-metrics #confidence-intervals #large-language-models #compliance #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to assess an asset's code, distribution, team, legal characterisation and market integrity faster and more accurately than the venue that listed it first — and whoever does it without redoing the same analysis every other exchange already did takes the listing advantage.

## The Problem
Token listing is a judgement rendered by a committee reading documents. The assets that subsequently collapsed, were exploited, were abandoned by their teams or turned out to be concentrated in three wallets are all on record, with their pre-listing characteristics preserved on a public ledger and in public repositories. That is a labelled dataset about which listing signals predict failure, and every exchange has one. None has used it to calibrate the criteria the committee applies.

## Why Nobody Has Built This
Listing was a legal and commercial judgement, so nobody framed it as prediction — the committee's job was to approve or refuse, not to estimate. Delisting is treated as an unrelated event handled by a different process. Listing revenue rewards throughput. And the outcome record is scattered across incident reports, delisting notices and market data that nobody assembled.

## What to Build
Calibrate the criteria against the outcome record. Assemble the historical listings with their outcomes — exploited, abandoned, delisted, concentrated, still trading — which is the core and is the dataset the entire category has never built. Extract the pre-listing characteristics from the public record, since the contract code, distribution, repository activity, team history and market structure at listing time are all preserved and recoverable. Model which signals predicted failure, as the committee's weighting has never been tested and some of it will be wrong. Compute distribution concentration systematically, because it is the single most mechanical and most predictive signal and is currently eyeballed. Analyse contract code for the patterns that preceded exploits, which is a capability the audit industry has and the listings process does not consume in a structured way. Score and rank rather than approve or refuse, so marginal assets get monitoring instead of a binary. Reuse assessments across the industry where public, since every exchange reads the same audit report and the duplication is total. Monitor the listing assumptions after listing, because concentration, team activity and liquidity all change and nothing watches them. Record the committee's reasoning in a structured form, which is what makes the next calibration possible. And report listing outcome rates, since a listings function that never measures its own hit rate is not learning.

## Target Customer
Listings and legal leadership, exchange risk committees, token issuers facing inconsistent assessment, and market data and audit vendors adjacent to the artefacts.

## Impact If Built
Listing was framed as a judgement rather than a prediction, so the outcome record was never used. Thousands of listings with known outcomes and publicly preserved pre-listing characteristics is a labelled dataset every exchange holds and none has opened.
