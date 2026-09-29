# The Epsilon Chosen for Utility

**Niche:** [[niches/synthetic-data-providers/utility-privacy-certification/profile|Utility–Privacy Certification]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Fix (Pain Point)
**One-liner:** The differential privacy parameter is set to whatever value keeps the data useful, reported as though it were a protection decision, and nobody states which it was.
**Tags:** #hypothesis-testing #confidence-intervals #descriptive-statistics #evaluation-metrics #monte-carlo-methods #compliance #quick-win #bayesian-inference
**Contested on:** Every serious competitor in this niche is fighting to certify that a synthetic dataset is simultaneously safe to release and useful to train on — and whoever issues that claim credibly takes the category, because it is the only claim customers are actually buying.

## The Problem
A generation run is configured with a privacy parameter. The value was arrived at by trying several and choosing the one at which the data still supported the customer's model — which is a utility decision. It is reported in the deliverable as a privacy guarantee, in a field labelled epsilon, with no indication of how it was selected. The customer's privacy officer reads it as a protection level that was chosen for protection reasons. The field acknowledges this practice informally and does not report it, which means a formal guarantee with a genuine mathematical meaning is being used as a label.

## Why It's Still Broken
The parameter's practical interpretation is genuinely contested, which has made almost any value defensible to an audience that cannot evaluate it. Choosing it for utility is the only way to deliver data that works, given that a meaningfully protective value frequently destroys the utility — which is the real finding and is uncomfortable to state. Nobody reports the selection process because nobody asks. And the customer who could ask is the privacy officer, who is the least equipped to interrogate it.

## What a Fix Looks Like
State how the value was chosen and what it means empirically. Report the selection process explicitly — chosen to meet a utility target, chosen to meet a protection standard, or chosen by convention — which is a one-line disclosure that changes how the number is read and is the single most honest improvement available. Report the empirical attack results at the chosen value, which grounds the parameter in a demonstrated leakage rather than a theoretical bound and is what a privacy officer can actually reason about. Show the frontier, so the customer sees what protection they gave up for the utility they received rather than a single number presented as a decision. State the accounting assumptions, since the parameter's meaning depends on the unit of privacy, the composition across queries and the adjacency definition, and vendors differ on all three in ways that make published values incomparable. Compare against published practice, so a customer knows whether their value is conservative or unusual. And stop presenting a utility-driven choice as a protection guarantee, which is the substance of the fix and is a disclosure decision rather than a technical one.

## Who Feels the Pain
Privacy officers approving releases on a number chosen for a different purpose; the individuals in the source data whose protection was traded for utility without anybody stating it; and the vendors whose formal guarantee is discredited by the practice of selecting it this way.

## Impact If Fixed
Disclosing how the parameter was selected is a one-line change that transforms how it is read, and reporting empirical attack results at that value grounds it in something a privacy officer can evaluate. Stating the accounting assumptions is what would make published values comparable across vendors at all.
