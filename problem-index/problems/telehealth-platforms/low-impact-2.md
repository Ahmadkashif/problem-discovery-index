# Intake, Documentation and Coding

**Industry:** [[telehealth-platforms|Telehealth Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The clinician spends as long documenting the visit as conducting it, on a record that will not reach the patient's actual doctor.
**Tags:** #transformers #large-language-models #bert #gradient-boosting #evaluation-metrics #compliance #automation #data-integration

## The Problem
Every visit generates documentation: the clinical note, the diagnosis codes, the prescription record, the patient instructions and whatever the payer requires. On short virtual visits the documentation burden is proportionally enormous — a fifteen-minute visit can carry ten minutes of typing — and it is the largest single contributor to clinician dissatisfaction in virtual care as it is in medicine generally.

Intake is the other half. Patients complete questionnaires whose design determines what the clinician sees, and the questionnaires are generic by condition rather than adaptive to the answers given. A patient with a complex history answers the same twelve questions as one with none, and the clinician receives a form rather than a history.

The record then goes nowhere useful. The note sits in the platform's own system, which typically does not integrate with the patient's primary care record, so the next clinician — whether on this platform or at the patient's practice — starts without it. For episodic care of a self-limiting complaint that may not matter; for anything chronic or recurrent it is the central failure of the model.

Coding sits on top, with its own accuracy and compliance stakes, and is frequently done by the clinician under time pressure.

## What Already Exists
Ambient clinical documentation has advanced substantially, with Abridge, Nuance DAX, Suki and others generating notes from the consultation audio, and adoption is growing quickly. Template and macro systems are universal. Coding assistance exists in most electronic health record systems. Adaptive intake questionnaires exist in some platforms. Health information exchange networks and interoperability requirements under the information blocking rules have improved external record availability, though participation by direct-to-consumer platforms is uneven.

## The Customisation Gap
Ambient documentation is designed for longer in-person consultations and needs adapting to short virtual and asynchronous encounters, where the audio is thinner, the structure is different, and a substantial share of visits have no consultation audio at all because they are message-based.

Intake should be adaptive and should pull rather than only ask. An intake that branches on the answers given, and that requests the patient's external records through an exchange network before the visit rather than relying entirely on recall, changes what the clinician has to work with. That is an integration problem and a consent problem rather than a modelling one.

Outbound record sharing is the gap with the largest clinical consequence. Sending the visit summary to the patient's primary care practice, with consent, is technically routine under current interoperability infrastructure and is not done consistently — which means the fragmentation that makes virtual care risky is partly a choice.

And documentation should support the outcome measurement rather than only the billing. Structured capture of the decision made, the reasoning and the safety-netting advice given is what makes it possible to evaluate a clinical decision later, and free-text notes optimised for coding do not provide it.

## Impact If Solved
Documentation burden is the leading driver of clinician burnout and consumes a large share of a short visit's clinical time. Adapting ambient documentation to virtual and asynchronous encounters returns that time; adaptive intake with external record retrieval changes the quality of the information the decision is made on; and consistent outbound sharing addresses the record fragmentation that is virtual care's central clinical weakness.
