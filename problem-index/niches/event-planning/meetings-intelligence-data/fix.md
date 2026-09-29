# Researcher Judgment About What a Signal Means Is Recorded as a Record

**Niche:** [[niches/event-planning/meetings-intelligence-data/profile|Meetings & Events Intelligence Data]]
**Industry:** [[industries/event-planning|Event Planning]]
**Type:** Fix (Pain Point)
**One-liner:** A researcher decides that a reader board entry represents a two-hundred-person annual conference rather than a departmental offsite, and the database stores the conclusion without the evidence or the confidence.
**Tags:** #tacit-knowledge-ml #bert #transformers #word-embeddings #evaluation-metrics #confidence-intervals #descriptive-statistics #k-means-clustering #worker-facing #data-integration

## The Problem
Collection is inference. A researcher sees a fragment — a board entry, a room block signal, a contact's remark — and infers the organization, the event type, the size, and the recurrence pattern. Those inferences populate the fields subscribers act on. The evidence behind each one and the researcher's confidence in it are not retained. So the database presents a firmly sourced record and a thin inference identically; consistency between researchers is unmeasurable; a subscriber challenging a record gets no explanation; and a departing researcher takes with them the local knowledge that made their market's records good — which property staff talk, which board formats mean what, which recurring entries are the same event under a changed name.

## Why It's Still Broken
Researchers are measured on records collected, which rewards throughput and treats capturing evidence as overhead. The collection system was designed to store the resulting record because that is what the product ships. And the interpretive skill is regarded as the researcher's craft, with the usual consequence — it stays personal, and its variance is invisible until someone leaves and a market's data quality drops.

## What a Fix Looks Like
Evidence and confidence captured alongside each record at the moment of collection, at negligible cost: the signal observed, the source type, the inferences made, and how confident the researcher is in each field. Once records carry that, the database can express what it actually knows — a size figure sourced from a contract is different from one inferred from a room block, and subscribers should see which. Consistency between researchers becomes measurable, and systematic differences become a training input rather than an invisible quality gradient. Recurring inference patterns — this board format at this property always means that event type — become candidates for encoding, so knowledge that is currently local becomes institutional. And where a record is later confirmed or contradicted, the original evidence makes it possible to learn which signals were reliable, which is the only route to improving collection rather than merely expanding it.

## Who Feels the Pain
Researchers whose market knowledge leaves with them; the research director with no instrument to measure consistency across markets; hotel sales teams acting on records whose reliability they cannot assess; and the product, whose accuracy reputation is set by its weakest inferences.

## Impact If Fixed
Turns collection craft into institutional capital in a business where human inference is the entire production process. It also makes coverage measurement and entity resolution tractable — both need to know how firmly each record is established before they can say anything useful.
