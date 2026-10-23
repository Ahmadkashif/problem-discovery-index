# Workscope Changes Waiting on Customer Approval by Email

**Niche:** [[niches/aircraft-mro-shops/engine-shop-visits/profile|Engine Shop Visits & Overhaul]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Fix (Pain Point)
**One-liner:** Teardown finds a scrapped blade set, the shop emails a change quote, and the engine sits on a stand for a week while the owner's engineers ask questions the quote didn't answer.
**Tags:** #large-language-models #workflow-orchestration #automation #quick-win #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every engine shop is fighting to release a serviceable engine at the lowest cost per flight hour inside the date it quoted. Cost and date are won by different capabilities, though: the workscope and life-limited-part decisions are won on records and engineering prediction, while the date is won on slot capacity and control of parts and repair vendors. Decomposed into contested sub-niches below.

## The Problem
Most shop visits change after teardown. The shop finds damage beyond repair limits, an LLP closer to its limit than the records suggested, or a module needing more than the initial workscope. Each change goes to the owner as a quote change with photos and a short justification, usually by email to the operator's powerplant engineer or the lessor's technical manager. Questions come back, the shop answers, and approvals arrive in fragments. Work on the affected module stops in the meantime.

## Why It's Still Broken
Change requests are written ad hoc by busy shop engineers, each in their own format, with the evidence the owner needs (measurements against limits, repair options with cost and expected life, the effect on the release date) scattered or missing. The owner's engineers can't decide without it, and nobody tracks how long approvals take.

## What a Fix Looks Like
A standard change package drafted from the teardown findings: the finding with photos and measured values against the manual limit, the options (repair, new part, used serviceable material) with cost, lead time and effect on life and release date, and the shop's recommendation. It goes out through a portal that records questions and approvals per item and shows the shop which approvals are holding up the critical path.

## Who Feels the Pain
Shop engineers writing change requests between teardown and assembly; owners' powerplant engineers approving dozens of items across several shops; planners whose release dates slip on approvals.

## Impact If Fixed
Cutting average approval time per change from ~3–5 days to ~1 day (estimate) could take a week off a visit with several rounds of changes, worth ~$25,000–$50,000 in spare-engine lease cost alone.
