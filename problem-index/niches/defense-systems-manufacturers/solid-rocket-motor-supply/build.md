# A Qualification Evidence Engine for Second-Source Motors

**Niche:** [[niches/defense-systems-manufacturers/solid-rocket-motor-supply/profile|Solid Rocket Motor & Propellant Ingredient Supply]]
**Industry:** [[industries/defense-systems-manufacturers|Defense Systems Manufacturers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A new motor maker's path to rate runs through qualification, and the evidence (batch records, CT results, static fires, ageing data) is assembled by hand for every motor and every ingredient change.
**Tags:** #tacit-knowledge-ml #cnns #semantic-segmentation #gradient-boosting #large-language-models #compliance #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to put qualified motors on missile lines at the contracted rate, and whoever delivers the most flight-qualified motors per month takes the account.

## The Problem
Before a missile prime accepts a motor from a new source, the maker must prove that the motor and its components meet the specification across the required qualification environments, and that its process repeats. That proof is hundreds of documents: batch records, ingredient certificates, CT dispositions, static-fire data and test reports. When an ingredient source changes, parts of it must be rebuilt. Engineers spend months assembling evidence that already exists in fragments.

## Why Nobody Has Built This
Only two companies made these motors for most of two decades, and both built their evidence trails in-house. The data are ITAR-controlled and partly classified, so commercial quality software vendors have stayed out, and the new entrants are too young to have bought anything but an ERP.

## What to Build
An on-premises evidence engine that joins every batch's ingredient lots, process records, operator interventions, CT volumes and dispositions, and static-fire results into one record per motor; pre-marks CT indications against acceptance criteria for the radiographer; flags batches drifting from the qualified process; and assembles qualification and change-justification packages from the record, mapped to the prime's specification paragraphs.

## Target Customer
Quality and operations leaders at Anduril, Ursa Major, X-Bow and the incumbent motor plants, and propulsion supply-chain leads at the primes who review the evidence.

## Impact If Built
Cutting months from a second source's qualification adds motor supply when the industry needs it most. For a new entrant, every month earlier at qualified rate means hundreds of motors delivered (estimate) on a contract that might otherwise go to an incumbent.
