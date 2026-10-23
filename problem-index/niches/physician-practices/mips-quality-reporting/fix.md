# Measures Computed From Fields Nobody Fills In

**Niche:** [[niches/physician-practices/mips-quality-reporting/profile|MIPS & Quality Measure Reporting]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Fix (Pain Point)
**One-liner:** Certified measures count a screening only when a specific structured field is filled; physicians document it in the note, so the measure rate understates the care delivered.
**Tags:** #bert #large-language-models #data-integration #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to land each clinician's MIPS score above the 75-point threshold from data the practice already holds, and whoever clears the threshold for the most clinicians without adding manual chart abstraction takes the account.

## The Problem
A physician writes "depression screen negative" or "discussed tobacco cessation" in the note. The eCQM looks for a coded PHQ-9 result or a specific counselling code. The patient counts as a gap. Quality staff then abstract charts by hand or nag physicians to click boxes.

## Why It's Still Broken
EHR measure logic is certified against structured data elements, and changing workflow to fill them costs physician clicks. Ambient notes make the gap wider: richer text, same empty fields.

## What a Fix Looks Like
Read the note and the transcript for measure-relevant facts, propose the structured entry with the supporting sentence, and let the clinician or MA accept it at sign-off. Measure rates then reflect documented care without extra clicks during the visit.

## Who Feels the Pain
Quality managers abstracting in January; physicians asked to re-document; groups whose scores sit just under the threshold.

## Impact If Fixed
Capturing documented-but-uncoded care could lift several measure rates by ~5–15 points (estimate) and remove most January abstraction.
