# Variable-Availability Menu Costing Engine

**Niche:** [[niches/independent-restaurants/farm-to-table-fine-dining/profile|Farm-to-Table & Seasonal Menu Restaurants]]
**Industry:** [[industries/independent-restaurants|Independent Restaurants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product today calculates contribution margins for dishes that change weekly using ingredients with volatile pricing from small-farm vendors.
**Tags:** #linear-regression #regression #tabular-ml #revenue-impact #data-integration

## The Problem
A farm-to-table chef creates 5-10 new dishes per week based on what arrives from local farms. Each dish needs a menu price, but the chef has no tool that can rapidly compute food cost from ingredients with prices that fluctuate 20-40% week to week. The result is pricing by instinct: the chef guesses a margin and often discovers weeks later (via aggregate P&L) that several seasonal dishes were priced below cost.

## Why Nobody Has Built This
Existing recipe costing tools assume a stable ingredient catalog with prices updated monthly from broadline distributors. Farm-to-table procurement is the opposite: 15 vendors with handwritten invoices, Venmo payments, and pricing that changes with every delivery. Building a costing engine for this context requires a flexible ingredient database that handles informal vendor communications, price volatility tracking, and rapid new-recipe entry (the chef cannot spend 20 minutes entering a recipe for a dish that will exist for 5 days).

## What to Build
A mobile-first recipe costing tool that ingests farm invoices via photo/text parsing, maintains a running price index per ingredient per vendor, and allows the chef to cost a new dish in under 60 seconds by selecting ingredients from a visual catalog and specifying quantities. The output is an instant contribution margin estimate with a confidence range reflecting ingredient price volatility.

## Target Customer
Chef-owners of farm-to-table restaurants ($1M-$4M revenue) who change 30-50% of their menu weekly and currently price new dishes by feel.

## Impact If Built
Accurate per-dish costing on volatile menus recovers $20K-$60K annually in margin that is currently lost to mispriced seasonal dishes — critical for a segment where average net margin is already under 5%.
