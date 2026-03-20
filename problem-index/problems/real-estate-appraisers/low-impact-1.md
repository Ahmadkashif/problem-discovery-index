# Comparable Sale Selection Assistance

**Industry:** [[real-estate-appraisers|Real Estate Appraisers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** MLS search tools let appraisers filter and sort sales but don't rank comparables by overall similarity to the subject property — the multi-attribute similarity judgment that experienced appraisers make intuitively to select the three best comparables from 20 candidates.
**Tags:** #gradient-boosting #feature-engineering #cross-validation #evaluation-metrics #norms-and-inner-products #bias-variance-tradeoff #automation

## The Problem

Comparable sale selection is the most consequential judgment in a residential appraisal — the best three comps for this subject, from 15-25 candidates that pass basic proximity and recency filters. An experienced appraiser quickly identifies the three comps that best bracket the subject: similar in size (within 15% of GLA), similar vintage, similar condition, similar location tier, with minimal adjustments required. A junior appraiser selects comps that look fine on paper but require large adjustments, which creates CU risk and produces less defensible conclusions.

The selection judgment is multi-attribute: a comp that is slightly farther away but much more similar in size and condition is better than a nearby comp requiring large GLA adjustments. Formalizing this tradeoff into a similarity score is tractable.

## What Already Exists

MLS platforms allow filtering and sorting by individual attributes. Fannie Mae's CU scores appraisals after submission (backward-looking feedback). No tool scores comp candidates by overall multi-attribute similarity before the appraiser selects them.

## The Customisation Gap

A comp selection assistance tool needs: (1) the subject property's key attributes (GLA, bedroom/bath, age, condition tier, lot size, location); (2) a similarity scoring model that weights each attribute difference by its local market adjustment rate (a 200 sq ft GLA difference in a market where GLA adjustments are $80/sq ft is a $16,000 adjustment — more disqualifying than a 5-year age difference that carries a $2,000 adjustment in this market); (3) a ranked list of the 5-7 highest-similarity comparables with similarity score and estimated adjustment magnitude. The market-specific adjustment weighting is the domain component.

## Impact If Solved

Reduces comp selection time from 20-30 minutes of MLS searching to a 5-minute review of the ranked list. Reduces CU flags from poorly-selected comps with large adjustments. Enables junior appraisers to select defensible comps from their first independent assignments.
