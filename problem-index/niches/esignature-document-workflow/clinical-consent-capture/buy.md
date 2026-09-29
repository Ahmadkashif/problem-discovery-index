# Readability and Translation Applied to Consent Forms

**Niche:** [[niches/esignature-document-workflow/clinical-consent-capture/profile|Clinical Consent Capture]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Readability measurement is a century old and machine translation is excellent, and consent forms are written at a reading level most patients cannot follow, in a language a substantial minority do not speak.
**Tags:** #large-language-models #transformers #bert #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #worker-facing
**Contested on:** Every serious competitor in clinical consent is fighting to capture the right consent form for the procedure actually being performed, bound to the correct patient and encounter, and land it in the chart before the patient goes to theatre — and whoever does that reliably takes the health system.

## The Problem
Informed consent is a legal and ethical requirement that the patient understood. The forms are written by risk management and counsel, in the register that produces, and repeated studies place their reading level far above that of the average patient. For patients with limited English proficiency the form is often in English with an interpreter reading it aloud, or in a translation nobody has validated. The signature is obtained, the requirement is recorded as met, and whether the patient understood is not measured by anything.

## What Already Exists
Readability metrics are standard and trivially computable. Plain-language rewriting is something current language models do well. Medical machine translation has improved substantially and professional medical translation is available for validation. Teach-back — asking the patient to explain the procedure in their own words — is an established, evidence-supported technique with a literature behind it. Health literacy research has produced validated plain-language consent templates for many common procedures. Very little of this reaches the form the patient signs.

## The Customization Gap
The adaptation is to a document with legal consequence where an error changes meaning. It requires: (1) rewriting constrained to preserve the legally material content — the specific risks, alternatives and the fact of uncertainty — which means a human review step and a diff against the original rather than an unattended rewrite, and this is non-negotiable; (2) readability measured on medical text specifically, since generic scores penalise necessary clinical terms and reward short sentences that say nothing, so the metric needs a medical-vocabulary allowance; (3) translation validated by a qualified medical translator per form and version, with machine translation used to produce the draft and to detect when a source revision has left a translation stale — which is the part that actually fails today; (4) teach-back captured structurally, which is far stronger evidence of informed consent than a signature and is currently recorded, if at all, as a sentence in a note; and (5) a language and interpretation record on every consent, since that is both required and routinely missing.

## Target Customer
Health system risk management and patient experience functions, ambulatory surgery centres, and the consent and perioperative platform vendors whose form libraries this would improve.

## Impact If Solved
The gap between the legal standard — that the patient understood — and the operational reality is wide, well documented and addressable with entirely mature tools. Stale-translation detection and structured teach-back are the two changes with the most immediate effect, and neither requires anything novel.
