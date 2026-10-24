# The Store Picker Chasing a Pick Rate

**Industry:** [[grocery-stores|Grocery Stores]]
**Type:** Worker Life Changing
**One-liner:** A store-employed online-order picker walks eight to twelve miles a shift against an items-per-hour target, hunting for products the system says are in stock and in a location the system says is right, and is scored on misses that are mostly the store's data errors.
**Tags:** #gradient-boosting #logistic-regression #k-nearest-neighbors #feature-engineering #worker-facing #automation #workflow-orchestration

## The Problem
Since the robotic warehouses retreated (Kroger said in November 2025 it would close three Ocado-powered centres and refocus on store fulfilment, Grocery Dive), most online grocery orders are picked inside the store. At chains that pick with their own staff rather than through a marketplace shopper, the picker is a store employee. They push a cart with six to twelve totes through the aisles, batch-picking several orders at once while regular shoppers fill the same aisles. The handheld gives a pick path and a target, often 80 to 120 items an hour (estimate), and tracks every scan.

The path assumes the item is where the planogram says and that the on-hand count is right. Often neither is true. The item was moved in last week's reset, the shelf is empty though the system shows twelve, the backstock is on a top shelf in the back room, or the produce item has to be weighed and chosen by hand. Each miss costs a minute or more of searching, then a substitution decision under a timer. The picker eats the time against their rate and the complaint against their quality score when the customer rejects the swap. Frozen and refrigerated items are picked last, under a temperature clock, by which point the batch is behind.

## Why It Matters to the Worker
The rate is the job. Pickers below target are coached, moved to other shifts or let go, and the rate does not adjust for the store's data errors that slowed them down. The physical load is real: miles of walking on concrete, repeated bending to bottom shelves, lifting cases of water, and long stretches in the freezer aisle. The work happens in front of customers who resent the carts blocking the aisle.

It is also a skill nobody records. Experienced pickers learn where things really are, which items are always out, and which substitutions customers accept. They carry the store's real inventory map in their heads, and the system never learns from it.

## What a Solution Looks Like
A pick path built on the store's real locations and on-hand truth, learned from pickers' own scans. Every "not found", every scan in an unexpected aisle, and every successful find after a search updates an item's likely location and its probability of being on the shelf now. Before the batch starts, items likely to be missing are flagged so the picker checks backstock first or a substitute is proposed in advance. The rate is adjusted for what the store's data cost them, and pickers' location corrections feed back to the reset and inventory teams as fixes rather than disappearing.

## Impact If Solved
If found-first-time rates rise from ~85% to ~95% (estimate), a picker on a 100-items-per-hour target saves ~10 minutes of searching an hour, more than an hour a shift. They also stop being written up for errors they did not make, and the store gets a running list of its own location and count errors.
