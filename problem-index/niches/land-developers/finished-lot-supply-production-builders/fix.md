# The Dry-Utility Request Sent Too Late

**Niche:** [[niches/land-developers/finished-lot-supply-production-builders/profile|Finished-Lot Supply to Production Builders]]
**Industry:** [[industries/land-developers|Land Developers]]
**Type:** Fix (Pain Point)
**One-liner:** Lots sit paved and accepted but undeliverable for months because the electric, gas or fibre design request went in after the paving plans were final.
**Tags:** #survival-analysis #workflow-orchestration #data-integration #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to deliver finished lots into each builder's takedown schedule, phase by phase, and whoever delivers the highest share of contracted lots by the contract delivery date takes the account.

## The Problem
Electric co-ops and utilities, gas companies and fibre providers each design and install service to a new phase on their own queue. Their design cannot start until they have the final plat or utility layout, and their install waits on materials (transformers have had long lead times) and crews. Developers routinely submit the requests late, when paving is under way, and the dry utilities become the last item holding the takedown.

## Why It's Still Broken
No one owns the trigger. The civil engineer finishes the plans, the superintendent is running the wet utilities and paving, and the utility application sits with whoever remembers. Each provider's real lead time is known only to superintendents who have waited on it before. The provider's side is mapped under Electric Utilities at [[niches/electric-utilities/new-service-connection-design/profile|New Service Connection Design]].

## What a Fix Looks Like
Tie each provider's application to a project milestone (approved utility plans, preliminary plat), with a lead time learned from the developer's own history per provider and region. Alert when a phase's projected paving completion minus the provider's lead time has passed without a submitted request, and track each request's status in the delivery schedule.

## Who Feels the Pain
Superintendents blamed for late lots; builders with starts planned on lots that cannot get a meter; finance carrying finished lots it cannot bill.

## Impact If Fixed
Starting dry-utility requests on time removes the most common avoidable wait between paving and takedown, often weeks to months per phase (estimate), at almost no cost.
