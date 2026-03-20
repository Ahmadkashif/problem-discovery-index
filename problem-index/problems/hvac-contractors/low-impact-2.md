# Equipment Efficiency Upgrade Recommendation Engine

**Industry:** [[hvac-contractors|HVAC Contractors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic energy calculators exist but don't integrate a specific customer's equipment age, measured energy consumption, local utility rates, and available manufacturer rebates into a personalized 10-year cost-of-ownership comparison that a technician can present at the service call.
**Tags:** #linear-regression #feature-engineering #evaluation-metrics #arithmetic-and-basic-algebra #descriptive-statistics #automation #revenue-impact

## The Problem

HVAC equipment replacement is the highest-ticket sale in residential HVAC — a central system replacement is $6,000–$15,000. Equipment replacement is most successfully sold when the technician can present a data-driven economic case for replacement vs. continued repair: the current equipment's age, current SEER efficiency rating vs. available replacements, estimated utility savings from efficiency upgrade, available manufacturer and utility rebates, and the 10-year cost comparison of repair vs. replace.

Currently, this analysis requires a technician to manually look up utility rebates, remember the efficiency comparison across equipment tiers, and calculate projected savings — a 20-30 minute task that most technicians skip, defaulting to a simple price quote instead.

## What Already Exists

Carrier, Trane, and Lennox provide savings calculators on their websites that compare SEER ratings. Utility companies publish rebate databases. No tool integrates the customer's specific equipment data, local utility rate, and available rebates into a one-click sales presentation that a technician can generate on a tablet in 2 minutes.

## The Customisation Gap

An HVAC replacement recommendation tool needs: (1) current equipment data from the service call (model number, age, SEER from nameplate); (2) local utility rate from the address's utility territory; (3) current manufacturer and utility rebate lookup for the equipment tier being proposed; (4) a regression model estimating annual savings from efficiency upgrade given house size, equipment tonnage, climate zone, and SEER delta; (5) a formatted 10-year cost comparison presentation with visual display. The integration of these data sources — customer equipment, utility rate, rebate database, and savings model — requires HVAC domain knowledge to specify correctly.

## Impact If Solved

Enables every technician to deliver a data-driven replacement recommendation on equipment ≥ 10 years old. Equipment replacement rate on maintenance visit customers with data-driven recommendations vs. price-quote-only: estimated 2-3× higher close rate on replacement conversations.
