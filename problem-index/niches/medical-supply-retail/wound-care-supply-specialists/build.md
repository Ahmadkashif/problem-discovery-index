# Wound Assessment to Product Selection Engine

**Niche:** [[niches/medical-supply-retail/wound-care-supply-specialists/profile|Wound Care Supply Specialists]]
**Industry:** [[industries/medical-supply-retail|Medical Supply Retail]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool maps wound characteristics (type, stage, size, drainage, infection status) to the optimal product selection from a formulary of hundreds of dressings — leaving product selection to clinical expertise that takes years to develop and varies by individual nurse.
**Tags:** #gradient-boosting #multiclass-classification #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
A wound care nurse evaluating a Stage III pressure ulcer with moderate drainage and no infection must select from 300+ dressing options: foam dressings for absorption, alginate for heavy drainage, hydrocolloid for light drainage, antimicrobial variants for infection risk, barrier creams for surrounding skin protection, and negative pressure wound therapy for non-healing wounds. The selection depends on wound characteristics, patient factors (allergies, skin sensitivity, self-care ability), and insurance formulary (which products are covered under this patient's plan). An experienced wound care nurse matches wound to product instantly from pattern recognition developed over years; a new nurse takes 30-60 minutes per patient and may select a suboptimal product that slows healing.

## Why Nobody Has Built This
Clinical wound care product selection has been treated as a clinical decision that only nurses and physicians can make, not a software problem. The knowledge base is complex: wound care product science evolves rapidly (new dressing technologies, updated clinical guidelines), formulary coverage varies by payer, and individual patient factors create exceptions to general rules. Building a recommendation engine requires structured capture of wound assessments, product selections, and healing outcomes across thousands of patients — data that exists in home health agency EHRs but has never been linked to DME supplier product selection data.

## What to Build
A wound-to-product matching tool that takes structured wound assessment data (wound type, stage/grade, dimensions, drainage level, infection status, surrounding skin condition) and patient factors (allergies, insurance formulary, self-care ability), applies clinical guidelines and formulary rules, and recommends a ranked product selection with clinical rationale. The system learns from outcomes: if a product selection leads to faster wound healing (measured by wound size reduction over time), that mapping is reinforced. Integrates with the supplier's inventory and billing system to verify product availability and insurance coverage before recommendation.

## Target Customer
DME suppliers with wound care product lines managed by clinical coordinators who want to standardize product selection, reduce clinical variation, and accelerate new hire competency.

## Impact If Built
Standardizes product selection across clinical staff, reducing the 20-30% variation in product choices between nurses for similar wounds. Reduces wound healing time by 10-15% through optimized product matching (clinical studies show appropriate dressing selection is the #1 modifiable factor in wound healing outcomes). Accelerates new wound care nurse competency from 12-18 months to 3-6 months.
