# XBRL Is Not the Answer, It Is the First Draft

**Niche:** [[niches/financial-data-vendors/standardised-fundamentals/profile|Standardised Fundamentals]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** XBRL parsers and taxonomy mapping tools turn tagged filings into tables; they do not know that this issuer's custom extension means what a standard tag means at its peer.
**Tags:** #word-embeddings #transformers #k-nearest-neighbors #evaluation-metrics #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to standardise a new filing correctly within hours and to show how each derived number was produced — and whoever does that best becomes the source every client's comp table and backtest silently trusts.

## The Problem
Issuers tag their filings with the US GAAP taxonomy and, frequently, with their own extension elements. Tags are chosen by the issuer's filing agent, sometimes wrongly, and the same economic item appears under different tags across issuers and over time.

## What Already Exists
Open-source and commercial XBRL processors (Arelle, filing-agent tooling from Workiva and DFIN), SEC structured data sets, and taxonomy-to-template mapping tables maintained by each vendor.

## The Customization Gap
Mapping extension elements to the vendor's template using label semantics, calculation relationships and the issuer's history; detecting standard tags used incorrectly by a specific issuer; tracking an element's meaning when an issuer silently changes how it uses it; and producing a confidence the collection tool can act on. Each depends on the vendor's own historical mappings, which are the training data.

## Target Customer
Content technology leaders at fundamentals vendors and at smaller as-reported specialists.

## Impact If Solved
Extension mapping is a recurring quarterly cost at every vendor. Learning it from history removes most of it and surfaces the issuers whose tagging cannot be trusted.
