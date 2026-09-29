# Regulatory Information Management Without the Pharma Overhead

**Niche:** [[niches/hair-salons-independent/cosmetic-regulatory-consulting/profile|Cosmetic Regulatory & Safety Substantiation Consulting]]
**Industry:** [[industries/hair-salons-independent|Hair Salons (Independent)]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The available systems were built for one molecule over ten years, and cosmetics is ten thousand products over one year.
**Tags:** #data-integration #workflow-orchestration #compliance #automation #ocr

## The Problem
A consultancy serving twenty brands is tracking thousands of products across dozens of jurisdictions, each with its own registration requirements, ingredient restrictions, and labelling rules. Which products are registered where, which registrations expire when, which formulas contain an ingredient a jurisdiction just restricted, and what was filed for each — that is the operational core of the business.

It is run on spreadsheets. Not because nobody has tried to replace them, but because the replacements cost more than the practice earns and take longer to implement than a MoCRA deadline allows.

## What Already Exists
Regulatory information management platforms — Veeva Vault RIM, Ennov, ArisGlobal — are mature and genuinely capable: submission management, registration tracking, dossier assembly, change control, full audit trails. They are the backbone of pharmaceutical regulatory operations.

## The Customization Gap
The shape mismatch is close to total.

**Product count against per-product depth.** Pharma RIM is architected around a small number of products with enormous submission dossiers. Cosmetics inverts it: thousands of products, each with a comparatively thin file. Screens, workflows, and licensing models all assume the pharma shape, and the cosmetic user drowns in per-product ceremony.

**The formula is the object, not the product.** In pharma the active substance is fixed and the questions are clinical. In cosmetics the regulatory question is almost entirely about composition — which ingredients, at what concentration, in what product type — and a system that cannot query across formulas cannot answer the question the practice is actually asked most often, which is "which of our clients' products contain this."

**Ingredient restriction as a live feed.** Jurisdictions restrict and delist ingredients continuously. The needed primitive is a standing watch that maps a restriction change onto every affected formula in every client portfolio. Pharma RIM has nothing like it because the situation does not arise.

**Consultancy multi-tenancy.** These platforms assume one manufacturer managing its own portfolio. A consultancy manages many clients' portfolios with strict separation, while wanting to reuse ingredient-level knowledge across all of them. That is a data model the incumbents do not have.

**A price and implementation profile that fits.** Pharma RIM deployments are measured in hundreds of thousands of dollars and many months. A cosmetics practice needs something that pays for itself inside a compliance cycle.

## Target Customer
Head of regulatory operations at a cosmetic consultancy or at a mid-size manufacturer's in-house regulatory group — the same shape of problem, and the same absence of a fitting tool.

## Impact If Solved
The practice stops running its core asset on spreadsheets that one person understands. Restriction changes get answered in an afternoon instead of a fortnight. And the firm can take on portfolio volume that currently gets declined because tracking it manually is the actual constraint.
