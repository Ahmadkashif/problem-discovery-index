# EDI Platforms Taught to Read SPA Agreements

**Niche:** [[niches/electrical-distributors/spa-ship-and-debit-claims/profile|Manufacturer SPAs & Ship-and-Debit Claims]]
**Industry:** [[industries/electrical-distributors|Electrical Distributors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The distributor's EDI provider already carries every 844 and 849; it doesn't know what the agreement behind them says.
**Tags:** #large-language-models #transformers #k-nearest-neighbors #data-integration #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to turn every job-specific SPA the distributor quoted into a paid ship-and-debit credit — the 844 claim accepted on the manufacturer's 849 — before the agreement or claim window closes, and whoever gets the most SPA dollars paid on first submission takes the account.

## The Problem
Claims flow over EDI, but the agreements behind them arrive as PDFs, portal screens and emails in each manufacturer's format, and are keyed into the ERP by hand. The EDI layer can't check a claim against terms it has never seen.

## What Already Exists
EDI translators and value-added networks, IDEA's EDI services for the electrical channel, manufacturer portals, and ERP contract-pricing tables.

## The Customization Gap
Document extraction of SPA terms into a structured agreement record (job, contractor, ship-to, items, quantities, price, expiry); part-number aliasing through IDEA data; pre-submission checks of each 844 line against the agreement; quantity-cap tracking across branches; and 849 reason-code handling mapped to actions.

## Target Customer
Distributors whose EDI provider or IDEA connection already carries ship-and-debit and who want terms checked in the same flow.

## Impact If Solved
Agreements are loaded once and checked automatically. Removing manual keying of ~100–500 SPAs a month at a mid-size distributor (estimate) saves ~1–2 analyst FTEs (estimate) and most keying-error rejections, without a new platform.
