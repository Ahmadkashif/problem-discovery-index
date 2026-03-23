# AI-Guided Supplement Identification from Impact Pattern Analysis

**Niche:** [[niches/auto-body-shops/supplement-negotiation/profile|Supplement Negotiation Workflow]]
**Industry:** [[industries/auto-body-shops|Auto Body Shops]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool predicts which hidden damage a body shop will likely find during disassembly based on the visible impact pattern, vehicle structure, and collision severity — experienced estimators do this intuitively.
**Tags:** #cnn #multiclass-classification #computer-vision #tacit-knowledge-ml #revenue-impact

## The Problem
An experienced collision estimator looks at a rear-end impact on a 2020 Honda Accord and intuitively knows: the bumper reinforcement bar is bent (visible impact suggests 15+ mph), the trunk floor has rippling (energy transfer pattern on unibody), and the quarter panels need blend (paint won't match without blending adjacent panels). A junior estimator sees only the bumper cover and taillight damage. The experienced estimator writes an initial supplement immediately during disassembly because they anticipated the hidden damage; the junior discovers it piecemeal over 3 days, filing 2-3 supplements that irritate the adjuster and delay the repair.

## Why Nobody Has Built This
Mapping visible impact patterns to hidden damage requires a training dataset of thousands of collision repairs with before-disassembly photos labeled against after-disassembly findings. This dataset doesn't exist in structured form — it's distributed across shop repair files in CCC ONE and Mitchell, with no standardized way to correlate initial photos to final supplement data. The tacit knowledge lives in estimators' heads, developed over thousands of teardowns.

## What to Build
A computer vision system that analyzes photos of collision damage during initial assessment, cross-references against a database of similar impacts on the same make/model/year, and predicts probable hidden damage with confidence scores. The output is a "likely supplement checklist": "Based on this rear-end impact pattern on a 2020 Accord, check for: (1) bumper reinforcement bar deformation (92% probability), (2) trunk floor rippling (78% probability), (3) quarter panel stress cracking at wheel arch (65% probability)." The estimator uses this to write a comprehensive first supplement rather than discovering damage piecemeal.

## Target Customer
Body shop estimators writing 10-30 supplements per month who want to reduce supplement cycles from 2-3 per claim to 1 and increase total supplement recovery.

## Impact If Built
Reduces average supplement cycles per claim from 2.3 to 1.4, shortening repair time by 2-3 days. Increases total supplement recovery by 10-20% by catching damage that junior estimators miss. For a shop doing $100K/month in supplements, this represents $10K-$20K in additional monthly recovery.
