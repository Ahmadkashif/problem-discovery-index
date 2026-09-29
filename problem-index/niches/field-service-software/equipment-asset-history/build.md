# The Equipment Record Built From the Visit's Own Artefacts

**Niche:** [[niches/field-service-software/equipment-asset-history/profile|Equipment Asset History]]
**Industry:** [[industries/field-service-software|Field Service Software]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every platform has an equipment record, almost none are populated, and the reason is that filling one in costs a technician ten unpaid minutes for a benefit somebody else collects later.
**Tags:** #cnns #transformers #large-language-models #evaluation-metrics #confidence-intervals #data-integration #automation #worker-facing
**Contested on:** Every serious competitor in field service is fighting to populate an equipment record completely without costing the technician a minute — and whoever gets record completeness per visit highest takes the capability everything else in the category depends on.

## The Problem
A technician services a furnace. The equipment record for that address is empty, or contains "Carrier" and nothing else. Filling it properly means finding the nameplate, photographing it, transcribing a model and a serial, estimating an install date, noting the configuration and accessories, and assessing condition — ten minutes in a crawlspace at the end of a job. He skips it, as does the next technician, and as does everyone at every contractor in the country. The industry's most consequential dataset is empty by rational individual choice.

## Why Nobody Has Built This
The incentive structure is the whole problem and it has been treated as a discipline issue rather than a design one — contractors respond with policies requiring equipment capture, technicians respond with placeholder entries, and the data is worse than nothing because it looks populated. The technology to make capture nearly free has only recently become reliable enough: reading a model and serial off a nameplate photograph taken in poor light at an angle is a real vision problem, and doing it well requires per-manufacturer layout knowledge that no general text recognition supplies.

## What to Build
A record assembled from artefacts the visit produces anyway. One photograph of the nameplate yields make, model and serial through recognition tuned per manufacturer layout, with install date inferred from serial number encoding where the manufacturer's scheme is known — which it is, for most major brands, as published or reverse-engineered convention. Accessories and configuration are inferred from the other photographs taken during the job. Condition is captured from the technician's spoken summary, which they are giving anyway under the technician-tools niche, rather than as a separate assessment form. Parts consumed are scanned. The technician's only deliberate act is a photograph they would frequently take regardless, and a confirmation. Completeness per visit is the metric, published to the contractor, because it is the only way anyone will know whether the problem is being solved.

## Target Customer
Every field service platform vendor, and directly the contractors running maintenance agreement programmes whose economics depend on knowing what equipment they have agreed to maintain.

## Impact If Built
A populated equipment base unlocks the category's most valuable capabilities at once: diagnosis prediction, maintenance agreement management, replacement and warranty recovery. Warranty recovery alone is usually enough to fund it — contractors routinely fail to claim manufacturer warranty on parts because the serial number was never recorded. This is the foundational niche in field service and the one whose absence explains most of the others.
