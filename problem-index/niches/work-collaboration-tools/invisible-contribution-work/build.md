# The Contribution That Leaves No Artefact

**Niche:** [[niches/work-collaboration-tools/invisible-contribution-work/profile|Invisible Contribution Work]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The work that makes a team function — reviewing, answering, unblocking, mentoring, coordinating — is recorded in the collaboration tools and counted by nothing, so the people who do most of it appear to produce least.
**Tags:** #graph-theory #bert #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #worker-facing #compliance
**Contested on:** Every serious competitor that takes this seriously is fighting to make the work that produces no ticket — reviewing, unblocking, mentoring, responding, coordinating — visible in whatever the organisation uses to judge contribution, and whoever does it changes who gets promoted.

## The Problem
Two engineers. One ships a steady volume of features. The other ships less, and also reviews most of the team's changes thoroughly, answers the questions that would otherwise stall three people a day, handles the incidents nobody else understands, and has brought two new joiners to productivity. At promotion time the first has a portfolio of artefacts and the second has a set of assertions that a manager has to argue for from memory. The committee, doing its job with the evidence in front of it, promotes the first. Every trace of the second's contribution exists — review comments with timestamps and outcomes, threads where they resolved somebody's blocker, incident timelines, document histories — in the same systems that produced the first's artefact count.

## Why Nobody Has Built This
Artefact counting is trivially available and non-artefact work is not, so the measurement followed the data rather than the value, and over time the convenience became the definition. There is also a legitimate fear of what happens when this work is measured: anything counted becomes a target, and a review-count metric would produce performative reviewing exactly as commit counts produce padded commits. That is a real risk and it argues for a careful design rather than for leaving the work uncounted, since the current state is not neutral — it is a systematic undercount with a known demographic pattern.

## What to Build
Contribution evidence assembled per person from the traces, presented to them and to their manager rather than as a leaderboard. Review contribution measured by depth and outcome — comments that led to changes, problems caught before release — rather than by count, which is the distinction that prevents the metric being gamed. Unblocking measured by the question-and-answer structure of threads: who asked, who resolved it, and how quickly the asker proceeded afterwards, which is visible in the message graph. Mentoring inferred from sustained one-to-one interaction with newer colleagues and from their subsequent trajectory. Incident response from the incident record. Coordination from the handoff and dependency structure this industry's cross-functional niche describes. The output is a narrative with evidence attached — here is what this person did that produced no artefact, with the specific instances — which is what a promotion case actually needs and what is currently reconstructed from memory. It is delivered to the individual first, as their own evidence, which is both the fairest design and the one least likely to become a surveillance instrument.

## Target Customer
Engineering and operations leadership, performance and talent functions, and the individuals whose contribution is currently invisible — who are the constituency with the strongest interest and the least purchasing power.

## Impact If Built
The undercount is systematic, consequential for careers, and has a documented demographic skew, which makes it a fairness problem with a measurement cause. Assembling the evidence changes promotion outcomes directly, and designing it as personal evidence rather than a comparative metric is what determines whether it helps or becomes another thing to game.
