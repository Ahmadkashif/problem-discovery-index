# Served Under the Same Name

**Niche:** [[niches/ai-inference-providers/quantisation-quality-accounting/profile|Quantisation Quality Accounting]]
**Industry:** [[industries/ai-inference-providers|AI Inference Providers]]
**Type:** Fix (Pain Point)
**One-liner:** A quantised deployment is served under the original model's name, frequently without stating the scheme, so customers compare providers on a model identity that does not mean the same thing at each of them.
**Tags:** #compliance #evaluation-metrics #descriptive-statistics #confidence-intervals #hypothesis-testing #quick-win #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to state what a quantisation actually costs in quality on the customer's own task — and whoever does that takes the account, because the trade is being made on everyone's behalf and measured by almost nobody.

## The Problem
Three providers offer the same named open model. One serves it at full precision, one at eight bits, one at four bits with a particular scheme, and the naming is identical at all three. A customer benchmarks them, finds a quality difference, and attributes it to serving infrastructure. A provider changes their quantisation between evaluation and production and the customer's results stop reproducing. The model's publisher gets attributed with behaviour their weights do not produce. The identity everybody is transacting on does not identify what is being served.

## Why It's Still Broken
Disclosing the quantisation invites a direct comparison on the axis where a provider is weakest, and no one will do it unilaterally. There is no naming convention, so even a willing provider has no standard form to disclose in. Customers mostly do not know to ask, because the assumption that a model name identifies a model is reasonable. And the model publishers, who have the strongest interest in the name meaning something, have no leverage over how it is used.

## What a Fix Looks Like
Make the served artefact identifiable. Disclose the precision and scheme in the model identifier and in the API response, which costs nothing, is the minimum honest step, and immediately makes cross-provider comparison meaningful. Version the served artefact by a hash of the actual weights, so a customer can tell whether what they are served today is what they evaluated last month — this is the strongest form of the fix and removes any ambiguity. Notify customers before changing a deployment's precision, since a silent change is the mechanism by which reproducibility breaks. Offer full precision as an available option at a stated price, so the disclosure comes with a remedy. Report a quality delta against full precision on a published evaluation set, which is the number the disclosure implies and which any provider can produce. Support pinning to a specific served artefact for customers who need stability, which many regulated buyers require and nobody offers. Push for a naming convention across the industry, since unilateral disclosure is punished and a shared convention is exactly what fixes that. And encourage model publishers to state what may be served under their name, since they are the party whose reputation is being spent.

## Who Feels the Pain
Customers comparing providers on an identity that means different things; teams whose evaluated results stop reproducing after a silent change; and model publishers attributed with output their weights never produced.

## Impact If Fixed
The identity everyone transacts on does not identify what is served. Hashing the actual weights into the served artefact version removes the ambiguity entirely, and disclosing precision in the response is a free change that makes cross-provider comparison mean something.
