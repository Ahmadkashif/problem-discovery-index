# The Work-Card AD and SDR Checker

**Niche:** [[niches/aircraft-mro-shops/ad-work-card-compliance/profile|AD & Work-Card Compliance Checking]]
**Industry:** [[industries/aircraft-mro-shops|Aircraft MRO & FBO Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The rules for checking a work package against airworthiness directives and the fleet's failure history are public, the aircraft's records and work cards sit with the shop and its customer, and no product does the check.
**Tags:** #large-language-models #transformers #bert #evaluation-metrics #compliance #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to prove every work card cites the current AD revision and an approved method of compliance for that serial number, and whoever has the lowest missed-applicability rate takes the account.

## The Problem
Before an annual inspection, a phase inspection or a C-check is signed, an inspector checks that the package covers every applicable AD at the current revision by an approved method, and that recurring intervals are right. They work from a printed due list and the AD texts, by eye, for hours. Errors (a superseded revision, a serial range misread, an AMOC not on file) make the aircraft unairworthy and the signature a violation.

## Why Nobody Has Built This
Tracking vendors sell the due list and stop there; reading free-text work cards against AD paragraphs was not feasible before language models. Applicability often turns on facts buried in the aircraft's records (an embodied service bulletin, an installed part dash number), which no single system holds. Shops have accepted the manual check as part of the inspector's job.

## What to Build
An agent that ingests the work package and the aircraft's configuration and AD status, pulls ADs from the FAA's Dynamic Regulatory System and the Federal Register, and turns each AD's applicability, compliance and interval paragraphs into checkable rules. It then reports per AD (applies, doesn't, can't determine without a named fact) and per card (current revision, approved method, interval correct), with the AD paragraph quoted. It attaches the SDRs filed on each card's part numbers, from the FAA's yearly files, so the mechanic sees what failed on the fleet before. It runs as a pre-signature check and keeps an audit trail. A first version can be demonstrated on public ADs and a synthetic aircraft and package before any shop shares configuration records. For business and general aviation work, SDRs add little (~93% of 2025 reports came from air carriers), so the AD side carries the product.

## Target Customer
Chief inspectors and directors of maintenance at Part 145 stations and FBO shops; IAs signing general aviation annuals; airline engineering departments checking outsourced packages. Vendors building this now include Zymbly (YC W26, hiring a forward deployed engineer in San Francisco or London) and Fleetcraft (hiring a founding engineer in London only).

## Impact If Built
Turning a 2–4 hour AD reconciliation per package into a 20-minute review of flagged items saves ~150–400 inspector hours a year at ~100 packages (estimate). Catching one missed recurring AD before sign-off avoids a finding that can ground an aircraft and put a certificate at risk.
