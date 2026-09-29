# Corrosion Growth Rates Assumed, Then Used to Set a Deadline

**Niche:** [[niches/utility-contractors/pipeline-integrity-management/profile|Pipeline Integrity Management & In-Line Inspection]]
**Industry:** [[industries/utility-contractors|Utility Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** Reassessment intervals are computed from a corrosion growth rate an engineer chose, and the choice is recorded as a number in a calculation nobody revisits.
**Tags:** #tacit-knowledge-ml #evaluation-metrics #confidence-intervals #compliance #worker-facing

## The Problem
The output an operator acts on is not really the anomaly list. It is the schedule: which anomalies get dug this year, which can wait, and when the pipeline must be reassessed. That schedule is computed by applying an assumed corrosion growth rate to current anomaly sizes and projecting forward to a threshold.

Growth rate is where the judgment lives. An integrity engineer picks it from a mixture of sources: repeat inspection comparisons where available, industry default values, soil and coating condition, cathodic protection history, and experience with similar pipe. The choice moves the reassessment interval by years and the dig list by hundreds of locations.

It is recorded as a number in a calculation. The reasoning — which comparison runs were trusted, why a conservative default was chosen for one segment and a measured rate for another, what the engineer knew about that right-of-way — is not captured. The report states the assumption; it rarely states the basis, and never states what would change it.

Three things follow. Consistency is unmeasured: two engineers assessing comparable segments may assume materially different rates, and nothing surfaces it. Defensibility is reconstructive: when a regulator asks why this interval, someone re-derives the reasoning. And the judgment is concentrated in senior engineers in an ageing specialty, which means the firm's actual product is a set of careers.

Repeat inspections make this worse by making it answerable. When the same pipe is inspected twice, observed growth is measurable — and the assumed rate used in the earlier assessment is sitting in a file nobody joins to it.

## Why It's Still Broken
Assessments are project deliverables under deadline pressure, and nobody bills for recording rationale. The benefit lands years later, on someone else's engagement.

The calculation template is the substrate, and templates have cells for numbers rather than fields for reasoning.

And there is a genuine regulatory chill. Integrity documentation is examined in enforcement proceedings after incidents. A written record of an engineer weighing a less conservative growth rate is a document nobody wanted to create — which also prevents the firm demonstrating that its assumptions are evidence-based and consistent.

## What a Fix Looks Like
**Capture the assumption as a structured object.** Rate assumed, basis, segments it applies to, comparison runs relied on, and what evidence would revise it. Minutes per segment, inside a workflow that already exists.

**Join assumed rates to observed growth on reinspection.** Every repeat run tests every prior assumption on that pipe. Reporting assumed against observed by soil, coating and protection condition turns convention into measurement, and it needs no new data.

**Build the comparables library.** Engineers reason from similar segments constantly, and a queryable record of what was assumed for what conditions — and how it performed — is useful immediately, which determines whether anyone uses it.

**Report assumption distributions across the practice.** What growth rate do our engineers assume for poorly coated pipe in aggressive soil, and how wide is the spread. That single report tells the firm whether it has a standard.

**Decide the documentation posture with counsel first.** The current default of recording only conclusions is itself an exposure: a firm that cannot demonstrate a consistent, evidence-based method is in a worse position after an incident, not a better one.

## Who Feels the Pain
Senior integrity engineers, who are the bottleneck and the product; junior engineers, who cannot learn assumption-setting from a spreadsheet of numbers; operators, who receive a reassessment interval with no stated basis and cannot distinguish a well-founded assumption from a conservative default; and regulators, who are shown a schedule without the reasoning behind it.

## Impact If Fixed
The reassessment interval is the single most consequential output of pipeline integrity work — it determines when a pipe carrying gas through a populated area is next examined — and the assumption driving it is the least documented part of the analysis. Structuring it makes consistency measurable, makes the method defensible, and turns every repeat inspection into a test of every prior assumption, which is the only way this discipline learns.
