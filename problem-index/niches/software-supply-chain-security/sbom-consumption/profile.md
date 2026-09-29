# SBOM Consumption

**Parent Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Category:** Low Digitized
**Contested on:** Every serious competitor here is fighting to make a software bill of materials answer a question somebody actually has — and whoever does that takes the mandate, because the documents are generated, filed and read by nobody.

## Profile
**Market Size:** ~$310M US attributable to bill-of-materials production, exchange and use
**Share of Parent Industry:** ~10% of category revenue
**Digital Adoption:** Very Low in substance — generation is automated and consumption is absent
**Target Buyer:** Procurement, compliance and security functions receiving them
**Automation Potential:** Very High — the documents are structured and the questions are simple

## What Makes This a Distinct Niche
Bill-of-materials generation is standardised, automated and increasingly mandated, and the documents are produced, filed and never read — because the tooling generates them and nothing consumes them. The asymmetry is stark and unusual: an entire production ecosystem exists, driven by regulation, with no corresponding consumption ecosystem, which means the mandate is satisfied and the purpose is not. The questions the documents exist to answer are simple and are asked constantly: when a new vulnerability is published, which of our vendors' products contain the affected component; which of our own products would we need to notify customers about; what is in this thing we are about to buy. Each is a query over documents an organisation already holds and cannot run, because they arrive as files in a procurement folder with no ingestion, no normalisation and no index.

## Current Tools & Gaps
Generation tooling in every build system, two competing standard formats, exchange by attachment and portal upload, and regulatory requirements driving production. The gaps: there is no consumption side at all in most organisations, so received documents are stored rather than ingested; the two formats and their variations require normalisation nobody performs; component identity across documents is inconsistent, so the same library appears differently in two vendors' documents and cannot be matched; documents are point-in-time and the product changes, so a filed document describes a version no longer deployed; and nobody measures whether any question has ever been answered from one.

## Problems
- [[niches/software-supply-chain-security/sbom-consumption/build|🔨 Build: Generated, Filed, Never Read]]
- [[niches/software-supply-chain-security/sbom-consumption/buy|🛒 Buy: Master Data Management for Component Identity]]
- [[niches/software-supply-chain-security/sbom-consumption/fix|🔧 Fix: A Document Describing a Version Nobody Runs]]
