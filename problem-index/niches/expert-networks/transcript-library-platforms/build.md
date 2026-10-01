# A Hundred Thousand First-Hand Claims, None of Them Checked

**Niche:** [[niches/expert-networks/transcript-library-platforms/profile|Transcript Library Platforms]]
**Industry:** [[industries/expert-networks|Expert Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A transcript library holds timestamped first-hand statements about products, pricing, share and timing, most of which later became publicly checkable, and the library sells the corpus on size because it has never measured its accuracy.
**Tags:** #large-language-models #transformers #bayesian-inference #causal-inference #evaluation-metrics #confidence-intervals #revenue-impact

## The Problem
A former product director says in March that a competitor's new platform will slip to the following year. A distributor says pricing is holding through the summer. A customer says they are moving half their spend to a challenger. Each statement is dated, attributed to a described source, and sits in the library. Within months, many of them can be checked against earnings calls, filings, launches and press.

Subscribers implicitly weight these statements by intuition about the source. The library presents every transcript with equal standing and competes with other libraries on how many it has.

## Why Nobody Has Built This
Measuring accuracy risks finding that a meaningful share of expert claims are wrong, which is commercially uncomfortable for a product sold as primary insight. Per-expert scores would also strain the relationship with experts and raise fairness questions. And claim resolution looked like an analyst task, too expensive to run at corpus scale, until recent language models.

## What to Build
Extract checkable claims from the back catalogue with their date, subject and source characteristics. Resolve them against later public text — earnings transcripts, filings, product announcements — with human adjudication on a sample to measure resolution accuracy. Estimate reliability by source type: role, seniority, years since departure, relationship to the company, topic. Report aggregates, not individual expert scores. Surface reliability context beside search results ("claims from former employees more than three years out resolved correctly about half as often on this topic"). Feed the reliability estimates back into commissioning, preferring source types that have proved accurate on the topic.

## Target Customer
Chief Content Officer or Head of Research at a transcript library platform. The argument is that corpus size is converging across competitors and corpus quality is the next axis of competition, with the evidence already sitting in the platform's own archive.

## Impact If Built
A library that can say which kinds of expert statements prove right moves from selling volume to selling calibrated evidence — the property research teams actually need and currently supply from instinct — and it is the first time anyone in the industry would have measured its core product.
