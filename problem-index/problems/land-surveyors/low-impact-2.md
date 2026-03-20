# Permit and Regulatory Compliance Across Jurisdictions

**Industry:** [[land-surveyors|Land Surveyors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Survey firms operating across multiple counties and states must track different plat filing requirements, monument standards, minimum technical standards, and certification language for each jurisdiction — a fragmented compliance landscape that no generic tool manages and that causes 5-10% of plat submissions to be rejected on first filing.
**Tags:** #large-language-models #transformers #attention-mechanisms #transfer-learning #evaluation-metrics #entropy-cross-entropy-kl-divergence #compliance #data-integration

## The Problem

A survey firm in a metropolitan area may work across 3-5 counties, each with different plat filing requirements. County A requires 18x24" sheet size with a 1.5" left margin for binding; County B requires 24x36" with a 2" margin. County A accepts digital signatures; County B requires wet ink. County A's monument standard requires 5/8" rebar with a plastic cap bearing the PLS number; County B requires 1/2" iron pipe. The certification language differs ("I, [name], a Professional Land Surveyor licensed in the State of...") with specific wording mandated by each county's recording office.

For ALTA/NSPS surveys, an additional layer of national standards (Table A optional items, minimum standards of detail) overlays the local requirements. For construction staking, the general contractor's specifications may conflict with local standards. The surveyor must track all of these requirements and apply the correct combination for each project, a process that currently relies on office checklists (often outdated) and the surveyor's personal experience with each jurisdiction.

The consequence of non-compliance is plat rejection by the county recorder — a 5-10% first-submission rejection rate that requires revision and resubmission, adding 2-5 hours per rejection and delaying the client's project (especially consequential for real estate closings that depend on the survey).

## What Already Exists

AutoCAD template files can be configured per county but require manual selection and updating. State survey societies publish minimum standards documents, but these are PDF publications that must be manually referenced. The ALTA/NSPS standards committee publishes updates every 5 years. No system aggregates county, state, and national requirements into a queryable compliance database that integrates with the drafting workflow.

## The Customisation Gap

The needed tool is a jurisdiction-aware compliance engine that maintains current filing requirements for every county and state where the firm operates, integrated into the plat production workflow. When a surveyor starts a new project, the system identifies the applicable jurisdictions (county of filing, state of licensure, ALTA standards if applicable, client specifications) and configures the drafting environment accordingly: correct sheet size, margin requirements, required certifications, monument specifications, and signature blocks. Before filing, the system performs a compliance check: "Warning: County B requires the surveyor's email address on the certification — this is missing. County B requires digital filing via their portal — PDF must be under 10MB."

The system must be maintained as a living database — counties update requirements, states revise minimum standards, and ALTA revises its standards periodically. An LLM-assisted pipeline can monitor county recorder websites and state survey board publications for requirement changes, flagging updates for human verification before updating the compliance database.

## Impact If Solved

Reduces first-submission rejection rate from 5-10% to 1-2%, saving 2-5 hours per avoided rejection. For a firm filing 200 plats/year with a 7% rejection rate, that's 14 rejections eliminated — 28-70 hours saved and 14 project timelines un-delayed. Eliminates the 1-2 hours per project currently spent manually configuring templates and checking compliance, saving an additional 200-400 hours/year. Reduces professional liability risk from filing errors — a plat filed with incorrect certification language may be legally invalid, creating title problems that surface months or years later.
