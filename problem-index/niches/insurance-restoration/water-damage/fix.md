# Carrier Denials for Excessive Drying Time

**Niche:** [[niches/insurance-restoration/water-damage/profile|Water Damage Mitigation]]
**Industry:** [[industries/insurance-restoration|Insurance Restoration]]
**Type:** Fix (Pain Point)
**One-liner:** Carriers deny 15-25% of water mitigation invoices for "excessive drying time" because restorers' manual documentation can't prove that prolonged drying was justified by structural conditions, not equipment mismanagement.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #compliance #revenue-impact

## The Problem
Carriers have internal benchmarks for acceptable drying time (e.g., "standard drywall in a 12x14 room should dry in 3-4 days"). When a restorer's mitigation invoice shows 7 days of equipment rental, the carrier's desk adjuster flags it as excessive and reduces payment. The restorer's defense is their drying documentation — moisture readings showing that the materials genuinely required 7 days to dry. But if the documentation is incomplete (missed readings, gaps in the drying curve, no psychrometric calculations), the carrier's denial stands. Restorers write off 15-25% of mitigation revenue to drying-time disputes.

## Why It's Still Broken
Manual moisture documentation is inherently incomplete — technicians skip site visits on weekends, record readings at inconsistent times, and don't always capture psychrometric data. This creates gaps in the drying curve that carriers interpret as evidence of inattention rather than legitimate drying time. The restorer can't prove what happened between readings, so the carrier's benchmark prevails. Even when drying legitimately took longer (due to dense materials, contained environments, or elevated ambient humidity), the restorer lacks the scientific documentation to prove it.

## What a Fix Looks Like
A drying documentation package that is denial-proof: continuous moisture monitoring (every 4-6 hours, not once daily), complete psychrometric records showing ambient conditions that affected drying rate, drying-rate calculations showing that the actual rate matches the theoretical rate for the material and conditions, and a narrative explaining any deviations from standard drying time. The package shifts the burden of proof from "why did it take this long?" to "here is exactly why it took this long, backed by continuous data."

## Who Feels the Pain
Restoration company owners who write off $50K-$200K annually in drying-time denials. Project managers who spend 2-3 hours per dispute preparing rebuttals to carrier drying-time challenges.

## Impact If Fixed
Reduces drying-time denials by 60-80%, recovering $30K-$160K annually for a mid-size restoration company. Eliminates the adversarial dynamic between restorers and carrier desk adjusters over drying time, improving program relationships and referral volume.
