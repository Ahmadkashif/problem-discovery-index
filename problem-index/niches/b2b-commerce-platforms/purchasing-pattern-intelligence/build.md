# The Best-Posed Prediction in Commerce

**Niche:** [[niches/b2b-commerce-platforms/purchasing-pattern-intelligence/profile|Purchasing Pattern Intelligence]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The B2B buyer is a repeat purchaser buying known parts on a predictable cycle under a known agreement, and the storefront shows them a bestsellers carousel.
**Tags:** #time-series-forecasting #survival-analysis #gradient-boosting #matrix-decompositions #evaluation-metrics #revenue-impact #confidence-intervals #automation
**Contested on:** Every serious competitor in this niche is fighting to predict what a business customer will order next from the cleanest repeat-purchase record in commerce — and whoever does it accurately enough to act on owns the reorder before the customer initiates it.

## The Problem
A maintenance department orders the same forty consumables on a rhythm set by their equipment and their shifts. A contractor orders a recognisable bundle whenever they start a particular kind of job. A manufacturer draws components against a production schedule. All of it is recorded, identified to the account, and repeated dozens of times. The prediction — what will this customer order, when, and in what quantity — is as well-posed as any prediction in commerce. The storefront responds with products other customers bought, which is the answer to a question nobody in B2B is asking.

## Why Nobody Has Built This
The category imported its playbook from consumer commerce, where anonymity and sparsity are the defining constraints, and never noticed that neither applies. Recommendation is bought as a module and the module is built for retail. The transaction data sits in the resource planning system rather than the storefront, so the platform has partial visibility. And nobody in the organisation owns prediction as a function.

## What to Build
Model the customer's actual purchasing rhythm. Estimate a reorder interval per customer and part with uncertainty, which is the foundation and is directly learnable from a dense repeat history — this is the piece consumer systems cannot do and B2B can. Predict the next order's likely contents and timing, and surface it as a prepared basket the customer confirms rather than assembles, which is the single largest reduction in customer effort the channel can offer. Detect the missing line — a basket that historically includes a companion part and today does not — which is where the immediate revenue is and which reps do by memory today. Predict by job or project context where the pattern is event-driven rather than periodic, since contractors buy in recognisable bundles and calendar models miss them entirely. Model substitution acceptance per customer, drawing on the knowledge capture from the rep work, so a stockout becomes an offer rather than a lost line. Flag the stopped pattern for the fix note's attrition case. Push the prediction to both the customer's storefront and the rep's workspace at the right moment, since a prediction delivered in a report is not acted on. And measure against the honest baseline — repeat-the-last-order — because that baseline is strong in B2B and any system that cannot beat it is theatre.

## Target Customer
Distributors and manufacturers with repeat business customers, B2B commerce platforms, and category management teams.

## Impact If Built
The category imported consumer recommendation into a setting where neither anonymity nor sparsity applies. Per-customer reorder intervals are directly learnable from dense repeat history, and the missing-companion-line detection is where the immediate revenue sits.
