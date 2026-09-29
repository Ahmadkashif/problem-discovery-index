# Eligibility Rules From Documents Nobody Standardized

**Niche:** [[niches/mortgage-brokers/product-pricing-engines/profile|Product & Pricing Engines]]
**Industry:** [[industries/mortgage-brokers|Mortgage Brokers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Every lender publishes its own guidelines in its own prose, and the engine has to turn all of them into executable rules that are right today.
**Tags:** #ocr #large-language-models #text-classification #workflow-orchestration #data-integration

## The Problem
The engine's accuracy rests on two content streams. Rate sheets arrive daily, sometimes several times a day, in each lender's own format. Guidelines arrive as documents — matrices, bulletins, overlays on the investor guides — describing eligibility in prose that must become executable rules.

Both change constantly. A lender adds an overlay, adjusts an adjustment grid, or changes a documentation requirement, and the engine must reflect it before the next search or it returns a price the lender will not honour.

The work is done by content analysts reading documents and configuring rules. It is the largest operating cost, the constraint on how many lenders can be supported, and the source of every accuracy failure.

## What Already Exists
Document extraction and rules engines are mature, separately. Business rules management systems handle complex eligibility logic well. Language models read structured documents competently.

## The Customization Gap
The generic tools handle the pieces and not the specific shape of this content.

**Guidelines are overlays on overlays.** A lender's rules are the investor guide, plus the lender's overlays, plus programme-specific exceptions, plus temporary bulletins — and the operative rule is the composition. Modelling that inheritance explicitly, so a change to a base guideline propagates to every lender that adopts it, is the structural fix and no rules platform provides it.

**Rate sheets are dense, formatted, and non-standard.** Adjustment grids arrive as tables in PDFs with lender-specific conventions, and a misread adjustment produces a wrong price on every matching scenario until someone notices.

**Effective dating down to the hour.** Rate sheets supersede intraday, guidelines have effective dates, and a lock must be honoured under the terms in force at lock time. Reconstructing what the engine should have said at a moment last quarter is a dispute-resolution requirement.

**Errors are silent and directional.** A too-restrictive rule means the lender never appears and nobody complains; a too-permissive one produces a price the lender rejects and a broker escalation. Only one direction generates feedback, so error detection must be active rather than reactive.

**Cross-lender consistency as a check.** Comparable products across lenders should price within a band, and an outlier is usually a content error rather than a market position. That check is computable and rarely automated.

## Target Customer
VP of Content Operations or Chief Technology Officer at a pricing engine provider, where content maintenance governs lender coverage and content error is the product's main failure mode.

## Impact If Solved
Coverage and accuracy are the entire competitive claim, and both are constrained by analysts reading documents. Modelling guideline inheritance and detecting the silent over-restrictive errors improves the product on both axes — and lets the engine add lenders without adding analysts, which is the growth constraint.
