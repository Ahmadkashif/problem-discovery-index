# The Email Everyone Gets

**Niche:** [[niches/robo-advisors/drawdown-intervention/profile|Drawdown Intervention]]
**Industry:** [[industries/robo-advisors|Robo-Advisors]]
**Type:** Fix (Pain Point)
**One-liner:** The same market commentary goes to the client who has not logged in for a year and the client who has checked their balance eleven times today.
**Tags:** #quick-win #gradient-boosting #evaluation-metrics #automation #descriptive-statistics #workflow-orchestration #confidence-intervals #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to find out what actually stops a client selling at the bottom — and whoever has run the experiments owns causal evidence nobody else in the industry has.

## The Problem
Markets fall and the platform sends one message to everybody. The client who is calm and unaware gets told there has been a significant decline. The client refreshing their balance all morning gets the same general reassurance as everyone else. The client who already sold gets a message about staying the course. Nothing about the send is conditioned on anything the platform knows, which is a great deal.

## Why It's Still Broken
The market commentary is a communications artefact produced by one team on a deadline, so it is naturally uniform — a single approved message is the fastest thing to get out and the easiest to supervise. Segmenting requires the behavioural signal to reach the messaging system. Supervision review is simpler for one message than for ten. And nobody measures what the send does.

## What a Fix Looks Like
Condition the send on what the platform already knows. Segment by observed behaviour — recent login intensity, whether they have already sold, tenure, drawdown depth relative to their own history — which is the fix and uses signals the platform logs continuously. Suppress the send to clients showing no distress, since informing a calm client of a decline is the one outcome nobody wants and it is the current default. Escalate to a call for the highest-risk clients rather than sending them the same email, because the expensive intervention should go where it might matter. Say something different to a client who has already sold, as the standard message is actively wrong for them. Pre-approve message variants in supervision so segmentation is not blocked at the last moment, which is the practical obstacle and is solvable in advance. Measure what happens after the send — sales, logins, funding — since that is a straightforward observation nobody records. Hold out a small group to establish a baseline, which is the smallest possible step toward actually knowing. Write the messages before the event, because the copy produced under deadline in a falling market is the worst version available. Time the send deliberately, as arriving during the worst hour of the day is a choice being made by accident. And record what was sent to whom, so the next event can learn from this one.

## Who Feels the Pain
Clients told about a decline they had not noticed; at-risk clients receiving generic reassurance; service teams fielding calls triggered by the email; and platforms with no idea what their most consequential communication does.

## Impact If Fixed
A single approved message is the fastest to ship and the easiest to supervise, so uniformity was never a decision. Segmenting on behaviour the platform already logs, with variants pre-approved, removes the worst case and creates the first measurement.
