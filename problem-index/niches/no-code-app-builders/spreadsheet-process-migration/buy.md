# Spreadsheet Comprehension Tooling, Redirected

**Niche:** [[niches/no-code-app-builders/spreadsheet-process-migration/profile|Spreadsheet Process Migration]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Formula parsing, dependency extraction and spreadsheet smell detection were built for audit and risk, and the same analysis describes a process precisely enough to generate an application from it.
**Tags:** #graph-theory #spectral-graph-theory #large-language-models #bert #evaluation-metrics #confidence-intervals #automation #data-integration
**Contested on:** Every serious competitor here is fighting to turn an existing spreadsheet-and-email process into a working application without the owner rebuilding it from scratch — and whoever does that takes the department, because the rebuild is the only reason the process is still a spreadsheet.

## The Problem
There is a body of tooling and research that reads spreadsheets properly: parses formulas, builds dependency graphs, detects errors and structural smells, clusters similar formulas into ranges, and identifies the tables inside an unstructured sheet. It was built for financial audit and operational risk. Applied to the same workbook with a different question — what process does this describe — it would produce most of an application specification, and nobody has asked that question.

## What Already Exists
Spreadsheet audit tools with formula parsing and dependency mapping; academic work on spreadsheet structure recognition, table detection and error detection; open parsers for common formats; language models that interpret informal conventions and column semantics; and process mining, which handles the event-log half of the problem where email or system logs are available.

## The Customization Gap
The adaptation is from audit to specification. It requires: (1) intent classification over spreadsheet elements — deciding that this column is a status, that one a foreign key, this formula a derived metric and that colour rule a state transition — which audit tooling has no reason to attempt and which is the core of the translation; (2) entity and relationship extraction, since an application needs a data model and a spreadsheet flattens one into columns, so recognising that the customer columns describe a separate entity is what turns a table into an app; (3) convention interpretation with human confirmation, because every team's idiosyncrasies are different and a model proposing "amber means overdue" for confirmation succeeds where both pure inference and a questionnaire fail; (4) the email and messaging half, where process mining techniques apply to an event log assembled from message metadata and produce the workflow the spreadsheet omits; and (5) equivalence verification between the old and new, which is the only way the owner will switch and which requires running both and comparing outputs rather than asserting correctness.

## Target Customer
No-code platform vendors, spreadsheet risk and audit vendors with an adjacent market, process mining vendors, and implementation partners performing these migrations manually.

## Impact If Solved
A mature analysis capability answers a question it was never pointed at, and the answer is most of an application specification. Intent classification and convention confirmation are the two adaptations, and equivalence verification is what makes the result adoptable.
