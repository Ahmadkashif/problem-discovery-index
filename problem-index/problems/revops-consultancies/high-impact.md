# The Forecast Is Produced Weekly and Scored Never

**Industry:** [[revops-consultancies|RevOps Consultancies]]
**Type:** High Impact
**One-liner:** Every revenue organisation forecasts weekly, almost none retain the forecasts, and the discipline that exists to make revenue predictable cannot say whether its own predictions are getting better.
**Tags:** #time-series-forecasting #bayesian-inference #confidence-intervals #gradient-boosting #hypothesis-testing #evaluation-metrics #probability-distributions #revenue-impact

## The Problem
A revenue forecast is assembled every week. Representatives update their opportunities, managers apply judgement, a roll-up is produced, and a number goes to the leadership meeting. The following week the process repeats and the previous forecast is overwritten — the CRM holds current state, the spreadsheet is updated in place, and the slide is superseded.

So the historical series — what was forecast for this quarter on each of the thirteen weeks leading into it, and what actually closed — does not exist at most organisations. Without it nothing can be evaluated. Whether the sales leader's judgement adjustment improves on the raw roll-up, whether the new stage definitions helped, whether the forecast category probabilities bear any relationship to observed close rates, whether one region's manager is systematically optimistic — every one of those is answerable from a retained series and unanswerable without one.

The consequences are specific. Probability weights attached to pipeline stages are typically set once, by convention, and are frequently wrong by large margins for a given business; nobody checks because checking requires the history. Judgement adjustments are applied every week by people whose historical accuracy is unknown, including to themselves. And when a quarter misses, the post-mortem is conducted from memory and produces a narrative rather than a diagnosis.

For the consultancy the problem is compounded. Their central recommendation — adopt this forecast methodology, restructure these stages, instrument the funnel this way — cannot be validated at the client because the client has no baseline to compare against, and cannot be validated across clients because no such record is retained anywhere. A firm that has rebuilt sixty forecasting processes has sixty anecdotes.

## Why It's Unsolved
The retention failure is a systems artefact rather than a decision. CRM objects hold current state by design; stage history is captured in field history tracking that is often disabled or truncated for volume reasons; the forecast itself frequently lives in a spreadsheet that is edited rather than versioned. Nobody chose to discard the series, and nobody has been accountable for keeping it.

There is also a real and uncomfortable incentive. A scored forecast makes individual accuracy visible — which managers are optimistic, which representatives commit deals that do not close, whether the leader's adjustment adds value or subtracts it. That is exactly the transparency that makes a forecasting process politically difficult to instrument, and it is usually the reason the project stalls after the technical work is done.

The data quality underneath is genuinely poor and the poorness is structural. Stages are advanced because a manager asked, close dates are pushed a fortnight at a time because moving them further invites a conversation, and opportunities are created to satisfy activity targets. A forecast model trained on that data learns the reporting behaviour as much as the sales process, and the distortion is rarely quantified because quantifying it means telling a sales organisation that its data describes its incentives.

And the outcome horizon is long. A forecasting change takes several quarters to evaluate, which exceeds the length of most consulting engagements and most executives' patience.

## What a Solution Looks Like
Retain the series first. Snapshotting the full pipeline weekly — every opportunity with its stage, amount, close date, owner and forecast category, plus the roll-up and any judgement adjustments — is a week of engineering and is the precondition for everything else. It should be the first deliverable of every engagement in this discipline and it almost never is.

Score everything against it. Forecast error by week-out, by segment, by manager, by forecast category, with intervals. Calibration of stage probabilities against observed close rates from this business rather than convention. The value added or destroyed by each layer of judgement adjustment, which is measurable and almost never measured.

Forecast a distribution. A single number invites false precision and a point miss; a distribution with a stated interval reflects what is actually knowable eleven weeks out and changes how leadership reacts to normal variance.

Quantify the data distortion rather than working around it. Stage-skipping, close date pushing, and the timing of opportunity creation relative to period boundaries are all measurable, and reporting them as data quality metrics — attached to the forecast's confidence rather than to individuals — makes the distortion an input to the model instead of a hidden bias in it.

And for the consultancy, retain it across clients. Sixty engagements with retained pipeline series is the only corpus that could establish which forecasting practices actually improve accuracy, and it is the firm's route from opinion to evidence.

## Impact If Solved
Forecast accuracy governs hiring, spending and guidance in every revenue organisation, and it is currently improved by methodology arguments that nobody can settle. Retaining the series makes every subsequent claim testable, calibrated stage probabilities alone typically move accuracy more than any process redesign, and measuring judgement adjustment answers a question leadership teams have argued about for as long as forecasts have existed. For the consultancy it is the difference between selling a methodology and selling a measured improvement.
