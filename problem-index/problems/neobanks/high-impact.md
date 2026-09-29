# The Account Freeze Nobody Grades

**Industry:** [[neobanks|Neobanks]]
**Type:** High Impact
**One-liner:** A neobank freezes accounts by model, discovers within days whether it was right, and never writes that answer back to the model that decided.
**Tags:** #logistic-regression #gradient-boosting #graph-neural-networks #causal-inference #confidence-intervals #evaluation-metrics #feature-engineering #compliance #revenue-impact

## The Problem
A member's account is restricted. The trigger might be a deposit that pattern-matches a stolen cheque, a login from an unfamiliar device followed by a large transfer, a velocity rule, a name mismatch on an ACH credit, or a vendor score crossing a threshold that was set eighteen months ago by someone who has since left. The card stops working, the balance is unavailable, and the member receives a message referring them to the deposit agreement.

What happens next is the part that matters. The member calls. A risk analyst reviews the case, sometimes requests documentation, and either reinstates the account or closes it and returns the funds. Alternatively the member never calls, the account ages out, and the balance is escheated or returned.

Each of those endings is a grade on the original decision. A reinstatement is a false positive with a receipt attached: the institution decided this person was a risk, examined the evidence, and concluded otherwise. A closure with a confirmed fraud finding is a true positive. An account that goes quiet is ambiguous but not uninformative.

Almost none of this is fed back. The freeze is recorded in the risk platform. The review outcome is recorded in the case management tool. The member's subsequent behaviour — did direct deposit resume, did they come back — is in the core ledger. The three are joined for regulatory reporting at a quarterly aggregate level and never at the level of the individual decision, which is the only level at which a model can learn.

The result is a risk function that knows its alert volume and its manual review cost and does not know its precision. Thresholds move in response to loss spikes and to complaint volume, in alternating directions, with no measurement of the tradeoff either move is making.

## Why It's Unsolved
The decision and the outcome sit in different systems owned by different teams, and no one is accountable for the join. Risk engineering owns the models, operations owns the reviews, and the data team serves whoever files a ticket. A false positive costs the institution a customer quietly; a false negative costs it money loudly and shows up in the loss report. The asymmetry in visibility produces an asymmetry in tuning.

The vendor layer compounds it. Scores arrive from Socure, Sardine or Sift as numbers, and the institution's own outcome data is rarely returned to those vendors in a usable form, so the purchased models are tuned on the vendor's cross-customer population rather than on this customer's. Meanwhile the institution's internal rules sit on top of the vendor score with no shared evaluation frame, so nobody can say whether a given rule is adding signal or merely adding declines.

There is a genuine measurement difficulty underneath the organisational one. A frozen account that was going to commit fraud is prevented from doing so, which is the point, and also means the counterfactual is unobservable. Only the reviewed cases produce clean labels, and reviews are triggered by the member complaining — which correlates with being legitimate. The label set is therefore biased in a direction that flatters nobody and is usually handled by ignoring it.

And the regulatory frame discourages precision talk. BSA and suspicious activity obligations are described in terms of not missing things. There is no examination finding for freezing too many legitimate customers, so the institutional incentive runs one way even where the business incentive does not.

## What a Solution Looks Like
Construct the label set first and model second. Every restriction, the reason codes that produced it, the review decision, the documentation requested and supplied, the final disposition, and the member's ninety-day behaviour after reinstatement, joined into one record per decision. That table is the product. It already exists in pieces and nobody assembles it.

Grade each rule and each vendor score independently against it. Most rule libraries accumulate over years and contain rules that fire frequently and add nothing; precision per rule, measured against reviewed outcomes, identifies them immediately and retiring them is the cheapest available reduction in false positives.

Correct for the review-selection bias explicitly rather than pretending it is absent. Members who complain are not a random sample of those frozen, and treating reviewed cases as if they were produces a model that systematically underestimates false positives among the members least equipped to contest a freeze. Propensity weighting on complaint likelihood, plus a deliberately sampled audit of unreviewed freezes, is the honest version.

Graduated responses rather than a binary. Holding a single deposit, capping outbound transfers, or requiring step-up verification are all available and all reversible; a full freeze on an account holding a paycheque is the heaviest instrument available and is currently used for cases that do not need it because the system offers nothing lighter.

Reason codes exposed to the front line, so the agent who takes the call can act on the same information the model used.

## Impact If Solved
Fraud loss and false positives are treated as a single dial, tuned blind, by an institution that holds the evidence to tune it precisely. Assembling the decision-outcome join is weeks of data engineering rather than a research programme, and it converts the central risk question from a matter of institutional temperament into a measured tradeoff. The downstream effect is felt by the members least able to absorb a two-week loss of access to their own wages, which is the population these institutions were built to serve.
