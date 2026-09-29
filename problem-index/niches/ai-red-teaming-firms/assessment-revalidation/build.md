# One Model Update Invalidates Everything

**Niche:** [[niches/ai-red-teaming-firms/assessment-revalidation/profile|Assessment Revalidation]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Automated probing tools make re-testing cheap in principle, and in practice a client's model update invalidates an entire assessment with no established way to revalidate short of another engagement.
**Tags:** #automation #evaluation-metrics #workflow-orchestration #change-point-detection #confidence-intervals #compliance #hypothesis-testing #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to re-establish an assessment's conclusions after the system changes, at a fraction of the original cost — and whoever does that takes the account, because the alternative is a report that expires on the client's next model upgrade.

## The Problem
A client completes a four-week assessment in March, implements the mitigations, and receives a clean follow-up. In June their provider deprecates the model version and they move to the next one. The March assessment is now about a system that no longer exists. The findings may or may not reproduce, the mitigations may or may not still work, and new failure modes may have appeared. Their options are to commission another engagement at full cost, or to keep the March report in the compliance file and hope. Almost everyone chooses the second, and the industry's output is therefore a set of documents describing systems that have moved on.

## Why Nobody Has Built This
Engagement revenue is the business model and cheap revalidation cannibalises it, which is a real tension nobody has faced. Probes developed during an engagement are frequently exploratory and undocumented, existing as a researcher's notes rather than as executable artefacts. Nobody tells the firm when a client's model changes. And the client's compliance need is satisfied by a dated report, which removes the pressure to revalidate.

## What to Build
Make the assessment re-runnable. Record every probe executed during an engagement in executable form with its observed success rate, which is a working-practice change rather than a technical one and is the precondition for everything — without it revalidation is impossible and with it it is nearly free. Re-run the suite on demand and report which findings reproduce, which no longer do, and which new ones appear, at a fraction of an engagement's cost. Watch for client model changes with a behavioural probe, so revalidation is triggered by the event rather than by the calendar. Distinguish version-specific findings from structural ones, since a finding arising from the application's architecture will survive a model change and one arising from a model's particular behaviour may not — and telling the client which is which is immediately useful. Verify mitigations specifically, since a mitigation tuned against one model's behaviour is the most likely thing to silently stop working. Price revalidation as a subscription rather than as an engagement, which resolves the cannibalisation tension by converting a one-off sale into a recurring one. Report the revalidation result as a dated supplement to the original, so the compliance artefact stays current. And feed the retained probes into the technique catalogue, so engagement work compounds.

## Target Customer
Every client on a model upgrade path, the compliance functions holding dated reports, and the firms whose output currently has an undefined shelf life.

## Impact If Built
Recording probes in executable form is a working-practice change that makes revalidation nearly free where it is currently impossible. Distinguishing version-specific from structural findings tells a client immediately which conclusions survived their upgrade.
