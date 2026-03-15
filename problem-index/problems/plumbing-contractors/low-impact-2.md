# Permit Requirement Identification by Job Type and Jurisdiction

**Industry:** [[plumbing-contractors|Plumbing Contractors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic permit databases exist but don't resolve the specific question a plumber faces: does this specific job type in this specific municipality require a permit, and if so, what inspections are required and what is the current fee schedule?
**Tags:** #llm #text-classification #nlp #compliance #automation

## The Problem
Plumbing permits are required for virtually all new installation work (new water heater, new fixture, new gas line) and most replacement work in most US jurisdictions, but the specific requirements vary significantly by municipality — what requires a permit in one county doesn't in the neighboring county; what triggers a full inspection in one city requires only a final in another. Experienced plumbers have internalized these rules for their primary service area over years of working with local building departments. When they move into a new service area, or when a junior plumber takes a job in an unfamiliar jurisdiction, the permit question requires either a call to the building department (20-30 minutes of hold time and often an ambiguous answer) or a guess based on general rules. Pulling permits on work that didn't require one wastes time and money; skipping permits on work that required them creates liability for both the contractor and the homeowner.

## What Already Exists
PermitFlow and BuildZoom provide some permit process automation for larger projects. State contractor licensing boards publish permit requirement guidance. Individual municipal building department websites contain the information but are structured inconsistently and require manual lookup. No tool aggregates permit requirements for residential plumbing work at the job-type + jurisdiction level and presents it in a decision-support format.

## The Customisation Gap
A plumbing-specific permit tool needs: a structured database mapping job types (water heater replacement, gas line addition, bathroom addition, sewer line replacement, backflow preventer installation) to permit requirements by jurisdiction, with current fee schedules and inspection type requirements. The maintenance of this database — as jurisdictions update their requirements — is the hard part. An LLM layer that synthesizes the database lookup into a plain-language answer ("yes, a permit is required for a water heater replacement in Denver County; fee is $85; one inspection required — final only; typical approval time is 3-5 business days") adds the last-mile usability.

## Impact If Solved
Eliminates the 20-30 minute building department call per unfamiliar-jurisdiction job. Reduces permit compliance errors — both the liability of skipped required permits and the inefficiency of unnecessary permit applications. Particularly valuable for contractors expanding their service area or for apprentices handling jobs in jurisdictions their master hasn't worked in recently.
