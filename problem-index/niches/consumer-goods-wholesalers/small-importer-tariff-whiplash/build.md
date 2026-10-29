# A Duty Position for Importers Without a Trade Department

**Niche:** [[niches/consumer-goods-wholesalers/small-importer-tariff-whiplash/profile|Small Importer-Wholesalers Under Tariff Whiplash]]
**Industry:** [[industries/consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Give the owner of a small importer one ledger of every entry's duty by authority, its refund or protest status and its deadlines, built from the broker's files.
**Tags:** #large-language-models #transformers #feature-engineering #compliance #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to keep a small importer's duty bill as low as the law allows through each tariff change, and whoever leaves it paying the lowest net duty per dollar of imports after refunds takes the account.

## The Problem
The owner knows the total duty paid last year, roughly. She does not know which entries carried IEEPA duty, which are liquidated, which refunds have arrived, which protest windows are open, or whether her broker classified her items consistently.

## Why Nobody Has Built This
Brokers sell entry filing, not a client-side position, and trade software is priced for importers with compliance teams.

## What to Build
A ledger that ingests the broker's entry summaries and ACE reports, splits duty by authority (IEEPA, Section 122, Section 301, Section 232, ordinary duty) per entry and SKU, tracks liquidation dates, protest windows and refund status, flags classification inconsistencies across the importer's own items with an LLM check, and estimates drawback eligibility on exported goods.

## Target Customer
Owners of importer-wholesalers bringing in a few hundred to a few thousand entries a year.

## Impact If Built
For an importer that paid ~$500K of IEEPA duty (estimate), making sure every eligible entry is claimed before deadlines can be worth ~$50–100K that would otherwise be lost (estimate).
