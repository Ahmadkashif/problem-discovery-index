# Every Open Quote Checked on a Price File's Effective Date

**Niche:** [[niches/electrical-distributors/price-files-product-data/profile|Manufacturer Price Files & Product Data]]
**Industry:** [[industries/electrical-distributors|Electrical Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A manufacturer's increase loads into the ERP on its effective date, and hundreds of open project quotes stay priced on the old cost.
**Tags:** #k-nearest-neighbors #word-embeddings #feature-engineering #data-integration #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to load each manufacturer's price file and product changes into the ERP, the open quotes and the webstore on the day they take effect, and whoever leaves the fewest lines quoted or sold on a superseded cost takes the account.

## The Problem
A distributor carries open project quotes for months. When a manufacturer raises prices, the item master updates, but the quotes, the contract prices built on the old cost and the SPA cost bases don't, and orders released against those quotes ship below margin.

## Why Nobody Has Built This
Price-file tools stop at the item master. Quote, contract and SPA tables sit in different parts of the ERP, and linking them to a price change needs item matching that handles superseded numbers and pack changes.

## What to Build
A change engine that ingests each price file, maps items (including supersessions and pack-quantity changes) with embedding-based matching and rules, recomputes derived prices, and produces an impact list: every open quote, contract price and SPA cost basis affected, with the margin change and a suggested action (reprice, notify, request SPA update). Quote owners get their own list the morning the change takes effect.

## Target Customer
Pricing directors at mid-size and large electrical distributors.

## Impact If Built
Price increases pass through to open business on the day they take effect. If open quotes lag increases by ~1–3 months today (estimate), a distributor recovers ~0.2–0.5% of sales in margin each increase cycle (estimate).
