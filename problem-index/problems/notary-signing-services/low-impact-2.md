# The Fifty-State Journal and Certificate Rulebook

**Industry:** [[notary-signing-services|Notary & Signing Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Electronic journal apps already record notarial acts; none reliably tells a notary what this state requires for this act — the fields, the thumbprint, the certificate wording, the retention period — at the moment the entry is made.
**Tags:** #large-language-models #bert #decision-trees #evaluation-metrics #compliance #automation #data-integration

## The Problem
Notarial record-keeping is set by state statute, and the states disagree. California requires one active sequential journal, kept locked under the notary's exclusive control, with the date, time and type of act, a description of the instrument, the signer's signature, the identity evidence or the credible witnesses' details, the fee, and a right thumbprint for any deed, deed of trust, other real property document or power of attorney. Other states require a journal only for certain acts, and roughly half (estimate) require none. Remote acts bring separate rules on session recordings and retention periods that run for years (commonly five to ten, estimate). A signing agent working near a state line, or commissioned in one state and performing remote acts for signers in another, has to know which rules apply to each entry. Certificate wording adds a second layer: an acknowledgment that is valid in one state may be rejected by a recorder in another if the wording or venue is wrong.

## What Already Exists
Paper journals sold by the NNA and supply vendors; e-journal apps such as Notary eJournal (built around California rules, with a separate Bluetooth thumbprint scanner) and NotaryAssist; journal modules inside RON platforms; state notary handbooks and the NNA hotline for questions.

## The Customisation Gap
What is missing is the rule layer, maintained and applied at entry time: a per-state, per-act model of required fields, permitted identity evidence (including credible witnesses and their count), thumbprint triggers, whether electronic journals are allowed at all, retention and disposal rules, and acceptable certificate forms, kept current as legislatures amend them. The app should refuse to close an entry that is missing a required field, generate the correct certificate for the act and venue, and flag cross-state cases where the notary's commission state and the document's destination impose different requirements. Rules change by statute and by Secretary of State guidance, so the knowledge needs a maintained source rather than a one-off template.

## Impact If Solved
A notary whose journal entry is complete under their state's rules has their best defence when an act is challenged, and a title company can trust an act without re-checking it. For the signing agent, the burden lifted is the nagging uncertainty over whether a missed field or a wrong certificate will surface years later in a lawsuit.
