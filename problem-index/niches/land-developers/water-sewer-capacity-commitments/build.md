# Capacity Availability Map From Public Utility Records

**Niche:** [[niches/land-developers/water-sewer-capacity-commitments/profile|Water & Sewer Capacity Commitments]]
**Industry:** [[industries/land-developers|Land Developers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Developers learn whether a provider can serve a tract only by asking, one tract at a time, when plant capacities, service areas and committed connections are largely public.
**Tags:** #feature-engineering #gradient-boosting #survival-analysis #data-integration #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to secure binding water and sewer service commitments for a tract's planned lots before the land closes, and whoever obtains binding commitments covering the highest share of planned lots before closing takes the account.

## The Problem
Before tying up land, a developer wants to know which water and sewer providers could serve it, whether they have capacity, and how long a commitment will take. Today the answer comes from the utility engineer's memory and a letter request that can take months.

## Why Nobody Has Built This
The data is scattered: service-area maps at state commissions, plant capacity and flows in discharge permits and annual reports, committed connections in utility board minutes and development agreements, and district creation records. Each state is different, and no data vendor has treated utility capacity as a land dataset.

## What to Build
A map layer of providers and service areas, with plant capacity, current flows, and connections committed in board actions and development agreements, assembled from public filings and minutes. Add a history of commitments and how long they took per provider, and a screening score per tract: likely provider, headroom, expected months to a commitment.

## Target Customer
Land acquisition teams at builders and developers in Texas, Arizona, Utah, Idaho, Florida and other growth markets where capacity binds.

## Impact If Built
Screening out tracts with no near-term capacity before the earnest money goes hard avoids the most expensive kind of failed deal: ~$0.1–0.5M of non-refundable deposits, extension payments and studies per tract (estimate). It also sets realistic utility timelines for the rest.
