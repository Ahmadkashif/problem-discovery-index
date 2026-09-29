# Return-Reason Text as a Supervised Fit Signal

**Niche:** [[niches/alterations-tailoring/fit-recommendation-vendors/profile|Apparel Fit & Returns Analytics Vendors]]
**Industry:** [[industries/alterations-tailoring|Alterations & Tailoring]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every return carries a free-text reason describing exactly where a garment failed on a real body, and the entire industry collapses it into a dropdown value called "fit" before anyone reads it.
**Tags:** #bert #transformers #large-language-models #transfer-learning #word-embeddings #contrastive-learning #evaluation-metrics #feature-engineering #data-integration #revenue-impact

## The Problem
The fit model is trained on a target that is far coarser than the data available. A retailer's return record carries a structured reason code — "too small," "too large," "fit" — and, on a substantial share of returns, a customer-written comment: tight across the shoulders, sleeves long, rides up at the waist, gapes at the bust. The first is a scalar. The second is a garment-region-level diagnosis of a specific failure on a specific body, volunteered for free, at a volume no fit trial could ever buy. Modelling uses the scalar because it is clean, and the comments sit in a text column nobody has structured. The consequence is a recommendation engine that can tell a shopper to size up but cannot tell a brand that its shoulder-to-bust grading breaks down two sizes above the base, which is the finding the brand would actually pay for.

## Why Nobody Has Built This
The text is messy in ways that defeat generic approaches. Customers describe garment regions in vernacular that maps onto pattern geometry only loosely and differently by garment category — "tight in the arms" means the bicep circumference on a jacket and the armhole depth on a knit. Comments arrive in many languages across a multinational retailer base. And the same complaint means opposite things depending on the garment's intended ease: "loose at the waist" is a defect on a tailored shirt and the design intent on an overshirt, so any labelling scheme has to be conditioned on the garment's own specification. Retailers also hold the comments in their own systems under contract terms written for order data, so the vendor often has access in principle and no pipeline in practice.

## What to Build
An engine that converts return comments into structured fit failures at the garment-region level. Comments are parsed against a region ontology tied to actual pattern geometry — shoulder, armhole, bicep, chest, waist, hip, rise, inseam — with a direction and severity attached, and conditioned on the garment's specification so intended ease is not scored as failure. Multilingual handling is a requirement rather than a phase two. The resulting labels feed two consumers. The recommendation model gains a supervision signal describing where garments fail rather than merely that they did, which is what lets it distinguish a shopper who needs a size up from one who needs a different block entirely. And the brand-facing product gains the finding that is currently impossible to produce: this style fails at the shoulder in the upper half of the size run, on bodies with this measurement profile, at this rate — traceable to a specific grading rule.

## Target Customer
VPs of data science at fit intelligence vendors running 50-200 analysts, and the technical design and merchandising leaders at the brands who buy the resulting reports and currently receive size-level aggregates rather than pattern-level diagnosis.

## Impact If Built
Changes what the vendor is able to sell. Size recommendation is a commoditizing feature that retailers increasingly build themselves; pattern-level fit diagnosis grounded in millions of real garment failures is not, and it is bought by a different and better-funded budget inside the brand. Because the label set is derived from text the vendor already receives, the marginal data cost is zero and the moat compounds with every season of returns.
