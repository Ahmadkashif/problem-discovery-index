# Real-Time Supply House Inventory Lookup

**Niche:** [[niches/electrical-contractors/small-rural-electricians/profile|Small & Rural Electricians]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Fix (Pain Point)
**One-liner:** Rural electricians drive an hour to the supply house only to find the needed breaker or panel is out of stock — a real-time inventory and pricing lookup across nearby distributors would eliminate wasted trips and enable phone-based ordering for pickup.
**Tags:** #data-integration #automation #worker-facing #revenue-impact

## The Problem
A rural electrician gets a service call: the homeowner needs a new 200A panel and main breaker. The electrician drives 45 minutes to the supply house, walks in, and discovers they're out of the Square D QO 200A panel — they have the Siemens equivalent, but the homeowner's existing branch breakers are Square D and won't fit a Siemens panel. The electrician either buys the Siemens panel and all new breakers (spending an extra $200+ in materials that the estimate didn't include), drives another 30 minutes to a second supply house that might have the Square D, or orders it for 2-3 day delivery and reschedules the job. Each of these outcomes costs the electrician 1-3 hours and $50-300 in unbillable time or margin compression. This scenario plays out 2-4 times per week for rural electricians, especially for less common items (specific breaker types, large wire sizes, specialty connectors).

## Why It's Still Broken
Electrical distributors operate on a branch model — each location has its own inventory that varies based on local demand patterns. Distributor B2B portals show inventory by location but require logging into each distributor's system separately and searching by manufacturer part number (not always known to the field electrician who thinks in terms of "200A Square D main lug panel" not "QO140L200PG"). No tool aggregates inventory across multiple distributors in a geographic area. Distributors are reluctant to share real-time inventory data with third parties because it reveals competitive information (what's selling, what's overstocked). The data integration challenge is compounded by inconsistent product naming across distributors.

## What a Fix Looks Like
A mobile app where the electrician searches by description ("200A Square D panel, main lug, 40 space"), and the system returns real-time stock status and pricing at all electrical distributors within a configurable radius (e.g., 60 miles). Results show: in-stock quantity, price, distance, and drive time. The electrician selects a distributor, places a hold or order for pickup, and gets confirmation before driving. Data comes from a combination of distributor B2B portal integrations (where available), web scraping of distributor inventory pages, and community-sourced updates ("I was just at Graybar Springfield — they're out of 200A Square D QO panels"). Product matching uses a trained model to map electrician descriptions to distributor SKUs across inconsistent naming conventions.

## Who Feels the Pain
Rural electricians who lose 3-6 hours per week to wasted supply house trips, their customers who experience project delays when materials aren't available, and the electricians' bottom line — each wasted trip costs $100-200 in unbillable drive time.

## Impact If Fixed
Eliminates 60-80% of wasted supply house trips, recovering 2-4 hours per week of billable time ($150-600/week at typical rates). Reduces material cost variance by enabling price comparison across distributors before purchasing. Improves customer experience by accurately communicating material availability and project timelines upfront.
