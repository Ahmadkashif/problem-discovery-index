# Weight Rating Mismatches Discovered After Sale

**Niche:** [[niches/rv-dealerships/towable-rv-segment/profile|Towable RV Segment]]
**Industry:** [[industries/rv-dealerships|RV Dealerships]]
**Type:** Fix (Pain Point)
**One-liner:** Customers buy trailers their trucks can't safely tow because salespeople don't verify specific tow ratings — the mismatch surfaces as instability, overheating, or brake failure on the first highway trip.
**Tags:** #compliance #automation #revenue-impact #worker-facing

## The Problem
A customer buys a 9,500-lb travel trailer with a truck rated to tow "up to 10,200 lbs." On paper, there's margin. In reality, the truck's specific configuration (with the smaller engine, standard axle ratio, and crew cab) is only rated for 8,400 lbs. The salesperson used the headline tow rating from the manufacturer's website rather than the configuration-specific rating from the tow guide. The customer experiences trailer sway, brake fade, and transmission overheating on their first trip through mountains. They return the trailer, demand a refund, leave a 1-star review, and may pursue legal action. This scenario occurs 5-10 times per year at a typical high-volume towable dealer.

## Why It's Still Broken
Tow rating verification is treated as the customer's responsibility ("consult your vehicle's owner's manual"). Salespeople are not trained or required to verify specific tow ratings — they rely on the customer's assertion that "my truck can handle it." The DMS doesn't flag potential mismatches because it doesn't capture tow vehicle data as part of the sales process. Liability waivers exist but don't prevent the customer relationship damage, negative reviews, and potential lawsuits.

## What a Fix Looks Like
A mandatory tow compatibility check built into the sales process — when the deal is written in the DMS, the system requires the customer's tow vehicle information (VIN preferred) and runs an automated compatibility check against the trailer's specifications. If the truck is under-rated, the system blocks the sale or requires a manager override with documented customer acknowledgment. The check becomes a liability shield for the dealer and a safety gate for the customer.

## Who Feels the Pain
Customers who discover their truck-trailer combination is unsafe only after a dangerous highway experience, and dealer principals who face returns, negative reviews, and potential liability claims from tow mismatches.

## Impact If Fixed
Prevents 5-10 unsafe tow matches per year per dealership, each costing $5,000-$15,000 in returns, goodwill, and potential legal exposure. Protects the dealer from liability claims that can reach $50K-$500K for accidents caused by overloaded tow combinations.
