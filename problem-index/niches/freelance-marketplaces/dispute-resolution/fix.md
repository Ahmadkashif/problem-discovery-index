# Fix: The Same Facts, Two Agents, Two Outcomes

**Niche:** [[niches/freelance-marketplaces/dispute-resolution/profile|Dispute Resolution]]
**Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Type:** Fix (Pain Point)
**One-liner:** Nobody at the platform knows whether two agents given the same dispute would decide it the same way, because it has never been measured.
**Tags:** #hypothesis-testing #descriptive-statistics #evaluation-metrics #confidence-intervals #cross-validation #workflow-orchestration #compliance #quick-win
**Contested on:** Whether the platform is willing to measure the consistency of decisions it makes about its users' money.

## The Problem

Dispute outcomes are decided by individual agents applying a policy document to a message thread. Different agents read the same facts differently, weigh the parties' statements differently, and have different implicit thresholds for how much delivered work justifies how much payment. Queue pressure, time of day and the order in which they read the statements all move outcomes.

None of this is controversial — it is what happens in any human adjudication function. What is remarkable is that no platform measures it. There is no inter-rater agreement statistic, no blind double-review sample, no audit of outcome distribution by agent. The quality of the function is entirely unobserved, which means it can be as bad as it likes indefinitely.

## Why It's Still Broken

Because measuring it creates a fact that has to be acted on. If blind double-review shows agents agree on 60% of disputes, the platform then knows that a large share of its payment decisions are arbitrary, and it knows that in a written, discoverable form. Not measuring is the safer choice for anyone whose job depends on the function looking fine.

Structurally, dispute resolution usually sits inside support, which is measured on time to resolution, ticket volume and customer satisfaction. None of those are decision-quality metrics, and satisfaction scores on disputes are dominated by whether the respondent won. There is no metric in the function that points at correctness, so nobody built one.

And there is no ground truth, which makes the problem feel unmeasurable. That is a mistake: agreement can be measured without truth, and agreement is the thing that matters most here, because a decision procedure that gives different answers to the same facts is unfair regardless of which answer is right.

## What a Fix Looks Like

Measure agreement. It requires no ground truth, no modelling and no new data.

Take a standing sample of disputes and route each to a second agent blind to the first's decision, with the outcome recorded but not applied. Compute agreement — on the binary of who prevailed and on the proportion of funds released. Report it monthly by dispute type, by disputed amount, by agent tenure. Run it as a continuous process rather than an audit, so it tracks drift.

Publish the outcome distribution internally. Release rate by agent, by category, by amount band, by whether the freelancer or the client initiated, by the tenure of each party. Agents whose distributions sit far from their peers' are either applying a different standard or handling a different mix, and the difference is worth knowing. This is a group-by over the dispute table.

Then act on where agreement is low. A dispute type with poor agreement does not need better agents; it needs a policy decision made once, at the top, and written into guidance — the platform has simply not decided what its answer is, and is delegating that decision to whoever picks up the ticket. Turning low-agreement categories into decided policy is the highest-value output of the whole exercise.

Build the calibration set as you go. Resolved disputes with their facts and outcomes, reviewed and agreed by a panel, become both the training material for new agents and the test set for any future tooling. Without it there is no way to know whether a change to the process helped.

And give the losing party the basis. Not a form letter — the specific finding: the contract scope said this, delivery showed that, the decision follows. The outcome is the same and the experience is entirely different, and it is the difference between a freelancer who accepts a loss and one who tells everyone the platform is arbitrary.

## Who Feels the Pain

Freelancers, for whom a disputed contract is often a month's income decided by an unknown person in an unknown way. Clients who lose disputes they believe were clear. Agents, who make consequential decisions with no feedback on whether they are making them well and no way to improve. And the platform, whose escrow promise is the foundation of the trust that makes the marketplace work, backed by a process it has never examined.

## Impact If Fixed

The platform finds out how consistent its adjudication is, which is uncomfortable exactly once. Low-agreement dispute types become policy questions answered deliberately rather than daily coin flips. Agents get feedback and a precedent set. And the escrow promise acquires an evidentiary basis — which matters most at the moment someone outside the company asks for one.
