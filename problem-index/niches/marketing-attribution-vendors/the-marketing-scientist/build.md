# Knowing the Estimate Is Weaker Than the Chart

**Niche:** [[niches/marketing-attribution-vendors/the-marketing-scientist/profile|The Marketing Scientist]]
**Industry:** [[industries/marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A trained statistician spends their quarter explaining to channel owners why the model reduced their contribution, knowing the estimate is less certain than the chart implies and being unable to say so.
**Tags:** #worker-facing #confidence-intervals #bayesian-inference #evaluation-metrics #hypothesis-testing #monte-carlo-methods #descriptive-statistics #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to let the scientist communicate the uncertainty they actually have — and whoever makes an honest interval presentable changes what this profession is able to say.

## The Problem
The scientist knows the model could not separate two channels, that the contribution for one of them is largely the prior, and that a reasonable alternative specification would move it by half. The deliverable is a bar chart. The channel owner whose bar shrank is in the meeting and will attack the number. If the scientist says the estimate is uncertain, the channel owner uses that to dismiss it entirely; if they say it confidently, they are overstating what they know. There is no available register between confident and useless, and the person with the best understanding of the estimate is the one most constrained in describing it.

## Why Nobody Has Built This
Deliverables are charts because charts are what organisations act on, and a chart has no vocabulary for doubt — the format constrains the communication and nobody has designed a better one. Vendors compete on confidence in sales processes and cannot then hedge in delivery. Channel owners' incentives make any admitted uncertainty a weapon. And the scientist has no standing to change the format.

## What to Build
Build a format that carries uncertainty into a decision. Present decision-relevant ranges rather than point estimates, framed as what the evidence supports doing rather than as what the number is, which is the core — an interval that answers a decision is actionable where an interval around a bar is an invitation to argue. Show specification and prior sensitivity as part of the standard deliverable, connecting to the mix modelling work, so the range has a stated source rather than appearing as vendor hedging. Separate the confident findings from the weakly identified ones explicitly, since a report where everything is equally uncertain is unusable and one where the difference is visible is not. Give the scientist a defensible answer to the channel owner's challenge, which is prepared evidence rather than improvised composure. Record caveats formally with the deliverable, so what was said is retrievable when a decision is reviewed. Pre-empt the predictable objections with analysis, since channel owners raise the same five arguments and they are answerable in advance. Train the client organisation to read uncertainty, which is a long project and is the only durable fix. Support the scientist in the meeting with material rather than leaving them to hold the room. Report what the model cannot answer as a standard section, which turns an admission into a professional disclosure. And measure how often stated caveats turn out to have mattered, since that record is what builds the scientist's credibility over time.

## Target Customer
Measurement vendor science and delivery teams, the scientists themselves, and client measurement functions receiving estimates they cannot calibrate.

## Impact If Built
The format has no vocabulary for doubt, so the person who understands the estimate best is the most constrained in describing it. A decision-relevant range with its sensitivity shown is actionable where an interval around a bar is an invitation to argue.
