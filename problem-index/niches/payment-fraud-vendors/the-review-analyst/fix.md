# Graded on Half the Decisions

**Niche:** [[niches/payment-fraud-vendors/the-review-analyst/profile|The Review Analyst]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The analyst's score comes from chargebacks on what they approved, so declining everything is the safest way to look good.
**Tags:** #worker-facing #evaluation-metrics #quick-win #descriptive-statistics #confidence-intervals #hypothesis-testing #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to make forty seconds enough to decide correctly on exactly the cases the model could not — and whoever equips that decision changes the outcome of the transactions the product is worst at.

## The Problem
Analyst performance is measured by the chargeback rate on their approvals and by handle time. A decline produces no measurable consequence for the analyst, ever. The incentive is therefore unambiguous: when uncertain, decline. Analysts are not being careless — they are responding correctly to the measurement system, which grades one type of error and not the other, on the queue where uncertainty is by definition highest.

## Why It's Still Broken
Chargebacks are the only outcome that returns, so the metric was built from what exists — a performance system measures the observable half and then shapes behaviour toward it. Nobody wants to appear to encourage approving fraud. The merchant's lost revenue does not appear in the vendor's reporting. And the fix requires either outcome data on declines or a substitute, and neither was pursued.

## What a Fix Looks Like
Measure both directions, even imperfectly. Track approval rate alongside chargeback rate per analyst, which is the fix and immediately reveals the analysts who are declining their way to a clean score. Compare analysts on the same case mix, since raw rates confound difficulty with judgement and a matched comparison does not. Duplicate a sample of cases across analysts and measure agreement, as consistency is obtainable without any outcome data and is highly informative. Review a sample of declines with the merchant, because the merchant often knows the customer and this is the cheapest ground truth available. Use the randomised approval sample to evaluate declines properly where it exists, which connects this directly to the label problem. Show analysts the outcomes of their approvals and, where obtainable, of their declines, since the role currently receives feedback on half its work. Remove handle time as a primary metric on the hardest queue, because speed on ambiguous cases is not a virtue. Report the cost of declines at team level, so the invisible half becomes visible to management even before individual attribution. Recognise good judgement on hard cases rather than only absence of loss. And tell analysts how they are measured and why, since the current incentive is obvious to them and demoralising.

## Who Feels the Pain
Analysts steered toward declining; merchants losing customers to a metric; good customers turned away at the ambiguous margin; and vendors whose review function optimises one error.

## Impact If Fixed
A performance system measures the observable half and then shapes behaviour toward it, so declining became the safe choice. Approval rate, matched case mix and cross-analyst agreement measure the other direction without needing any new outcome data.
