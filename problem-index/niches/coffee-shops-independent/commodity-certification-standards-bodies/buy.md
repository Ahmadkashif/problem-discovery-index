# Chain of Custody Tracing Adapted to Aggregated Supply

**Niche:** [[niches/coffee-shops-independent/commodity-certification-standards-bodies/profile|Agricultural Certification Standards Bodies]]
**Industry:** [[industries/coffee-shops-independent|Independent Coffee Shops]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Supply chain traceability platforms track a lot through custody transfers; certified coffee is pooled, blended, and mass-balanced at every stage, so the thing being traced stops being a physical lot several steps before the roaster.
**Tags:** #graph-theory #graph-neural-networks #optimization-fundamentals #evaluation-metrics #probability-distributions #confidence-intervals #compliance #data-integration #automation #workflow-orchestration

## The Problem
The certification seal makes a claim about origin that the physical supply chain cannot literally support. Cherries from many smallholders are pooled at a wet mill, dry mills combine lots, exporters blend to specification, and importers pool further — and most schemes permit mass balance accounting precisely because physical segregation is impossible at smallholder scale. So the credible claim is an accounting one: certified volume entering the chain must be at least the certified volume leaving it, tracked through every transformation. Verifying that today means reconciling volume declarations across dozens of independent operators with different systems, largely by hand, and the reconciliation is exactly where over-selling of certified volume occurs — the failure mode that most damages a scheme when it surfaces.

## What Already Exists
Supply chain traceability is a crowded market. SAP's traceability suite, Provenance, TE-FOOD, Transparency-One, and a long list of blockchain-based platforms all handle custody transfer recording, event capture against standard schemas, document attachment, and participant onboarding. Several are marketed specifically at agricultural commodities and deforestation compliance.

## The Customization Gap
Nearly all of them model a physical unit moving through custody, which is the wrong model for a mass-balance commodity. When product is pooled and blended, per-lot provenance is not merely hard to capture — it does not exist, and a platform that pretends otherwise produces a false record rather than a missing one. What the scheme actually needs is a volume conservation model over the transformation network: certified volume as a conserved quantity flowing through pooling, processing yield factors, and blending, with reconciliation testing whether the declarations across all participants are mutually consistent. Yield factors are the crux — the conversion from cherry to parchment to green varies by region and season, and a wrong factor is indistinguishable from over-selling, which is why reconciliation needs empirically estimated yield distributions rather than fixed constants. The adaptation is that conservation model plus anomaly detection over the declaration network, flagging participants whose declared flows cannot be reconciled with their neighbours' — which is the analysis that finds over-selling and that no custody-tracking platform performs.

## Target Customer
Heads of assurance and chain of custody at certification bodies, and the sustainability compliance teams at roasters who must now demonstrate due diligence on physical supply under deforestation regulation.

## Impact If Solved
Addresses the specific integrity failure that most damages certification schemes, using a model that matches how the commodity actually moves rather than one that assumes it away. As deforestation rules push toward physical traceability, being able to state precisely where the chain is segregated, where it is mass-balanced, and how well the accounting reconciles is the difference between a defensible scheme and a contested one.
