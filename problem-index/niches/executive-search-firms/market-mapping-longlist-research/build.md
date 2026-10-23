# Title Levelling That Reads Scope, Not Words

**Niche:** [[niches/executive-search-firms/market-mapping-longlist-research/profile|Market Mapping & Longlist Research]]
**Industry:** [[industries/executive-search-firms|Executive Search Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A "Vice President" at a bank and a "Vice President" at a large manufacturer are different jobs, and researchers level every title by hand from fragments of evidence.
**Tags:** #bert #word-embeddings #k-nearest-neighbors #graph-theory #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to produce a complete, correctly levelled map of who holds every target role at every target company, and whoever's map is still accurate on the day the partner makes the first call takes the account.

## The Problem
A brief asks for a divisional finance leader running a business of a given size. Across target companies the person is called CFO, finance director, VP finance, head of FP&A or SVP controller, and the same title spans very different scopes. Researchers infer scope from company size, segment reporting, reporting lines in press releases and conference bios, and record the judgement nowhere reusable.

## Why Nobody Has Built This
Job-architecture tools level jobs inside one employer; executive databases record titles as written. The cross-company question, which only search firms ask at scale, has no vendor.

## What to Build
A levelling model trained on the firm's own historical maps, where researchers have already levelled thousands of people: embeddings of title, employer size and structure, segment and reporting-line evidence, with nearest-neighbour retrieval of similar levelled cases and the evidence shown. Org-chart inference from filings and announcements fills reporting lines. Researchers confirm or correct, and every correction trains the next search.

## Target Customer
Global heads of research at large firms, and research outsourcers serving many boutiques.

## Impact If Built
Consistent levelling across researchers and offices, fewer mis-pitched approaches, and a firm-wide map that can be reused because it means the same thing everywhere.
