# Forty Seconds, Properly Equipped

**Niche:** [[niches/payment-fraud-vendors/the-review-analyst/profile|The Review Analyst]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The hardest decisions in the pipeline are made in under a minute by someone assembling context from four browser tabs.
**Tags:** #large-language-models #k-nearest-neighbors #worker-facing #evaluation-metrics #confidence-intervals #graph-theory #automation #gradient-boosting
**Contested on:** Every serious competitor in this niche is fighting to make forty seconds enough to decide correctly on exactly the cases the model could not — and whoever equips that decision changes the outcome of the transactions the product is worst at.

## The Problem
The case in front of the analyst was routed there because the model could not decide. That means the signals conflict: a new device but a matching address, a high-value order but an established customer, a shipping mismatch with a plausible explanation. Resolving it well requires context — what similar cases turned out to be, what this customer has done before, what this merchant's legitimate edge cases look like — and the analyst has a case screen, some lookup tools, and forty seconds.

## Why Nobody Has Built This
Review was treated as capacity rather than as capability, so the tooling optimises throughput — a function measured in cases per hour gets a faster screen rather than a better one. The model's job was considered finished when it routed the case. Decline decisions produce no outcome, so analyst accuracy is unmeasurable in the current setup and therefore unmanaged. And review is often outsourced, which distances it from product development.

## What to Build
Give the analyst what the model could not resolve. Assemble the full case context automatically — customer history, device and network relationships, similar past cases and their outcomes, merchant-specific legitimate patterns — which is the core and returns the forty seconds to judgement rather than gathering. Retrieve similar resolved cases with what happened, since that is the single most useful input and the analyst currently relies on memory. Explain why the model was uncertain, because knowing which signals conflict tells the analyst where to look. Show the customer's relationship graph, as connections are what distinguish a genuine customer from a ring and are invisible on a case screen. Rank the queue by value and time sensitivity rather than by age, so effort follows consequence. Measure analyst consistency on duplicated cases, which is the only quality signal available without outcomes and is not collected. Capture the reason for every decision in a structured form, since that is the training data for automating the easier half of the queue. Feed outcomes back where they exist, and use the randomised approval sample to evaluate declines, which connects this directly to the label problem. Automate the cases where analysts are unanimous, as a portion of the queue is not genuinely ambiguous at all. And measure decision quality rather than handle time, because the current metric optimises the wrong thing on the hardest cases in the product.

## Target Customer
Review operations leadership, the analysts themselves, merchants whose hardest transactions are decided here, and review outsourcers competing on quality.

## Impact If Built
A function measured in cases per hour gets a faster screen rather than a better one, so review became capacity rather than capability. Assembling context and retrieving similar resolved cases returns the forty seconds to the judgement it was meant for.
