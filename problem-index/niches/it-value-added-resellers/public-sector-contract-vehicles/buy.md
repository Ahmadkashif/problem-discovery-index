# Channel CPQ Taught the Vehicle's Rules

**Niche:** [[niches/it-value-added-resellers/public-sector-contract-vehicles/profile|Public-Sector Contract Vehicles]]
**Industry:** [[industries/it-value-added-resellers|IT Distributors & Value-Added Resellers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The reseller's CPQ already prices every quote; it treats a contract price as just another price book.
**Tags:** #descriptive-statistics #feature-engineering #compliance #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to quote every public-sector order from the right contract vehicle at an allowed contract price, and whoever has the lowest share of orders rejected or modified for off-contract items or prices takes the account.

## The Problem
Reps load a vehicle's price list into the CPQ as a price book, so the tool cannot tell an off-contract item from an unpriced one, or warn that a ceiling has changed.

## What Already Exists
ConnectWise CPQ, QuoteWerks, Kaseya Quote Manager and Salesforce-based CPQ with multiple price books and distributor feeds.

## The Customization Gap
The adaptation needs: vehicle eligibility by buyer type and state; ceiling enforcement as a hard rule; modification versions with effective dates; SKU successor mapping; fee and sales-report fields per vehicle; and an audit trail showing which price list each quote used.

## Target Customer
Public-sector sales operations at mid-sized resellers.

## Impact If Solved
Rules inside the existing quoting tool stop most off-contract quotes at creation (estimate: ~70%) without a new system.
