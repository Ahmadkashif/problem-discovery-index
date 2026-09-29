# DICOM Worklist Adapted to the Ophthalmic Lane

**Niche:** [[niches/healthcare-practice-software/ophthalmology-ehr-imaging-chain/profile|Ophthalmology EHR — the Imaging-to-Code Chain]]
**Industry:** [[industries/healthcare-practice-software|Healthcare Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Modality worklist is a solved, bought radiology component that eliminates manual patient entry at the device, and it is under-deployed in ophthalmology because the ophthalmic lane breaks every assumption the radiology version makes.
**Tags:** #evaluation-metrics #descriptive-statistics #workflow-orchestration #data-integration #automation #quick-win #worker-facing #compliance
**Contested on:** Every serious competitor in ophthalmology EHR is fighting to make diagnostic images from every device in the lane arrive in the chart already bound to eye, date and the interpretation that justifies the code — and whoever closes that chain best takes the account.

## The Problem
Most binding failures are created at the device, not in the chart: a technician types a patient name at a console under time pressure, transposes a character, and the study arrives unmatched. Radiology solved this two decades ago with modality worklist — the device queries the scheduling system and the technician picks the patient from a list. In ophthalmology it is inconsistently deployed, because the lane is not a radiology suite. Tests are ordered mid-exam rather than scheduled in advance, a patient moves between four devices in twenty minutes, both eyes may be imaged in one sitting with different procedures, and much of the installed base predates or half-implements the standard.

## What Already Exists
DICOM Modality Worklist is mature, universally specified and supported by every current-generation ophthalmic device and by the broker products — DICOM routers, integration engines and the ophthalmic image management platforms — that sit between devices and the record. The pieces are all purchasable. What is missing is the adaptation to the lane, which is why practices that own the components still run a holding queue.

## The Customization Gap
The adaptation requires: (1) driving the worklist from the live encounter rather than from a scheduled order, so a test decided on mid-exam appears at the device within seconds; (2) modelling the procedure step per eye so that a bilateral study arrives as two correctly lateralised objects rather than one ambiguous one; (3) a lane-aware worklist that shows the technician the handful of patients currently in the practice instead of the day's full schedule, which is the difference between a list that is used and one that is scrolled past; (4) a graceful path for devices that cannot query — a broker that attaches context from the lane's current state and flags the result as inferred rather than asserted; and (5) reporting unmatched-study rate per device per week as a standing operational metric, because that number is what tells a practice which console to replace.

## Target Customer
Ophthalmology practices with four or more imaging devices and an existing holding queue, and the image management and integration vendors already selling into them who can bundle the adaptation rather than build a platform.

## Impact If Solved
Practices that get worklist working in the lane typically eliminate the majority of unmatched studies outright, which is a larger effect than any downstream matching improvement can achieve, because the error is prevented instead of corrected. It also converts the remaining queue into a tractable exception set for the build note's inference layer, making the two complementary rather than competing.
