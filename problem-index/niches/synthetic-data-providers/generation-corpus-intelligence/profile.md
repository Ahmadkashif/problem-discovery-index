# Generation Corpus Intelligence

**Parent Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to turn the accumulated record of generation runs and their outcomes into a certification standard the field lacks — and whoever assembles it defines how the category is judged, which is worth more than any individual product in it.

## Profile
**Market Size:** ~$160M US
**Share of Parent Industry:** ~11% of category revenue
**Digital Adoption:** None — the corpus exists as logs and is used for nothing
**Target Buyer:** The vendors themselves, and the standards and assurance bodies that should exist
**Automation Potential:** Very High — the corpus is already machine-readable

## What Makes This a Distinct Niche
The providers collectively hold thousands of generation runs paired with fidelity evaluations, privacy attack results and, occasionally, downstream model performance. That is the empirical basis for the certification standard the field is missing: which configurations achieve which points on the frontier, for which data shapes; where the trade-off actually sits rather than where theory says it could; which privacy parameters correspond to which measured leakage in practice; which generators fail on which structures. No vendor has assembled it. The reason is not technical — the logs exist and are machine-readable — but that the results would constrain what any of them is able to claim, and the first vendor to publish the picture publishes their own limits alongside everyone else's.

## Current Tools & Gaps
Run logs, internal experiment tracking where it exists, and published research on individual methods evaluated on academic datasets. The gaps: no vendor treats their own run history as an asset; the relationship between configuration and outcome is rediscovered per customer by solutions engineers; the empirical frontier is uncharacterised, so every customer's operating point is chosen by intuition; and nothing exists that a regulator or assurance body could use as a reference for what good looks like.

## Problems
- [[niches/synthetic-data-providers/generation-corpus-intelligence/build|🔨 Build: The Corpus That Would Constrain the Claims]]
- [[niches/synthetic-data-providers/generation-corpus-intelligence/buy|🛒 Buy: Meta-Learning and Experiment Analysis Machinery]]
- [[niches/synthetic-data-providers/generation-corpus-intelligence/fix|🔧 Fix: Configuration Knowledge That Lives in Four People]]
