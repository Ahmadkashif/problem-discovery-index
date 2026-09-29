# Two Metric Sets That Do Not Compose Into the Claim

**Niche:** [[niches/synthetic-data-providers/utility-privacy-certification/profile|Utility–Privacy Certification]]
**Industry:** [[industries/synthetic-data-providers|Synthetic Data Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Customers buy a guarantee that synthetic data is both safe to release and useful to train on, and the industry ships two separate sets of metrics that do not compose into that claim.
**Tags:** #bayesian-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #monte-carlo-methods #cross-validation #compliance #gaussian-processes
**Contested on:** Every serious competitor in this niche is fighting to certify that a synthetic dataset is simultaneously safe to release and useful to train on — and whoever issues that claim credibly takes the category, because it is the only claim customers are actually buying.

## The Problem
A bank wants to give a synthetic version of its transaction data to an external modelling team. The vendor delivers a report: marginal distributions match closely, correlations are preserved, and the generation used a differential privacy parameter of eight. The bank's privacy officer does not know what a parameter of eight permits. The modelling team does not know whether a model trained on this will work, because distribution similarity is not the same as supporting a predictive task. Nobody can say whether a different setting would have been better for both, because the frontier between the two properties has not been characterised. The decision is made on institutional comfort.

## Why Nobody Has Built This
The two properties are evaluated by different communities with different vocabularies — statistical fidelity from the modelling side, formal and empirical privacy from the security side — and nobody has built the bridge because it belongs to neither. Characterising the frontier requires generating at multiple settings and evaluating both properties at each, which costs compute and produces a picture in which the vendor's chosen operating point is one option among several rather than the answer. And the utility measure that matters — downstream model performance — requires the customer's actual task, which the vendor frequently does not have.

## What to Build
Characterise and certify the joint property. Generate across a range of privacy settings and evaluate both properties at each, producing the frontier for this dataset and this task rather than a single point — which is the artefact the decision requires and which no vendor produces. Use downstream task performance as the utility measure wherever the customer's task can be specified, since statistical similarity is a proxy that is frequently uninformative about whether a model will work, and the customer can supply a task even when they cannot supply the data. Run empirical privacy attacks as a standard, not an option: membership inference, attribute inference and record linkage, at each operating point, which grounds the formal guarantee in a demonstrated one. Report the frontier with an interpretation, so the customer chooses an operating point knowing what they are trading. State the residual risk in terms a privacy officer can act on, which the dedicated niche below addresses. Separate the certification from the generation organisationally where possible, since a vendor certifying their own output is the position the field is in and is the reason nobody trusts the numbers. And publish the methodology, because a certification whose method is proprietary is an assertion.

## Target Customer
Privacy, legal and model teams jointly, the generation vendors who would be certified, and the independent assurance bodies for whom this is an unclaimed role.

## Impact If Built
The category sells a joint guarantee and reports two separable metric sets, which leaves the customer's actual decision unsupported. The frontier is the artefact the decision needs, and downstream task performance is the utility measure that makes it meaningful.
