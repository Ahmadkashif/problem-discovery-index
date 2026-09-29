# Specification Generation From API Tooling

**Niche:** [[niches/product-design-studios/deliverable-production/profile|Deliverable Production & Handoff]]
**Industry:** [[industries/product-design-studios|Product Design Studios]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** API tooling generates documentation, clients and tests from one definition, and design handoff is a document someone writes.
**Tags:** #automation #workflow-orchestration #data-integration #evaluation-metrics #compliance #sets-and-logic #large-language-models #quick-win
**Contested on:** Every serious competitor in this niche is fighting to get a design from a file into something a development team can build without a designer spending days producing specifications — and whoever automates that handoff takes the account.

## The Problem
API development solved this with a single machine-readable definition from which documentation, client libraries, mock servers, validation and tests are all generated. Nobody writes API documentation by hand any more, and nobody accepts a definition that leaves error cases unspecified, because the tooling makes both unnecessary and visible. Design handoff is a set of files plus a written document describing behaviour, produced manually and inevitably incomplete.

## What Already Exists
Single machine-readable definitions as the source; generated documentation, clients and mocks; completeness and lint checking on the definition; contract testing against the implementation; and versioned definition evolution.

## The Customization Gap
The adaptation is to a specification that is visual and behavioural rather than structural. It requires: (1) a definition that must capture layout, state and interaction rather than request and response shapes, for which no standard format exists — this is the substantive difference and is the reason design has no equivalent; (2) completeness defined by user-facing states rather than by schema coverage; (3) a designer as the author rather than an engineer, so the definition must be produced from the design work rather than written; (4) verification against a rendered interface rather than a response body; and (5) a handoff across an organisational boundary rather than within one team.

## Target Customer
Design studios, design operations, client development teams, and design and frontend tooling vendors.

## Impact If Solved
API tooling made hand-written specifications unnecessary and incompleteness visible. A definition capturing layout, state and interaction, authored by a designer rather than written, is what design lacks and must generate.
