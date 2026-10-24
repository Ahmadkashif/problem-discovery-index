# Split-Eligibility Screen Across a City's Parcels

**Niche:** [[niches/land-developers/infill-lot-split-subdividers/profile|Infill Lot-Split & Small-Lot Subdividers]]
**Industry:** [[industries/land-developers|Land Developers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Infill developers check one parcel at a time whether it can be split, when the rules, parcel geometry and past approvals could screen a whole city overnight.
**Tags:** #feature-engineering #gradient-boosting #large-language-models #evaluation-metrics #quick-win #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to identify the urban parcels that current zoning and state lot-split laws let it divide and get each split approved without a variance, and whoever gets the most splits approved per hundred parcels it pursues takes the account.

## The Problem
A small infill developer looks at listings and off-market parcels and asks, for each, whether it can legally be split and into how many lots. The answer depends on lot dimensions, frontage, the zoning district, the state's split law and the city's implementing ordinance, plus easements and utility access, and it takes a planner's or surveyor's time per parcel.

## Why Nobody Has Built This
The rules are new, changed often, and differ by city. Parcel geometry from assessors is approximate, and easements are buried in recorded documents. The buyers are small firms.

## What to Build
Encode a city's split and minimum-lot rules, run every parcel's geometry and zoning against them, add easement and utility checks where data allows, and learn from the city's approved and denied split applications which parcels actually get through. Output a ranked list of qualifying parcels with the expected lot count and the main risk for each.

## Target Customer
Small infill developers and owner-builders in cities that have adopted lot-split or small-lot rules.

## Impact If Built
Screening a whole city instead of single parcels finds the qualifying lots first. If ~1 in 3 surveyed parcels would fail, screening first saves ~$3–5K of survey and design on each one (estimates).
