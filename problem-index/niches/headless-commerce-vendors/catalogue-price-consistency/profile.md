# Catalogue & Price Consistency

**Parent Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to make every service's copy of the catalogue agree about the price a customer will be charged — and whoever does that removes the category's most visible failure, because the copies disagree and the customer notices.

## Profile
**Market Size:** ~$480M US
**Share of Parent Industry:** ~12% of category revenue
**Digital Adoption:** Low — copies that disagree
**Target Buyer:** Data and commerce engineering
**Automation Potential:** Very High — divergence detection is mechanical

## What Makes This a Distinct Niche
Every service in the stack keeps its own copy of the catalogue for performance, synchronisation is a solved engineering problem, and the copies still disagree in ways that charge customers the wrong price. The search index has one price, the content platform has a cached one, the personalisation service has a stale one, the pricing engine has the authoritative one, and the front end shows whichever it fetched first. Each service's synchronisation works; what nobody checks is whether the copies agree at any given moment, which is the only question the customer's experience depends on. It is the most visible correctness failure in composable commerce and the one most obviously detectable.

## Current Tools & Gaps
Event-driven synchronisation, caches with time-based expiry, and reconciliation jobs at some retailers. The gaps: no continuous comparison of the copies; staleness is bounded by a cache setting rather than measured; no authoritative source is designated for the customer-facing price; divergence is discovered through complaints; and promotions, which apply differently in each service, are the largest source and are unmodelled.

## Problems
- [[niches/headless-commerce-vendors/catalogue-price-consistency/build|🔨 Build: Six Copies That Disagree]]
- [[niches/headless-commerce-vendors/catalogue-price-consistency/buy|🛒 Buy: Data Replication and Reconciliation Practice]]
- [[niches/headless-commerce-vendors/catalogue-price-consistency/fix|🔧 Fix: The Promotion That Applies in One Place]]
