# Scenes That Pass Review and Fail the Customer

**Niche:** [[niches/satellite-operators/eo-tasking-delivery/profile|Earth-Observation Tasking & Delivery]]
**Industry:** [[industries/satellite-operators|Satellite Operators]]
**Type:** Fix (Pain Point)
**One-liner:** Quality review checks a scene's overall cloud percentage, so an image with 5% cloud sitting exactly on the customer's target ships as a pass and comes back as a complaint.
**Tags:** #semantic-segmentation #cnns #evaluation-metrics #automation #quick-win
**Contested on:** Every serious competitor in this niche is fighting to deliver a usable, cloud-free image of the customer's target inside the promised window, and whoever turns tasking orders into successful collections at the highest rate takes the tasking contract.

## The Problem
Acceptance criteria are written as scene-level cloud percentages because that is what processing chains compute. Customers care about their target: a port, a runway, a field, a tank farm. Analysts catch some target-level failures by eye, but under time pressure many ship, and a re-collection costs another pass and another day.

## Why It's Still Broken
Cloud masks are computed per scene, contracts were written around them, and target geometry is often in the order but not passed to quality review.

## What a Fix Looks Like
Quality checks that intersect the cloud, haze and shadow masks with the order's target geometry, score usability at the target, and trigger automatic re-tasking for target-level failures before delivery, with acceptance criteria rewritten per target.

## Who Feels the Pain
Imagery operations analysts; customers who receive unusable images; account managers handling credits.

## Impact If Fixed
Fewer unusable deliveries and re-collections triggered a pass earlier, which is often the difference between meeting a delivery window and missing it.
