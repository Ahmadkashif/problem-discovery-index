# Analyst Overrides Are the Product and Are Recorded as Numbers

**Niche:** [[niches/auto-dealers-independent/vehicle-valuation-guides/profile|Vehicle Valuation Guide Publishers]]
**Industry:** [[industries/auto-dealers-independent|Independent Auto Dealers]]
**Type:** Fix (Pain Point)
**One-liner:** What separates a published guide from a raw transaction average is the analyst's judgment on top, and that judgment is stored as an adjusted value with the reasoning discarded.
**Tags:** #tacit-knowledge-ml #large-language-models #bert #transformers #gradient-boosting #evaluation-metrics #descriptive-statistics #feature-engineering #data-integration #worker-facing

## The Problem
Anyone can average auction results. What clients license is the editorial layer: an experienced analyst recognizing that a spike reflects a fleet dump rather than demand, that a discontinued model's values are about to step down, that a regional divergence is a weather event and not a trend. Those judgments are applied continuously and recorded as adjusted values. The reason is not recorded, or is recorded as a short free-text note nobody can query. The consequence is that the publisher's single genuine differentiator exists only in the heads of the analysts applying it. When a senior analyst retires, their segment's quality degrades in ways that show up months later as complaints. When a client asks why a value moved, the answer is reconstructed from memory. And no new analyst can learn from the accumulated body of past judgment, because it is not in a form that can be read.

## Why It's Still Broken
The publishing pipeline was built to produce values, and a value is what it stores. Overrides happen under a daily or weekly release deadline, where any additional keystroke is a real cost and the analyst is the person paying it — so even where a notes field exists, it is used inconsistently and phrased for the analyst's own recall rather than for retrieval. There is also a longstanding view that editorial judgment is craft rather than process, which makes systematic capture feel like an attempt to codify something that cannot be, and that view has protected the status quo more effectively than any technical obstacle.

## What a Fix Looks Like
Structured capture of the override at the moment it is made, designed to cost the analyst almost nothing: the adjustment, a reason selected from a controlled vocabulary that grows from actual use rather than being imposed up front, the evidence consulted, and a free-text field that is parsed rather than merely stored. Because the vocabulary is derived from what analysts already write, adoption does not depend on retraining anyone. Once overrides carry reasons, three things become possible that are impossible today. The publisher can measure which override types improved accuracy against realized values and which did not, turning craft into evidence. It can detect recurring situations — the same reason applied to structurally similar configurations by different analysts — and surface them as candidates for the model, so judgment consistently applied becomes methodology rather than remaining manual forever. And it can answer a client's question about a value movement with the actual reasoning, which is a materially better answer than the one available now.

## Who Feels the Pain
Analysts whose accumulated expertise leaves with them; the research director who cannot measure or transfer the thing that makes the product worth paying for; client-facing staff explaining value movements they cannot reconstruct; and licensees setting capital against numbers whose editorial basis is undocumented.

## Impact If Fixed
Converts the publisher's core differentiator from personal expertise into institutional capital. Override reasoning is the most valuable unrecorded dataset in the business — it is the labelled record of where raw market data is misleading and why, generated free every day by the people best placed to know. Capturing it makes quality measurable, makes methodology improvable, and makes the product defensible when the client asks the one question that currently has no good answer.
