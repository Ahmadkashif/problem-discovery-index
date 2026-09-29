# Nobody Measures Who Carries the Rota

**Niche:** [[niches/observability-vendors/on-call-engineer/profile|The On-Call Engineer]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Page load across a rota is wildly uneven and entirely recorded, and no organisation computes it until somebody resigns and explains why.
**Tags:** #descriptive-statistics #hypothesis-testing #confidence-intervals #evaluation-metrics #survival-analysis #worker-facing #quick-win #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to make on-call sustainable — fewer pages, better ones, fairly distributed, with the context attached — and whoever does that takes the engineering organisation, because on-call burden is a leading cause of the attrition that leadership actually feels.

## The Problem
A rota of eight people looks fair: one week each, in rotation. In practice one person's weeks coincide with a monthly batch process that pages reliably, another covers a service that is currently unstable, and a third is the informal escalation for a system only they understand and is therefore contacted whether or not they are on call. Over a year the distribution of disturbed nights across those eight people differs by a factor of several. The paging platform has every page with its timestamp and recipient. Nobody has run the query, and the first time anyone does is after a resignation.

## Why It's Still Broken
The rota looks fair by construction, and calendar fairness is what gets designed, so nobody suspects the outcome differs. Page records live in the paging platform and are reported per incident and per service rather than per person over time. Engineers under-report the burden, partly because complaining about on-call is culturally loaded and partly because each individual night feels survivable. And the informal escalation — being contacted because you are the one who knows — is invisible to the paging platform entirely.

## What a Fix Looks Like
Compute the distribution and manage it. Pages per person per period, weighted by time of day and by whether they were sleep-disrupting, which is the headline number and is a query over the paging platform's own records. Time spent, including the recovery that follows a disturbed night rather than only the incident duration, since the cost is much larger than the minutes logged. Repeat pages by service and by cause, which identifies the handful of underlying problems generating most of the load and is the fastest route to reducing it — usually a small number of services account for a large majority of pages. Informal escalations, captured from the incident channels rather than from the paging platform, since being the person everyone contacts is a real and invisible load. Trend per person, so a rising burden is visible before it becomes a resignation. And publish it to the team and to their managers, because a distribution nobody can see cannot be rebalanced, and the imbalance is almost always larger than anybody expects.

## Who Feels the Pain
The people carrying a disproportionate share of nights; teams that lose the person who knew the most; and engineering leaders who learn the distribution during an exit conversation.

## Impact If Fixed
The paging records contain everything needed and the query takes an afternoon, and the result is reliably more skewed than the rota's design implies. The repeat-page analysis identifies the small number of services generating most of the load, which is the fastest available reduction.
