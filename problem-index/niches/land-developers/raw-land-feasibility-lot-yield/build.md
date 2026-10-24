# Yield Predictions Graded Against Final Plats

**Niche:** [[niches/land-developers/raw-land-feasibility-lot-yield/profile|Raw-Land Feasibility & Lot Yield Screening]]
**Industry:** [[industries/land-developers|Land Developers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Land teams price tracts on screened lot counts that are never compared with the lot counts the final plats actually recorded.
**Tags:** #gradient-boosting #cnns #semantic-segmentation #optimization-fundamentals #evaluation-metrics #tacit-knowledge-ml #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn a parcel into a lot count and cost per lot that a land committee will underwrite before the feasibility period ends, and whoever's screened lot counts land closest to the final recorded plats takes the account.

## The Problem
The lot count at screening sets what the developer can pay. If the final plat records fewer lots (because of a wetland, a detention pond, a street standard or a council condition) the land was overpaid, and the loss surfaces only when the project is built out.

## Why Nobody Has Built This
Screens and final plats live in different systems and different years, and layout vendors sell the screen, not its accuracy. Recorded plats are public but rarely digitised as lot counts linked to the original tract.

## What to Build
Link each screened tract to its recorded plats, count the lots, and build a model of the gap between screened and final yield from the constraints (floodplain, wetlands, slope, soils, utility depth, jurisdiction, product width). Apply it to each new screen as a correction with an interval, and show which constraints a layout tool typically underestimates.

## Target Customer
VPs of land acquisition at builders and developers screening hundreds of tracts a year.

## Impact If Built
A calibrated yield with an honest interval lets the developer bid what the land will actually produce. On a 300-lot tract, a 5% yield miss is 15 lots, ~$1.6M of lot revenue at Forestar's fiscal 2025 average of $108,400 a lot (estimate).
