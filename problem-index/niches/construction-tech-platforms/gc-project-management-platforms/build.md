# Slip Forecasting from the Signals Already Captured

**Niche:** [[niches/construction-tech-platforms/gc-project-management-platforms/profile|General Contractor Project Management]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Platforms hold RFI latency, submittal turnaround, crew counts and change order flow for hundreds of thousands of projects and use them to draw a status view, when the same data is the leading indicator of every slip the industry treats as unforeseeable.
**Tags:** #survival-analysis #gradient-boosting #time-series-forecasting #graph-neural-networks #confidence-intervals #evaluation-metrics #causal-inference #revenue-impact
**Contested on:** Every serious competitor in GC project management is fighting to tell a project team which activities will slip weeks before the schedule shows it — and whoever forecasts a slip earliest, with evidence a superintendent believes, takes the account.

## The Problem
An activity three weeks out depends on a submittal that has been with the architect for nineteen days against a fourteen-day contractual turnaround, an RFI on an adjacent detail that has been open for eleven days, and a subcontractor whose manpower has been under its committed count for two weeks. Every one of those facts is in the platform. None of them appears on the schedule, which still shows the activity starting on time because nobody has updated it. The slip becomes visible when the crew arrives and cannot work — at which point the mitigation options are expensive and the argument about whose fault it is has already started.

## Why Nobody Has Built This
Construction schedules are contractual instruments as well as plans, which makes a forecast politically loaded in a way a forecast in another industry is not: a platform that predicts a slip is generating evidence in a future delay claim, and vendors have been acutely aware that their customers are parties to those claims. The modelling is also genuinely hard — activities are linked in a network so a slip propagates, the relationships between activities differ per project, and the outcome data is confounded by the mitigations that a warned team undertakes. And the industry's tolerance for a wrong forecast is low, because a superintendent who is told twice that something will slip and sees it not slip will never look at the feature again.

## What to Build
A forecasting layer over the platform's own cross-project corpus that predicts, per activity, the probability and expected magnitude of a start or finish slip, propagated through the schedule network so that the output is a completion distribution rather than a date. Features are the ones the field already trusts: open RFI age weighted by which activities depend on the answer, submittal turnaround against contractual windows by reviewer, manpower against commitment, change order flow in the area, weather and trade sequencing. Every forecast is delivered with its drivers named — "this activity is at risk because submittal 214 is nine days past its window" — because an unexplained warning is ignored and an explained one becomes a phone call. Calibration is published inside the product: for every past forecast band, what actually happened, which is the only way this feature survives contact with a superintendent.

## Target Customer
General contractor platform vendors with a large cross-project corpus, and directly the mid-to-large general contractors and construction managers who carry schedule risk.

## Impact If Built
Two to four weeks of warning on a slip is the difference between resequencing and paying for acceleration, and on a commercial project the cost difference is measured in six figures per event. For the vendor, a calibrated forecast built on a cross-project corpus is the first capability in the category that a competitor cannot replicate by copying a workflow — which is the position every platform in this market has been trying to reach by adding modules.
