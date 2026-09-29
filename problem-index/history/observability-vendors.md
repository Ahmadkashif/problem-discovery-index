# History: Observability Vendors

**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Primary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Secondary Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**Origin Parent:** Native birth — no origin parent. See below.
**Episode Tier:** 1
**Transferable Pattern:** A billing model that charges for the volume of a signal will always fight the customer's actual goal, which is to need less of that signal — and a vendor umbrella term can merge three separately-evolved tools into one category before anyone checks whether the merge was technical or commercial.

> **Origin Parent — there genuinely is none.** This category was not a client of an incumbent industry the way retail banking fed payment processors or telecom fed CRM. Log search, metrics monitoring and distributed tracing each grew directly out of running distributed software systems at internet scale, starting from the mid-2000s. It is a Wave-6/Wave-7 native birth, and this file names that rather than reaching for a parent that isn't there.

## Before the Dashboard

Before there was a category called observability, there was a server room and a person who knew it. An engineer who had built a system also knew, informally, what its normal behaviour looked like, and diagnosed a problem by knowing where to look — a specific log file, a specific process. This did not scale past the point where one person could hold the whole system in their head, and the internet-scale distributed systems built through the 2000s passed that point quickly: a single user request touching dozens of services, on machines nobody individually understands end to end.

**Splunk, founded in October 2003**, was the first real commercial answer, and it answered a narrower question than "observability" eventually claimed to: how do you search and index the log files distributed systems already produce. Threshold-based infrastructure monitoring (Nagios and its descendants) answered a different, narrower question again: is this specific number outside this specific range. Neither tool spoke to the other, because neither vendor was trying to build the same thing.

## The Origin Event — a word arrives decades after the tools it now describes

**"Observability" is a real, dated term — just not a software one.** Rudolf E. Kálmán introduced it in control theory between 1960 and 1963, to describe whether a system's internal state can be fully inferred from its external outputs. Software engineering borrowed the word much later and applied it to telemetry — metrics, logs, traces, profiling — as evidence of internal system state.

The specific packaging that dominates vendor marketing today, "the three pillars of observability" (metrics, logs, traces), traces to Cindy Sridharan's 2018 O'Reilly book *Distributed Systems Observability*. By that point, the tools it describes were ten to fifteen years old: Splunk (2003) for logs, New Relic (founded 2008) for application performance metrics, Datadog (founded 2010 by Olivier Pomel and Alexis Lê-Quôc) for unified infrastructure metrics and dashboards, and distributed tracing emerging separately out of Google's internal Dapper system and Twitter's open-sourced Zipkin in the early 2010s. **The category name arrived after the category already existed as three unrelated products solving three unrelated problems.** This file's honest origin event is therefore not a founding moment but a naming moment — and the naming is contested.

## What Became Cheap

**Storing and querying an ever-growing volume of telemetry from systems too large for one person to observe directly.** This is [[series/eras/wave-07-big-data|Wave 7]]'s mechanism arriving a layer up: once "the cost of keeping everything" fell for data generally, it fell specifically for the exhaust a running distributed system produces about itself — every log line, every metric point, every trace span — and [[series/eras/wave-06-cloud-saas|Wave 6]]'s compute-as-a-meter made running that collection pipeline itself a subscription rather than a capital project. Splunk could sell log search as a product because indexing text at scale had become commercially viable; Datadog could sell infrastructure metrics as a dashboard because ingesting and graphing them no longer required a company to run its own time-series database cluster. What stayed expensive — and is the subject of the next two sections — is not the collecting. It is deciding, after the fact, which of it was ever worth collecting.

## The Contest — Is This One Category or Three?

