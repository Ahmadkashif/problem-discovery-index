# Multi-Market Inventory Allocation and Sales Tracker

**Niche:** [[niches/specialty-food-retail/farmers-market-vendors/profile|Farmers Market Vendors]]
**Industry:** [[industries/specialty-food-retail|Specialty Food Retail]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool helps farmers market vendors decide how to split limited perishable inventory across 3-5 markets per week — or track what sold where to improve next week's allocation.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact #worker-facing

## The Problem
A baker producing 200 loaves per week sells at 3 markets: Saturday downtown (high volume), Sunday suburban (medium volume), and Wednesday evening (low but growing). How should they split: 100/60/40? 80/80/40? They won't know until 6pm Saturday whether they under- or over-allocated, and by then it's too late to fix Sunday's load. Past sales data exists only in Square transaction totals (not broken down by product) or in the vendor's memory. Weather, seasonal events, and market-specific factors (a competing baker at the Wednesday market) affect allocation but aren't tracked. The vendor makes allocation decisions by gut feel — and gut feel is the right answer 60% of the time and wrong 40%.

## Why Nobody Has Built This
Farmers market vendors have extremely low technology budgets ($0-50/month) and limited time for tool adoption. The multi-market scheduling problem is niche within a niche — most POS and inventory tools assume a single location. Building a useful allocation recommendation requires aggregating sales data by market, product, day, and weather condition over multiple weeks — data that doesn't exist until the vendor starts tracking it. The chicken-and-egg problem (need data to provide value, need value to get adoption) has blocked product development.

## What to Build
A mobile-first market planning tool: the vendor logs what they bring and what they sell at each market (ideally via Square integration or quick manual entry at day's end). Over 4-6 weeks, the system builds market-specific demand profiles by product and generates allocation recommendations for the coming week, adjusted for weather forecast and any known events. The key output is simple: "Saturday downtown: bring 90 sourdough, 30 rye, 20 brioche. Sunday suburban: bring 50 sourdough, 20 rye, 40 brioche." Must work offline on a phone and take under 5 minutes per market day.

## Target Customer
Farmers market vendors selling at 2+ markets per week with perishable inventory they must allocate across locations.

## Impact If Built
Reduces end-of-market unsold perishable inventory by 20-30% through better allocation. Increases total weekly revenue by 5-10% by ensuring the right products reach the right markets. Simple enough to deliver value within 4 weeks of adoption — no upfront configuration required beyond logging sales.
