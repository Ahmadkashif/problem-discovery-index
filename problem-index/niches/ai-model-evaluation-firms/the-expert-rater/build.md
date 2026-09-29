# A Physician at Piece Rates

**Niche:** [[niches/ai-model-evaluation-firms/the-expert-rater/profile|The Expert Rater]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A practising physician or attorney rating model outputs is doing genuinely hard cognitive work at piece rates, against rubrics that do not cover the cases they actually encounter, with no way to record that the question itself was wrong.
**Tags:** #worker-facing #tacit-knowledge-ml #evaluation-metrics #descriptive-statistics #confidence-intervals #hypothesis-testing #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to keep scarce practising specialists willing to do this work — and whoever does that takes the supply, because the entire domain evaluation business depends on a pool that is currently being spent down.

## The Problem
An attorney takes contract review rating work in the evenings. Each item pays a fixed amount assuming a few minutes. Some items are straightforward. Some require reading a clause, reconstructing the governing law, and working out whether the model's reading is defensible — twenty minutes of real professional work at a rate that makes it worth less than their lowest-value billable hour. The rubric has four categories and the case in front of them is a fifth. There is no field for that. They pick the closest option, make a note nobody will read, and after two months they stop taking the work.

## Why Nobody Has Built This
The interfaces were adapted from generic annotation platforms built for high-volume, low-skill labelling, and the assumptions came with them. Piece rates are operationally simple and make cost predictable. Difficulty is not measured, so it cannot be priced. Attrition is invisible because raters drift away rather than resigning, and the firm sees a recruitment cost rather than a retention failure. And the buyer never meets the rater, so the experience never reaches anyone who could change it.

## What to Build
Treat the expert as the scarce asset. Price by measured difficulty rather than by item count, using time distributions from prior items of the same type, so a twenty-minute case pays like one — which is the central fix, is straightforwardly computable, and directly addresses why people leave. Build a flag-and-escalate channel as a first-class action, which the fix note develops. Design the interface for a professional rather than for an annotator: full case context, references to hand, the ability to say the answer depends and state on what, and a place for the reasoning they will inevitably want to give. Capture that reasoning and use it, since it is the most valuable output of the whole exercise and is currently discarded — it is the raw material for better rubrics and for the grading criteria asset. Route items by sub-specialty, because a generalist rating a sub-specialist case is a quality problem the firm currently absorbs silently. Report back to the rater what their input changed, which is the single most common request from people doing this work and costs almost nothing to provide. Measure and publish retention and time-to-attrition per cohort, since a pool being spent down is the business's real risk and nobody tracks it. And schedule around a practising professional's life, because the alternative is losing the people who are actually practising, who are the ones whose judgement is worth having.

## Target Customer
Evaluation firms staffing expert rating, the practising specialists doing it, and the customers whose domain evaluations depend on this supply.

## Impact If Built
The supply of practising specialists is the binding constraint on the whole domain evaluation business and is being spent down invisibly. Pricing by measured difficulty addresses the main reason people leave, and capturing their reasoning turns discarded output into the rubric asset the category needs.
