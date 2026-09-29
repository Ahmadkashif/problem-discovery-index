# The False Positive Nobody Counts

**Niche:** [[niches/online-marketplaces/the-seller-appeals-agent/profile|The Seller Appeals Agent]]
**Industry:** [[industries/online-marketplaces|Online Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** Detection systems are tuned on how much bad activity they catch, and the sellers wrongly suspended are absorbed by support as tickets rather than reported as errors.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #logistic-regression #compliance #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to give the person handling an appeal the reason for the suspension and the authority to act on it — and whoever does that takes the account, because this conversation is where a marketplace's relationship with its sellers is decided.

## The Problem
A detection model is tuned to catch fraud and reports its recall. Its false positives arrive as support tickets, are handled individually, and a proportion are reinstated. Nobody aggregates the reinstatements into a false positive rate per rule, so the risk team does not know which of their rules generate the most wrongful suspensions, and the support cost and the seller churn are booked to support and to churn rather than to detection. A rule that wrongly suspends one legitimate seller in twenty and one in two hundred look identical from where the tuning happens.

## Why It's Still Broken
Recall is measurable directly and false positives are only observable through appeals, which means the rate is systematically understated by however many wrongly-suspended sellers simply leave. The teams are separate and the data is not joined. The support cost sits in a different budget from the detection benefit. And a reinstatement is recorded as a resolved ticket rather than as a model error.

## What a Fix Looks Like
Count the errors and route them back. Join appeal outcomes to the rule that triggered each suspension and report a false positive rate per rule, which is a straightforward join and immediately ranks the rules by the harm they do — this is the fix and it takes a data engineer a week. Estimate the unappealed false positives, since sellers who leave without appealing are the silent majority of the harm and a reinstatement rate among appeals understates it badly; sampling suspended-and-departed accounts for review is the way to size it. Attribute the support cost and the lost supply to detection rather than to support, so the tuning decision faces its own costs. Tune thresholds against a stated cost of a wrongful suspension rather than to a recall target, which is the substantive change and requires the business to state what a wrongly-suspended seller is worth. Escalate before suspending where the case is marginal and the seller has history, since a warning or a restriction is frequently sufficient and a suspension is not reversible in its effect on trust even when it is reversed. Report reinstatement rates to the risk team weekly, so the feedback is continuous rather than annual. Use appeal outcomes as training labels, which is free supervision on exactly the cases the model gets wrong. And report the seller retention rate after a reinstated suspension, because it is much lower than after no suspension and that gap is the true cost.

## Who Feels the Pain
Sellers wrongly cut off from their income; support agents absorbing anger caused by a threshold decision; and operators whose supply churn has a cause nobody has attributed.

## Impact If Fixed
Joining appeal outcomes to the triggering rule is a week of work and ranks rules by the harm they do. Sizing the unappealed false positives is what reveals the real cost, since the sellers who leave without appealing are the silent majority of it.
