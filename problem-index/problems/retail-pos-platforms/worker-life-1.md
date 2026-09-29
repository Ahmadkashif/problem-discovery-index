# Cycle Counts and Shrink Investigation

**Industry:** [[retail-pos-platforms|Retail POS Platforms]]
**Type:** Worker Life Changing
**One-liner:** Store staff stop spending evenings counting shelves in a fixed rotation and stop investigating discrepancies that were caused by a receiving error four months ago, because the system counts what matters and explains what it finds.
**Tags:** #bayesian-inference #gradient-boosting #change-point-detection #hypothesis-testing #confidence-intervals #evaluation-metrics #worker-facing #automation

## The Problem
Inventory records drift, so retailers count. Full physical inventories once or twice a year, and cycle counts continuously — a section at a time, on a rotation, usually after close or before open, by staff who have already worked a shift.

The rotation is almost always arbitrary. Aisle by aisle, category by category, alphabetically. It counts the slow-moving low-value goods as diligently as the fast-moving expensive ones, which means the effort is spread evenly across items whose count accuracy matters very unevenly.

When a discrepancy appears, someone investigates. The record says twelve, the shelf has nine, and the question is what happened. Was it stolen? Was the delivery short? Was it sold and mis-scanned? Was it moved to the back? The trail is cold — the discrepancy may have originated months earlier — and the investigation usually ends with an adjustment and no conclusion.

Staff know the investigations go nowhere. They do them because a number has to be reconciled.

## Why It Matters to the Worker
Cycle counting is unglamorous work done at the ends of days, and it is the part of retail employment that most reliably extends the shift. In a sector with high turnover and thin wages, the after-hours count is a recurring grievance.

The shrink investigation carries something worse. Discrepancies in a small store implicitly point at a small number of people, and an unresolved shrink number creates an atmosphere of suspicion that falls on staff who have done nothing. Managers know this and dislike it, and there is no tool that helps them distinguish a receiving error from a theft, so the ambiguity persists.

The waste is the plainest part. Most counted items were correct and did not need counting; the items that were wrong were frequently not on the rotation.

## What a Solution Looks Like
Counting directed by expected error and consequence. The system should know which items have not been verified recently, which categories drift fastest in this store, which items sell quickly enough that an error matters this week, and which are expensive enough that being wrong is costly. A short prioritised list beats a full aisle.

Discrepancy diagnosis from pattern rather than from memory. Receiving errors, register mis-scans and theft leave different signatures — in timing, in which items, in which shifts, in whether the discrepancy is a clean multiple of a case pack. Classifying them is a modest analysis on data the POS already holds, and it is the difference between an investigation with a direction and an adjustment with a shrug.

Continuous small counts triggered by the system, sized to fit into ordinary shift gaps rather than into after-hours sessions.

## Impact If Solved
Shrink is a significant and poorly understood cost line in independent retail, and the labour spent chasing it is largely misdirected. Prioritised counting produces better accuracy for a fraction of the hours, and diagnosis converts an atmosphere of suspicion into a set of specific, fixable process problems.
