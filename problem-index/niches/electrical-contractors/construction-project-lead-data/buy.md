# Plan Extraction Adapted to Trade Scope

**Niche:** [[niches/electrical-contractors/construction-project-lead-data/profile|Construction Project Lead & Plan Data]]
**Industry:** [[industries/electrical-contractors|Electrical Contractors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Document AI reads construction drawings well enough to extract text and sheets; what an electrical contractor needs to know is whether there is enough electrical work in this project to be worth pursuing, which is a scope judgment nobody automates.
**Tags:** #cnns #object-detection #transformers #bert #large-language-models #transfer-learning #evaluation-metrics #feature-engineering #automation #data-integration

## The Problem
Leads are classified by project type and total value, and a trade subscriber needs something different — the size and character of their portion. An electrical contractor deciding whether to pursue a project wants to know the approximate electrical scope, whether it involves the systems they specialize in, and whether the design suggests complexity they price well. Determining that means reading the drawings, which the publisher's researchers do at the level needed for classification and not at trade scope depth. So subscribers download plan sets and make the judgment themselves, one project at a time, which is the expensive part of pursuit qualification and the reason estimating capacity gets wasted.

## What Already Exists
Construction document AI is a real and improving market. The document intelligence services handle sheet classification, text extraction, and table parsing on drawing sets; several construction-specific vendors offer takeoff assistance and drawing search; symbol detection on plans is an established capability.

## The Customization Gap
Available tooling is built either for general document extraction or for detailed takeoff on a project a contractor has already committed to. The gap is the qualification layer in between — a fast, approximate read of trade scope across many projects, where the goal is not a precise count but a reliable sense of magnitude and character. That needs different tolerances and different outputs: approximate device and circuit counts with explicit uncertainty, identification of the systems present, and complexity indicators drawn from what the design implies, delivered across a lead feed rather than for one project. Extraction has to be robust to the enormous variation in drawing conventions, sheet quality, and completeness at early project stages, where the plans are frequently partial — and where the qualification decision is most valuable. Confidence must be explicit, because an approximate scope presented as precise is worse than none.

## Target Customer
Heads of content and product at project lead publishers, and the estimating leaders at trade contractors who currently qualify pursuits by reading plan sets by hand.

## Impact If Solved
Moves the product from project leads to trade-qualified opportunities, which is a different and more valuable thing for the trade subscribers who make up most of the subscriber base. It also differentiates against competitors publishing the same projects, since the qualification layer is where the value is and the plan corpus needed to build it is already held.