Charity Majors and colleagues, in *Observability Engineering* (O'Reilly, 2022), argue directly against the three-pillars framing that Sridharan's book popularised: they hold that the real requirements are high cardinality, high dimensionality and explorability — the ability to ask a question about system state that nobody anticipated when the instrumentation was written — and that metrics and pre-aggregated logs structurally cannot provide this, because "adding a new metric is impossible without shipping new code." Honeycomb, the company Majors co-founded in 2016, was built specifically on wide structured events as an alternative to the three-pillars model, not an implementation of it.

This is a genuine, live disagreement inside the industry about what the product even is, not a settled technical consensus wearing a marketing label. It matters practically: a vendor selling "observability" as metrics-plus-logs-plus-traces is selling three separately-billed collection pipelines bolted together, while a vendor selling wide-event tracing is making a specific bet that the three-pillars split was the wrong cut in the first place. An FDE evaluating this space should treat "we offer full observability" as a claim to be unpacked, not a category to be taken at face value.

## The Trade-Off

Every major vendor in this category bills, in some form, by the volume of telemetry ingested, retained, or queried — per-host, per-GB, per custom metric, per unique label combination. This creates a straightforward misalignment: the vendor's revenue grows with the customer logging more, while the customer's actual operational goal, once past a certain maturity, is to log more *precisely* — fewer signals, chosen for what they answer, not accumulated because storage got cheap. This vault's own hub note for this industry states the consequence directly: "customers cannot tell which telemetry is earning its cost," and the category's own worker-life note observes that a support engineer's job is now largely about a single label "about to multiply a metric by ten thousand" before the bill reflects it.

There is a well-documented public genre of companies writing up how they cut a large observability bill by switching vendors or re-architecting instrumentation — "why is our Datadog bill so high" is a recognisable blog-post category across engineering teams — but I could not verify a specific, individually-sourced case with an audited before-and-after figure in this session, and the vault's discipline is not to borrow a number from a genre. Treat the pattern as real and widely discussed, and any specific dollar figure attached to it elsewhere as unverified until it is checked.

## The Binding Constraint

The actual physical limit underneath every observability pricing model is **cardinality** — the number of unique combinations a label or tag can produce. A metric tagged by customer ID, container ID, or request ID can silently multiply the number of distinct time series a system must store and query by orders of magnitude, and this is a property of the data, not a decision any vendor's pricing team makes. No amount of clever billing design moves this constraint; every pricing model in the category is, underneath its marketing, a tax on cardinality, whether it is named that way or not.

## The Graveyard — Consolidation, Not Collapse

Nobody in this category has gone bankrupt the way Wirecard did, or been broken up in litigation the way an earlier wave's incumbents were. The closest this file has to a graveyard is **Cisco's acquisition of Splunk**, announced 21 September 2023 and closed 18 March 2024 for **$28 billion** — the largest deal in Cisco's history, and the end of the category's oldest independent vendor as an independent company. This is closer to CRM's Siebel-into-Oracle pattern than to a competitive death: Splunk did not lose a product fight, it was absorbed by a networking incumbent building out a security and observability portfolio. New Relic, Grafana Labs, and Honeycomb remain independent as of this writing. The honest framing is consolidation of the founding generation, not defeat of it.

## What's Still Open

- [[problems/observability-vendors/high-impact|🔴 Causal Diagnosis During an Incident]] — the gap between "shows everything" and "answers something"
- [[niches/observability-vendors/incident-diagnosis/profile|Incident Diagnosis]]
- [[niches/observability-vendors/telemetry-cost-and-value/profile|Telemetry Cost and Value]] — pricing the cardinality tax honestly
- [[niches/observability-vendors/observability-support-cardinality/profile|Observability Support & Cardinality]]
- [[niches/observability-vendors/on-call-engineer/profile|The On-Call Engineer]] — the person the category was built to help

## The Transferable Pattern

> **Check who is paid for the volume of a signal before assuming a complaint about cost is a complaint about the product. And check whether a category's name describes one invention or a marketing merger of several — because the pricing, the roadmap, and the honest evaluation criteria are different for each of the parts.**

**Sources:** Wikipedia, *Splunk*, *Datadog*, *Observability*, *Observability (software)*; Cindy Sridharan, *Distributed Systems Observability* (O'Reilly, 2018); Charity Majors, Liz Fong-Jones, George Miranda, *Observability Engineering* (O'Reilly, 2022); Cisco press release, Splunk acquisition (21 Sept 2023, closed 18 March 2024); this vault's `industries/observability-vendors.md`.
