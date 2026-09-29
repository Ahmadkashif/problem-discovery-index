# Build: Content With Evidence Behind It

**Niche:** Training Content & Delivery
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Content tested against behaviour rather than completion — spaced, role-specific, delivered at the moment of risk, with the modules that do not change anything retired.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #causal-inference #bayesian-inference #transfer-learning #worker-facing #automation
**Contested on:** Whether the training changes what people do, or produces a completion record.

## The Problem

A module is assigned, watched and completed. A quiz is passed. The record is updated. Nobody knows whether anything changed.

The measurement problem is not hard in principle. These platforms sit alongside a simulation programme that produces behavioural observations continuously, and alongside an organisation that records real reporting, real incidents and real policy compliance. Whether a module changed subsequent behaviour is testable — assign it to some people and not others, or vary the timing, and compare.

Nobody runs the experiment. Content is produced, refreshed for freshness, and assigned. Module effectiveness is inferred from engagement metrics — completion, time spent, quiz scores — which measure whether someone sat through it.

The design choices are similarly untested. Annual delivery is set by compliance requirements and is close to the worst possible schedule for retention, which is well understood. Uniform content ignores that risk exposure varies enormously by role. And the moment of delivery is an assignment email rather than the moment when the behaviour is relevant, which is where behaviour change research consistently finds the effect.

## Why Nobody Has Built This

**Completion is the contracted deliverable.** Compliance requires evidence that training was delivered, so the product optimises for a defensible completion record.

**Testing content might show it does not work.** A vendor running proper experiments on its own library risks discovering that several modules change nothing, which is valuable and commercially unattractive.

**Experimentation on employees needs governance.** Assigning content to some and not others is an experiment on the workforce, which requires a framework the category does not have — the same gap as in [[niches/security-awareness-training/simulation-harm/profile|🎯 Simulation Harm & Consent]].

**The outcome measure is contested.** Simulation performance is available and is itself a questionable measure, and real-world behaviour is harder to observe. Choosing the endpoint is genuinely difficult.

**Production quality is what sells.** Buyers evaluate content by watching it, so investment goes into production values rather than into efficacy.

**Annual cadence is regulatory.** Compliance frameworks specify annual training, so the schedule is set by an external requirement that has nothing to do with learning.

## What to Build

**Test modules against behaviour, properly.** Randomised assignment with a behavioural endpoint — subsequent simulation performance at calibrated difficulty, reporting rate, or an observable policy behaviour. This is straightforward experimental design and it is the thing nobody does.

**Retire what does not work.** A library where modules have measured effects, and those with none are removed. This is the output that would distinguish a serious vendor and the reason none has done it.

**Space the delivery.** Short, repeated exposure beats an annual block by a wide margin, which is one of the better-established findings in learning research and is entirely incompatible with the compliance schedule. Delivering both — a compliance completion and a spaced programme — is achievable.

**Deliver at the moment of risk.** A short prompt when someone is about to do the risky thing — sending data externally, approving a payment change, entering credentials on an unfamiliar domain — is where behaviour change research finds the effect. This requires integration with the systems where the behaviour happens and is where the category is weakest.

**Match content to actual exposure.** A finance team receiving payment redirection attempts needs different content from a warehouse team, and role-based targeting is covered in its own niche for a reason.

**Measure durability.** Test at three and six months rather than immediately after viewing. Immediate quiz scores measure recall, not retention, and the difference is the entire question.

**Publish the efficacy data.** A vendor publishing which of its modules change behaviour, including the ones that do not, would establish a standard the rest would have to answer.

## Target Customer

Security leadership at organisations that have run programmes for years and suspect the annual module is theatre — which is a large and quietly frustrated population.

Vendors willing to compete on efficacy, for whom tested content is a genuine claim and the first in the category.

Insurers and auditors, who accept training completion as evidence of a control and would use an efficacy measure if one existed.

## Impact If Built

Content acquires an evidence base, which an entire category currently lacks while selling behaviour change.

Retiring modules that demonstrably change nothing would shrink the annual burden on every employee and improve the programme simultaneously.

And delivering at the moment of risk rather than on an annual schedule is where the behaviour change research points, and it is the intervention the category is furthest from and would benefit from most.
