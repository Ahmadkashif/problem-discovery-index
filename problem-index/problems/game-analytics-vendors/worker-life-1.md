# The Analyst Asked Why Retention Fell, Again

**Industry:** [[game-analytics-vendors|Game Analytics Vendors]]
**Type:** Worker Life Changing
**One-liner:** Every week a metric moves, the analyst is asked why by Thursday, and the answer is assembled from partial data by forming hypotheses and checking whether the numbers contradict them.
**Tags:** #change-point-detection #causal-inference #time-series-forecasting #large-language-models #confidence-intervals #evaluation-metrics #worker-facing #data-integration

## The Problem
A game data analyst's week is dominated by the same recurring request. A metric moved; leadership wants an explanation; the deadline is the next review. The analyst segments the movement by every dimension available, checks the build release calendar, asks the live operations team what changed, asks user acquisition about the source mix, and assembles a story that is usually directionally right and rarely provable.

Half the causes are outside the analytics system, so the work is partly investigative — messaging people in other teams to find out what shipped. The other half is the confounding: several things changed at once and the data cannot separate them.

Alongside sits the ad-hoc queue. Every team wants a number: how many players reached this stage, what is the conversion on this offer, how does this cohort compare. Each is a small query and together they consume the week, which is why the analytical work that would actually change decisions — economy health, the shape of the progression curve, whether the acquisition strategy makes sense — never starts.

And the dashboards are a maintenance obligation. Each one built for a request becomes something the analyst supports indefinitely, breaks when instrumentation drifts, and gets cited by someone in a meeting without the caveats.

## Why It Matters to the Worker
The analyst is asked for certainty about a system that does not provide it, weekly, and the honest answer — several things changed and we cannot separate them — is not an acceptable answer in a leadership review. So analysts produce plausible narratives and carry the private knowledge that the attribution was not established.

The work is also almost entirely reactive. The role is sold as informing decisions, and the week is consumed by explaining the past and answering lookups, which means the person hired for analytical judgement is functioning as a query service.

And the credibility is fragile. A number that is later contradicted, or a dashboard that turns out to have been broken, damages trust disproportionately — and instrumentation drift means both happen regularly through no fault of the analyst.

## What a Solution Looks Like
Decompose automatically. Cohort mix, acquisition source, version distribution, platform mix, content state and seasonality are computable, and a standing decomposition of any metric movement into those components — with an honest unexplained residual — answers most of the weekly question before anyone asks it.

Compare to the market. Whether comparable games moved the same way that week is the first thing an analyst wants and the thing they cannot get, and it resolves the majority of movements into known market events.

Bring the causes into one place. Build releases, configuration changes and acquisition mix, integrated and timestamped alongside the metrics, removes the investigative half of the work entirely.

Let people answer their own lookups. Most ad-hoc requests are queries someone could run given a usable interface and the definitional caveats attached automatically — which removes the single largest interruption load and the source of numbers being quoted without context.

And monitor the dashboards. Instrumentation drift affecting a dashboard should be an alert to the analyst on the day, not a credibility event in a meeting three weeks later.

## Impact If Solved
This role exists to improve decisions and is consumed by explaining the past with partial data and answering lookups. Automatic decomposition, a market comparison and integrated cause data would answer most of the recurring question before it is asked, and self-service lookups would return the week to the analysis that actually changes what a studio does.
