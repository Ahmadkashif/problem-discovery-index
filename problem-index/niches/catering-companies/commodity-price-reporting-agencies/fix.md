# Reporter Contact Networks Are Personal and Undocumented

**Niche:** [[niches/catering-companies/commodity-price-reporting-agencies/profile|Food Commodity Price Reporting Agencies]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Fix (Pain Point)
**One-liner:** The agency's ability to price a market is the accumulated trust of a reporter's personal contacts, held in their own phone, and it leaves with them.
**Tags:** #graph-neural-networks #graph-theory #word-embeddings #bert #descriptive-statistics #evaluation-metrics #tacit-knowledge-ml #data-integration #worker-facing #workflow-orchestration

## The Problem
Price discovery in these markets is a relationship business. A reporter who has covered protein for fifteen years is called back because the market trusts them, knows which of their sources are candid and which shade the truth, and knows who actually trades the grades that matter. None of that is institutional. Contacts live in personal phones and inboxes; the assessment of each source's reliability lives in the reporter's head. When a reporter leaves — and they are recruited by competitors precisely for this — the agency loses coverage quality in a market immediately and cannot say by how much until subscribers complain. Onboarding a replacement means rebuilding a network from scratch over a year or more, during which the published assessments in that market are quietly weaker than the ones the subscriber is paying for.

## Why It's Still Broken
The confidentiality of sources is a genuine and load-bearing constraint: contacts speak on the understanding that their identity and their information stay with the reporter, and any system that appears to centralize that risks the relationship the whole business depends on. Reporters also have a straightforward personal interest in their network remaining personal, since it is their market value. And the traditional structure of these agencies treats the reporter as the product, so there has never been an organizational owner for coverage as an institutional asset rather than a personal one.

## What a Fix Looks Like
Coverage documented as a structural property without exposing source identity. What the agency needs to know is not who the contacts are but what the coverage looks like: how many independent sources contribute to each assessment, what segments of the market they represent — producer, trader, buyer, region, grade — how recently each has contributed, and how their information has historically compared to what the market subsequently confirmed. All of that can be maintained under pseudonymous source identifiers held by the reporter, so the institution sees the shape of the network and never the names. That immediately answers questions nobody can answer today: which assessments rest on too few or too correlated sources, which markets are one departure away from losing coverage, and where source diversity has quietly eroded. Reliability scoring becomes evidence-based rather than remembered, since a source's historical accuracy can be measured against subsequent confirmed trade. And a new reporter inherits a documented coverage map with introduction paths rather than an empty contact list.

## Who Feels the Pain
The editor who discovers a coverage gap when a reporter resigns; new reporters spending a year rebuilding what the agency already had; subscribers receiving assessments whose sourcing depth they cannot see and would pay to know; and the agency itself, whose franchise in a market can be transferred to a competitor by hiring one person.

## Impact If Fixed
Converts the single largest concentration risk in the business into a managed one. It also improves the product directly, because source diversity and recency are measurable inputs to assessment quality that nobody currently measures, and thin or correlated sourcing is exactly where published prices go wrong.
