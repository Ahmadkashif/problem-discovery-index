# Configuration as Versioned, Testable Artefacts

**Niche:** [[niches/insurtech-platforms/policy-admin-and-billing/profile|Policy Administration & Billing]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Insurance product configuration is software written by people who are not called engineers, in a user interface with no diff, no branch and no automated test — which is why a configurable system produces a change cycle measured in months.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #automation #workflow-orchestration #compliance #data-integration #graph-theory
**Contested on:** Every serious competitor in policy administration is fighting to get a product, rate or form change into production across every state it is filed in without breaking billing, reporting or reinsurance — and whoever shortens that cycle most takes the account.

## The Problem
A product analyst changes a rating factor for one state. There is no way to see precisely what changed relative to what was there before, no way to develop it in isolation from three other changes in flight, no automated check that the premium for every affected risk moved the way it should and nothing else moved at all, and no record connecting the change to the filing that authorised it. Every one of those absences is a normal engineering practice that this discipline has not adopted, and together they are the reason the change cycle is long.

## Why Nobody Has Built This
Configuration was deliberately positioned as not-software, so that business users could change products without engineering — a genuinely valuable idea that arrived without any of the disciplines that make changing software safe. The vendors have followed, since a configuration experience that looks like an engineering workflow undercuts the positioning that sold the system. And carriers staffed the function with product and actuarial analysts rather than engineers, so nobody in the room has advocated for the practices they have never used.

## What to Build
Configuration as a first-class engineering artefact without making it feel like engineering. Every configuration change is versioned with a reviewable diff expressed in domain terms — this factor changed from this to that for these states, effective this date — rather than as a database delta. Changes develop in isolated branches and merge with conflict detection, because three product initiatives running simultaneously on the same rating structure is the normal case and is currently managed by scheduling. Every change runs an automated rating regression over a representative risk population, reporting what moved and by how much, which is the check that catches unintended effects. Filing linkage is structural: a rate configuration references the filing that authorises it, and a state whose production configuration diverges from its filed rate is detected automatically rather than at audit. The product surface stays a business user's tool; the discipline underneath it is the engineering one.

## Target Customer
Core system vendors, carriers running large configuration estates, and the implementation partners who currently supply headcount for manual validation.

## Impact If Built
Change velocity is the entire value proposition of a modern core system and is consumed by validation. Automated rating regression with a domain-level diff removes the largest block of the cycle and, in doing so, delivers what the configurability was bought for. The filing linkage also converts a compliance exposure managed by diligence into one managed by a check.
