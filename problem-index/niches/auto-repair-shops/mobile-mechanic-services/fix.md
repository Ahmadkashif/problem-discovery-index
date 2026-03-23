# Accurate Quoting Without Pre-Inspection Access

**Niche:** [[niches/auto-repair-shops/mobile-mechanic-services/profile|Mobile Mechanic Services]]
**Industry:** [[industries/auto-repair-shops|Auto Repair Shops]]
**Type:** Fix (Pain Point)
**One-liner:** Mobile mechanics must quote a price before seeing the vehicle, leading to 20-30% of jobs requiring awkward on-site price adjustments that erode customer trust.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
Unlike a traditional shop where the customer drops off the car for inspection before an estimate, mobile mechanics must quote over the phone based on a customer's description: "it's making a grinding noise when I brake." The mechanic arrives to find the rotors are deeply gouged and the calipers are seized — doubling the actual cost. Either the mechanic eats the difference (losing $200-$400) or asks the customer for more money on-site (losing trust). Experienced mobile mechanics develop an intuition for how to price based on vehicle age, customer description patterns, and common failure modes, but this skill takes years to develop.

## Why It's Still Broken
There is no structured data linking customer symptom descriptions to actual repair outcomes for mobile mechanic scenarios. Traditional estimating guides (Mitchell, Motor) provide accurate labor times once you know the repair, but they can't predict the repair from a customer's verbal description. The customer's description is inherently unreliable — "grinding when braking" could be $150 (pads only) or $800 (pads, rotors, calipers, and a brake line).

## What a Fix Looks Like
A quoting assistant that takes the customer's symptom description and vehicle info (year/make/model/mileage), cross-references against historical repair outcomes for similar descriptions, and generates a price range with probability-weighted scenarios: "70% chance pads and rotors only ($280-$350), 20% chance includes calipers ($500-$650), 10% chance additional issues ($700+)." The mobile mechanic presents a range rather than a fixed price, with clear explanations of what would push the price higher.

## Who Feels the Pain
Mobile mechanics who lose 1-2 customers per week due to on-site price increases, and who absorb $500-$1,500/month in underquoted jobs to avoid confrontation.

## Impact If Fixed
Reduces on-site price adjustment incidents by 50-60%, recovers $500-$1,500/month in previously absorbed underquoting losses, and improves customer trust and rebooking rates by 20-30%.
