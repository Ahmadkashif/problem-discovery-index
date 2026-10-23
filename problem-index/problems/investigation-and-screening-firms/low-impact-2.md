# Enhanced Due Diligence Beyond the Screening Hit

**Industry:** [[investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Watchlist and adverse-media databases tell a compliance team that a counterparty might be a problem; the investigation firm hired to find out still builds each enhanced due diligence report by hand from registries, court files and press archives in the local language.
**Tags:** #large-language-models #transformers #graph-theory #word-embeddings #compliance #workflow-orchestration #data-integration

## The Problem
A manufacturer appointing a distributor in a high-risk market, a private equity firm about to back a founder, a bank onboarding a client whose screening returned a possible match: each asks an investigation firm for an enhanced due diligence report. The analyst confirms the subject's identity, traces company ownership through registries in two or three countries, searches litigation and insolvency records, reads local-language press going back a decade, and sometimes makes discreet source inquiries. The report is tiered by price and depth, due in one to three weeks, and judged by whether it found what a database screen would have missed.

Much of the analyst's time goes to assembly rather than judgement: pulling filings from registries with different formats, transliterating names, deciding whether "Ivanov Holdings" in one registry is the same entity as a similarly named firm in another, and writing the sources up in the firm's house format. Each report starts nearly from scratch even when the firm has looked at the same group before.

## What Already Exists
World-Check, Dow Jones Risk & Compliance and LexisNexis provide sanctions, politically exposed person and adverse-media screening; Moody's Orbis, Sayari and national registries provide ownership data; third-party risk platforms orchestrate questionnaires and screening workflows. These are analysed in the vault under [[niches/customs-brokers/sanctions-screening-data-providers/profile|Sanctions & Restricted Party Screening Data]]. General research tools and translation engines are widely used.

## The Customisation Gap
Screening tools return hits; due diligence firms sell a judgement on what the hits mean. The adaptation needs scoping by risk tier and jurisdiction (which registries, courts and press sources are worth searching for this country and this question), entity resolution across transliterations and registries with no shared identifier, a source-cited draft in which every statement links to a retrieved document, and a confidentiality wall that lets the firm reuse its own method and source maps across engagements without reusing one client's findings for another. Generic tools have no notion of the house standard for what counts as a corroborated red flag.

## Impact If Solved
Cutting assembly time on a standard enhanced due diligence report from ~2–3 analyst days to ~half a day (estimate) would free ~60–75% of analyst time per report for the judgement and source work clients pay for, and shorten delivery from ~2–3 weeks to under a week (estimate), letting firms offer deeper tiers at the prices compliance teams now pay for screening-plus.
