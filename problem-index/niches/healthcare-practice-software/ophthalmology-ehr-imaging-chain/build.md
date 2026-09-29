# Laterality-Bound Image Ingestion Across Mixed Device Estates

**Niche:** [[niches/healthcare-practice-software/ophthalmology-ehr-imaging-chain/profile|Ophthalmology EHR — the Imaging-to-Code Chain]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No ophthalmology platform reliably binds an inbound diagnostic image to the right patient, eye and encounter when the device does not say which eye it photographed, which is most of the older estate in most practices.
**Tags:** #cnns #object-detection #semantic-segmentation #transfer-learning #evaluation-metrics #confidence-intervals #data-integration #automation
**Contested on:** Every serious competitor in ophthalmology EHR is fighting to make diagnostic images from every device in the lane arrive in the chart already bound to eye, date and the interpretation that justifies the code — and whoever closes that chain best takes the account.

## The Problem
A technician runs four tests on a glaucoma patient across four devices. Two emit clean DICOM with laterality populated and land correctly. One emits DICOM with an empty laterality field because the operator skipped it on the device console. One emits a rendered PDF report with the eye printed in a corner as text. The last two arrive in a holding queue, and someone opens each one, reads the eye off the image, and files it. At a busy practice that queue runs to hundreds of items a day. Errors in it are quiet and expensive: an OCT filed to the wrong eye produces a claim with the wrong modifier and a chart that says something untrue about a patient's optic nerve.

## Why Nobody Has Built This
The binding problem sits in a gap nobody owns. Device manufacturers have no commercial reason to fix an older console's metadata behaviour, and many of the devices in service are a decade old. EHR vendors treat the holding queue as a support workflow rather than a product defect, because it is staffed successfully — the practice absorbs it. And the technical work is genuinely per-modality: reading laterality off a fundus photograph, a visual field printout and an OCT report are three different problems, only solvable with labelled examples of each, which no single practice has enough of and which the vendors hold and have never pooled.

## What to Build
An ingestion layer that resolves patient, eye, date and study type from whatever the device emits, using metadata where present and the image itself where not. Fundus and OCT laterality is inferable from anatomy — optic disc position relative to the macula is the standard cue — and report-style outputs carry the eye as printed text in a stable position per device model. The layer returns a binding with a confidence, files automatically above a threshold, and routes the remainder to a human with its best guess pre-filled rather than blank. Every human correction is a label, so the per-device-model accuracy improves in place. The essential product discipline is calibration: a wrong automatic binding is worse than a queue item, so the threshold is set from the practice's own tolerance and reported on continuously.

## Target Customer
Ophthalmology EHR and ophthalmic image management vendors, and the multi-site ophthalmology and optometry groups whose device estates span enough manufacturer-generations that the holding queue is a staffed function.

## Impact If Built
Automatic binding of 85-95% of inbound imaging removes one to two FTE-equivalents of reconciliation at a mid-size practice and eliminates the laterality error class at its source. For the vendor it is the first ophthalmic capability that is measurable in a bake-off — run both platforms against the practice's real device estate for a week and compare bind rates, which is a comparison the interface-count incumbents cannot win by adding interfaces.
