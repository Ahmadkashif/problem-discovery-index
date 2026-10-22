# Counter Grading That Predicts the Warehouse Grade

**Niche:** [[niches/wireless-retail-agents/trade-in-intake-promo-eligibility/profile|Trade-In Intake & Promo Credit Eligibility]]
**Industry:** [[industries/wireless-retail-agents|Wireless Retail Agents]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The rep promises a trade-in credit based on a glance, and the processing centre decides the real one weeks later.
**Tags:** #cnns #object-detection #semantic-segmentation #transfer-learning #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche (trade-in administrators' in-store tools and device diagnostic vendors such as Phonecheck) is fighting to grade a traded-in phone at the counter the same way the processing centre will grade it weeks later, and whoever closes the gap between promised and paid credit takes the dealer's trade-in workflow.

## The Problem
Programme grades hinge on details a rep misses under time pressure: hairline cracks under certain light, scratches past a threshold, burn-in, a lens chip. A missed defect becomes a reduced credit, a customer complaint and sometimes a cancellation inside the chargeback window.

## Why Nobody Has Built This
Final grades sit with the trade-in administrators, not the dealers, and the grading definitions are programme-specific. Without labels from the processing centre, counter grading can't be trained.

## What to Build
A guided photo capture on a store tablet with a simple light box. A defect-detection model trained on the administrator's final grades predicts the programme grade and the probability of a downgrade before the promise is made. Where risk is high, the rep sets the customer's expectation before the deal is closed.

## Target Customer
Operations leads at exclusive chains, co-developed with a trade-in administrator that gains fewer disputes.

## Impact If Built
Fewer surprise credit reductions, fewer angry return visits, and fewer cancellations triggered by trade-in disputes.
