# Nobody Can List Tomorrow's Missing Consents

**Niche:** [[niches/esignature-document-workflow/clinical-consent-capture/profile|Clinical Consent Capture]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Fix (Pain Point)
**One-liner:** Consents are stored as scanned images attached to an encounter, so the only way to know whether tomorrow's list is fully consented is for someone to open every chart.
**Tags:** #descriptive-statistics #logistic-regression #cnns #evaluation-metrics #confidence-intervals #compliance #quick-win #automation
**Contested on:** Every serious competitor in clinical consent is fighting to capture the right consent form for the procedure actually being performed, bound to the correct patient and encounter, and land it in the chart before the patient goes to theatre — and whoever does that reliably takes the health system.

## The Problem
A pre-operative nurse works through tomorrow's list one chart at a time, looking for a consent, checking it names the right procedure, checking it is signed and dated and that the clinician's signature is there. Twenty-two cases, an hour and a half, every evening. The ones that are missing are chased at nine at night or discovered at seven the next morning. The health system cannot answer "how many of tomorrow's cases are fully consented" without a person doing this, and therefore does not know its own rate.

## Why It's Still Broken
Consent arrives in the chart as an image — scanned paper or a flattened PDF — with no structured fields, so nothing about it is queryable. Even electronically captured consents are frequently stored as documents rather than as data, which throws away the structure at the last step. The manual check works well enough that it has never been escalated, and its cost is absorbed by nursing staff whose time is not billed separately. And the metric does not exist, so nobody is accountable for it.

## What a Fix Looks Like
Make consent status a queryable field. For electronically captured consent this is a storage decision rather than a project: record procedure, laterality, patient, encounter, obtaining clinician, date, language and interpreter as structured fields alongside the document. For the scanned backlog and for paper, classification and extraction on the image gives most of the same fields at adequate accuracy, and a confidence-routed exception queue handles the rest. Then run the check across the list rather than per chart: a daily report of tomorrow's cases with consent status, mismatches against the scheduled procedure, and missing clinician signatures — which is the same work the nurse does, done in seconds, leaving the nurse to chase the exceptions rather than to find them. Measure the rate and the causes over time, which turns an invisible nightly grind into a number that can be improved and attributed.

## Who Feels the Pain
Pre-operative and perioperative nurses doing ninety minutes of chart-opening every evening; surgeons and patients whose cases are delayed on the day; and risk management, who discover the missing consent during a claim.

## Impact If Fixed
The structured-capture half is a storage decision with no technical difficulty that has simply not been made, and it converts the nightly manual sweep into a report. The extraction half handles the legacy and paper remainder, and the resulting rate is a metric health systems currently cannot produce at all.
