# Lineage: RevOps Consultancies

**Industry:** [[industries/revops-consultancies|RevOps Consultancies]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the SiriusDecisions Demand Waterfall — a five-stage lead funnel (inquiry, marketing qualified lead, sales accepted lead, sales qualified lead, closed deal) with a conversion rate measured at each handoff, first launched in 2006
**Builder:** SiriusDecisions
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Marketing and sales could not agree on what a lead was.

Marketing counted names: form fills, event badges, downloads. Sales counted deals. Between them was a handoff nobody had defined, so each side measured itself in its own unit and blamed the other for the gap. Marketing said sales ignored its leads; sales said the leads were junk. Neither claim could be tested, because there was no shared stage at which a lead changed hands, and so no conversion rate for anyone to own.

The cost was budget. A marketing leader could not show which spend produced revenue, and a sales leader could not show whether the problem was volume or follow-up.

## What Got Built

A diagram with names on it.

The original Demand Waterfall has five core stages. In SiriusDecisions' own description: marketing generates **inquiries**; a subset is designated **marketing qualified leads** ready for sales; sales **accepts** them; sales **qualifies** them for readiness to buy; and sales **wins** the deal. MQL, SAL, SQL are handoff points — each one a place where one function signs something over to another and where a conversion rate can be measured.

The model was revised twice. The Rearchitected Demand Waterfall (2012) added an automation qualified lead stage for lead-scoring thresholds and teleprospecting stages for inside qualification teams. The Demand Unit Waterfall (2017) switched the unit from the individual lead to the buying group, because B2B purchases are made by committees.

## Who Built It, And Why Them

SiriusDecisions, a B2B research and advisory firm in Wilton, Connecticut, founded in 2001 by John Neeson and Rich Eldh. Its own blog dates the Waterfall's launch to 2006; Wikipedia says "since 2005". Forrester Research acquired the firm in November 2018.

**Why an advisory firm and not a software vendor.** The Waterfall is a definition, not a product, and its value was being the same definition everywhere. An analyst firm selling research subscriptions to heads of marketing and sales could publish one vocabulary, benchmark conversion rates across clients, and sell the comparison back. A marketing-automation vendor promoting its own stage names would have fragmented the language. SiriusDecisions' clients included Adobe, IBM, GE, HP and Cisco — the companies whose adoption made "MQL" a common noun. Wikipedia credits the model with introducing the terms MQL and SQL; I could not confirm that independently.

## What It Cost

**It made the funnel measurable by making it a set of labels.** Each stage is a status someone sets. An MQL is whatever crosses a scoring threshold; an SAL is whatever sales clicks "accept" on. The conversion rates are only as honest as the people setting the statuses, and both sides have reasons to set them generously.

It also made the lead the unit of account, which the firm itself later abandoned for the buying group — after a decade in which quotas, comp plans and dashboards had been built on counting leads.

## What You Still Touch

A RevOps engagement still starts by redrawing the funnel and agreeing what each stage means. The client's CRM carries stage fields shaped by the Waterfall. The consultancy rebuilds the model at the next client, and there is no scoring of whether the redesign moved conversion.

- [[problems/revops-consultancies/worker-life-1|🟢 The Consultant Rebuilding the Same Funnel Model]]
- [[problems/revops-consultancies/low-impact-1|🟡 CRM Data Quality as a Measured Quantity]] — statuses set by the people measured on them
- [[niches/revops-consultancies/funnel-model-reuse/profile|Funnel Model & Reporting Reuse]]
- [[niches/revops-consultancies/attribution-modelling/profile|Attribution Modelling]]

**Sources:** SiriusDecisions blog, Steve Silver, "The Demand Waterfall®: What Sales Operations Needs to Know" (17 May 2018) — "First launched in 2006"; the rearchitected version 2012; Demand Unit Waterfall 2017; SiriusDecisions blog, Terry Flaherty, "The Demand Waterfall: A Modular System to End Chaos" (1 May 2018) — the five core stages, the automation qualified lead and teleprospecting stages, buying groups; both read via Internet Archive captures of siriusdecisions.com (July 2019). Wikipedia, *SiriusDecisions* (Wilton, Connecticut; founded 2001 by Neeson and Eldh; "since 2005"; MQL/SQL attribution; client list; Forrester acquisition 27 November 2018). ⚠️ **Not established:** the Waterfall's month of launch, its original author inside the firm, and whether "MQL" predates it — WebSearch was unavailable this session (session cap reached), and no pre-2006 source was reachable. The 2005/2006 conflict is left as found; the note follows the firm's own statement.
