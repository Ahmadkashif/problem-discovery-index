# Consent as an Executable Policy Over Fields

**Niche:** [[niches/healthcare-practice-software/behavioral-health-ehr/profile|Behavioral Health & SUD Practice Software]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Behavioral health vendors model 42 CFR Part 2 consent as a signed document and an access control, so the protection stops working at the exact moment the record leaves the system, which is the only moment that matters.
**Tags:** #bert #large-language-models #transformers #evaluation-metrics #confidence-intervals #compliance #data-integration #workflow-orchestration
**Contested on:** Every serious competitor in behavioral health software is fighting to share a patient record with a referring provider while withholding exactly the 42 CFR Part 2 material and proving it did so — and whoever makes that segmentation reliable takes the account.

## The Problem
A patient in an opioid treatment programme is admitted to hospital. The hospital requests records. The programme holds a consent naming that hospital, for treatment purposes, for ninety days. Someone now has to produce a record that contains the medication and dose the hospital urgently needs, without disclosing the Part 2 material the consent does not cover, and with the redisclosure notice attached. In practice, that person opens the chart, reads it, copies parts of it into a document, and sends it. The clinical content is buried in narrative, where the protected facts are sentences rather than fields, and the person doing the redaction is a records clerk under time pressure with a patient in an emergency department.

## Why Nobody Has Built This
Segmentation at the data level requires knowing which facts are protected, and in behavioral health most of the record is prose. Structured medication and diagnosis fields are the easy part; the hard part is that a therapy note discloses the same facts in narrative, and a system that exports structured fields cleanly while attaching an unredacted note has failed completely. Vendors have therefore treated the problem as procedural — train the clerk, keep the form — which is defensible and does not scale. There is also no safe failure mode: an over-redacted record that omits a medication can kill a patient, and an under-redacted one is a federal disclosure violation, so the product must be right rather than conservative.

## What to Build
A consent engine that compiles a signed consent into an executable policy — recipient, purpose, data classes, expiry — and a segmentation layer that applies it to every egress path the system has: C-CDA export, HIE query, payer request, fax, portal share. Structured data is filtered by class. Narrative is processed by span-level detection of protected content, which proposes redactions with confidence and routes anything uncertain to a human, presented as a diff against the original rather than as a blank page. Every disclosure produces an immutable record of what was released, under which consent, to whom, with the redisclosure notice — which is the artefact a Part 2 audit asks for and which almost no practice can produce today. The critical design decision is that the engine never silently drops clinically urgent structured data; a conflict between a consent and a medication list surfaces to a human immediately rather than resolving itself.

## Target Customer
Behavioral health and SUD EHR vendors — Netsmart, Qualifacts, Kipu and the mid-market tier — plus opioid treatment programmes and integrated behavioral health groups coordinating with medical providers at volume.

## Impact If Built
Segmentation turns "we cannot share" into "we can share this much, provably," which is the difference between a behavioral health provider being a participant in coordinated care and being a closed silo. It also removes the records clerk from a position where a reading error is a federal violation. For the vendor it is the only capability in the niche that a competitor cannot claim in a demo without demonstrating it against a real narrative record.
