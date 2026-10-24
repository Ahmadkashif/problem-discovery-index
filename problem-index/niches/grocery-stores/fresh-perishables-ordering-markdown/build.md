# One Lot Record From Order to Disposition

**Niche:** [[niches/grocery-stores/fresh-perishables-ordering-markdown/profile|Fresh Perishables Ordering & Markdown]]
**Industry:** [[industries/grocery-stores|Grocery Stores]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No system follows a case of fresh product from the order that brought it in to the sale, markdown, donation or cull that ended it, so a chain cannot say which decisions caused its shrink.
**Tags:** #survival-analysis #gradient-boosting #cnns #causal-inference #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is "every serious competitor in this niche is fighting to cut fresh-department shrink without emptying the shelves". But that contest splits in two. Ordering vendors win before the truck arrives, by cutting the most shrink at an unchanged in-stock rate. Markdown, surplus and dynamic-pricing vendors win after the product is aging, on margin recovered per lot. The buyers, data and winners differ. Decomposed into contested sub-niches below.

## The Problem
A chain's fresh shrink is reported monthly per department as one number. Behind it are thousands of lots, each shaped by several decisions: the order quantity, the supplier, the condition at receipt, the rotation on the floor, the markdown timing and the final disposal. The ordering tool sees orders and sales, the markdown tool sees label scans, and the scale sees weights. Nothing joins them to the same lot.

## Why Nobody Has Built This
Each vendor owns one step and sells against its own metric. Ordering vendors report shrink cut, markdown vendors report recovered margin, and both claim the same dollars. Lot identity in a store is weak: cases are broken, product is mixed on a display, and random-weight items carry no unit identity.

## What to Build
A lot ledger at the department level. Each received case becomes a lot with supplier, date and a condition grade from a handheld photo. Floor events (rotation, markdown, transfer to deli, donation, cull) are scanned against it, and sales are allocated first-in-first-out by item. On top, a survival model of time-to-disposition by lot, and an attribution report splitting shrink into order excess, receipt quality, rotation and markdown timing.

## Target Customer
VPs of fresh merchandising at regional chains of 30 to 300 stores, and the ordering vendors that want to prove their share of a shrink cut.

## Impact If Built
A 100-store chain with ~$500M of annual fresh sales that can attribute shrink by cause could target the biggest cause first; a one-point cut in fresh shrink is ~$5M a year (estimate).
