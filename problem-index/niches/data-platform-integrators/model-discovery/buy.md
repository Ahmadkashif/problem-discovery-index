# Generated Documentation From Software Tooling

**Niche:** [[niches/data-platform-integrators/model-discovery/profile|Model Layer Discovery]]
**Industry:** [[industries/data-platform-integrators|Data Platform Integrators]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software stopped writing reference documentation by hand and generates it from the source, and data catalogues are empty text boxes.
**Tags:** #large-language-models #automation #data-integration #workflow-orchestration #evaluation-metrics #word-embeddings #transformers #compliance
**Contested on:** Every serious competitor in this niche is fighting to make an existing asset findable so nobody builds a duplicate, and whoever makes discovery work takes the account.

## The Problem
Software resolved the documentation problem by generating it. Reference documentation is produced from the source and its annotations, published automatically on every change, and therefore never drifts. Nobody writes an API reference by hand any more, and a documentation site that is out of date is treated as a build failure. Data catalogues ask humans to fill in description fields and are consequently empty.

## What Already Exists
Documentation generated from source and annotations; publication on every change; drift impossible by construction; searchable generated references; and examples extracted from tests.

## The Customization Gap
The adaptation is to transformation logic whose meaning is business rather than technical. It requires: (1) descriptions that must express what a column means to the business rather than what the code does, which the source alone does not contain and must be inferred from lineage, naming and usage — this is the substantive difference; (2) examples drawn from real queries rather than from tests, since there are no tests describing intent; (3) an audience that includes analysts and business users rather than only engineers; (4) assets defined across several tools rather than in one repository; and (5) a catalogue that must merge generated and human-curated content without the human parts blocking the generated ones.

## Target Customer
Data platform teams and integrators, analytics engineering, catalogue and discovery vendors, and documentation tooling providers.

## Impact If Solved
Software stopped hand-writing references and made drift impossible by generating them. Descriptions that must express business meaning rather than code behaviour is what has to be inferred rather than extracted.
