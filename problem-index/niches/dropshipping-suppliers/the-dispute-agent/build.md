# Two Accounts and a Photograph

**Niche:** [[niches/dropshipping-suppliers/the-dispute-agent/profile|The Dispute Agent]]
**Industry:** [[industries/dropshipping-suppliers|Dropshipping Suppliers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A dispute agent adjudicates between a merchant and a supplier over an item neither of them has ever seen, with evidence consisting of a photograph and two conflicting accounts.
**Tags:** #worker-facing #large-language-models #evaluation-metrics #confidence-intervals #workflow-orchestration #compliance #descriptive-statistics #automation
**Contested on:** Every serious competitor in this niche is fighting to give the dispute agent evidence instead of two accounts — and whoever does that makes the platform's adjudication defensible, which is what merchants are actually buying.

## The Problem
The merchant says the goods arrived damaged and unsellable. The supplier says they shipped them in perfect condition and the carrier is responsible. There is one photograph, taken by an end customer, of something in a box. The agent has fifteen minutes, no physical access, no record of how this supplier has behaved in similar cases, no idea whether this merchant disputes everything, and a policy document written for clearer situations. They decide. Somebody loses money and concludes the platform is unfair. The platform holds the order history, the tracking record, the supplier's dispute pattern and the merchant's, and hands the agent none of it.

## Why Nobody Has Built This
Dispute handling is a support cost centre optimised for resolution time, and evidence assembly increases handling time before it reduces it. The relevant data lives across order, logistics, supplier and merchant systems with nobody owning the join. Adjudication quality has no metric, so there is nothing to improve against. And both parties are dissatisfied whatever happens, which normalises the outcome.

## What to Build
Assemble the case before the agent opens it. Pull the full context automatically — order, tracking, timing, supplier dispute history and outcomes, merchant dispute history, the product's return pattern across all merchants — which converts an adjudication between two assertions into one with a factual basis, and is the core of the build. Extract what the evidence actually shows: photographs, message threads and timestamps contain more than a busy agent will read, and structuring them is straightforward. Check the claim's consistency against the tracking record, since damage claims, non-delivery claims and timing claims are frequently contradicted by data already held and this is the fastest available resolution. Surface base rates — this product is damaged in four percent of shipments across nine hundred merchants — which reframes the case from a credibility contest to a probability and is the single most useful thing the platform can add. Show precedent from similar decided cases with their outcomes, which is how consistency is achieved in practice rather than by policy text. Recommend an outcome with its reasoning and confidence, leaving the decision with the agent, since the consequential and ambiguous cases need judgement and an automated verdict would be resented by both parties. Auto-resolve the unambiguous cases, which are a large share and currently consume the same queue. Record the decision and its basis in a form that supports appeal and analysis, which is currently a free-text note. Feed outcomes into supplier and merchant scores, so patterns of bad faith have consequences. And measure adjudication quality by appeal and reversal rates rather than by handling time.

## Target Customer
Support operations at dropshipping and sourcing platforms, the agents themselves, and marketplace trust teams handling merchant-supplier disputes.

## Impact If Built
The platform holds the tracking, the histories and the product's damage rate across nine hundred merchants, and hands the agent a photograph. Base rates reframe a credibility contest as a probability, and precedent is how consistency is actually achieved.
