# The Account Manager Running Four Hundred Campaigns by Hand

**Industry:** [[retail-media-networks|Retail Media Networks]]
**Type:** Worker Life Changing
**One-liner:** Retail media account managers spend their weeks pulling keyword reports, adjusting bids in a spreadsheet and rebuilding the same quarterly business review for forty brands, none of which is the advice the brand is paying for.
**Tags:** #time-series-forecasting #gradient-boosting #large-language-models #exponential-smoothing #evaluation-metrics #worker-facing #automation #workflow-orchestration

## The Problem
A retail media account manager carries a book of brand advertisers — anywhere from fifteen to fifty depending on the network and their size. Each brand runs sponsored product, sponsored brand and display campaigns across dozens of SKUs and hundreds of keywords, and each expects the account manager to keep them performing and to explain what happened.

The week is bid adjustments, keyword harvesting, negative keyword additions, budget shifts between campaigns, out-of-stock pauses, and reporting. The reporting alone is substantial: an export, a pivot table, a slide deck, per brand, per month, plus a larger quarterly business review with the same charts and a narrative written from scratch. The out-of-stock work is the most maddening — a SKU goes unavailable in a region, the campaign keeps spending, nobody notices until the weekly check, and the brand asks why they paid for clicks on something nobody could buy.

At the largest networks brands often run their own campaigns through an API and the account manager's role is nominally strategic; in practice it becomes the same work in a different seat, because the brand's agency is also running spreadsheets.

## Why It Matters to the Worker
The role is sold as a partnership — the person who understands both the brand's business and the retailer's shopper, and who can tell a brand something it cannot learn anywhere else. That conversation is the only part of the job that is not replicable by software and the only part brands remember. It happens in the gaps.

The work that fills the gaps is not just tedious, it is anxiety-shaped: the failures are silent and discovered late. A campaign that overspent on an out-of-stock SKU, a budget that flatlined because a card expired, a keyword that quietly became expensive — each surfaces at reporting time, in front of a client, and the account manager explains it. Nobody sees the four hundred campaigns that ran fine.

Quarterly business review season compresses all of it. Forty decks, the same twelve charts, a fortnight of evenings, and the insight section — the part that would justify the meeting — written last, quickly, from whatever the charts happened to show.

## What a Solution Looks Like
Kill the silent failures first, because they cost the most trust for the least work. Out-of-stock and low-availability pauses should be automatic and regional, driven from the same inventory feed the ranker should already be using. Budget exhaustion, card failures, sudden cost-per-click changes and campaigns that stop delivering should be exceptions raised the hour they happen, not discovered at the monthly export.

Then the routine optimisation. Bid adjustment, keyword harvesting and negative keyword identification are pattern-recognition tasks over data the network already holds, and they should arrive as a reviewed queue of proposals with expected effect, not as a spreadsheet the account manager rebuilds each Monday.

Then the reporting. A quarterly business review is a known structure over known data; the charts should assemble themselves and the draft narrative should be written from the actual movements in the account — this brand lost share in this subcategory to this competitor in these regions — leaving the account manager to do the part that requires knowing the brand: what to recommend and what to leave out.

## Impact If Solved
Account management is the cost line that scales with a retail media network's customer count, and it is the function that determines whether brands renew. Removing the silent failures removes the recurring credibility damage; automating the reporting returns a fortnight per quarter per manager; and the combination is what lets a network serve its mid-tail brands at all, which is where its growth has to come from once the top fifty advertisers are signed.
