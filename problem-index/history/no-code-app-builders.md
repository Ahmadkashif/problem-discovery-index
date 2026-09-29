# History: No-Code App Builders

**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Primary Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**Secondary Wave:** [[series/eras/wave-03-pc-spreadsheet|3 — The PC & the Spreadsheet]]
**Origin Parent:** Native birth — no origin parent. See below.
**Episode Tier:** 1
**Transferable Pattern:** A tool that lets anyone build software inherits the maintenance burden of software without inheriting the discipline that made software maintainable — and it competes against an incumbent, the spreadsheet, that already won this exact fight once by being infrastructure under audited process rather than a new thing to learn.

> **Origin Parent — there genuinely is none.** No pre-computer industry fed this one. Its real ancestor is a failed product inside computing's own history, not a parent business this vault tracks elsewhere — which is a different shape of absence than telecom or process manufacturing's, and worth stating precisely rather than papering over.

## Before the Builder

For a small business with a process to track — job status, inventory, approvals — there were exactly two ways to get software: hire or contract a programmer, which cost more than the process was worth, or build it in a spreadsheet, which cost nothing and required no permission. [[series/eras/wave-03-pc-spreadsheet|Wave 3]] made the second option universal, and it stayed the default for four decades for reasons that have not gone away: zero training cost, no procurement decision, and the tool doubling as the audited financial infrastructure of the business, not a side project living outside it.

One serious attempt existed to give ordinary people something better than a spreadsheet for building actual interactive tools. **Apple shipped HyperCard on 11 August 1987**, created by Bill Atkinson, under the slogan "programming for the rest of us." It let a non-programmer build a stack of linked cards with buttons, logic and simple scripting — recognisably the same pitch this industry makes today. It did not survive: Apple moved it to its Claris subsidiary and began charging for the full version after bundling it free, generating real user backlash; Steve Jobs killed a planned HyperCard 3.0 in 2000; and the World Wide Web offered the same basic idea — linked, buildable documents with logic — without HyperCard's single-machine limitation. Retrospectives and some vendors like to draw a straight line from HyperCard to modern no-code platforms. The documented connection is conceptual, not technical: the pitch repeats, the codebase and the architecture do not. Treat any claim of unbroken lineage here as marketing, not history.

## The Origin Event

There is no single one; there is a three-year cluster, all downstream of Wave 6's cloud economics making it viable to host somebody else's business logic cheaply. **Zapier started as a side project in 2011** in Columbia, Missouri (Wade Foster, Bryan Helmig, Mike Knoop), built to eliminate the repetitive integration work its founders kept redoing for clients, and launched publicly in 2012. **Airtable was founded in 2012** (Howie Liu, Andrew Ofstad, Emmett Nicholas), pitched explicitly as a spreadsheet with a database's discipline underneath it — typed fields, linked records — rather than a wholly new paradigm. **Bubble was founded the same year**, targeting a harder problem: full web applications, not workflow glue or structured data, built visually rather than coded. **Forrester coined the specific term "low-code" on 9 June 2014**; the category's own commercial roots trace to around 2011, before the word existed to describe it.

A later split matters for evaluating this space honestly: **Retool, founded in 2017**, targets professional engineers who want to assemble internal tools quickly, not the citizen developer this vault's other niches describe. "No-code" is not one audience. It is at least two — people avoiding code, and people who can code choosing to avoid writing the boring 90% of it — sold through overlapping marketing.

## What Became Cheap

**Turning a business process into running software without hiring an engineer, provisioning a server, or waiting for an IT backlog to clear.** This is Wave 6's compute-cost collapse carried one level further up the stack: not cheaper hosting for professionally written software, but cheaper *authorship* of software by people who were never going to write code at all.

## The Contest — Against the Spreadsheet, and Mostly Losing

The honest fight here is not between no-code vendors. It is between the entire category and the incumbent it was built to replace, and `series/eras/wave-03-pc-spreadsheet.md`'s own account of why the spreadsheet wins generalises directly: it is infrastructure under audited process, it owns the ad hoc, and it costs nothing to learn. A no-code tool asks a builder to learn a new logic model — tables, triggers, workflows, a platform's own conventions — in exchange for capability the spreadsheet cannot cleanly provide: multi-user structured workflows, an interface a non-owner can safely use, an external-facing form. That trade is real and no-code wins it in a genuine, growing slice of cases. But it does not win the rest, and this vault's own niche list for the industry names the unresolved boundary directly: `spreadsheet-process-migration` exists as its own niche precisely because the handoff from spreadsheet to app is not a clean migration most businesses complete — they run both, forever, moving only the piece the spreadsheet visibly could not do.

The Panko finding this vault has already logged elsewhere sharpens the comparison rather than settling it in either tool's favour: roughly 94% of *audited operational* spreadsheets contain errors, at a field cell-error rate near 5.2%. No-code apps do not eliminate this failure mode; they relocate it from a formula a human can at least open and read to a visual workflow a non-builder frequently cannot debug at all.

## The Trade-Off

No-code trades governance for speed, explicitly and by design. A citizen developer gets something running today, without a procurement cycle or an IT review — at the direct cost of the practices that make software survivable past its builder's tenure: documentation, error handling, a named owner, a test of what happens when an upstream field changes shape. This is not a side effect of the category; it is close to the whole value proposition, and the bill comes due later, to a different person than the one who built the thing.

## What's Still Open

- [[problems/no-code-app-builders/high-impact|🔴 The Maintenance Cliff]] — the crossing from convenience to dependency, currently invisible
- [[niches/no-code-app-builders/load-bearing-app-detection/profile|Load-Bearing App Detection]]
- [[niches/no-code-app-builders/spreadsheet-process-migration/profile|Spreadsheet Process Migration]] — the boundary this file names as still open, not closed
- [[niches/no-code-app-builders/shadow-app-inventory/profile|Shadow App Inventory]]
- [[niches/no-code-app-builders/inherited-app-administration/profile|Inherited App Administration]] — the bill, and who it lands on

## The Transferable Pattern

> **The constraint was never the building. It was always what happens after the builder moves on — and a category that removes the cost of creating software without touching the cost of maintaining it has not solved the problem, it has deferred it to whoever inherits the app.**

An FDE evaluating this space should ask what an incumbent tool already does well enough before assuming the gap is technical. Here, twice over, it is not: once against HyperCard's failed attempt at the same pitch, and once, continuously, against the spreadsheet the industry's own hub note admits it has not displaced.

**Sources:** Wikipedia, *HyperCard*, *Airtable*, *Zapier*, *Low-code development platform*; Forrester Research, first documented use of "low-code" (9 June 2014); this vault's `series/eras/wave-03-pc-spreadsheet.md` and `industries/no-code-app-builders.md`. Retool's 2017 founding and Bubble's 2012 founding are widely reported in industry coverage; I could not independently re-verify either against a primary source in this session and note that here rather than presenting them with false precision.
