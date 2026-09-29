# Permitted Routing Across State Rule Sets

**Niche:** [[niches/freight-tech-platforms/flatbed-specialized-freight/profile|Flatbed & Specialised Freight]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every state publishes its oversize permit rules, restrictions and routes, and planning a four-state heavy haul move is still a permit service on the telephone with a stack of PDFs.
**Tags:** #graph-theory #dynamic-programming #optimization-fundamentals #large-language-models #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in specialised freight software is fighting to plan and re-plan a legal, permitted route for an oversize load without a permit service and a telephone — and whoever turns permitted routing into a self-serve minute takes the account.

## The Problem
A transformer moves from Ohio to Texas: sixteen feet wide, fourteen feet six inches high, 180,000 pounds. Each state has its own permit application, its own fee calculation, its own approved routes for those dimensions, its own escort and curfew requirements, and its own lead time. Some states will route you; some require you to propose a route. The dispatcher works through it over two days with a permit service, and when a bridge on the approved route in one state goes under repair a week later, the whole thing is redone. Every rule involved is published.

## Why Nobody Has Built This
Assembling fifty states' permit rules, restriction data and route networks is a substantial content and data acquisition project with no standard formats and inconsistent publication, and the segment is small enough that no general freight platform has wanted to fund it. The permit services, who have the expertise, are service businesses whose value is precisely the expertise — automating it commoditises them, which is a familiar dynamic. And the correctness bar is high: a routing error puts an oversize load onto a bridge that cannot carry it, which is a safety event rather than a service failure, so the product must be right rather than helpful.

## What to Build
A permitted routing engine over an assembled, maintained cross-state rule and restriction dataset. Road network with structural attributes — clearances, bridge ratings, geometry — combined with each state's dimensional thresholds, approved and restricted routes, curfews, escort requirements and seasonal limits. Routing is a constrained path problem over that network for the specific load's dimensions and weight, returning a route that is permittable rather than merely drivable, with the permits required at each state line, the fees, the lead times and the escort requirements enumerated. Re-planning on a restriction change is the same query run again, which is where the value concentrates because it is currently the most painful scenario. Confidence and provenance matter as much as the answer: every constraint applied cites its source, and anything the dataset does not cover is stated as unknown rather than silently ignored.

## Target Customer
Heavy haul and specialised carriers, permit services who would rather scale than staff, project cargo forwarders, and the utility, wind energy and industrial shippers who move this freight regularly.

## Impact If Built
Two days of dispatcher and permit service work per complex move, reduced to minutes, in a segment where the per-load values are high enough to justify real software. The re-planning case is the sharper one: a mid-move restriction change currently costs days and can strand a load, and a re-query is the difference between a delay and a crisis.
