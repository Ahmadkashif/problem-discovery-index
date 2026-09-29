# Buy: Fatigue Risk Management Pointed at Trauma

**Niche:** Presentation & Dosimetry
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Aviation and rail constrain rostering on accumulated cognitive load with regulator-accepted models, and the same structure — accumulate, threshold, enforce through scheduling — is exactly what trauma exposure needs.
**Tags:** #evaluation-metrics #confidence-intervals #survival-analysis #markov-decision-processes #compliance #worker-facing #workflow-orchestration
**Contested on:** Whether the intensity of each unavoidable exposure, and its accumulation across a shift and a career, is deliberately controlled or left to a full-fidelity default nobody chose.

## The Problem

There is an established way to manage a cumulative occupational hazard that cannot be eliminated: model the accumulation, set a threshold, and enforce it through the work schedule rather than through the worker's discretion. Aviation does this with fatigue. So do rail, long-haul trucking and increasingly healthcare rostering. The models are validated, the software is mature, and regulators accept the output as evidence of compliance.

The structural match to trauma exposure is close. Both hazards accumulate. Both are worsened by concentration and improved by recovery. Both are poorly self-assessed by the person experiencing them — a fatigued pilot and a distressed reviewer are similarly unreliable narrators of their own state. Both are best controlled by constraining assignment before the exposure rather than supporting the person after it.

Content moderation has none of it. It has counselling, which is the equivalent of treating pilot fatigue with a rest area and no duty-time limits.

## What Already Exists

Fatigue risk management systems: Fatigue Science, CASA- and FAA-accepted biomathematical models such as SAFTE-FAST and FAID, and the fatigue modules inside aviation crew-rostering platforms from Jeppesen, AIMS and Lufthansa Systems. These accumulate load across duty periods, score a roster against a threshold, and block or flag assignments that breach it.

Workforce management generally: NICE, Verint, Genesys and Alvaria schedule contact-centre labour at large scale against forecast volume and skill, and are already deployed at moderation vendors for exactly that purpose.

Occupational health: EHS platforms with cumulative dose tracking and medical surveillance; trauma-exposure screening instruments developed for emergency services.

## The Customization Gap

**The load model has no equivalent.** Fatigue models rest on decades of sleep science with validated parameters. Trauma exposure has no equivalent model, no accepted unit and no dose-response curve. This is the gap, and it is research rather than software — but the software structure around it transfers essentially unchanged, which is the point.

**Load arrives per item, not per duty period.** Fatigue accrues with time and circadian phase, which is smooth and predictable. Trauma exposure arrives in discrete, highly variable events whose severity is only known when the item is classified. The accumulation model has to be event-driven and updated in real time as work is assigned, which is a different computational shape from a roster scored the night before.

**Enforcement must be at assignment, not at rostering.** A fatigue system blocks a roster in advance. A trauma system has to intervene at the moment an item is about to be routed, which means integration with the review queue rather than with the scheduling system — and no fatigue product has ever needed a real-time assignment hook.

**Workforce management platforms optimise the wrong objective.** The contact-centre systems already installed at these vendors schedule for service level and occupancy. They have no concept of a hazard budget, and adding one inverts part of their optimisation — the system must sometimes decline to assign available work to an available person.

**Recovery is qualitatively different.** Fatigue recovers with sleep, which is well characterised. Psychological recovery from trauma exposure is far less understood, varies enormously between individuals, and may not fully occur at all — which means the model must be conservative in a way fatigue models need not be, and must treat career-cumulative exposure as a real quantity rather than something that resets.

**Regulatory acceptance is the destination.** Fatigue models are valuable largely because regulators accept them. Whoever builds the trauma equivalent should build it for that endpoint from the start, because a model a regulator will accept is what turns this from a cost into a requirement everyone must meet.

## Target Customer

Fatigue Science, or a crew-rostering vendor with a fatigue module, are the credible adapters — they own the accumulate-threshold-enforce structure and the regulatory-acceptance experience, which is the hard-won part.

The workforce management incumbents already deployed at these vendors are the alternative path: the integration with the queue exists, and what is missing is the hazard model.

Buyers are the moderation vendors, and then every screen-delivered trauma workforce: emergency dispatch, child protection, claims handling on catastrophic loss, and in-house platform trust and safety teams.

## Impact If Solved

The most successful template in occupational hazard management reaches a hazard currently managed with counselling. Enforcing limits through the schedule, rather than relying on the worker to recognise their own state, is the specific insight that made fatigue management work, and it transfers directly.

It puts the control at the right moment. Intervening when an item is about to be assigned is far more effective than any support offered after it has been seen.

And a regulator-acceptable model would restructure the market. Once exposure limits are enforceable and demonstrable, competing on price by tolerating more harm stops being available, which is the only thing that will change conditions across the whole industry rather than at one thoughtful vendor.
