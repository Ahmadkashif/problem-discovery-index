# Woken at Three by a Number

**Niche:** [[niches/observability-vendors/on-call-engineer/profile|The On-Call Engineer]]
**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The page says a metric crossed a threshold and nothing else, so the engineer starts from zero at the hour they are least capable, and the platform knew the context the whole time.
**Tags:** #gradient-boosting #change-point-detection #graph-theory #descriptive-statistics #evaluation-metrics #confidence-intervals #worker-facing #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to make on-call sustainable — fewer pages, better ones, fairly distributed, with the context attached — and whoever does that takes the engineering organisation, because on-call burden is a leading cause of the attrition that leadership actually feels.

## The Problem
The page at 03:12 says: error rate on the orders service above two percent. The engineer opens a laptop and begins: is anyone actually affected, is this the same as the one three weeks ago, did something deploy, is the upstream provider degraded, does this need me now or could it have waited four hours. Every one of those questions is answerable from data the platform holds, and none is in the page. Twenty minutes later they establish that a dependency was briefly degraded, it has recovered, and nothing needed doing. They do not get back to sleep, and the same alert fires again next month.

## Why Nobody Has Built This
Alerting was designed around conditions rather than around the person receiving them: a threshold is a simple thing to configure and a rich, contextualised page requires joining the dependency graph, the change stream, the customer impact estimate and the incident history — which is the incident diagnosis capability applied at wake-up rather than at investigation. Paging platforms own the delivery and not the content, and observability platforms own the content and not the delivery, so the page is a message passed between two products neither of which is accountable for whether it was useful. And the cost is absorbed by individuals at night, where it is invisible to every metric the organisation reports.

## What to Build
Make the page carry what the engineer needs to decide. Blast radius first — how many users or transactions are affected — because the first question is always who is affected and how many, and a page that says nobody is affected can frequently wait. Whether this has happened before, with what cause and what resolution, since repeat incidents are a large share of pages and the answer is in the incident record. What changed, from the joined change stream, which is the single most valuable field. Two or three ranked hypotheses with their evidence, from the diagnosis capability, which turns twenty minutes of orientation into two. An explicit urgency assessment — does this need action now or at the start of business — since a large share of night pages are for conditions that could have waited and nothing currently makes that call. Then measure the page itself: was it actioned, was it a repeat, did it need to be a page at all, which is the alert quality inventory applied to the human consequence. And route by that assessment, because the fastest way to reduce night pages is to stop sending the ones that did not need to be.

## Target Customer
Engineering leadership responsible for on-call sustainability, site reliability functions, and the incident response and observability vendors on either side of a page neither owns.

## Impact If Built
The context an engineer spends twenty minutes assembling at three in the morning is held by the platform and omitted from the page. Blast radius and an urgency assessment alone would let a meaningful share of night pages become morning tickets.
