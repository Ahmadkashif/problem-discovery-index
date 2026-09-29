# The Caller Says the Car Will Not Start and That Is All Anyone Knows

**Niche:** [[niches/towing-companies/roadside-assistance-network-analytics/profile|Roadside Assistance Network Analytics]]
**Industry:** [[industries/towing-companies|Towing Companies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The dispatch decision turns on what is wrong with the vehicle, the only source is a distressed person describing it, and the wrong equipment arriving means starting again.
**Tags:** #large-language-models #transformers #gradient-boosting #evaluation-metrics #workflow-orchestration

## The Problem
Every roadside event begins with a triage: what is wrong, and therefore what needs to be sent. A jump start, a tyre change, a lockout, a fuel delivery and a tow each require different equipment, and a heavy or low-clearance or all-wheel-drive vehicle requires different equipment again. Sending the wrong thing means a second dispatch, a doubled cost, and a customer waiting twice.

The information available is a person by the roadside, often anxious, often in the dark, describing a symptom in ordinary language. "It won't start" covers a dead battery, a failed starter, an immobiliser fault, an empty tank and a car in the wrong gear. "There's a noise" covers almost anything.

Triage is done by agents working through scripted decision trees, and the quality of the outcome depends heavily on which agent took the call. Networks know their re-dispatch rate and treat it as an operations cost.

What is not used is the corpus. Every past event pairs the caller's description and the vehicle's details with what the provider actually found and what equipment resolved it. That is millions of labelled examples of symptom-to-diagnosis, in the caller's own words, with the answer attached — and the triage runs on a decision tree written by hand.

## What Already Exists
Language models handle short conversational descriptions well and are already deployed in call centres for intent classification and summarisation. Contact centre platforms ship with intent models. Vehicle data services provide specifications from a registration or identification number.

None of it produces the required output. Generic intent classification routes a call to a queue; this needs a predicted service type and equipment requirement with a confidence, because the cost of being wrong is a truck. Off-the-shelf models are trained on generic customer service language, not on roadside symptom description, and they have no notion of the vehicle-specific constraints — clearance, drivetrain, weight, wheel lock — that determine what can actually perform the job.

## The Customization Gap
**The label is what the provider found, not what the caller said.** Training on the caller's description against the provider's completion record is what makes this work, and only the network holds both sides.

**Vehicle attributes are half the answer.** Drivetrain, weight, clearance and key type change the equipment requirement independent of the symptom. Joining decoded vehicle specification to the symptom model is a domain integration no generic tool performs.

**The output is an equipment requirement with a cost-weighted confidence.** Under-specifying causes a re-dispatch; over-specifying sends an expensive truck to a flat tyre. The threshold is an economic decision that varies by market and provider availability, and it has to be exposed, not buried.

**It has to work inside a live call.** The agent is talking to a distressed person. The model's job is to suggest the next question that most reduces uncertainty and then to propose a dispatch — a sequential decision, not a one-shot classification.

**Connected vehicle data should be an input where it exists.** Fault codes from the vehicle itself are the ground truth the caller is approximating, and where a manufacturer relationship supplies them, the model should use them and learn how far the caller's description diverges from them.

**Failures are observable and must feed back.** Every re-dispatch is a labelled error with the reason attached, arriving within hours. This is the rare deployment where the correction signal is immediate and free.

## Target Customer
VP of Operations or Chief Data Officer at a roadside assistance network, owning both the contact centre and the dispatch economics.

## Impact If Solved
Re-dispatch is one of the largest controllable costs in roadside assistance and the single biggest driver of the delays customers complain about. Accurate triage from the caller's own words — trained on what providers actually found — reduces both at once, and the corrective signal arrives within hours of every mistake.
