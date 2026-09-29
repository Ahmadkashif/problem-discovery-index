# Evidence Acquisition and Timeline Construction

**Industry:** [[digital-forensics-firms|Digital Forensics Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The first week of an incident is spent collecting evidence from systems nobody has an inventory of and assembling a timeline from a dozen incompatible sources by hand.
**Tags:** #change-point-detection #graph-neural-networks #gradient-boosting #bert #time-series-forecasting #evaluation-metrics #automation #data-integration

## The Problem
Response begins with acquisition. Which systems are in scope, how to reach them, how to collect without destroying evidence, and how to do it at the speed the incident demands. In practice this means deploying monitoring into an environment mid-incident, imaging systems, pulling logs from wherever they are, and requesting cloud audit exports — while the client's own team is simultaneously trying to contain and restore.

The inventory problem bites immediately. Organisations rarely know their own estate precisely, so responders spend the first days establishing what exists before they can establish what happened. Systems that matter are discovered late.

Timeline construction is the analytical core and is largely manual. Events come from endpoint telemetry, operating system artefacts, application logs, authentication systems, network records and cloud audit trails, each with its own format, its own clock and its own idea of what constitutes an event. Normalising, correlating and ordering them into a defensible sequence is skilled work performed under time pressure, and it is where most examiner hours go.

Clock skew, timezone handling and gaps introduce errors that matter. A timeline is used to establish sequence — what preceded what — and a misaligned source can reverse a causal reading, which in a forensic context is a serious error.

## What Already Exists
Endpoint platforms provide rich telemetry when deployed and are the single biggest improvement of the last decade. Forensic suites handle acquisition, parsing and artefact extraction competently. Timeline tools — Plaso and its ecosystem, commercial equivalents — normalise many sources and produce large event sets requiring curation. SIEM platforms aggregate where the client had one. Cloud providers export audit logs in their own formats. Triage collection scripts are standard practice for rapid acquisition.

## The Customisation Gap
Timeline tools produce volume and the work is reduction. A parsed timeline contains millions of events and the investigation concerns dozens, and identifying the ones that matter is expert judgement applied to an enormous list. Surfacing candidates — events anomalous for this environment, events matching known intrusion patterns, events clustered in time with something suspicious — is a filtering problem the corpus supports and the tooling does not attempt.

Cross-source correlation is the second gap. The same action appears in several sources in different forms, and recognising that a process execution, an authentication event and a network connection are one action is the correlation that builds the narrative. It is done by hand and is mechanically expressible.

Clock reconciliation should be automatic and reported. Skew is detectable by correlating events observable in multiple sources, and the residual uncertainty in ordering should be carried through to the findings rather than assumed away.

And environment baselines make anomaly detection possible. What is normal in this estate — which accounts log in where, which processes run, which connections are ordinary — can be established from the retained data even mid-incident, and without it every unusual-looking event must be checked manually.

## Impact If Solved
Acquisition and timeline construction consume the majority of examiner hours in a response, at the moment when senior expertise is scarcest and the clock is running. Automated correlation, environment-baselined anomaly surfacing and reported clock reconciliation would compress the path from evidence to narrative — which directly shortens the period in which the client does not know their scope and the notification decision cannot be made.
