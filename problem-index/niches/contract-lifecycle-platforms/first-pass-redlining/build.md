# Knowing Which Clause Not to Touch

**Niche:** [[niches/contract-lifecycle-platforms/first-pass-redlining/profile|First-Pass Redlining]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Automated redlining that is right ninety percent of the time saves nothing, because the lawyer must read everything to find the ten percent, so the product is judged entirely on whether it knows its own boundary.
**Tags:** #large-language-models #transformers #bayesian-inference #confidence-intervals #evaluation-metrics #cross-validation #hypothesis-testing #automation
**Contested on:** Every serious competitor in automated redlining is fighting to make the routine edits correctly without counsel and to know reliably when a provision is not routine — and whoever holds that boundary takes the legal function, because being wrong once on the wrong clause ends the deployment.

## The Problem
A review tool processes an incoming agreement and produces twenty-three suggested edits. Counsel reads all twenty-three and the surrounding provisions, because they have no way to know which suggestions are reliable and because the consequence of an unnoticed error on the liability clause is severe and personal. The review takes nearly as long as it would have without the tool. The tool's accuracy is genuinely high; its value is near zero, because accuracy without a trustworthy boundary does not reduce the reading.

## Why Nobody Has Built This
The category is optimising for coverage and fluency, which is what demonstrations reward, and refusal makes a worse demonstration. Calibration is hard and is not what the model providers optimise for. There is also no established way to evaluate the boundary: the benchmarks measure whether the right edit was suggested, not whether the system correctly declined on the cases it should have. And the customers have not yet articulated the requirement, because they experience the failure as a general feeling that the tool cannot be trusted rather than as a specific missing capability.

## What to Build
The boundary as the product. Classify every provision by whether the playbook determines the answer: a provision matching a known type with a stated position and no unusual features is routine and is edited; anything with non-standard structure, an unusual interaction with another clause, a deal characteristic outside the policy's stated conditions, or simply low model confidence is escalated with the reason stated. Calibrate that classification against held-out contracts reviewed by the customer's own lawyers rather than against a public benchmark, since the boundary is specific to this company's policy and risk appetite. Present the output in two clearly separated groups — handled, and needs you — with the second group small and specific, because that separation is the entire mechanism by which reading time is saved. Attach consequence to every deviation, so the lawyer reads why it matters rather than that it differs. Learn from every correction, since a lawyer overriding a suggestion is the highest-quality training signal available and is currently discarded. And measure hours returned against a controlled baseline rather than counting accepted suggestions, which is the metric the buyer actually needs and the one vendors avoid.

## Target Customer
General counsel and legal operations at companies with high contract volume, CLM vendors shipping review features, and the specialist contract review vendors competing on accuracy.

## Impact If Built
Value in this product is entirely determined by whether the lawyer can stop reading, which depends on the boundary rather than on the average. Calibration against the customer's own lawyers and a two-group presentation are what convert a high-accuracy tool into saved hours.
