# The Model That Costs More Than the Team

**Niche:** [[niches/data-platform-integrators/consumption-cost/profile|Consumption Cost Engineering]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Fix (Pain Point)
**One-liner:** One hourly full-refresh model turned out to be a substantial share of the annual platform bill.
**Tags:** #quick-win #optimization-fundamentals #descriptive-statistics #evaluation-metrics #revenue-impact #data-integration #automation #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to make the cost consequences of a transformation layer visible during delivery rather than on a bill — and whoever surfaces that takes the account.

## The Problem
Platform cost is concentrated. A small number of models — typically a full refresh on a large table running far more often than anyone needs — account for a large share of the bill. Nobody knows which ones, because cost is reported by warehouse rather than by model. The client sees a rising bill, applies a general austerity, and the actual cause continues running hourly.

## Why It's Still Broken
Cost is not attributed to models — a bill reported by warehouse cannot identify which of four hundred models is responsible, so the response is a general cost programme rather than a specific fix. Query history and cost data are not joined. Schedules are set once. And nobody owns the bill and the model layer at once.

## What a Fix Looks Like
Attribute the spend to models and look at the top ten. Join query history to cost and rank models by spend, which is the fix and is available on every major platform. Look at the top ten, since the concentration means that is where almost all the recoverable cost is. Check each one's schedule against what its consumers actually need, as over-frequent scheduling is the commonest and cheapest fix. Convert full refreshes to incremental where the data allows, which is usually the single largest saving. Check whether the expensive models are used at all, since the intersection of expensive and unused is the easiest win available. Look at ad hoc query cost by user too, which is often a surprising share. Report cost per model to the people who own them, which changes behaviour without any policy. Set an alert on a model whose cost rises sharply, so regressions are caught. Re-run the ranking quarterly, as the estate and its costs move. And put the cost next to the model in whatever tooling the engineers use.

## Who Feels the Pain
Clients facing a bill nobody can explain; engineers applying general austerity to the wrong things; finance functions questioning the platform's value; and the specific model, still running hourly.

## Impact If Fixed
A bill reported by warehouse cannot identify which of four hundred models is responsible, so the response is a general programme rather than a specific fix. Ranking models by spend surfaces a concentration that is usually startling.
