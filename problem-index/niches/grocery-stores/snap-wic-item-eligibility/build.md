# An Eligibility Engine That Cites the Clause

**Niche:** [[niches/grocery-stores/snap-wic-item-eligibility/profile|SNAP & WIC Item-Eligibility Compliance]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Chains need each item's SNAP and WIC status per state with the rule clause behind it, scheduled by effective date and reversible on a court order, and no tool provides it for their own item file.
**Tags:** #large-language-models #bert #transformers #decision-trees #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to keep every register's SNAP and WIC eligibility flags right across states, waivers and court orders, and whoever has the fewest wrongly blocked or wrongly allowed benefit scans per million takes the account.

## The Problem
A waiver says SNAP may not buy "candy" or "soft drinks", and defines them in a paragraph. The chain has 60,000 items, including its own brand and items made in the deli and bakery. Someone must decide, item by item, which are covered, record why, load the flag on the right date, and undo it if a court blocks the waiver.

## Why Nobody Has Built This
Eligibility databases cover national-brand UPCs and stop there. POS vendors carry the flag but leave its value to the retailer. The waivers are new, numerous and contested.

## What to Build
An engine that turns each waiver and FNS guidance into rules plus a language-model classifier for the ambiguous cases. It applies them to the chain's full item file, using attributes and label text, and outputs a per-state flag with a confidence and the clause relied on. Borderline items go to a reviewer. Effective dates are scheduled, court orders are tracked, and every change is logged for the state agency.

## Target Customer
Item-data and POS directors at chains in waiver states, and POS vendors serving independents.

## Impact If Built
For a chain with 60,000 items in four waiver states, auto-classifying 90% of items saves ~2,000 review hours per waiver cycle (estimate), with a clause-level record for every flag.
