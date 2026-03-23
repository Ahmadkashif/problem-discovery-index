# CBA-to-Benefits Configuration Engine

**Niche:** [[niches/insurance-tpa/municipal-benefits/profile|Municipal & Public Entity Benefits]]
**Industry:** [[industries/insurance-tpa|Insurance TPA]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product exists that can parse collective bargaining agreements and automatically generate benefit plan configurations for each bargaining unit, job classification, and seniority tier.
**Tags:** #llm #named-entity-recognition #nlp #automation #compliance

## The Problem
A single municipal entity may have 5-12 bargaining units (police, fire, public works, clerical, management, etc.), each with a different CBA specifying different health benefit provisions. The TPA must configure separate plan designs for each unit — different deductibles, different copays, different dependent eligibility rules, different retiree benefits. When CBAs are renegotiated (every 2-4 years), all configurations must be updated. This is done manually by reading the CBA document and translating provisions into system configurations, a process that takes 20-40 hours per bargaining unit.

## Why Nobody Has Built This
CBAs are written in legal language with cross-references to prior agreements, side letters, and arbitration decisions. The benefit provisions are embedded within labor relations language (grievance procedures, seniority rules, management rights) and must be extracted contextually. The market is fragmented — each municipality is a small client, so no single vendor has enough volume to justify building specialized tooling.

## What to Build
An NLP pipeline that ingests CBA documents (PDFs, often scanned), extracts benefit-related provisions (health, dental, vision, life, disability), structures them by bargaining unit and job classification, and outputs a configuration file compatible with major adjudication platforms. Includes a diff view showing changes between old and new CBA versions to streamline reconfiguration during contract renegotiations.

## Target Customer
TPAs specializing in public entity benefits, managing 20-100 municipal clients with 100-500 bargaining units total.

## Impact If Built
Reduces CBA-to-configuration time by 70% (from 30 hours to 9 hours per bargaining unit). For a TPA managing 200 bargaining units, saves 4,200 hours annually in configuration labor — approximately $250K in analyst time.
