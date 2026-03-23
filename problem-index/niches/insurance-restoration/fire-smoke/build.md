# Smoke Damage Salvageability Assessment Tool

**Niche:** [[niches/insurance-restoration/fire-smoke/profile|Fire & Smoke Restoration]]
**Industry:** [[industries/insurance-restoration|Insurance Restoration]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product helps restorers systematically assess whether smoke-damaged surfaces and contents can be cleaned or must be replaced, based on soot type, material, penetration depth, and cost-effectiveness.
**Tags:** #gradient-boosting #multiclass-classification #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
After a fire, experienced restorers walk through a property and make rapid clean-versus-replace decisions for hundreds of items and surfaces. A seasoned restorer looks at soot on a granite countertop and says "clean" — then looks at the same type of soot on a textured ceiling and says "replace." This judgment depends on soot chemistry (protein soot from kitchen fires penetrates differently than synthetic soot), surface porosity, cleaning method availability, and cost comparison (is it cheaper to clean or replace?). Junior technicians lack this judgment and either over-clean (wasting labor on unsalvageable items) or over-replace (increasing the estimate unnecessarily, which carriers challenge).

## Why Nobody Has Built This
The decision is multifactorial and contextual — the same soot type on the same material might be cleanable in one situation and not another based on exposure duration, ambient temperature during the fire, and whether fire suppression chemicals were used. Building a decision model requires capturing the expert's assessment alongside the variables they considered, across thousands of fire losses. This training data doesn't exist in structured form — it lives in the heads of experienced fire restorers.

## What to Build
A mobile assessment tool where the technician photographs a surface, selects the soot type (from a visual guide), surface material, and exposure characteristics, and receives a clean/replace recommendation with the recommended cleaning method if cleanable. Built on a decision model trained on assessments from experienced restorers across thousands of fire losses. Includes cost comparison (estimated cleaning cost versus replacement cost) to support the recommendation with economic logic carriers accept.

## Target Customer
Restoration companies handling 20-50 fire losses per year, employing junior technicians who need decision support for salvageability assessments.

## Impact If Built
Reduces salvageability assessment errors by 30-40%, preventing $2,000-$5,000 in wasted labor or unnecessary replacement per fire loss. Provides documented rationale for clean/replace decisions that reduces carrier disputes. Enables junior technicians to make expert-level assessments, reducing training time from 3 years to 6 months.
