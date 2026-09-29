# Knowing the Promise and Not the Performance

**Niche:** [[niches/contract-lifecycle-platforms/obligation-performance-monitoring/profile|Obligation Performance Monitoring]]
**Industry:** [[industries/contract-lifecycle-platforms|Contract Lifecycle Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An obligation register records that the company promised a 99.9 percent service level and says nothing about whether it delivered one, because nothing joins the contract to the monitoring system.
**Tags:** #graph-theory #time-series-forecasting #change-point-detection #descriptive-statistics #evaluation-metrics #confidence-intervals #data-integration #compliance
**Contested on:** Every serious competitor here is fighting to join contract terms to operational reality and say whether a commitment is actually being met — and whoever does that takes the commercial function, because knowing the obligation and knowing whether it is honoured are different products and only the first exists.

## The Problem
The obligation register lists, for a major customer, a 99.9 percent monthly availability commitment with service credits, a quarterly security report, an annual penetration test summary, and thirty-day deletion of customer data after termination. Availability is measured continuously in the monitoring platform, and nobody has ever compared the two. The quarterly report has been sent twice in two years. The penetration test happened and nobody told the customer. The company discovers all of this when the customer's procurement team runs a contract compliance review and arrives with a credit claim and a list.

## Why Nobody Has Built This
CLM products end at the repository boundary, and monitoring an obligation means integrating with systems owned by engineering, delivery and finance, which is a different buyer and a different integration surface. Obligations were modelled as tasks because a task is easy to implement, and a task with a due date can be completed without anything having been verified. The category's buyer is legal, and legal's question is what was promised, so the product answered that question and stopped. And breach is usually discovered by the counterparty, which converts it into a commercial dispute rather than a product requirement.

## What to Build
Obligations as monitored conditions with evidence. Classify each extracted obligation by how it can be verified: measurable against an operational data source, evidenced by an artefact, or attested by a person — since the three require different treatment and conflating them is why registers become task lists. For the measurable ones, define the join to the system that holds the answer — monitoring for service levels, billing for volume commitments and price terms, the security programme for attestations, delivery records for milestones — and compute compliance continuously rather than asking someone. For the evidenced ones, track the artefact and its currency, since an expired insurance certificate is a common and entirely preventable breach. For the attested ones, keep the attestation but record who and when and against what wording. Predict breach rather than reporting it, since a service level trending toward its threshold two weeks before month end is actionable and a breach notice is not. Compute the financial exposure — accrued credits, penalties, termination rights triggered — which is the number that makes this a commercial product rather than a legal one. And do all of it for the counterparty's obligations too, which is where the recoverable money usually is.

## Target Customer
Commercial, delivery and finance functions at companies with service level and volume commitments; and the CLM vendors whose obligation registers currently decay after implementation.

## Impact If Built
Extraction without monitoring produces a register nobody opens, which is why obligation management has the reputation it has. The join to operational systems is the whole product, and predicting breach before it happens is what makes it worth paying for.
