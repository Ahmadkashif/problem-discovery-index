# ClassPass Revenue Cannibalization

**Niche:** [[niches/gyms-independent/boutique-fitness-studios/profile|Boutique Fitness Studios]]
**Industry:** [[industries/gyms-independent|Independent Gyms]]
**Type:** Fix (Pain Point)
**One-liner:** Studios list on ClassPass to fill empty spots but can't distinguish incremental ClassPass visitors from existing members who switch to ClassPass for cheaper access — cannibalizing $15-40 per visit in lost direct revenue.
**Tags:** #data-integration #anomaly-detection #revenue-impact #tabular-ml

## The Problem
ClassPass pays studios $8-15 per visit for classes that retail at $25-40. The pitch is that ClassPass fills otherwise-empty spots with new customers. But studios have no way to verify this claim. Existing members discover that ClassPass membership ($50-100/month for 4-8 classes) is cheaper than the studio's direct membership ($150-300/month unlimited), and quietly switch — the studio sees the same face in class but receives 60-70% less revenue per visit. Without cross-referencing ClassPass visitor lists against their own member database, studios can't detect this cannibalization until it shows up as unexplained revenue decline months later.

## Why It's Still Broken
ClassPass doesn't share detailed visitor data that would make cross-referencing easy — studios see ClassPass check-ins in their booking system but the ClassPass user identity is obfuscated. Matching requires comparing ClassPass visitor names/emails against the studio's member database, which is a manual process nobody has time for. ClassPass has no incentive to make cannibalization visible because it would discourage studios from participating. Studios' own booking platforms (Mindbody, Mariana Tek) don't flag when a ClassPass visitor matches an existing or recently-churned member.

## What a Fix Looks Like
An automated cannibalization detector that: (1) cross-references ClassPass check-in data against the studio's current and recently-churned member database using name/email matching, (2) flags members who appear to have migrated to ClassPass, (3) calculates the net revenue impact (ClassPass payment minus lost direct membership revenue), and (4) provides a ClassPass ROI dashboard showing true incremental visitors vs. cannibalized members. This gives studios the data to decide whether ClassPass participation is actually profitable.

## Who Feels the Pain
Studio owners who notice declining direct membership revenue but can't prove it's related to ClassPass cannibalization versus normal churn — and who make pricing and partnership decisions blind.

## Impact If Fixed
Identifying 5-15 cannibalized members per studio saves $15K-50K annually in revenue that would have been collected at direct membership rates — and gives studios the negotiating data to demand better ClassPass terms or exit the platform.
