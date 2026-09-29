# Deciding the Economics With No Feedback

**Niche:** [[niches/recommerce-platforms/the-intake-processor/profile|The Intake Processor]]
**Industry:** [[industries/recommerce-platforms|Recommerce Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Intake processors inspect, grade, photograph and list hundreds of items a shift against a quota, making judgements that determine the platform's economics with no feedback on whether they got them right.
**Tags:** #worker-facing #evaluation-metrics #confidence-intervals #gradient-boosting #cnns #automation #descriptive-statistics #tacit-knowledge-ml
**Contested on:** Every serious competitor in this niche is fighting to give the person making the platform's most economically consequential judgements the support and the feedback to make them well — and whoever does that takes the quality, because the whole model's economics are decided at that station.

## The Problem
A processor handles four hundred items in a shift. For each one they judge condition, choose a category, enter attributes, take photographs and confirm a price. Every one of those decisions has a measurable consequence — a sale, a return, a markdown, a disposal — that occurs weeks later in a different system and never returns to them. After two years they have made hundreds of thousands of consequential judgements and have received feedback on almost none of them, so their calibration has drifted in whatever direction their intuition took it, and the platform has no idea in which direction.

## Why Nobody Has Built This
Intake is designed as a throughput operation and feedback loops are not part of warehouse process design. The outcome data is in commerce systems and the processor works in a warehouse system, and the join was never made. Individual feedback risks being read as performance management, which has prevented it being built at all. And the quota leaves no time in the shift for anything that is not processing.

## What to Build
Close the loop and support the judgement. Show each processor their own outcome statistics regularly — how their graded items sold relative to prediction, their return rate by grade, their listing quality against comparable items — which is a data join, takes minutes a week to consume, and is the single change most likely to improve calibration across the whole operation. Frame it as calibration rather than performance, because the loop that is resisted is worth nothing. Provide decision support at the station: the predicted price, the comparable items, the attributes extracted automatically from the photographs, the defects the vision system has flagged, so the processor's minute goes to judgement rather than to data entry. Capture their observations in structured form rather than compressing them into a grade, since the detail is valuable downstream and they are already making it. Let them flag an item as uncertain and route it rather than forcing a call, since an item they are unsure about is exactly the one worth a second look and the quota currently forbids that. Recognise expertise, since processors develop real category knowledge and the operation treats them as interchangeable. Design the pacing around item difficulty, which the fix note develops. And measure the operation on realised outcome rather than on items per hour, because that is the metric that produces the behaviour.

## Target Customer
Operations leadership, the processors, and the pricing and quality functions downstream of their decisions.

## Impact If Built
Hundreds of thousands of consequential judgements with no feedback means calibration drifts in an unknown direction. The outcome join takes minutes a week to consume and is the change most likely to improve quality across the whole operation, provided it is framed as calibration rather than as performance.
