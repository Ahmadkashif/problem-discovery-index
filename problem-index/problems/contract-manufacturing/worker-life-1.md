# SPC Alarm Triage and Root Cause Suggestion

**Industry:** [[contract-manufacturing|Contract Manufacturing]]
**Type:** Worker Life
**One-liner:** Process engineers responding to SPC out-of-control alarms need rapid triage — which alarms require immediate process intervention, which can wait for end-of-shift review, and what the most likely root cause is — rather than individually investigating every alarm as it fires during high-volume production.
**Tags:** #gradient-boosting #multiclass-classification #tabular-ml #automation #worker-facing

## The Problem

Statistical process control (SPC) systems on a production line generate dozens of alarms per shift — Western Electric rule violations, trend signals, and control limit breaches. The process engineer on shift is responsible for investigating each alarm and determining whether to stop production, adjust a parameter, or continue monitoring. During a busy shift, alarm volume creates an impossible cognitive load: the engineer either investigates every alarm (taking them off the floor during the most critical periods) or triages informally by feel.

Two failure modes result. Under-response: a process drift that's generating a trend alarm is ignored until it crosses a control limit and generates significant scrap. Over-response: an alarm caused by a known measurement artifact (a specific gauge that drifts at the start of each shift) triggers an unnecessary process investigation and production stop.

## The Solution

An alarm triage model that classifies each SPC alarm by urgency (stop-now / investigate-within-30-minutes / monitor) and suggests the 2-3 most probable root causes based on which parameters are alarming simultaneously, the time pattern of the alarm, the recent maintenance history of the machine, and the historical root cause distribution for similar alarm patterns on this machine. The process engineer receives a triage dashboard showing alarms ranked by urgency with root cause hypotheses, enabling structured exception management rather than reactive investigation.

## Impact

Reduces average alarm investigation time from 15-20 minutes to 5-minute confirmation/dismissal for correctly triaged alarms. Prevents the most costly failure mode: slow process drift that generates multiple trend alarms before crossing a control limit and producing a large scrap lot. Particularly valuable for engineers managing multiple machines or product lines simultaneously.
