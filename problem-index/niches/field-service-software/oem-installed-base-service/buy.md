# Condition Monitoring Stacks Wired to the Service Platform

**Niche:** [[niches/field-service-software/oem-installed-base-service/profile|OEM Service on Its Own Installed Base]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Condition monitoring, vibration analysis and industrial anomaly detection are mature purchasable capabilities, and most manufacturers have bought one and connected it to a dashboard instead of to the dispatch system.
**Tags:** #time-series-forecasting #change-point-detection #autoencoders #evaluation-metrics #confidence-intervals #data-integration #workflow-orchestration #automation
**Contested on:** Every serious competitor in OEM service software is fighting to convert telemetry and engineering knowledge from the manufacturer's own installed base into a dispatched action before the customer notices a fault — and whoever converts most reliably takes the account.

## The Problem
A manufacturer has spent several years and a large budget on a connected-product programme. Machines are connected, telemetry flows, dashboards exist, and reliability engineers look at them. The service organisation's work order queue is populated by customer phone calls, exactly as it was before. The programme's return on investment review is uncomfortable, and the conclusion drawn is usually that predictive maintenance does not work, when what was actually built was a monitoring system with no path into an action.

## What Already Exists
Industrial condition monitoring is a mature market: vibration analysis, thermal and acoustic monitoring, and the associated signal processing have decades of practice. Cloud IoT platforms handle ingestion, storage and alerting. Anomaly detection on multivariate time series is available off the shelf. Service platforms expose APIs for work order creation, parts reservation and scheduling. Every component is purchasable and, in most manufacturers, already purchased.

## The Customization Gap
The adaptation is the path from a signal to a scheduled visit with a part. It requires: (1) an event model that carries a component and a horizon rather than an anomaly score, because a work order needs to say what to bring; (2) automatic work order generation with parts reservation and a proposed scheduling window, so the output lands in the queue the dispatcher actually works rather than in a dashboard; (3) closed-loop labelling — the technician's confirmed finding written back against the prediction, which is the step that turns a monitoring deployment into a learning system and is almost universally missing; (4) suppression and de-duplication tuned to service economics rather than to engineering curiosity, since an alert that costs a truck roll has a very different threshold than one that costs a glance at a screen; and (5) customer-facing framing, because a proactive visit needs to be explained to the person paying for the contract and the explanation is part of the product.

## Target Customer
Manufacturers with existing connected-product deployments that have not affected service operations, and the service platform vendors sitting between them and the dispatch queue.

## Impact If Solved
Most manufacturers in this position have already paid for the hard parts and are missing the connection, which makes this among the highest-return adaptations available in the vault. The closed-loop labelling is the piece with compounding value: without it the deployment stays static forever, and with it the prediction quality improves with every visit.
