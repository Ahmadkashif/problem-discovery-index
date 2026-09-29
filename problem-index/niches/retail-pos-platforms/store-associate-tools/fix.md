# Shrink Investigations That Never Conclude

**Niche:** [[niches/retail-pos-platforms/store-associate-tools/profile|Store Associate Tools]]
**Industry:** [[industries/retail-pos-platforms|Retail POS Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A count comes up short, someone spends an evening investigating, and the cause turns out to be a receiving error from four months ago or is never found at all — and no store records which it was, so the same investigation happens again.
**Tags:** #descriptive-statistics #hypothesis-testing #change-point-detection #confidence-intervals #evaluation-metrics #automation #worker-facing #quick-win
**Contested on:** Every serious competitor building for store staff is fighting to let an associate answer a customer's question from the sales floor without walking to the back — and whoever the associates actually use takes the store.

## The Problem
The count shows eleven units and the system says seventeen. A manager spends two hours: checking recent sales, looking for the item elsewhere in the store, reviewing returns, checking whether a case was received as a unit. Sometimes the cause emerges — a receiving error, a mis-scan at the register, a transfer never posted. Frequently it does not, and the adjustment is posted as shrink. Nobody records which outcome occurred, so the store's shrink figure includes an unknown proportion of data errors, and the investigation is repeated next quarter on the same item for the same reason.

## Why It's Still Broken
Investigation is unstructured work done by whoever is available, and its output is an adjustment rather than a finding. There is no cause field, no taxonomy, and no expectation that one exists. The store's shrink number, which drives real decisions about security spending and staffing, is therefore a mixture of theft, data error, damage and process failure in unknown proportions — and treating a data error problem as a theft problem produces exactly the wrong response, including suspicion falling on staff for discrepancies that were clerical.

## What a Fix Looks Like
Structure the investigation and record the cause. When a discrepancy appears, the system assembles what an investigator would look for automatically: recent sales of the item, returns, transfers, the receiving record for the last delivery including whether case quantities were posted correctly, and any prior discrepancies on the same item. Much of the time that assembly identifies the cause immediately, which converts a two-hour investigation into a two-minute confirmation. The cause is recorded from a short list — receiving error, register error, transfer, damage, unlocated, theft, unresolved — and aggregated. Within a quarter the store knows what its shrink actually consists of, which is almost always a surprise and frequently shows that the largest component is a process error at receiving rather than theft. That finding changes what the store does, and it also matters to the staff who were quietly suspected.

## Who Feels the Pain
Managers losing evenings to inconclusive investigations; associates under suspicion for discrepancies caused by clerical errors; and owners spending on loss prevention against a number they cannot decompose.

## Impact If Fixed
Automatic evidence assembly resolves a large share of discrepancies without an investigation, and cause coding turns shrink from an undifferentiated number into a decomposition that points at a specific fixable process. The most common finding — that receiving errors dominate — is both cheaper to fix than theft and fairer to the people currently carrying the suspicion.
