# Milestone Evidence for Pharma Partners

**Industry:** [[biotech-research-firms|Biotech Research Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A biotech's partnership revenue arrives as milestone payments triggered by scientific criteria written into the contract, and the evidence that a criterion was met is assembled by hand from assay data, decks and emails for each joint steering committee.
**Tags:** #large-language-models #bert #feature-engineering #hypothesis-testing #compliance #workflow-orchestration #revenue-impact

## The Problem
Partnerships are the industry's main source of non-dilutive cash. J.P. Morgan counted over $252B of biopharma licensing deal value in 2025, with upfronts at about 7% of it, so most of the headline value is milestones. A discovery collaboration pays when the biotech delivers, for example, a lead series meeting a target product profile: potency below a threshold, selectivity against named off-targets, oral bioavailability in rat above a percentage, a clean early safety panel. Before each quarterly joint steering committee, the biotech's alliance manager and project leader assemble a deck showing progress against each criterion. They argue that a milestone was met, and then negotiate when the partner's scientists read the same data differently. They argue, for instance, about whether the selectivity assay used the agreed format, whether three of four criteria count, or whether a compound tested in a different salt form qualifies.

## What Already Exists
Contract lifecycle management tools (Icertis, Ironclad) hold the agreement and its obligations. Project tools (Smartsheet, Microsoft Project) track milestone dates. Alliance management practice has its own professional body and playbooks. ELNs and registries hold the underlying assay data.

## The Customisation Gap
None of these connects the contract's scientific definitions to the data. The partnership-specific logic is: parsing milestone criteria from the agreement into testable conditions with their assay, species, units and statistical requirements; joining them to the registry so each compound's status against each criterion is computed, not asserted; recording which assay protocol version the partner agreed to; showing where a criterion is borderline or measured once; and keeping the evidence trail for a payment dispute or an audit of revenue recognition. The CLM sees obligations as dates; the ELN sees results as rows; nobody owns the join.

## Impact If Solved
Milestone status computed continuously against the contract's own definitions would shorten the argument at each steering committee and pull payments forward. Earlier payments matter to a biotech measuring runway in months. It would also give finance a defensible basis for recognising milestone revenue.
