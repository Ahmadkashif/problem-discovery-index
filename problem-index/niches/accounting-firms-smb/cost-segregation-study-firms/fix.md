# Site Inspection Photo Archives Are Evidence, Not Data

**Niche:** [[niches/accounting-firms-smb/cost-segregation-study-firms/profile|Cost Segregation Study Firms]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Every study generates hundreds of site photographs that are filed as substantiation and never looked at again — even though they are a labeled visual record of exactly the components the firm spends its days classifying.
**Tags:** #cnns #object-detection #semantic-segmentation #transfer-learning #evaluation-metrics #data-integration #automation

## The Problem
A site inspection produces 200-600 photographs documenting components, finishes, dedicated equipment, and site improvements. They go into the file as substantiation — proof the engineer was there and the component exists. They are named by camera default, stored in a folder per property, and never referenced again unless an examination requires them. Meanwhile the engineer writes component descriptions from field notes, and when a description is ambiguous months later there is no practical way to find the photograph that would resolve it among four hundred untitled images. The firm has, in aggregate, hundreds of thousands of photographs of building components that it has already classified in the accompanying study — a labeled dataset assembled at considerable cost and used once.

## Why It's Still Broken
Photographs are treated as a compliance artifact rather than an input, so no part of the workflow asks anything of them. Document management systems index by file and folder, not by content, and nothing links a photograph to the component line it substantiates — that association exists only in the engineer's head during the inspection and evaporates on upload. Building the link retroactively across an archive is not feasible by hand, and no cost segregation firm has treated its photo archive as an asset worth the engineering effort to organize.

## What a Fix Looks Like
Two connected changes. At capture, the field application ties each photograph to the component being documented, so the association is recorded when it is free rather than reconstructed when it is expensive — the engineer is already looking at the component and already logging it. Across the archive, a vision model trained on the firm's own historical photographs paired with the classifications from their accompanying studies learns to recognize recurring component types, letting the system propose component identification and draft descriptions from the inspection photos themselves, and letting an engineer retrieve every prior photograph of a given component type across all properties. The immediate payoff is retrieval and description drafting; the durable payoff is that the archive becomes a growing labeled dataset in a domain where no public equivalent exists.

## Who Feels the Pain
Field engineers who photograph diligently and derive nothing from it; report writers who cannot resolve an ambiguous field note without calling the inspector; and examination defense staff who must locate specific substantiation in an unindexed archive years after the fact.

## Impact If Fixed
Turns the largest untapped data asset in the practice into working infrastructure. Cuts description drafting and makes substantiation retrievable on demand during examination. Over time, component identification from inspection photographs shortens the inspection-to-draft cycle, which is the constraint on how many studies a given engineering headcount can deliver in a filing season.
