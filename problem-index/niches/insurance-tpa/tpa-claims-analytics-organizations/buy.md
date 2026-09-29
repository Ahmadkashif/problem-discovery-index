# Claims Platforms That Were Never Built to Be Queried

**Niche:** [[niches/insurance-tpa/tpa-claims-analytics-organizations/profile|TPA Claims Analytics Organizations]]
**Industry:** [[industries/insurance-tpa|Insurance Third-Party Administrators (TPAs)]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The claim history is in mainframe files, adjuster notes, and scanned documents, and the analytics team spends most of its time getting it out.
**Tags:** #data-integration #ocr #large-language-models #named-entity-recognition #workflow-orchestration

## The Problem
Pass 1 records the state of the estate: many TPAs run on legacy mainframe systems or heavily customized packages with manual workarounds. A single administrator may operate several platforms at once, inherited through acquisition, each with its own claim model, its own coding conventions, and its own decades of accumulated customization.

The analytically valuable content is worse than the structure. What actually happened on a claim lives in adjuster notes — free text entered under time pressure, containing the injury description, the treatment path, the reason a reserve moved, and the fact that an attorney called. Correspondence and medical documents arrive as scans. The structured fields carry codes whose meaning changed twice and whose lookup tables were edited in place.

So the analytics function's real work is data archaeology, and every new analysis starts by rebuilding an understanding of where the data is and what it means.

## What Already Exists
Data integration, warehousing, and lakehouse tooling is mature. Mainframe modernization and data virtualization products exist. Document processing and text analytics are commodity capabilities with strong vendors.

## The Customization Gap
The generic products assume a schema whose meaning is stable and documented. Neither holds.

**Semantics drift inside the same field.** A cause-of-loss code that meant one thing in 2011 and another after a system consolidation produces a false trend for anyone who does not know. Reconstructing what a field meant at a point in time is the precondition for any longitudinal analysis, and it requires a temporal semantic layer no integration platform provides.

**Adjuster notes are the primary source, not enrichment.** In most document-processing deployments text is supplementary. Here the structured record often says a reserve changed and the note says why. Extracting events — attorney retained, surgery authorized, return-to-work attempted and failed, settlement discussion opened — from terse operational prose is the core capability.

**Claim identity across merged platforms.** Acquisitions mean the same claimant and the same employer appear in several systems under different keys, and the corpus is only valuable joined. This is entity resolution over administrative records with weak identifiers and real privacy constraints.

**PHI has to be segregated by design.** Medical treatment records inside workers' compensation files are protected health information, and the analytics that matter — reserve accuracy, litigation prediction, duration — mostly do not need them. An architecture that separates the protected component from the rest is what makes the corpus usable at all, and generic integration tooling has no concept of it.

**Client data segregation with cross-client learning.** Each carrier and self-insured employer owns its own claims, and the models are far better trained across all of them. That is a data governance architecture, not a pipeline feature.

## Target Customer
Chief Data Officer or VP of Data Engineering at a large TPA, where analytics capacity is consumed by extraction rather than analysis.

## Impact If Solved
The analytics organization stops spending most of its effort assembling data and starts spending it on questions. More concretely, the adjuster note corpus is the richest description of claim causation anywhere in insurance, and it is currently unread — every model in this niche gets materially better the moment it becomes accessible.
