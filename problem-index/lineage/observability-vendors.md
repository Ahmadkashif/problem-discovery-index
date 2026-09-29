# Lineage: Observability Vendors

**Industry:** [[industries/observability-vendors|Observability Vendors]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** the Dapper trace — a tree of spans, each carrying a trace id, span id and parent id, propagated through RPC libraries across every service a single request touches; described in Google Technical Report dapper-2010-1
**Builder:** Google
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A slow request had no address.

The Dapper paper opens with web search. A front end sends a query to "many hundreds of query servers," each searching its own slice of the index, and to further subsystems for ads, spelling, images, video and news. "Thousands of machines and many different services might be needed to process one universal search query."

When that query was slow, an engineer "looking only at the overall latency may know there is a problem, but may not be able to guess which service is at fault, nor why." The engineer may not know which services are even in use, since they change "from week to week"; each is "built and maintained by a different team"; and shared machines mean the slowness may belong to someone else's workload.

**Logs and metrics were per machine and per service. The question was per request.** Nothing joined them.

## What Got Built

An identifier that travels with the request.

Dapper models each request as a **trace**: a tree of **spans**, one per unit of work such as an RPC. Every span carries a span id and its parent's id; every span in one trace shares a **trace id**. The ids travel with each outgoing call, so the pieces recorded on different machines can be reassembled into one tree afterwards, showing where the time went.

Two decisions made it deployable across Google. First, instrumentation was confined to "a rather small number of common libraries" — threading, control flow and RPC — so even web search "could be traced without additional annotations." Second, **sampling**: the first production version traced about one request in every 1,024, because tracing everything visibly slowed latency-sensitive services.

The report, *Dapper, a Large-Scale Distributed Systems Tracing Infrastructure*, by Benjamin H. Sigelman, Luiz André Barroso, Mike Burrows and five co-authors, is dated **April 2010** and describes more than two years of production use.

## Who Built It, And Why Them

Google — because it hit the problem earliest at the scale where no human could hold the call graph, and because it owned the one lever that made a fix cheap.

The lever was homogeneity. The paper is explicit that transparency "is easier to achieve since our deployment environment is blessed with a certain degree of homogeneity": nearly every service used the same RPC and threading libraries. Instrument those, and every service is traced without its team doing anything. A company with a dozen RPC stacks could not have done it in a few libraries; Google could.

It also had the motive. Web search users "are sensitive to delays," and a tail-latency regression in any one of hundreds of backends shows up directly in the product.

Google published the design; it did not release the code. **Then the inheritors.** Twitter open-sourced **Zipkin**, modelled on Dapper, in June 2012. The trace-id-and-parent-id shape became the W3C **Trace Context** `traceparent` header — `version-traceid-parentid-flags` — a W3C Recommendation from **6 February 2020**.

## What It Cost

**Sampling means the trace you need was usually not kept.** One in 1,024 is fine for seeing typical behaviour in a high-volume service. It is poor for the rare slow request at three in the morning, and the paper concedes low-traffic workloads "may miss important events at such low sampling rates."

The library trick also exported badly. Outside Google's homogeneous stack, the "few common libraries" became many languages, frameworks and proxies, each needing its own instrumentation, and the trace is only as complete as its least-instrumented hop. And a trace shows *where* time went, not *why*: it narrows the search without supplying the cause.

## What You Still Touch

The `traceparent` header on your service's requests, and the span waterfall in your observability vendor's UI, are Dapper's tree. The gaps you hit mid-incident — a missing span, a sampled-out request — are its trade-offs.

- [[problems/observability-vendors/high-impact|🔴 Causal Diagnosis During an Incident]] — a trace locates; it does not explain
- [[problems/observability-vendors/worker-life-1|🟢 The On-Call Engineer at Three in the Morning]]
- [[niches/observability-vendors/incident-diagnosis/profile|Incident Diagnosis]]
- [[niches/observability-vendors/instrumentation-coverage/profile|Instrumentation Coverage]] — the least-instrumented hop

**Sources:** Sigelman, Barroso, Burrows, Stephenson, Plakal, Beaver, Jaspan and Shanbhag, *Dapper, a Large-Scale Distributed Systems Tracing Infrastructure*, Google Technical Report dapper-2010-1, April 2010 (read in full text: universal-search example and all quotations, span/trace-id model, 1/1024 sampling, "over two years" in production, homogeneity quotation, low-traffic caveat); Twitter Engineering blog, "Distributed Systems Tracing with Zipkin" (2012) and secondary histories for the June 2012 open-sourcing; W3C, *Trace Context* Recommendation (initial Recommendation 6 February 2020; `traceparent` format); this vault's `history/observability-vendors.md` (cited as vault material, not independent corroboration). ⚠️ **Not established:** the exact year Dapper was first built — "over two years" of use before April 2010 implies about 2008, but the paper gives no start date. The names of the engineers who first proposed it internally were not found beyond the paper's author list. Zipkin's exact month rests on secondary sources; the Twitter post itself was not opened.
