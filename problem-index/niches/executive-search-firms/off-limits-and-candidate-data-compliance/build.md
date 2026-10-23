# A Corporate-Family Off-Limits Resolver

**Niche:** [[niches/executive-search-firms/off-limits-and-candidate-data-compliance/profile|Off-Limits, Conflicts & Candidate-Data Compliance]]
**Industry:** [[industries/executive-search-firms|Executive Search Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Whether a candidate is off-limits depends on which corporate family their employer belongs to today and which terms that family's client agreement set, and nobody resolves both automatically.
**Tags:** #graph-theory #k-nearest-neighbors #word-embeddings #evaluation-metrics #compliance #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to clear every name on a longlist against every client's off-limits terms and every candidate's privacy obligations before the first approach, and whoever keeps the most names callable without a single client breach takes the account.

## The Problem
A candidate works for a subsidiary acquired last year by a client's parent, or for a portfolio company of a sponsor the firm serves, or for a joint venture half-owned by a client. The CRM flags the client's name, not its family. Researchers either miss the conflict or, unsure, strike the candidate.

## Why Nobody Has Built This
Search CRMs model clients as companies, not families with dated terms, and the large firms' conflict checks are run by risk teams with spreadsheets. Corporate hierarchy data is sold for sales and compliance, not for people-level checks.

## What to Build
A resolver that maps each candidate's free-text employer to an entity in a corporate graph (parents, subsidiaries, sponsor portfolios, joint ventures, recent acquisitions), stores every client's off-limits terms as rules (scope, level, geography, start and end dates, sourcing versus recruiting), and returns a callable/not-callable decision with the rule and the path through the graph that triggered it. It re-runs on every new mandate and every lapse date, and logs the check for the client.

## Target Customer
General counsel and risk leads at global firms; chief operating officers at mid-sized firms with multi-office client books.

## Impact If Built
Fewer accidental approaches to clients' executives, fewer available candidates struck out of caution, and an audit trail clients can be shown.
