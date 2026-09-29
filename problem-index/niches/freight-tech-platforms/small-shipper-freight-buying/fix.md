# The LTL Reclassification Nobody Can Contest

**Niche:** [[niches/freight-tech-platforms/small-shipper-freight-buying/profile|Small Shipper Freight Buying]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** An LTL shipment quoted at one price arrives as an invoice at a higher one because the carrier reweighed or reclassified it, and the small shipper has no evidence, no expertise and no practical way to dispute it.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #cnns #compliance #automation #revenue-impact
**Contested on:** Every serious competitor selling freight to small shippers is fighting to give a business with no volume a rate it can trust and a way to check it — and whoever makes pricing legible to a shipper with no leverage takes the segment.

## The Problem
A shipper quotes an LTL shipment at class 70, 1,200 pounds, and is charged for class 125 at 1,480 pounds after the carrier's terminal put it on a dimensioner. The invoice is 60% higher than the quote. The shipper does not know whether the reclassification is correct, has no record of the shipment's actual dimensions and weight at the moment it left, and the amount in dispute is small enough that pursuing it costs more than it recovers. They pay. This happens routinely, and across a year it is a substantial and invisible cost that the shipper experiences as freight being unpredictable.

## Why It's Still Broken
The carrier has a dimensioner and the shipper has a scale at best. The evidence asymmetry is total: the carrier's measurement is the only measurement, taken after the shipment left the shipper's control. Classification itself is genuinely intricate — density, stowability, handling and liability all bear on it — and a small shipper cannot be expected to get it right, which means reclassification is frequently legitimate and the shipper cannot tell which instances are. Dispute processes exist and are calibrated for shippers with volume and a claims person.

## What a Fix Looks Like
Capture the evidence before the shipment leaves. A photograph and a dimensional capture at the dock, which a phone can do adequately now, plus a weight from whatever scale is available, timestamped and attached to the bill of lading — that single act converts a shipper from having no evidence to having contemporaneous evidence, which changes the dispute entirely. Compute the correct class from the captured dimensions and weight so the shipment is quoted right in the first place, since a large share of reclassifications are the shipper's own specification error and are avoidable. Track reclassification rate by carrier and by lane, because the pattern is informative — a carrier reclassifying a high share of a shipper's shipments is either receiving bad specifications or applying an aggressive practice, and the shipper currently cannot distinguish those. Automate the dispute where the evidence supports it, since the reason these are not contested is the effort rather than the merits.

## Who Feels the Pain
Small shippers paying invoices they cannot evaluate; the finance staff who reconcile freight bills that never match quotes; and honest carriers, whose legitimate reclassifications are resented because nobody can tell them apart from the others.

## Impact If Fixed
Dock capture is a thirty-second act that removes the evidence asymmetry, and correct classification at quote time eliminates the avoidable share of reclassifications outright. For a small shipper the recovered amount is material and, more importantly, freight cost becomes predictable — which is what they actually want.
