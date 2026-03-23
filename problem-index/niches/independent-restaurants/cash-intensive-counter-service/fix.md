# Cash Shrinkage Detection and Accountability

**Niche:** [[niches/independent-restaurants/cash-intensive-counter-service/profile|Cash-Intensive Counter-Service Restaurants]]
**Industry:** [[industries/independent-restaurants|Independent Restaurants]]
**Type:** Fix (Pain Point)
**One-liner:** Cash-heavy restaurants lose 2-5% of cash revenue to theft, miscounts, and "friendly" discounting — but without item-level cash tracking, the owner cannot distinguish theft from error.
**Tags:** #anomaly-detection #isolation-forest #tabular-ml #revenue-impact

## The Problem
A counter-service restaurant doing $500K/year with 50% cash loses $5K-$12K annually to cash shrinkage — a combination of employee theft (voiding transactions after collecting cash, underringing items, pocketing bills), honest miscounts, and unauthorized discounting. The owner suspects the problem but cannot prove it: end-of-night cash counts show a drawer that is $20-$50 short, but they cannot determine whether it was theft, a miscount, or a legitimate transaction error.

## Why It's Still Broken
Detecting cash theft requires comparing expected cash (from item-level POS transactions) against actual cash (in the drawer), by shift and by employee. Most cash-heavy restaurants do not ring every transaction through the POS — especially during rushes, items are handed over with a verbal price and cash goes into the drawer with no digital record. Without item-level cash transaction logging, there is no expected value to compare against, making detection impossible.

## What a Fix Looks Like
Mandatory item-level POS entry for all transactions (cash and card), combined with shift-level cash reconciliation that compares expected vs. actual drawer amounts per employee. Anomaly detection flags employees whose drawers are consistently short, transactions that are voided and re-entered at lower amounts, and patterns of high-void-rate shifts. The system must be simple enough that it does not slow the counter during a lunch rush — one-tap item entry, not menu navigation.

## Who Feels the Pain
The owner who knows they are losing money from the cash drawer but has no data to identify the source, the amount, or the responsible parties — and who risks accusing the wrong employee without evidence.

## Impact If Fixed
Reducing cash shrinkage from 4% to 1% saves $7K-$15K annually for a typical cash-heavy counter-service restaurant, directly improving net income by 30-50% in a segment with 3-5% margins.
