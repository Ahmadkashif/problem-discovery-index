# Paying the Higher Rate for Data You Had

**Niche:** [[niches/payment-processors/fee-and-interchange-optimisation/profile|Fee & Interchange Optimisation]]
**Industry:** [[industries/payment-processors|Payment Processors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Interchange qualification depends on data and timing the merchant frequently controls, the conditions are published, and merchants pay the higher rate indefinitely without knowing why.
**Tags:** #compliance #evaluation-metrics #data-integration #descriptive-statistics #automation #revenue-impact #optimization-fundamentals #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to get transactions qualifying at the interchange rate they are entitled to — and whoever does that returns money merchants are currently paying for data they had and did not send.

## The Problem
A transaction qualifies for a particular interchange rate depending on whether certain data was submitted, whether it settled within a window, whether the card was present, what type of card it was, and a dozen other published conditions. A merchant sending incomplete data or settling late pays a higher rate on every affected transaction. The schedules are public. The qualification is determinable. The statement shows a blended rate that conceals which transactions downgraded and why. Merchants pay the difference continuously and most do not know the mechanism exists.

## Why Nobody Has Built This
Processor pricing models frequently blend the underlying interchange into a single rate, which removes the merchant's visibility of the qualification entirely — the pricing structure hides the problem, and the processor's incentive under a blended model runs the wrong way. The schedules are genuinely complicated, which discourages engagement. Qualification failures are invisible without a transaction-level analysis nobody runs. And the loss is a small percentage on every transaction rather than a visible event.

## What to Build
Determine the qualification and fix the causes. Evaluate every transaction against the published conditions to establish what it could have qualified for, which is the core and is mechanical once the schedule is encoded. Attribute every downgrade to its specific cause — missing data, late settlement, card type, authorisation mismatch — which turns an unexplained rate into a fixable defect. Fix the causes at source in the integration, since most are data fields or a settlement timing the merchant controls and can change once. Quantify the recoverable amount per merchant, which is the number that gets the work prioritised and is currently unknown. Monitor qualification performance continuously, so a regression caused by an integration change is caught rather than paid indefinitely. Handle commercial card data levels specifically, since the additional data requirements are substantial and the rate difference is large. Report the true interchange under blended pricing, which is an honesty question about the processor's own commercial model and is a genuine differentiator. Support the merchant's own verification, since a merchant who can check is a merchant who trusts. Update as the schedules change, because they do and a static implementation decays. And report the qualification rate as a standing merchant metric, since it is directly actionable and is currently reported nowhere.

## Target Customer
Merchants paying downgraded interchange, processors differentiating on total cost rather than headline rate, and the interchange optimisation consultancies doing this manually.

## Impact If Built
Blended pricing removes the merchant's visibility of qualification and points the processor's incentive the wrong way. Evaluating every transaction against published conditions and attributing each downgrade to its cause turns an unexplained rate into a defect the merchant can fix once.
