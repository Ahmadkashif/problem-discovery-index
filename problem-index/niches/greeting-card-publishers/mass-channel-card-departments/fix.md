# The Department Average That Hides Dead Pockets

**Niche:** [[niches/greeting-card-publishers/mass-channel-card-departments/profile|Mass, Drug & Grocery Card Departments]]
**Industry:** [[industries/greeting-card-publishers|Greeting Card Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** Card department performance is reviewed as sales per linear foot by store and occasion, so a few hundred pockets that have sold almost nothing for a year stay on the fixture.
**Tags:** #descriptive-statistics #bayesian-inference #hypothesis-testing #quick-win #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to win the retailer's whole card department at the multi-year contract renewal by proving, pocket by pocket in the retailer's own scan data, more sales per linear foot net of shrink than the incumbent publisher, and whoever proves it takes the department.

## The Problem
Weekly reports roll pocket sales up to occasion and department. A pocket that sells one card a month in most stores is invisible in that roll-up, and so is a pocket that sells well but has been empty for six weeks in a third of stores. Refresh decisions are made by occasion managers who see the averages, and dead pockets survive several resets.

## Why It's Still Broken
Pocket-level sales are noisy: at a few units a week per store, a single week says almost nothing, and nobody wants to pull a design on noise. Reports were designed for retailer reviews, which happen at department level. And separating "weak design" from "empty pocket" needs merchandiser data that sits in a different system.

## What a Fix Looks Like
A monthly pocket health report: each pocket's sales rate estimated across stores with uncertainty, ranked against its occasion peers and its fixture position, with weeks flagged where scans stopped but shipments continued (likely empty or misfiled). Pockets that are reliably in the bottom tier for two cycles go on the refresh list automatically, with the evidence attached.

## Who Feels the Pain
Occasion and line managers choosing what to refresh; category managers walking into a renewal with a department that underperforms for reasons they cannot see; retailers paying for space that does not earn.

## Impact If Fixed
Refresh effort goes to the pockets that are costing the most, and the department's productivity rises before the renewal rather than being explained after it.
