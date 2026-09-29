# Direct Store Delivery Reconciled Against Actual Movement

**Niche:** [[niches/retail-pos-platforms/independent-grocery-convenience/profile|Independent Grocery & Convenience]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A large share of an independent grocer's goods are stocked and invoiced by the vendor's own driver, verified by a signature, and the store has no way to check whether what was billed was what was left.
**Tags:** #descriptive-statistics #hypothesis-testing #change-point-detection #confidence-intervals #evaluation-metrics #gradient-boosting #revenue-impact #automation
**Contested on:** Every serious competitor in independent grocery software is fighting to reconcile direct-store-delivery invoices against what the vendor actually left on the shelf — and whoever catches the variance takes the account.

## The Problem
A beverage driver arrives, stocks the cooler, counts what he put in, and hands an invoice to whoever is at the counter, who signs it. The store is billed for that count. Verifying it would mean counting the cooler before and after, which nobody has time for on any of the dozens of direct deliveries a week. Industry practitioners have discussed short deliveries and overbilling in this channel for decades, and the reason it persists is not that retailers are unaware — it is that verification costs more attention than any independent store has. Over a year the leakage on thin grocery margins is material.

## Why Nobody Has Built This
The verification has always been framed as a counting problem, which is a labour problem, and labour is exactly what the store does not have. Framing it as a reconciliation problem instead — comparing invoiced quantities against subsequent scan movement and inventory position over time — makes it a data problem the POS can solve, and nobody has done that because grocery POS vendors are older-generation systems whose product development has been focused elsewhere. The commercial dynamic matters too: the aggregators who collect scan data sell it to the vendors rather than using it for the store, so the analysis that would catch vendor overbilling is performed by the vendor's own supplier ecosystem.

## What to Build
A reconciliation between what was invoiced and what the store can observe. For each direct-delivery item, invoiced quantities over a period are compared to units scanned at the register plus the change in shelf position, with waste and shrink accounted for. A systematic discrepancy — invoiced consistently above what could have moved — is detectable statistically over weeks even though it is invisible on any single delivery, which is the whole insight. Report by vendor, by driver and by item, with the magnitude and the confidence, because the output has to survive a conversation with a vendor representative. Add targeted verification: rather than counting everything, the system nominates the specific deliveries worth counting this week based on where the discrepancy signal is strongest, which turns an impossible task into a ten-minute one. Present the annual value, since the leakage is invisible precisely because it arrives in small increments.

## Target Customer
Independent grocers, convenience store operators and small chains, and the grocery POS vendors serving them who currently sell the store's scan data onward.

## Impact If Built
Direct store delivery leakage is a long-standing, widely acknowledged and rarely measured cost on the thinnest margins in retail, and detecting it statistically removes the labour barrier that has protected it. The effect is also behavioural: a store that demonstrably audits its deliveries is treated differently from one that signs whatever is presented.
