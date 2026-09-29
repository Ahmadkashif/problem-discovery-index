# Forecast Accuracy the Sales Leader Will Actually Use

**Industry:** [[crm-platforms|CRM Platforms]]
**Type:** High Impact
**One-liner:** Forecast from behaviour rather than from self-reported stage — engagement, response latency, buying-committee breadth and deal momentum are unfalsifiable, and the platform already carries all of them.
**Tags:** #gradient-boosting #survival-analysis #logistic-regression #time-series-forecasting #feature-engineering #cross-validation #confidence-intervals #evaluation-metrics #revenue-impact

## The Problem
Every CRM ships a forecast. Almost no sales leader uses it. The universal practice is a call-down: each manager reviews deals with each representative, applies judgement, and produces a number that goes into a spreadsheet, which is then adjusted upward or downward by the leader based on how the last four quarters went.

The reason is that the CRM's forecast is a function of two fields the representative controls and is incentivised to distort. Stage advances when a representative wants it to look advanced. Close date slips a month at a time, forever, because moving it to next quarter is an admission. Probability is a lookup from the stage, so it inherits the distortion.

The platform holds far better inputs and does not use them. How many people at the account have engaged, and whether that number is growing — the strongest single predictor of enterprise deal outcome. How quickly the buyer responds to emails, and whether that latency is increasing. Whether meetings are being scheduled or postponed. Whether the champion has gone quiet. Whether anyone from procurement or legal has appeared. Whether the deal's pattern of activity resembles deals that closed or deals that died.

All of that is behavioural, none of it is self-reported, and all of it flows through the platform's own email and calendar integrations.

## Why It's Unsolved
The category built its data model around what a representative types, and the incentives to type accurately have never existed. Everyone knows this and it has been treated as a training problem — better hygiene, better discipline, mandatory fields — for twenty-five years, rather than as a signal problem to be routed around.

Activity capture is the practical obstacle. Email and calendar integration is available and adoption is inconsistent, partly because representatives resist it and partly because it raises legitimate questions about surveillance that vendors have handled awkwardly.

There is also a hard modelling reality nobody advertises: forecasting is a small-sample problem at the level anyone cares about. A leader wants the quarter's number for a segment with perhaps two hundred deals. Aggregate accuracy across a large customer base is easy and useless; accuracy on this team's quarter is what determines adoption, and it requires honest uncertainty rather than a point number.

And the vendors ceded the territory. Revenue intelligence companies built exactly this on data flowing through the incumbents' own platforms, which suggests the obstacle was organisational rather than technical.

## What a Solution Looks Like
A deal-level model that predicts close and timing from behaviour, treating the representative's stage and date as weak features rather than as the specification. Buying-committee breadth and its trajectory, response latency trends, meeting cadence, champion engagement, competitive mentions, and the deal's similarity to prior won and lost deals in the same segment.

Time to close should be modelled as a survival problem, because the real question is not whether a deal will close but whether it will close in this quarter — and slipping deals, not lost deals, are what break a forecast.

The output has to arrive with an interval and with reasons. A leader will act on "this deal has had no new contact engaged in five weeks and the economic buyer has not attended the last two meetings." They will not act on a score, and one confidently wrong call ends adoption permanently.

## Impact If Solved
Forecast accuracy determines hiring, capacity, inventory and guidance, and it is currently produced by a call-down over data everyone knows is fabricated. Forecasting from behaviour is the one capability that would make the system of record into a system of insight, and the incumbents have the data flowing through them already.
