# Product and Fee Mapping in a Core Conversion

**Industry:** [[community-banks|Community Banks]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Data migration tooling is mature, but converting an acquired community bank onto the buyer's core still means mapping hundreds of deposit products, fee codes and loan types by hand across two processors' data models, and the errors surface as customer complaints and Regulation DD notice problems after the conversion weekend.
**Tags:** #large-language-models #k-nearest-neighbors #feature-engineering #evaluation-metrics #data-integration #workflow-orchestration #compliance

## The Problem
When one community bank buys another, the deal is usually followed within ~six to twelve months (estimate) by a core conversion. The acquired bank's checking, savings, CD and loan products, each with its own interest calculation, fee schedule, service charge rules, statement cycle and disclosure, must be mapped to the acquirer's product set on the acquirer's core. A small bank can have ~a hundred deposit product codes (estimate), many of them legacy plans with a few dozen accounts each, plus hundreds of fee and transaction codes and general ledger mappings. The conversion team, a handful of operations staff from both banks working with the core vendor's conversion manager, builds the mapping in spreadsheets, runs two or three mock conversions, and reconciles balances, accrued interest and fee totals between old and new systems. Customers whose product changes must receive advance notice of changed terms under Regulation DD and Regulation E. Bank M&A ran at its busiest since 2021 in 2025, so many banks are doing this now.

## What Already Exists
Core vendors run conversion programmes with their own extract, transform and load tools and standard data maps from competing cores; Jack Henry, Fiserv and FIS each convert hundreds of banks a year in both directions. Generic data migration and reconciliation tools exist, and consultancies sell conversion project management.

## The Customisation Gap
What the vendor tools do not do is decide the business mapping. The bank-specific logic is: matching each legacy product to the nearest acquirer product by its actual economics (rate tiering, minimum balance, fee waivers, interest compounding), not its name; identifying which customers' terms change materially enough to trigger a change-in-terms notice and drafting it; mapping fee and transaction codes so the first statement after conversion does not double-charge or miss charges; reconciling accrued interest that the two cores calculate differently; and capturing the acquired bank's undocumented exceptions (the fee waived for a church, the officer-approved overdraft limits) that live only in its staff's memory. Each conversion rebuilds this from scratch.

## Impact If Solved
A mapping assistant that proposes product matches from account-level economics, quantifies which customers are affected, drafts the notices and reconciles mock conversions automatically would cut weeks from each conversion, reduce the post-conversion complaint spike that costs an acquirer the deposits it paid a premium for, and keep the acquired bank's exceptions from being lost.
