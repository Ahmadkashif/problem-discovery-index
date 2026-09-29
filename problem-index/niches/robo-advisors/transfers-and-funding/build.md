# The Contribution That Stopped

**Niche:** [[niches/robo-advisors/transfers-and-funding/profile|Transfers & Funding]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A client whose recurring contribution stopped a year ago is the clearest attrition signal in the business and nothing in the product notices.
**Tags:** #survival-analysis #change-point-detection #gradient-boosting #evaluation-metrics #revenue-impact #automation #confidence-intervals #logistic-regression
**Contested on:** Every serious competitor in this niche is fighting to keep money arriving — through an account transfer that stalls and a contribution that quietly stops — and whoever detects and recovers both without a human takes the growth the funnel currently leaks.

## The Problem
Recurring contributions are the entire growth engine for most clients. They stop for many reasons: a job change, a new bank account, a temporary cash squeeze that was never resumed, a failed transfer nobody followed up, a loss of confidence after a drawdown. Each of those has a different remedy and the platform treats them identically, which is to say it does nothing. The balance stays, the fee continues, and eighteen months later the client closes the account having contributed nothing since.

## Why Nobody Has Built This
Funding was built as a payment integration, so a stopped contribution registers as an absence rather than as an event — and systems do not fire on things that fail to happen. Growth is measured in new accounts and net flows at the aggregate level, where individual cessation is invisible. Reactivation feels like marketing rather than service. And nobody separated the deliberate pause from the silent failure.

## What to Build
Treat cessation as an event with a cause. Detect a stopped contribution immediately rather than discovering it in an aggregate, which is the core and requires only that absence be modelled as a signal. Classify the likely cause — bank change, failed payment, deliberate pause, post-drawdown withdrawal of confidence, income change — since the remedy differs entirely and a generic reactivation email addresses none of them. Detect the failed payment path separately, because it is the most recoverable case and is frequently just an expired account detail. Predict cessation before it happens from the preceding behaviour, as the signals — reduced logins, a lowered amount, a skipped month — usually precede the stop. Reach out with the right remedy at the right time, since recovery rates fall steeply with elapsed time and the current delay is measured in months. Distinguish a client who cannot contribute from one who has chosen not to, because pressing the former is harmful and pressing the latter is the job. Model contribution resumption as the outcome and measure it, which is the metric the function needs. Connect cessation after a drawdown to the intervention work, since that is a behavioural case rather than an operational one. Make resuming trivially easy, as friction at the moment of willingness destroys most recoveries. And report contribution continuity as a headline metric, because it predicts revenue better than balance does.

## Target Customer
Operations and growth leadership, clients whose funding failed without their knowledge, and retention and payment vendors whose products serve subscription billing rather than investment funding.

## Impact If Built
Funding was built as a payment integration, so cessation registers as an absence and systems do not fire on absences. Modelling the stop as a classified event with a matched remedy turns the clearest attrition signal in the business into an action.
