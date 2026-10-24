# The Technician's Pretest and Visual Field Gauntlet

**Industry:** [[optometry-practices|Optometry Practices]]
**Type:** Worker Life Changing
**One-liner:** Ophthalmic technicians run every patient through five or six devices on a schedule built for the doctor, and they repeat unreliable visual fields and bad scans with no help telling which results will be thrown back at them.
**Tags:** #worker-facing #cnns #semantic-segmentation #logistic-regression #evaluation-metrics #workflow-orchestration #automation

## The Problem
Before the optometrist sees a patient, an ophthalmic technician takes them through pretesting. That means history, visual acuity, autorefraction and keratometry, non-contact tonometry, often a retinal photograph or Optomap, and, for medical patients, an OCT and a threshold visual field. There are 20,200 ophthalmic medical technicians in optometry offices, earning a mean of $38,020 (BLS OEWS 2023). Many are trained on the job. A busy technician works up thirty or more patients a day (estimate) while the schedule assumes each workup takes a fixed slot.

The visual field is the worst part. A threshold field takes several minutes per eye in a darkened room. The patient has to fixate and click when they see a light, and many older or anxious patients produce unreliable results with high false positives, fixation losses or a learning effect. The technician has to judge whether to coach and repeat or move on. If they move on, the doctor may reject the field and the patient comes back. If they repeat, the schedule slips and the waiting room fills. OCT scans have the same problem in a different form: a blink, a floater or poor signal produces a scan that looks fine on the screen but has a segmentation error the doctor will spot later.

## Why It Matters to the Worker
Technicians take the blame for the doctor's running late and for repeat visits, but they have no tool that tells them, while the patient is still in the chair, whether a result is usable. The work is repetitive and physically close. The pay is low for a job that needs judgement, and turnover is high (estimate). A technician who learns to read field reliability and scan quality well becomes indispensable, then gets poached by the practice across the street.

## What a Solution Looks Like
A quality check that runs as each test finishes. It reads the field's reliability indices and point pattern, and the OCT's signal strength and segmentation. It tells the technician in plain language: usable, repeat this eye now, or usable but flag for the doctor. It suggests a coaching script for the next attempt. It also predicts each patient's likely workup time from age, history and tests ordered, so the schedule leaves room for the hard ones instead of compressing everyone.

## Impact If Solved
Cutting repeat-visit fields and unusable scans by a third would save a technician roughly 30–45 minutes a day (estimate). It would also save patients a second trip, and give technicians a defined skill ladder instead of being blamed for results they had no way to check.
