# Voyage Management Systems Extended to Fixture Grading

**Niche:** [[niches/ocean-shipping-carriers/dry-bulk-tanker-chartering/profile|Dry Bulk & Tanker Chartering]]
**Industry:** [[industries/ocean-shipping-carriers|Ocean Shipping Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Voyage-management systems already hold the estimate and the actual voyage result; they rarely join the two into a grade for each fixture.
**Tags:** #linear-regression #evaluation-metrics #feature-engineering #data-integration #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to fix each open ship on the cargo that earns the most once port time, bunkers and laytime are counted, and whoever fixes the fleet at the highest time-charter equivalent against the Baltic route average takes the account.

## The Problem
Owners run estimates, fix, perform the voyage and close the accounts in one system, then judge the desk on total earnings, which mix market luck with chartering skill.

## What Already Exists
Veson IMOS and similar voyage-management systems track estimates, fixtures, voyage P&L, laytime and post-fixture accounts. Baltic Exchange indices give the market benchmark.

## The Customization Gap
Grading a fixture needs the estimate as made, the voyage as performed and the market at the fixing date. Each fixture's TCE must be compared with the relevant Baltic route assessment for the same window and ship size, with differences attributed to rate, speed and consumption, port time, laytime outcome and ballast. Owners' fleets differ from the index's standard ship, so the benchmark needs adjusting for size and consumption. That reporting layer, and the discipline of freezing the estimate at fixing, is the customisation.

## Target Customer
Commercial directors at tramp owners and pool managers who report earnings against the index to investors.

## Impact If Solved
A fixture-by-fixture view of where the desk beats or trails the market, separating skill from luck. A desk that finds $300 a day of systematic underperformance on 20 ships and fixes it recovers ~$2.2M a year (estimate).
