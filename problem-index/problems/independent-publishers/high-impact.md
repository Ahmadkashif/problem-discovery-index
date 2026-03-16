# Manuscript Acquisition Prediction

**Industry:** [[independent-publishers|Independent Publishers]]
**Type:** High Impact
**One-liner:** Acquisitions editors can predict a manuscript's market trajectory from five pages of prose — encoding that tacit literary-commercial judgment into a model transforms how independent publishers allocate their most constrained resource: acquisition slots.
**Tags:** #bert #transformer #regression #nlp #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
An experienced acquisitions editor reads the first five pages of a submission and forms a reliable intuition about whether the manuscript has commercial potential — assessing voice quality, narrative momentum, prose rhythm, and market positioning simultaneously. This pattern recognition is built across thousands of evaluated manuscripts and hundreds of tracked outcomes, yet the editor cannot fully articulate the decision rules. Independent publishers receive 2,000-10,000 submissions annually but can only acquire 15-40 titles, meaning 99%+ of editorial reading time is spent on manuscripts that will be rejected, while the small number of acquisitions carry outsized financial risk because each title represents a significant fraction of annual revenue.

## Why It's Unsolved
**Data collection challenge:** Capturing the expert signal requires pairing manuscript text with the editor's assessment *and* eventual market outcome (units sold, revenue, review sentiment, award longlists). Most publishers lack structured records connecting submission text to commercial performance — rejected manuscripts disappear, and acquired titles' outcomes live in royalty systems disconnected from editorial notes. **Labeling challenge:** Experienced editors disagree with each other and with themselves over time; a manuscript rejected in 2019 might be acquired in 2023 as market taste shifts. The "ground truth" is entangled with timing, list composition, and marketing investment. **Deployment challenge:** Editors distrust automated literary judgment and will reject any system that claims to replace their taste; the model must augment (surface high-probability manuscripts from the slush pile) rather than gatekeep.

## What a Solution Looks Like
A transformer-based model ingests the first 5,000-10,000 words of a manuscript along with structured metadata (genre, comp titles, author platform metrics, submission source) and outputs a market-potential score calibrated against the publisher's historical acquisition outcomes. The system surfaces a ranked shortlist of submissions most likely to match the publisher's commercial profile, with attention-highlighted passages showing which textual features drove the score. Editors use it as a first-pass filter on the slush pile, not as a final decision tool.

## Impact If Solved
Reduces editorial triage time by 60-70%, allowing acquisitions editors to focus deep-reading time on the 5-10% of submissions with genuine potential. A single avoided bad acquisition (typical advance + production cost: $30K-$80K for an indie press) or a single surfaced sleeper hit pays for the system many times over.
