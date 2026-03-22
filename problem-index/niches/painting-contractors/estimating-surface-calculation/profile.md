# Estimating & Surface Calculation

**Parent Industry:** [[industries/painting-contractors|Painting Contractors]]
**Category:** Highly Automatable

## Profile
**Market Size:** $2-3B (embedded in all painting segments)
**Share of Parent Industry:** Cross-cutting function embedded in every painting niche
**Digital Adoption:** Low-Medium — PaintScout and Estimate Rocket handle calculation but measurement input is still manual. LiDAR adoption is minimal. Most painters estimate square footage from memory or rough mental math.
**Target Buyer:** Painting company owner or estimator across all painting segments
**Automation Potential:** Very High — surface area calculation from photos is a computer vision problem with well-understood geometry, and material quantity estimation is a deterministic function of measured area, coating system, and application method

## What Makes This a Distinct Niche
Estimating accuracy is the single most important determinant of profitability in painting contracting. A 15% overestimate on square footage produces a bid that loses to competitors; a 15% underestimate produces a bid that wins but loses money. The average painting company's estimating error rate is 12-18% on square footage alone, before factoring in prep time variability. The root cause is that measurement is manual and time-consuming: an estimator in a furnished room must measure around furniture, estimate areas behind built-ins, calculate odd geometries (cathedral ceilings, angled walls, stairwells), and subtract non-paintable surfaces (windows, doors, stone fireplaces, tile backsplashes). The mental math required to convert these measurements into total paintable area, then into gallons of paint, primer, and coats of each, is error-prone even for experienced estimators. Material waste (over-ordering) runs 10-25% industry-wide, with small companies over-ordering more because they'd rather have leftover paint than make a second trip to the store.

## Current Tools & Gaps
PaintScout converts square footage into pricing, material quantities, and professional proposals — but it starts from manually entered measurements. MagicPlan creates floor plans from LiDAR or photos but outputs room dimensions, not paintable surface area. Room measurement apps (Planner 5D, RoomScan) measure walls but don't distinguish between paintable and non-paintable surfaces. Apple's LiDAR (iPhone Pro, iPad Pro) enables point-to-point measurement but not automated surface classification. No end-to-end solution takes room photos as input and produces paintable square footage plus material list as output.

## Problems
- [[niches/painting-contractors/estimating-surface-calculation/build|🔨 Build: AI Surface Area Calculator from Room Photos]]
- [[niches/painting-contractors/estimating-surface-calculation/buy|🛒 Buy: PaintScout Photo Measurement Input]]
- [[niches/painting-contractors/estimating-surface-calculation/fix|🔧 Fix: Material Quantity Calculation Errors]]
