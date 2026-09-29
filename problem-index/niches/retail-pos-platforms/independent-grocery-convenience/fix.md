# The Category Reset the Store Cannot Evaluate

**Niche:** [[niches/retail-pos-platforms/independent-grocery-convenience/profile|Independent Grocery & Convenience]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A vendor representative proposes a shelf reset using data the store cannot see, the store agrees, and nobody afterwards computes whether the category's sales and margin improved.
**Tags:** #hypothesis-testing #descriptive-statistics #confidence-intervals #evaluation-metrics #change-point-detection #revenue-impact #quick-win #automation
**Contested on:** Every serious competitor in independent grocery software is fighting to reconcile direct-store-delivery invoices against what the vendor actually left on the shelf — and whoever catches the variance takes the account.

## The Problem
A vendor's category manager arrives with a planogram, a syndicated data presentation and a recommendation: give this section more facings, drop these two competing items, add these three of ours. The analysis is real and the interest is obvious. The store agrees, because the vendor's representative is the only person in the conversation with data. Six months later nobody has asked whether the category's total sales and total margin went up or down — only whether the vendor's items did, which the vendor will happily report.

## Why It's Still Broken
The store's own data is in its POS and is not analysed by anyone, while the vendor's data is syndicated, well presented and free to the store. Evaluating a reset requires comparing category performance before and after against what would have happened otherwise, which is a small piece of analysis that no independent has anyone to do. And there is a relationship dynamic: challenging a vendor's recommendation with the store's own numbers is a conversation many owners would rather not have with a partner they depend on for deliveries, credit and promotional support.

## What a Fix Looks Like
Compute the category's own before-and-after automatically. When a reset occurs, record it as a dated event, and compare total category units, revenue and margin over the following weeks against the preceding period and against the same category's behaviour in comparable stores on the platform, which controls for seasonality and market movement. Report at the category level rather than at the vendor's item level, because the question is whether the store's shelf is working harder, not whether one supplier's share grew. Track the items that were dropped, since the most common failure of a vendor-led reset is removing an item with modest volume and high margin or high loyalty. Give the owner a one-page result they can put in front of the representative at the next visit — which changes the nature of that meeting permanently and costs nothing but the comparison.

## Who Feels the Pain
Owners accepting recommendations they cannot evaluate; category performance that quietly declines while a supplier's share grows; and customers who can no longer find an item the store used to carry.

## Impact If Fixed
Reset evaluation is a small, standard before-and-after comparison on data the store already owns, and it is the only instrument an independent has for negotiating with parties whose analytical resources dwarf its own. The asymmetry in these conversations is total today and is closable with one page.
