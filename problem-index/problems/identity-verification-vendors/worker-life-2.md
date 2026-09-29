# The Solutions Engineer Explaining the Rejection

**Industry:** [[identity-verification-vendors|Identity Verification Vendors]]
**Type:** Worker Life Changing
**One-liner:** Solutions engineers field escalations about specific people who could not open an account, and must explain a decision the system cannot articulate.
**Tags:** #large-language-models #bert #gradient-boosting #k-nearest-neighbors #evaluation-metrics #worker-facing #workflow-orchestration #compliance

## The Problem
A customer escalates. A specific applicant has failed verification three times. They are a real person, the customer knows this, and they want to know why the system rejected them.

The solutions engineer pulls the record. There are sub-scores from several checks: a document score, a face match score, a database resolution result, a device signal. Some are thresholded internally. Some are composite. Several are model outputs with no human-legible explanation.

So the answer is a reconstruction. The document image was low contrast and the security feature check was inconclusive; the face match scored just below threshold; the address history did not resolve. Each is a partial reason, none is the reason, and the applicant experienced a single word: failed.

Meanwhile the customer wants to know whether to loosen a threshold, which the engineer cannot answer without knowing how much fraud that loosening would admit — a number nobody has for this customer's population.

These escalations are frequent and each takes hours. They arrive with a real person attached and a customer who is losing patience, and often the honest answer is that the applicant's document, device or address history sits in a region where the system performs poorly, which is not an answer anyone wants to give.

## Why It Matters to the Worker
The engineer is asked to explain systems that were not built to be explained, and does it by inference, repeatedly, under pressure, for individual people whose circumstances they can see.

The honest answer is frequently uncomfortable. Telling a customer that their applicant failed because they have an older phone, an uncommon document and a thin file is closer to the truth than any single reason code, and it is not a comfortable sentence to write.

The threshold conversation has no evidence behind it. The engineer is asked to advise on a fraud-versus-conversion tradeoff for which the vendor has never measured one of the two axes, and must give advice anyway.

The same explanation is written repeatedly. The failure patterns are few and recurring, and each escalation is reconstructed from scratch.

And the engineer is the only person in the chain who regularly sees the individual human consequences of the threshold, with no channel through which that observation reaches product.

## What a Solution Looks Like
Explanations generated from the actual decision path. Which checks ran, what each returned, which drove the outcome, and what would have changed it — assembled automatically rather than reconstructed by hand.

Attribution that distinguishes capture problems from identity problems. A blurred photograph and an unresolvable address history are entirely different situations and are currently both a failure.

Actionable guidance for the applicant. Retake in better light, use a different document type, try the alternative verification path — specific to what actually failed, delivered to the person at the moment of failure rather than to a solutions engineer three weeks later.

Threshold impact estimation per customer population, so the conversation about loosening has numbers on both sides. Where a randomised or audit-based measurement exists, this becomes a real recommendation rather than an opinion.

Escalation patterns fed back to product. The failure modes appearing repeatedly in escalations are the vendor's actual quality problems, and this role sees them first and has no route to report them.

Self-service diagnostics for customers, so the recurring explanations are available without an engineer reconstructing them.

## Impact If Solved
This role is the only place in the industry where the individual consequences of verification failure become visible, and it has no tooling and no channel. Generated explanations, applicant-facing guidance at the point of failure and measured threshold advice turn a reactive escalation burden into a feedback loop the product currently lacks entirely.
