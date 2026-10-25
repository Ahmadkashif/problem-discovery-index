# Stream-Level Routing Between Direct Burn and the Blend Tank

**Niche:** [[niches/hazardous-waste-firms/thermal-treatment/profile|Thermal Treatment: Incineration & Fuel Blending]]
**Industry:** [[industries/hazardous-waste-firms|Hazardous Waste Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A consolidator that owns both incinerators and fuel-blending outlets decides by habit which profiles burn directly and which go to cement-kiln fuel, so scarce incinerator slots are spent on waste a kiln could have taken.
**Tags:** #optimization-fundamentals #gradient-boosting #time-series-forecasting #feature-engineering #revenue-impact #workflow-orchestration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to destroy generators' high-hazard and high-heat-value wastes inside a combustion permit, but incinerator operators win by guaranteeing scarce burn capacity to the streams only an incinerator can take, while fuel blenders win by turning liquids into fuel a cement kiln will accept. Decomposed into contested sub-niches below.

## The Problem
An approved profile can often go more than one way. A solvent stream with high heat value may qualify for fuel blending, which earns a lower price but uses no incinerator capacity; the same stream with too much water, halogen or metal content for the kiln's specification must burn. Routing is set when the profile is approved and rarely revisited, even when the incinerators are full and the blend plant has room, or the reverse.

## Why Nobody Has Built This
The two outlets often sit in different business units with different P&Ls, systems and sales teams. The data to route well (profile fields, fingerprint history, kiln specifications, incinerator capacity) lives in separate systems, and routing decisions belong to approval chemists who route by experience.

## What to Build
A routing layer over approved profiles. For each stream it estimates eligibility for each thermal outlet from profile and fingerprint history against each kiln's specification and each incinerator's permit acceptance, forecasts capacity and margin by outlet over the next quarter, and proposes reassignments for the chemist to approve when one outlet tightens. It records why each stream went where, for the generator's file.

## Target Customer
Directors of disposal operations at networks with both incineration and fuel-blending capacity: Clean Harbors, Veolia and the larger independents.

## Impact If Built
Moving ~5% of direct-burn tons that qualify for blending (estimate) frees ~25,000–30,000 tons a year of incinerator capacity across a network of Clean Harbors' size, worth ~$15–30M of high-margin burn revenue at ~$600–1,000 a ton (estimate).
