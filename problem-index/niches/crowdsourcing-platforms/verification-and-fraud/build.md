# Build: Calibrated Fraud Detection With a Measured False Positive Rate

**Niche:** [[niches/crowdsourcing-platforms/verification-and-fraud/profile|Worker Verification & Fraud Control]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Detect automated and duplicate submissions with an error rate that is actually measured, and with graduated responses instead of exclusion.
**Tags:** #graph-theory #gradient-boosting #evaluation-metrics #confidence-intervals #hypothesis-testing #large-language-models #compliance #automation
**Contested on:** Whether the false positive rate can be measured on a population that never appeals.

## The Problem

Fraud controls here run on signals that honest workers share with fraudulent ones. A shared household device looks like a duplicate account. A university network looks like a bot farm. A VPN looks like location misrepresentation. Fast completion looks like automation. Terse free text looks like generated text, and looks that way most strongly for workers writing in a second language.

Platforms tune these controls against requester complaints, which arrive when fraud gets through, and never against false positives, which arrive as nothing at all — an excluded worker with no appeal route mostly disappears. So the controls drift steadily toward aggression, and the population they wrongly exclude is disproportionately the workers in the countries where this income matters most.

## Why Nobody Has Built This

The measurement is genuinely hard by construction. Establishing that an excluded worker was honest requires evidence about someone you have already turned away, which nobody gathers.

The incentives compound it. A requester whose study is polluted complains loudly; a worker excluded in error does not complain to anyone with authority. Tuning against the loud signal is what any operation will do absent a deliberate decision to do otherwise.

And generative text detection has arrived as a genuine new problem with poor available tools, creating pressure to deploy something whose error properties are not understood and whose errors are systematically biased.

## What to Build

A detection system with measured errors and a proportionate response.

**Separate the fraud types, because they have different signatures and different costs.** Automated submission, duplicate accounts, location misrepresentation, and generated free text are four problems. Treating them as one "fraud score" is why honest workers get caught — a shared household is evidence for duplicates and evidence for nothing else.

**Build the graph properly for duplicates.** Identifier overlap, behavioural similarity and timing correlation over a worker graph, with base rates stated — a shared IP in a country with heavy NAT means almost nothing, a shared payment instrument means a great deal. Most false positives come from treating weak and strong evidence identically.

**State the base rates and the benign explanations.** For each signal, what proportion of honest workers exhibit it. This is computable from the population and it is what turns a fraud score into a calibrated one.

**Measure the false positive rate deliberately.** Sample excluded accounts and review them properly, with the exculpatory evidence sought. This is the only way to see an error class that generates no complaints, it is a bounded ongoing cost, and it is the number the function currently does not have.

**Use graduated responses.** Additional verification, restriction from sensitive study types, reduced concurrency, a review period — instead of exclusion. Most detections are moderate-confidence and deserve a moderate response, and today the only response is removal.

**Treat generative text detection with appropriate scepticism.** Available detectors have poor accuracy and error rates that fall hardest on non-native speakers, which in this workforce is most people. Use behavioural and timing evidence alongside, require multiple independent signals, and never exclude on a detector score alone. Stating this as policy is what prevents a bad tool becoming a discriminatory one.

**Build an appeal that works.** Plain-language reason, a route to contest, a human review, and restoration including of the reputational consequence. Without it the error rate remains unmeasurable and unbounded.

## Target Customer

Platform trust and safety leadership, and particularly the research-participant platforms, where data integrity is the product, the requesters are institutions with ethics obligations, and wrongful exclusion of participants is itself a research ethics concern.

## Impact If Built

Fraud detection acquires a measured error rate in both directions rather than only the one requesters complain about. Moderate suspicion gets a proportionate response. Generative text detection gets used as one signal among several rather than as a verdict. And the honest workers who resemble fraud — shared devices, institutional networks, second-language brevity — stop being removed without explanation.
