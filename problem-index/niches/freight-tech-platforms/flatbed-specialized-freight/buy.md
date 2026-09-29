# Truck Routing Engines Extended to Permit Constraints

**Niche:** [[niches/freight-tech-platforms/flatbed-specialized-freight/profile|Flatbed & Specialised Freight]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Commercial truck routing engines already model height, weight, length and hazmat restrictions across the national road network, and they stop exactly where oversize freight begins.
**Tags:** #graph-theory #dynamic-programming #optimization-fundamentals #evaluation-metrics #confidence-intervals #data-integration #compliance #automation
**Contested on:** Every serious competitor in specialised freight software is fighting to plan and re-plan a legal, permitted route for an oversize load without a permit service and a telephone — and whoever turns permitted routing into a self-serve minute takes the account.

## The Problem
A dispatcher uses a commercial truck routing product, which correctly avoids a low bridge and a restricted parkway for a standard tractor-trailer. For a sixteen-foot-wide load it is useless, because width restrictions, bridge load ratings for a specific axle configuration, and state-approved oversize routes are not in the model. So the routing engine, which has most of the road network data needed, is abandoned and the work is done manually.

## What Already Exists
Truck routing with restriction modelling is a mature commercial category — the major map and routing providers all offer it, with dimensional and hazmat restriction data maintained at national scale. State departments of transportation publish bridge inventory data, structural ratings, permit route maps and restriction notices. Road network data with geometry is commodity. The base layer is bought; the permit layer is the gap.

## The Customization Gap
The adaptation is to extend a routing engine with permit-domain constraints. It requires: (1) bridge structural capacity evaluated against the specific load's axle configuration and gross weight rather than against a posted limit, which is the technically demanding part and is where heavy haul routing actually differs from truck routing; (2) state permit rule sets as routing constraints — approved corridors, prohibited segments, superload thresholds above which routing becomes a case-by-case engineering review; (3) temporal constraints as first-class, since curfews, weekend and holiday restrictions and construction closures make a route legal at one hour and illegal at another, and most routing engines treat time only as traffic; (4) escort and utility coordination requirements surfaced as outputs, because they drive cost and lead time as much as the route does; and (5) a clear boundary where the engine stops and a human engineer is required, stated explicitly, since superloads genuinely require engineering judgement and a product that pretends otherwise is dangerous.

## Target Customer
Heavy haul carriers and permit services, the truck routing providers who could extend upward into this segment, and state permitting offices whose own review workload would fall.

## Impact If Solved
Extending a bought routing engine is far cheaper than building a network, and the permit constraint layer is where the entire value sits. The explicit boundary at superload complexity is what makes the product trustworthy in a domain where an overconfident answer is a bridge strike.
