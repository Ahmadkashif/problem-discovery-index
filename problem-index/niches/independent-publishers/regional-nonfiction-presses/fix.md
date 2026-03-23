# Royalty Calculation Across Multiple Sales Channels

**Niche:** [[niches/independent-publishers/regional-nonfiction-presses/profile|Regional Nonfiction Presses]]
**Industry:** [[industries/independent-publishers|Independent Publishers]]
**Type:** Fix (Pain Point)
**One-liner:** A regional publisher selling through Amazon, IngramSpark, local consignment, direct website, and author events has 5 different revenue streams with 5 different discount structures — and calculates royalties by hand in a spreadsheet twice a year.
**Tags:** #automation #data-integration #quick-win

## The Problem
A regional publisher with 15 titles in print and 8 authors owes royalties based on net receipts — but "net" means something different for every sales channel. Amazon pays 40% of list price. IngramSpark wholesale pays 45–55% depending on the distribution tier. Consignment sales at local shops pay 60% of list. Direct website sales pay 100% minus credit card fees. Author event sales (where the author sells copies personally) have a different split. The publisher must: (1) collect sales data from each channel (Amazon reports monthly, IngramSpark quarterly, consignment data from a notebook), (2) calculate net revenue per channel, (3) apply the royalty rate (which may differ by author contract — some are net receipts, some are list price, some have escalators), and (4) produce a royalty statement. This takes 20–40 hours twice a year and is error-prone because the channel data is in different formats and the contract terms are in paper files.

## Why It's Still Broken
Royalty management software exists (MetaComet, Royalty Tracker, PubMatch) but is designed for publishers processing thousands of sales transactions across hundreds of titles. These tools cost $500–$5,000/month and require integration with enterprise sales systems. A regional press with 15 titles and $200K in annual revenue can't justify the cost or the setup time. QuickBooks can track revenue but doesn't model royalty contracts (per-unit rates, escalators, reserves against returns, multiple rights holders per title). So the publisher builds a custom spreadsheet for each author contract and manually enters data from 5 different sources.

## What a Fix Looks Like
A lightweight royalty calculator where the publisher: (1) enters each author's contract terms once (royalty rate, escalator thresholds, calculation basis), (2) imports or manually enters sales data by channel per reporting period, (3) the system auto-calculates royalties per title per author across all channels, (4) generates a royalty statement PDF that shows unit sales and revenue by channel, net receipts calculation, and royalty earned, and (5) tracks cumulative payments and advance earn-out. No API integrations required — CSV upload or manual entry for a press doing $200K in annual sales. Priced at $20–$40/month.

## Who Feels the Pain
Owner-publishers who spend an entire weekend twice a year calculating royalties, and authors who receive late, unclear, or inaccurate royalty statements that erode trust.

## Impact If Fixed
Reduces royalty calculation time from 40 hours per year to 4 hours. Eliminates the 5–10% error rate in manual calculations that leads to author disputes and corrections. Produces professional royalty statements that strengthen publisher-author relationships — critical for retaining authors who have other publishing options.
