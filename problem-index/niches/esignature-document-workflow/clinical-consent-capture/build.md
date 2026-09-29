# The Consent That Does Not Match the Procedure

**Niche:** [[niches/esignature-document-workflow/clinical-consent-capture/profile|Clinical Consent Capture]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Consent form selection is a human picking from a library of hundreds, and the scheduled procedure, its laterality and its additions are all structured data sitting in the same system.
**Tags:** #logistic-regression #bert #word-embeddings #graph-theory #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in clinical consent is fighting to capture the right consent form for the procedure actually being performed, bound to the correct patient and encounter, and land it in the chart before the patient goes to theatre — and whoever does that reliably takes the health system.

## The Problem
A patient is scheduled for a procedure on the left side. Consent is obtained in clinic three weeks earlier using a general form for the procedure family, without laterality specified. In the interval the surgeon adds a second procedure. On the day, the pre-operative nurse finds a consent that names one procedure and no side, for an operation that is now two procedures on a specified side. The case is delayed while someone finds the surgeon to re-consent, or it proceeds on a consent that does not describe what is about to happen. The scheduling system knew about the change on the day it was made.

## Why Nobody Has Built This
Consent has been treated as paperwork rather than as clinical documentation, so it was digitised as a form to sign rather than as a record to validate. The form libraries are large, locally customised and often maintained by a committee, which makes mapping them to procedure codes a data project nobody has funded. The electronic health record vendors own the scheduling data and treat consent as a minor module. And the failure is usually caught by a nurse on the day, which converts a systemic defect into routine unglamorous labour that never rises to a project.

## What to Build
Consent driven by the scheduled procedure rather than chosen by a person. A maintained mapping from procedure codes and scheduling descriptions to the correct consent form, including laterality and multi-procedure composition, so the form is generated from the booking rather than selected from a list. Continuous revalidation, so a change to the scheduled procedure after consent was obtained invalidates the existing consent and flags it immediately rather than at the pre-operative check — which is the single highest-value behaviour and requires only that something watches the schedule. Structured capture of who obtained consent, when, in what language and with what interpretation, all of which are currently in free text or absent. Binding to the patient and encounter identifiers rather than to a name and date of birth typed twice. And a pre-operative completeness check that runs across tomorrow's list rather than patient by patient at the desk, which is the operational output the whole thing exists to produce.

## Target Customer
Health system perioperative and risk management leadership, ambulatory surgery centres where the margin for a cancelled case is thinnest, and the EHR and perioperative platform vendors who hold the scheduling data.

## Impact If Built
Consent defects are a well-documented contributor to case delays and cancellations and a recurring theme in claims, and the information needed to prevent them is already structured and already present. Revalidation on schedule change is a small piece of logic addressing the most common failure.
