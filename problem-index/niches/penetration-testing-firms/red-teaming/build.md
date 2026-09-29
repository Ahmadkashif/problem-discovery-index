# Build: The Instrumented Exercise

**Niche:** Red Teaming & Adversary Simulation
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An exercise record that logs every technique attempted with its timestamp and outcome, joined to what the defenders' telemetry saw, so the deliverable is a detection coverage map rather than a story.
**Tags:** #graph-theory #evaluation-metrics #confidence-intervals #change-point-detection #hypothesis-testing #markov-decision-processes #automation #data-integration
**Contested on:** Whether the exercise reflects how a real adversary would behave against this organisation, or how this particular red team habitually operates.

## The Problem

A red team engagement ends with a narrative. Initial access through a phishing campaign, credential harvesting, lateral movement through a service account, privilege escalation, objective achieved on day nine. The defenders saw some of it. The report describes the path and lists recommendations.

What the client wanted to know was the shape of their detection coverage, and the narrative answers that only for the single path the red team happened to take. Techniques the operators tried and abandoned because they were noisy do not appear. Techniques they never tried — because this team does not use them, or did not need to — are indistinguishable in the report from techniques that were tried and defeated. The client learns that one route worked and cannot tell whether the other forty would have.

The detection side is worse. Whether an activity generated telemetry, whether the telemetry triggered a rule, whether the rule fired an alert, and whether anyone actioned it are four different failures with four different fixes. Reconstructing which occurred, weeks later, from the defenders' recollection and a partial log review, is approximate at best — and it is the single most valuable output of the exercise.

Meanwhile the red team's operational log — every command, every timestamp, every implant check-in — exists in full and is used for nothing beyond writing the story.

## Why Nobody Has Built This

**Instrumentation feels contrary to the exercise.** A red team is meant to behave like an adversary, and adversaries do not fill in a technique log. There is a real cultural resistance to anything that makes the operation feel like a checklist rather than a covert engagement.

**Logging attempts exposes the team's own methods and failures.** A record showing which techniques were attempted and failed is a record of what this team is not good at, which is commercially sensitive and professionally uncomfortable.

**The denominator problem again.** Reporting which techniques were never attempted requires a defined universe of techniques, and while ATT&CK provides one, a red team that reports covering eleven per cent of the matrix has produced a number that looks bad and is arguably meaningless — coverage of the matrix is not the same as realistic adversary coverage.

**Detection joining requires the defenders' telemetry.** Correlating red team actions against the client's SIEM requires access and effort from the blue team, which turns a covert exercise into a collaborative one — which is what purple teaming is, and why purple teaming produces better measurement and sells less well.

**The narrative is what the buyer wants.** A compelling story of how the adversary reached the crown jewels is what gets presented to a board and what justifies the budget. A coverage matrix is less persuasive in that room, even though it is more useful to the security team.

## What to Build

**Capture attempts automatically from the operator's own tooling.** Command and control framework logs, operator terminal history and tooling output, parsed into a technique timeline without the operator recording anything. This is the adoption constraint: any solution requiring the red team to maintain a parallel log will be abandoned in the first engagement.

**Classify every action to a technique taxonomy, including the failures.** ATT&CK or equivalent, applied to attempts rather than only to successes. The three-way distinction — succeeded, attempted and defeated, never attempted — is the output the category lacks, and the middle category is the one that most changes what a client learns.

**Join to the defenders' telemetry at four levels.** For each attempted technique: did it generate telemetry, did the telemetry match a detection rule, did the rule alert, did anyone action the alert. Four separate outcomes, each with a different remedy — instrumentation gap, rule gap, tuning gap, process gap. This is the diagnostic clients most need and almost never receive.

**Pick the adversary from intelligence, not from habit.** Select the technique set from threat intelligence about actors that actually target this sector and this organisation's profile, and state the selection explicitly in the plan. This turns "we simulated an advanced adversary" into "we simulated the behaviours reported for the actors most likely to target you", which is both more honest and more defensible.

**Report coverage against the selected adversary profile, not the whole matrix.** The realistic denominator is the technique set the chosen adversary actually uses, not every technique ever catalogued. Coverage against that is a meaningful number; coverage against the full matrix is not.

**Make it comparable across exercises.** The same instrumentation next year produces a detection coverage trend, which is the only way a client can tell whether their security investment did anything. Nothing in the category currently supports this and it is the strongest commercial argument for the whole approach.

## Target Customer

Red team practices at firms with a detection engineering-oriented client base, where the buyer already wants coverage rather than a story.

Detection engineering and security operations leadership are the pull side and the better advocate — they are the people who need the four-level diagnostic and who currently receive a narrative.

Clients running annual exercises are the natural early adopters, because the comparability argument only pays from the second exercise onward.

## Impact If Built

The exercise produces a measurement rather than an anecdote. A client learns the shape of their detection coverage instead of the shape of one successful path.

The four-level detection diagnostic is the highest-value single output. Distinguishing a missing log source from an untuned rule from an ignored alert directs remediation precisely, and today those are collapsed into "we did not detect it".

And a comparable measurement across years is what would finally let a security team demonstrate that their detection investment improved something — which is the question every CISO is asked and none can currently answer.
