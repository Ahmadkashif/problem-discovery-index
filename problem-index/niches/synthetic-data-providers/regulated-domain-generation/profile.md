# Regulated Domain Generation

**Parent Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to produce records a domain expert cannot tell are impossible — and whoever does that takes the account, because in a regulated domain a single implausible record ends the evaluation.

## Profile
**Market Size:** ~$180M US
**Share of Parent Industry:** ~12% of category revenue
**Digital Adoption:** Very Low — generic models have no notion of what cannot occur
**Target Buyer:** Healthcare, financial services and industrial data teams
**Automation Potential:** Medium — the constraint set is domain knowledge, the enforcement is mechanical

## What Makes This a Distinct Niche
In healthcare, finance, insurance and industrial process data, plausibility is not a statistical property. A clinician reads a synthetic patient record with a paediatric dose on a seventy-year-old, a diagnosis code that cannot co-occur with the procedure billed, or a lab value incompatible with life, and the evaluation is over in ten seconds. A general generator has no representation of what is impossible — it has only what was frequent — and the impossible cases are frequently the ones near the boundary of the observed distribution, which is exactly where a generative model interpolates most freely. The contest is domain-constrained generation, where the constraint set comes from clinical, regulatory and physical knowledge rather than from the data.

## Current Tools & Gaps
General-purpose tabular generators, a small number of clinically oriented synthetic record tools, and manual review by domain experts as the de facto quality gate. The gaps: medical and financial coding relationships are formally specified in published ontologies and terminologies that generators do not consume; physical and physiological bounds are not encoded; regulatory rules that make certain combinations impossible rather than rare are not represented; and nobody reports an expert-detectable implausibility rate, which is the metric the buyer is actually applying.

## Problems
- [[niches/synthetic-data-providers/regulated-domain-generation/build|🔨 Build: Statistically Faithful Nonsense]]
- [[niches/synthetic-data-providers/regulated-domain-generation/buy|🛒 Buy: Clinical and Financial Ontologies That Already Encode the Rules]]
- [[niches/synthetic-data-providers/regulated-domain-generation/fix|🔧 Fix: The Expert Review That Is the Real Acceptance Test]]
