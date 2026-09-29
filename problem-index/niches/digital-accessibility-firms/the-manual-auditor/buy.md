# Evidence Capture From Field Inspection

**Niche:** [[niches/digital-accessibility-firms/the-manual-auditor/profile|The Manual Auditor]]
**Industry:** [[industries/digital-accessibility-firms|Digital Accessibility Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Field inspection made capture a tap on a phone with the report generated afterwards, and accessibility auditing uses a spreadsheet.
**Tags:** #worker-facing #automation #workflow-orchestration #data-integration #evaluation-metrics #compliance #descriptive-statistics #large-language-models
**Contested on:** Every serious competitor in this niche is fighting to support an auditor working a site keyboard-only and then twice with screen readers for weeks, documenting each failure against a criterion — and whoever supports that work takes the account.

## The Problem
Field inspection across building, safety and quality disciplines solved the same shape of problem: an expert observes defects, each must be classified against a standard, located, evidenced and reported, and the writing-up used to take as long as the inspection. The answer was mobile capture — tap the defect, select from a standard list, attach a photo, location recorded automatically — with the report generated from the captured record. Inspection time fell sharply and consistency rose.

## What Already Exists
In-the-moment capture against a standard list; automatic location and context capture; photographic evidence attached at capture; report generation from the record; and consistency through structured capture.

## The Customization Gap
The adaptation is to a digital artefact where location is a document position and the evidence is behaviour over time. It requires: (1) location captured as an element path and page state rather than a physical position, which is both easier and more brittle since the page changes — this is the substantive difference; (2) evidence that is what an assistive technology announced over a sequence of interactions rather than a photograph; (3) an auditor whose hands are on a keyboard and whose attention is on audio output, so capture must not require switching context; (4) an auditor who may themselves use assistive technology, making the capture tool's own accessibility a hard requirement; and (5) criteria requiring interpretation rather than a defect type selected from a list.

## Target Customer
Accessibility firms, in-house accessibility teams, audit tooling vendors, and field inspection software providers.

## Impact If Solved
Field inspection moved capture into the moment and generated the report afterwards, cutting time and raising consistency. Evidence that is what a screen reader announced over a sequence, captured without breaking the auditor's context, is what has to be rebuilt.
