# Revenue Today, Unsubscribe Over a Year

**Niche:** [[niches/email-sms-marketing-platforms/message-fatigue-and-long-run-cost/profile|Message Fatigue & Long-Run Cost]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every platform ships send-time optimisation trained on opens, and none of them models the thing that actually matters, which is what an extra message costs in the recipient's future willingness to hear from you.
**Tags:** #survival-analysis #causal-inference #bayesian-inference #confidence-intervals #evaluation-metrics #revenue-impact #markov-decision-processes #time-series-forecasting
**Contested on:** Every serious competitor in this niche is fighting to price what an extra message costs in the recipient's future willingness to hear from a brand — and whoever measures that changes how much the whole channel sends.

## The Problem
A brand adds a fourth weekly message. Revenue rises immediately and is reported immediately. Over the following year, some recipients unsubscribe, more stop opening, complaint rates drift up, and placement degrades as providers observe declining engagement. Every one of those effects is delayed, distributed and confounded, and none appears in the campaign report that showed the fourth message working. The brand adds a fifth. The platform, paid by volume, reports the revenue. The cost is real and is measurable in this system — uniquely, because the same database holds the message, the recipient, the engagement and the order — and nobody has been asked to measure it.

## Why Nobody Has Built This
The platform's revenue rises with volume, which means the party best positioned to measure the cost of volume is the party least motivated to — the alignment problem is total and explains the absence entirely. The effect is long-run and confounded, so measuring it properly requires experiments held for months. Brands see immediate revenue and treat unsubscribes as a small percentage. And no single campaign is responsible for a gradual decline.

## What to Build
Price the cost of a send. Model each recipient's responsiveness as a state that sending depletes and time restores, which is the conceptual core and turns an unmodelled externality into a quantity — the data to estimate it is present in every one of these platforms. Measure the long-run effect with holdout cohorts held for months at reduced frequency, since only a long-horizon experiment can see this and the platform can run it across its whole customer base at negligible cost. Charge the cost into the send decision, so the question becomes whether a message's expected revenue exceeds its expected damage rather than whether it produces revenue at all. Model unsubscribe, disengagement and complaint as one continuum, since they are stages of the same process and treating unsubscribe as the only cost misses most of it. Include the deliverability consequence, connecting to the placement work, because declining engagement degrades placement for everyone on the list including the people who wanted the mail. Estimate the dose-response curve per brand and segment, as tolerance varies enormously and one frequency policy fits nobody. Optimise the sequence rather than each message, which is the journey niche's framing and is where the real gains are. Give brands a frequency recommendation with the trade-off shown, which is the deliverable. Report lifetime value effects alongside campaign revenue, so the two sides of the ledger appear together. And publish the finding, since a platform that demonstrates its customers make more money sending less has an argument no volume-priced competitor can answer.

## Target Customer
Messaging platforms willing to price against their own volume incentive, brand leadership, and the lifecycle teams choosing frequency without evidence.

## Impact If Built
The party best positioned to measure the cost of volume is the one paid by volume, which explains the absence completely. Modelling responsiveness as a depletable state turns an unmodelled externality into a quantity the closed loop can actually estimate.
