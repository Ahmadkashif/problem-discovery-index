# Support During Service Failure

**Industry:** [[restaurant-tech-platforms|Restaurant Tech Platforms]]
**Type:** Worker Life Changing
**One-liner:** Support representatives stop taking calls from a manager standing in front of a stalled queue at seven on a Friday, because the failure was detected and worked before service started.
**Tags:** #change-point-detection #time-series-forecasting #gradient-boosting #evaluation-metrics #confidence-intervals #automation #workflow-orchestration #worker-facing

## The Problem
When restaurant technology fails, it fails during service. That is not coincidence — service is when the system is loaded, when the network is saturated, when every terminal and printer and card reader is in use at once. A POS that has been quietly degrading all week surfaces at seven on Friday with a queue at the counter and food going cold on the pass.

The manager calls support. They are on a phone in a loud kitchen, with customers waiting, staff looking at them, and orders that cannot be taken. They are not able to work through diagnostics calmly, and they should not have to. The support representative's first job is de-escalation, and only then troubleshooting, on a stack that includes hardware they cannot see, a network they do not control, an internet connection that may be the actual cause, and three integrations owned by other companies.

The representative usually resolves it. They do so under conditions where every minute is money and the customer knows it.

## Why It Matters to the Worker
This is among the most stressful support queues in software. The caller is not annoyed, they are in an active operational emergency, and the representative absorbs that directly for a full shift. Support in this category runs evenings and weekends by necessity, which selects for a workforce that is already carrying the least convenient hours.

What makes it demoralising rather than merely hard is the predictability. The kitchen printer that failed tonight had been dropping jobs intermittently for a week. The terminal that will not take cards had been logging read errors. The tablet that dropped off is the one on the far wall with weak signal that has dropped off every busy night for a month. The representative can see the history the moment they open the account, and it was visible to nobody until the emergency.

They are, in effect, staffing a monitoring gap in real time, with an audience.

## What a Solution Looks Like
Detection before service rather than during it. Terminal error rates, printer job failures, card reader retries, network latency and tablet connectivity are all telemetry the platform receives and treats as logs. Watching them for degradation trends — per device, against that location's own baseline — surfaces the failing printer on Tuesday, when the restaurant has time and the fix is a shipment rather than an emergency.

Pre-service readiness checks are the other half: an automated verification an hour before the dinner rush that every device is online, every integration is authenticated, every card reader is responding and the network is healthy, with anything failing escalated to a proactive outbound contact rather than an inbound one.

For the calls that still come, the representative should open the account with the device's history already surfaced and the likely cause ranked, rather than starting from a blank screen at the worst possible moment.

## Impact If Solved
Failures during service are the events that end vendor relationships, and they are also the shifts that make support in this category difficult to staff. Moving detection ahead of the rush converts the industry's most stressful support interaction into a routine maintenance ticket, and removes the moment where the restaurant concludes the technology cannot be relied on.
