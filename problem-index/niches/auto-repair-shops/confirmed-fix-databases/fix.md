# Fixes Are Recorded Without Whether They Held

**Niche:** [[niches/auto-repair-shops/confirmed-fix-databases/profile|Confirmed-Fix Diagnostic Knowledge Databases]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Fix (Pain Point)
**One-liner:** A record says a part was replaced and the code cleared; nobody ever asks whether the vehicle came back three weeks later, so a database of confirmed fixes contains an unknown fraction of confirmed guesses.
**Tags:** #survival-analysis #gradient-boosting #logistic-regression #evaluation-metrics #cross-validation #confidence-intervals #change-point-detection #data-integration #compliance #worker-facing

## The Problem
"Confirmed fix" is the product's central claim and it is confirmed only at the moment of repair. The technician replaced a component, the symptom went away, the record was written. Whether the symptom stayed away is not recorded, and in mechanical diagnosis that gap matters enormously — parts replaced adjacent to the real fault frequently produce temporary resolution, intermittent conditions disappear on their own, and clearing a code makes any repair look successful for a while. So the corpus contains a mixture of genuine root cause identifications and plausible-looking near misses, in unknown proportion, presented to subscribers with identical confidence. The records most likely to be wrong are the ones for intermittent and hard-to-reproduce faults, which are exactly the cases technicians consult the database about.

## Why It's Still Broken
Follow-up requires knowing what happened at the shop weeks later, and the publisher's relationship with the shop ends when the case closes. Shop management systems hold the repeat-visit data and belong to other vendors, sometimes competitors. There is also a commercial reluctance that is easy to understand and hard to defend: a publisher that measures fix durability is generating evidence that some of its confirmed fixes were not, and the segment competes on the size and authority of the corpus rather than on its measured reliability. Nobody has been forced to look, so nobody has.

## What a Fix Looks Like
Durability as a recorded property of every fix. Where the publisher's own tooling sits in the shop's workflow, comeback detection is straightforward — the same vehicle returning with the same or a related complaint within a defined window. Where it does not, integration with shop management platforms or a lightweight structured follow-up on a sample of cases gets enough coverage to calibrate. The measured signal then attaches to the corpus rather than to individual shops: fix records carry a durability indicator, patterns emerge showing which fault types and which repair actions have low durability, and the records for those are flagged as provisional rather than presented as settled. The most valuable output is negative and currently unavailable anywhere — the list of repairs the trade routinely performs that do not actually resolve the complaint, which is a genuinely new product and directly addresses the industry's most expensive habit.

## Who Feels the Pain
Technicians following a record to a repair that does not hold and losing both the labour and the customer's trust; vehicle owners paying twice; shops absorbing comebacks under warranty; and the publisher, whose entire proposition is the word "confirmed" and who has no evidence for it.

## Impact If Fixed
Replaces an unverified claim with a measured one, in a product whose only real competitive dimension is trust. Flagging low-durability records improves the corpus immediately, and the comeback analysis is a defensible new product that no competitor can build without the same shop-level observation. It also gives the publisher an honest answer to the question a sceptical shop owner always asks, which is how they know the fix is real.
