# Training Content and Targeting

**Industry:** [[security-awareness-training|Security Awareness Training]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Everyone receives the same annual modules regardless of what they do, what they are exposed to, or what they already know.
**Tags:** #gradient-boosting #bert #transformers #k-nearest-neighbors #confidence-intervals #evaluation-metrics #transfer-learning #worker-facing

## The Problem
Training in this category is predominantly uniform. A library of modules covering phishing, passwords, data handling and social engineering is assigned annually or quarterly, everyone completes the same content, and completion is tracked as the compliance artefact.

The population is not uniform in any relevant way. A finance team processing payment changes faces business email compromise; a developer faces credential theft and dependency attacks; an executive assistant is a high-value target for impersonation; a warehouse worker with a shared terminal faces something else entirely. The exposure differs, the plausible attack differs, and the training does not.

Prior knowledge differs too. Assigning introductory phishing content to a security-aware engineer is a waste of their time and a signal that the programme is a formality, which is precisely the impression that makes people click through it.

And the content is mostly delivered as an interruption rather than in context. A module watched in March has little connection to a suspicious message received in September, and the evidence on retention from one-off training is not encouraging.

## What Already Exists
Vendors provide large content libraries with role-based assignment options, and the better platforms have moved toward shorter continuous micro-training rather than annual modules. Some deliver just-in-time training immediately after a simulation failure, which is a genuine improvement on delayed assignment. Completion tracking and reporting is universal because it is the compliance requirement. A few vendors personalise difficulty and content by prior performance.

## The Customisation Gap
Targeting should follow exposure, which is observable. Who receives phishing attempts, of what kind, at what volume, is recorded by the email gateway; who has access to payment systems, customer data or production infrastructure is in the identity system; who has been impersonated externally is knowable from brand monitoring. Training assigned against real individual exposure would be different for nearly everyone and is currently assigned by job title at best.

Prior knowledge should be assessed rather than assumed. A short adaptive assessment placing an employee on a scale, and content assigned against the gap, is standard practice in education and rare here — largely because the compliance artefact is completion rather than capability.

Context delivery is the intervention most likely to work. Training attached to a moment — a genuinely suspicious message received, a payment change request, an unusual access grant — has the attention that a scheduled module does not, and the trigger conditions are observable in systems the organisation already runs.

And the content itself needs evaluating on retention rather than completion. Which modules produce durable behaviour change, measured weeks later against real behaviour, is testable and is not tested.

## Impact If Solved
Training time is a substantial organisational cost delivered uniformly to a population with wildly different exposure and knowledge. Exposure-driven targeting, assessed rather than assumed prior knowledge, contextual delivery at the moment of relevance and retention-based content evaluation would make the same budget buy considerably more — and would remove the click-through-the-module dynamic that a formality reliably produces.
