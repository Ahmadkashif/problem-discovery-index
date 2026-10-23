# The Superseded Part Number That Breaks the Quote

**Niche:** [[niches/electrical-distributors/price-files-product-data/profile|Manufacturer Price Files & Product Data]]
**Industry:** [[industries/electrical-distributors|Electrical Distributors]]
**Type:** Fix (Pain Point)
**One-liner:** A manufacturer replaces a catalogue number, the old one disappears from the price file, and every quote and SPA that used it stops resolving.
**Tags:** #k-nearest-neighbors #word-embeddings #quick-win #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to load each manufacturer's price file and product changes into the ERP, the open quotes and the webstore on the day they take effect, and whoever leaves the fewest lines quoted or sold on a superseded cost takes the account.

## The Problem
Supersessions arrive as notices, spreadsheets or silent removals. Quotes, SPAs and customer cross-references keep the old number until someone tries to order it.

## Why It's Still Broken
Supersession data is inconsistent across manufacturers and rarely mapped automatically.

## What a Fix Looks Like
Detect items that vanish from a price file, propose the replacement from manufacturer notices and attribute similarity, and update quotes, SPAs and cross-references once confirmed.

## Who Feels the Pain
Quoters, SPA analysts and purchasing agents who meet the dead number at the worst moment.

## Impact If Fixed
Old numbers resolve to current items before anyone has to ask. If ~2–5% of active SKUs are superseded each year (estimate), mapping them automatically removes most dead-number failures in quotes and SPAs.
