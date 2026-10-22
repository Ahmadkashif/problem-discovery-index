# The Pool's Property Schedule Built From Members' Spreadsheets

**Industry:** [[self-insured-benefit-pools|Self-Insured Benefit & Risk Pools]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every property renewal, a public entity pool stitches hundreds of members' building, vehicle and infrastructure lists into one statement of values for reinsurers, and commercial property valuation tools were not built for fire stations, water plants, bridges and park shelters.
**Tags:** #cnns #k-nearest-neighbors #gradient-boosting #feature-engineering #data-integration #automation #revenue-impact

## The Problem
A pool covering 250 cities, counties and special districts buys property reinsurance or excess cover above its retention every year, usually for a July 1 or January 1 renewal. The reinsurers price from a statement of values (SOV): every scheduled building with address, construction, occupancy, year built, square footage, protection class, roof and replacement cost, plus vehicles, contents and specialised assets. The pool does not own the assets. It asks each member for an updated schedule in the spring, and receives spreadsheets in a dozen layouts, PDFs from the finance office, and a note from a town clerk that nothing has changed since 2019. AGRiP's 2025 primer notes that many pools still keep exposures and underwriting calculations in spreadsheets. Montana's schools pool did its underwriting entirely in them before moving to a pool management system.

The consequences are concrete. Undervalued buildings leave members underinsured after a hail or wildfire loss: CIRSA's members had $15.4M of 2023 hail claims reserved while inspections were still running. Missing construction and roof data draws loadings, sublimits and exclusions from reinsurers. Pool underwriters spend the weeks before renewal cleaning data instead of negotiating terms.

## What Already Exists
Commercial property valuation tools and appraisal firms estimate replacement cost for standard building types. Catastrophe modelling vendors and reinsurance brokers run the SOV through hazard models. Pool management systems such as Origami Risk hold the schedule and give members a portal to update it. Geocoding and aerial imagery services can confirm a building exists and measure its roof.

## The Customisation Gap
The gap is public-entity assets and the pool's annual collection cycle. Valuation tools are calibrated on commercial and residential stock, not on wastewater plants, fire stations with apparatus bays, historic town halls, swimming pools, pump stations and bridges. Pools need the member-facing workflow: pre-filling last year's schedule, flagging assets whose values have not moved with construction cost trend, matching member lists to imagery and parcel data to find unscheduled buildings, and checking occupancy and construction against what the reinsurer's model needs. A customised layer would also reconcile the property schedule with the pool's own claim history, so a building that has had three roof claims is not still listed with a 2005 roof.

## Impact If Solved
A pool could cut the spring data chase from weeks to days, present reinsurers a cleaner schedule that earns better terms, and stop discovering underinsurance on the day of the loss. For members, contributions would track actual values instead of whatever was typed into a spreadsheet years ago.
