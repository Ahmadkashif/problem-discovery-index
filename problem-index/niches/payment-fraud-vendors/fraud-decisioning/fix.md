# Accuracy on a Population We Chose

**Niche:** [[niches/payment-fraud-vendors/fraud-decisioning/profile|Fraud Decisioning]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The quarterly report shows a fraud rate and an approval rate and cannot say anything about the transactions that were turned away.
**Tags:** #evaluation-metrics #descriptive-statistics #quick-win #confidence-intervals #hypothesis-testing #revenue-impact #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to approve the good transaction and decline the bad one — and the contest splits cleanly enough that it is not terminal.

## The Problem
Merchants receive reporting on fraud rate, approval rate, review volume and chargebacks. Every one of those describes approved transactions. The declines are a count. Whether those declines were good customers, whether they came back, what they were worth, and whether the rate is reasonable for this merchant's business are all absent, and merchants make renewal decisions on a scorecard that omits the larger loss.

## Why It's Still Broken
The metric set was built from the data that returns, so it measures approvals because approvals are what produce outcomes — a reporting suite naturally describes whatever is observable. Merchants contract on chargeback rates, which reinforces the omission. Reporting a false decline estimate invites a question the vendor cannot answer. And no competitor reports it either, so nobody is embarrassed.

## What a Fix Looks Like
Report the decline side with what is already knowable. Show decline volume and value by segment and reason, which is the fix and is descriptive reporting on data already held. Track whether declined customers returned and transacted successfully later, since that is a directly observable and highly informative proxy for a false decline. Report repeat customers who were declined, because a customer with a good history who is turned away is the clearest error available. Show the decline rate by merchant segment against a peer benchmark, which the vendor can produce and the merchant cannot. Flag the rules and score bands producing the most declines, so the merchant can see where their revenue goes. Report the value of declined transactions, as counting them without valuing them understates the loss dramatically. Separate fraud declines from other declines, since merchants conflate them and the remedies differ. Estimate false declines with stated uncertainty rather than staying silent, because an honest range beats an omission. Ask merchants what they want to know, since they have been asking about lost revenue for years. And commit to a measurement programme, as descriptive reporting is a start and the experiment is the answer.

## Who Feels the Pain
Merchants losing revenue they cannot see; good customers turned away without explanation; vendors competing on an unverifiable number; and a category whose dominant error is unmeasured.

## Impact If Fixed
The metric set describes approvals because approvals are what produce outcomes, so a reporting suite naturally omitted the larger loss. Decline volume, value, and the return behaviour of declined customers are all observable today.
