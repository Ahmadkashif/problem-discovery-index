# Build: A Queue That Resolves Itself

**Niche:** Employee Report Triage
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Resolve the mechanical majority automatically — duplicates, simulations, already-blocked and known-legitimate mail — acknowledge everyone immediately, and route the remainder to a human.
**Tags:** #bert #gradient-boosting #word-embeddings #evaluation-metrics #confidence-intervals #automation #workflow-orchestration #worker-facing
**Contested on:** Whether the reporting stream the programme creates is handled as a detection source or dumped on a security team that never asked for it.

## The Problem

Four hundred reports arrive in a week. An analyst works them.

The composition is predictable. A large share are duplicates — dozens of people reporting the same campaign, each assessed separately. A substantial number are the organisation's own simulations, reported by employees doing precisely what the programme asked. Many are messages the gateway already blocked, forwarded by people who saw the quarantine notice. Many more are ordinary marketing mail, newsletters and notifications the recipient did not recognise. And a small number are real, novel, and got past the filters.

The analyst reads all of them to find the last category. The work is mostly mechanical and the consequence of missing the real one is serious, which is the same structure as every high-volume triage problem in security.

Meanwhile the reporter hears nothing. Their message goes into a queue and no acknowledgement returns, or one returns days later. So the behavioural loop the entire awareness programme exists to create is closed badly or not at all.

Every one of the mechanical categories is automatically identifiable. Simulation reports are the organisation's own campaign. Gateway status is a lookup. Duplicates cluster trivially. Known senders are a list.

## Why Nobody Has Built This

**The queue arrived without a plan.** The awareness programme created the reporting behaviour and the reports landed on a security team who had no allocation for them.

**Ownership is split.** The awareness function creates the stream, security operations absorbs it, and neither owns the triage experience.

**Automated dismissal is feared.** Auto-resolving reports risks closing the real one, which pushes toward reading everything.

**Acknowledgement is not seen as part of security's job.** Operations is measured on detection and response, not on the reporter's experience, so the behavioural reinforcement is nobody's objective.

**The stream's value is unmeasured.** Nobody counts how many real threats came from employee reports versus from automated detection, so it is experienced as a cost.

**Simulation reports are treated as a nuisance.** The organisation's own campaigns clogging its own queue is an obvious problem with an obvious fix that nobody has implemented.

## What to Build

**Filter out the organisation's own simulations automatically.** These should never reach an analyst. The platform knows which messages it sent, and the reporter should receive an immediate, positive acknowledgement confirming they did the right thing.

**Check gateway status first.** A message already blocked or quarantined resolves immediately with a reassuring response to the reporter.

**Cluster duplicates into campaigns.** Dozens of reports of the same message become one item with a recipient count, which is both far less work and far more informative — a campaign hitting forty people is a different signal from one report.

**Classify against known-legitimate senders.** A maintained list of the organisation's own systems, vendors and regular correspondents resolves a substantial share.

**Acknowledge everyone immediately, always.** Within seconds, with a genuine response rather than a receipt. This is the behavioural reinforcement the entire awareness programme depends on and it is the cheapest thing in this niche.

**Tell them the outcome.** When a report turns out to be a real threat, tell the reporter it mattered. This is the single most effective thing an organisation can do to sustain reporting behaviour.

**Route the remainder with context.** The genuinely uncertain reports reach an analyst with the sender reputation, the campaign clustering, the gateway verdict and the recipient list already attached.

**Measure the stream's yield.** How many real threats arrived through employee reports and were not caught by automation. This converts the queue from a cost into a measured capability and is the argument for resourcing it properly.

## Target Customer

Security operations leadership, for whom the queue is an unfunded burden and automation of the mechanical majority is a straightforward capacity win.

Awareness programme owners, whose programme's behavioural goal depends entirely on what happens to a report after it is sent.

Vendors on both sides — awareness platforms that create the stream and email security platforms that could resolve most of it — neither of which has taken responsibility for the queue.

## Impact If Built

The majority of the queue resolves without a human, which turns an unfunded burden into a manageable detection source.

Immediate acknowledgement and outcome notification are close to free and are the mechanism by which reporting behaviour persists — without them the awareness programme is training a behaviour it then extinguishes.

And measuring the stream's yield would establish that employee reporting catches things automation does not, which is the argument for treating it as a capability rather than as a cost.
