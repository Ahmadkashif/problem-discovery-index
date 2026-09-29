# Instrumentation Nobody Owns

**Industry:** [[game-analytics-vendors|Game Analytics Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every analysis depends on events the game team chose to send, the schema was designed early by whoever was free, and it drifts silently as the game changes.
**Tags:** #change-point-detection #bert #word-embeddings #time-series-forecasting #gradient-boosting #evaluation-metrics #data-integration #workflow-orchestration

## The Problem
A game's analytics is bounded by its instrumentation. Events are defined during development, usually early, frequently by an engineer implementing a ticket rather than by anyone who will analyse the result. The taxonomy is a list in a document that ages badly.

Then the game changes. A feature is reworked and its events stop firing or start meaning something different. A new system ships with events invented by a different engineer in a different naming convention. A parameter that was always populated becomes optional. None of this produces an error, because the pipeline accepts what it receives.

The failure surfaces as a metric that looks wrong, investigated as a business problem, traced eventually to instrumentation. Analysts in this field describe a substantial share of their time spent establishing whether a number is real, and the answer is often that a change three weeks ago altered what an event means.

Coverage gaps are the quieter version. A question arises — why are players stopping at this point — and the events needed to answer it were never sent, so the answer requires shipping instrumentation and waiting weeks for data. That delay is the reason many questions simply go unanswered.

## What Already Exists
Analytics SDKs provide event APIs and some validation. Schema and tracking plan tooling exists in the general product analytics world — Segment Protocols, Avo — and is rarely adopted in games. Larger studios maintain internal event taxonomies with review processes of varying rigour. Some vendors offer schema validation and violation reporting. Data quality monitoring is a mature practice in general data engineering and is applied unevenly here.

## The Customisation Gap
Validation checks conformance to a declared schema and the failure is that the declaration and reality diverge continuously. What is needed is detection that reality changed — per-event arrival rates and parameter distributions forecast against their own history, with departures correlated against build releases so the cause is named rather than hunted.

The games-specific gap is that game builds are versioned and long-lived in a way that web analytics never deals with. Multiple client versions are live simultaneously for weeks or months, each sending a different event schema, and the analysis has to reconcile them. Web analytics tooling assumes everyone is on the current version; game telemetry never is, and the vendor's tooling largely pretends otherwise.

Coverage assessment is the third piece and the most useful. Given the game's structure — its progression, its economy, its features — which events are missing to answer the questions a studio in this genre typically asks is knowable from the vendor's cross-studio corpus, and telling a studio during development rather than after launch is the difference between an answerable question and a three-week wait.

And dependency visibility belongs where the change happens. An engineer renaming an event should see which dashboards, alerts and models depend on it, in the pull request rather than in a wiki.

## Impact If Solved
Instrumentation quality bounds everything downstream, and it degrades silently because nobody owns it and no system notices. Arrival and distribution monitoring with build correlation catches drift the day it ships; multi-version reconciliation addresses a structural feature of games that general tooling ignores; and cross-studio coverage assessment during development prevents the unanswerable question, which is the most expensive instrumentation failure of all.
