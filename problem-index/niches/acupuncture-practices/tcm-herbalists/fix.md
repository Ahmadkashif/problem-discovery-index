# Herb-Drug Interaction Checking for TCM Formulas

**Niche:** [[niches/acupuncture-practices/tcm-herbalists/profile|Traditional Chinese Medicine Herbalists]]
**Industry:** [[industries/acupuncture-practices|Acupuncture Practices]]
**Type:** Fix (Pain Point)
**One-liner:** TCM practitioners have no real-time tool to check whether a custom herbal formula interacts with a patient's Western pharmaceutical medications — they rely on memory and scattered references.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #compliance #worker-facing

## The Problem
Most TCM herb patients also take Western pharmaceuticals. An herbalist prescribing a formula containing Dan Shen (Salvia miltiorrhiza) needs to know it potentiates warfarin — but this interaction isn't in any TCM reference, and Western drug-interaction databases don't include TCM herbs. Practitioners rely on a handful of reference books (Chen & Chen's Chinese Medical Herbology), scattered journal articles, and years of clinical experience. Checking a 12-herb formula against a patient's 5 medications takes 15-30 minutes of manual research, if it happens at all.

## Why It's Still Broken
Herb-drug interaction data is fragmented across pharmacological research, TCM clinical literature, and case reports — much of it in Chinese-language journals. No comprehensive database maps the ~400 commonly used TCM herbs against the major Western drug classes. The FDA classifies herbs as dietary supplements, so there's no regulatory mandate driving database creation. Existing drug-interaction checkers (Epocrates, Lexicomp) cover a handful of popular supplements (St. John's Wort, Ginkgo) but not the full TCM pharmacopoeia.

## What a Fix Looks Like
A lookup tool where the practitioner enters a formula's herb list and the patient's medication list, and receives interaction alerts graded by severity (contraindicated, caution, monitor, theoretical). The database would be built from published interaction research, pharmacological mechanism data (e.g., CYP450 enzyme effects of individual herbs), and practitioner-reported adverse events. Updated quarterly as new research is published.

## Who Feels the Pain
TCM practitioners who worry about patient safety when prescribing herbs alongside pharmaceuticals, and patients who receive herbs without anyone checking for interactions — estimated to affect 40-60% of herb prescriptions.

## Impact If Fixed
Prevents potentially dangerous interactions, reduces practitioner liability exposure, builds patient trust, and enables TCM practitioners to confidently treat patients on complex medication regimens rather than defaulting to "no herbs if you take any medications."
