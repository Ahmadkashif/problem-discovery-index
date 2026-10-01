# Methodology Rulings Made in Email and Forgotten

**Niche:** [[niches/financial-data-vendors/content-operations-research/profile|Fundamentals & Estimates Content Operations]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The content organisation's research output — rulings on how to treat new accounting standards, new KPI types and edge cases — is produced in committee threads and lost, so the same question is re-decided by different people every year.
**Tags:** #large-language-models #word-embeddings #k-nearest-neighbors #tacit-knowledge-ml #evaluation-metrics #workflow-orchestration #compliance
**Contested on:** Every serious competitor's content organisation is fighting to add issuers, fields and history per analyst-hour without losing accuracy — and whoever turns collection judgement into a reusable asset first gets coverage growth that no longer scales with headcount.

## The Problem
Behind the collectors sits a methodology function: when ASC 842 moved leases on balance sheet, when issuers started reporting a new non-GAAP measure, when a sector invented a KPI, someone decided how the template treats it. Those rulings are the research workflow of a data vendor — question raised, precedent searched, memo drafted, committee review, policy update — and they happen in email, chat and slide decks. Collectors receive a summarised rule; the reasoning and the rejected alternatives are not retained in any searchable form. When the question recurs in another region or sector, it is re-researched from scratch, sometimes with a different answer.

## Why Nobody Has Built This
Methodology is a small, senior team that sees itself as editorial rather than as a process. Document management exists but captures files, not decisions. And the cost of inconsistent rulings is diffuse — it shows up as comparability errors clients find later, not as a line item.

## What to Build
A methodology research workspace that treats each ruling as a structured decision: the question, the issuers and filings that raised it, the precedents considered, the options and the reasoning, the final rule and its effective date, and links to every template field affected. Retrieval surfaces prior rulings when a collector escalates a new case, so the question arrives with its own precedent. Drafting assistance assembles the memo from the cited filings and prior rulings. Every subsequent mapping made under a ruling is linked to it, so the ruling's real-world consequences — client tickets, disagreements — feed back to its owner.

## Target Customer
Head of Methodology and Chief Content Officer at fundamentals and estimates vendors.

## Impact If Built
Turns the content organisation's most senior research output into a reusable corpus, removes repeated re-decisions across regions, and gives the policy-version stamps that every collection model needs for clean labels.
