# The Customer Can Now Do This Themselves

**Niche:** [[niches/web-data-extraction-firms/structured-extraction-services/profile|Structured Extraction Services]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Model-based extraction is available to anyone with an API key, so a structured extraction service must now be measurably more accurate and cheaper per page than the customer's own attempt, and neither is demonstrated.
**Tags:** #large-language-models #evaluation-metrics #transfer-learning #confidence-intervals #hypothesis-testing #cross-validation #automation #data-integration
**Contested on:** Every serious competitor in this sub-niche is fighting to return the right fields from a page nobody wrote a parser for, at a cost per page that beats the customer doing it themselves — and whoever does that takes the account, because the alternative is now genuinely available to the buyer.

## The Problem
A data team evaluates a structured extraction service. Over a weekend an engineer writes a script that fetches pages and asks a model for the fields, and it works reasonably well. The service costs more per page and claims higher accuracy without measuring it against anything. The team cannot tell whether they are buying meaningfully better extraction or a hosted version of what they just built. The service's genuine advantages — accumulated templates for the same sites across many customers, per-field validation, fallback strategies, silent-breakage detection — are real and are never demonstrated, so the comparison is decided on price.

## Why Nobody Has Built This
The service was positioned as access to a capability during a period when the capability was scarce, and the positioning did not update when it stopped being scarce. Measuring accuracy per field per source requires ground truth the firm has not built. Demonstrating superiority against the customer's own approach means running that comparison honestly, which some firms would lose. And the accumulated template asset is invisible to the customer and undervalued internally.

## What to Build
Compete on measured accuracy and on the assets a customer cannot replicate. Measure extraction accuracy per field per source against verified ground truth and publish it, since an unmeasured accuracy claim is worth nothing against an alternative the buyer can test in an afternoon — this measurement is the foundation of the whole position. Run the comparison against a naive model-based baseline in every evaluation and show the difference, which is the honest version of the sales conversation and is the one the customer is having silently anyway. Build and reuse site-specific templates across customers, since many customers extract from the same popular sites and a learned template that has been corrected a hundred times is genuinely better than a cold model call — this cross-customer asset is the defensible advantage and it is not currently treated as one. Use a cheap path where it works and escalate only where needed, which the fix note develops. Attach per-field confidence and validation, which a customer's weekend script will not have. Handle the long tail of page variants — regional versions, logged-out states, layout experiments — which is where a naive approach quietly fails and where accumulated experience shows. Detect silent breakage, which is the correctness niche and is the capability a customer will not build. And be explicit that the product is accuracy and reliability rather than access, because access is no longer the thing being sold.

## Target Customer
Data teams buying structure, and the firms whose positioning predates the availability of the capability they are selling.

## Impact If Built
The customer's alternative is now an afternoon's work, which makes an unmeasured accuracy claim worthless. Cross-customer site templates corrected a hundred times are the genuinely defensible asset and are currently invisible to everyone including the firm.
