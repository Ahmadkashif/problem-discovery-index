# Analyst Judgment Overrides the Model and Is Recorded as a Number

**Niche:** [[niches/crop-farming/ag-market-intelligence-providers/profile|Agricultural Market Intelligence Providers]]
**Industry:** [[industries/crop-farming|Crop Farming]]
**Type:** Fix (Pain Point)
**One-liner:** What separates the firm's crop estimate from a satellite model is an analyst deciding the model is wrong about a region this year, and the reason for that decision is never written down.
**Tags:** #tacit-knowledge-ml #large-language-models #bert #transformers #gradient-boosting #evaluation-metrics #feature-engineering #descriptive-statistics #data-integration #worker-facing

## The Problem
Crop and price models produce a number; the published estimate is that number after an analyst has adjusted it. The adjustments carry the real expertise — knowing that a region's early planting will not translate into yield because of a subsoil moisture deficit, that a reported condition rating reflects one wet week rather than the season, that a particular state's survey response has historically run optimistic. Those judgments are applied continuously and recorded as adjusted values. The reasoning exists in analyst notes and in memory. So the firm's genuine differentiator is entirely personal: when a senior analyst retires, estimate quality for their region degrades in ways that surface months later, and no new analyst can learn from the accumulated body of past judgment because it is not in a readable form.

## Why It's Still Broken
The publication pipeline stores estimates because estimates are what it publishes, and adjustments happen under a release deadline where any extra keystroke is a real cost paid by the analyst. There is also a longstanding view in market analysis that judgment is craft rather than process — which has protected the status quo more effectively than any technical obstacle and has left the firm's most valuable asset undocumented.

## What a Fix Looks Like
Structured capture of the override as it is made, at negligible cost: the adjustment, a reason from a controlled vocabulary that grows from what analysts actually write rather than being imposed, the evidence consulted, and a free-text field that is parsed rather than merely stored. Once overrides carry reasons, three things become possible. The firm can measure which override types improved accuracy against realized outcomes and which did not, turning craft into evidence — and because this domain resolves cleanly and quickly, that measurement is unusually tractable. Recurring situations become visible, so judgment consistently applied by several analysts can be promoted into the model rather than remaining manual forever. And a subscriber asking why an estimate moved receives the actual reasoning, which is a materially better answer than the one available now.

## Who Feels the Pain
Analysts whose accumulated regional expertise leaves with them; the research director who cannot measure or transfer the thing that makes the product worth subscribing to; client-facing staff explaining estimate movements they cannot reconstruct; and subscribers making marketing decisions on numbers whose analytical basis is undocumented.

## Impact If Fixed
Converts the firm's differentiator from personal expertise into institutional capital. Override reasoning is the most valuable unrecorded dataset in the business — a labelled record of where models are misleading and why, generated free every publication cycle by the people best placed to know — and in a domain that resolves within a season, it can actually be evaluated rather than merely collected.
