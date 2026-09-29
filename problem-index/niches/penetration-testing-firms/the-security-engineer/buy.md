# Buy: Vulnerability Management for the Manual Report

**Niche:** The Security Engineer Receiving the Report
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Vulnerability management platforms ingest, prioritise, route and track scanner findings at scale, and treat a penetration test report as a PDF someone has to retype.
**Tags:** #gradient-boosting #evaluation-metrics #confidence-intervals #data-integration #workflow-orchestration #automation #compliance
**Contested on:** Whether severity reflects what a finding means in this organisation's architecture, or a rating assigned by someone who has never seen it.

## The Problem

Everything the security engineer needs to do with a penetration test report is a solved problem for a different input. Vulnerability management platforms ingest findings continuously, deduplicate them, enrich them with asset context and exploitability intelligence, recompute priority against the organisation's own environment, map them to owning teams, create tickets in the team's format, and track closure with SLAs.

They do this for scanner output. A penetration test report — which contains the highest-quality, most carefully validated, most contextually reasoned findings the organisation will receive all year — arrives as a document and is handled by hand.

The reason is a format mismatch and nothing more. Scanners emit structured output through APIs. Testing firms emit PDFs. The platform that could do all of this work has no way to receive the findings, so a person retypes eighty of them into a spreadsheet.

## What Already Exists

Vulnerability management and prioritisation: Kenna Security, Nucleus, Vulcan Cyber, Brinqa, Seemplicity and the vulnerability modules in the larger platforms. Ingestion from many scanner sources, asset context enrichment, risk-based prioritisation, ownership routing, ticketing integration and SLA tracking.

Application security posture management: Apiiro, Cycode, Legit, Ox — service and ownership mapping from code to team, which is the piece that makes routing work in a large organisation.

Asset and context sources: CMDBs, cloud asset inventories, Wiz and the CSPM category for cloud reachability and data sensitivity, service catalogues in Backstage and its peers.

Testing firm platforms: Cobalt, Synack and the delivery platforms, some of which offer a client portal with findings and status and could export structured findings if anyone asked.

## The Customization Gap

**No standard structured format for manual findings.** This is the whole obstacle. Scanner output has established formats; a penetration test finding — with narrative, evidence, reproduction steps and a reasoned impact assessment — has none. A simple open schema would let every platform in the category ingest reports tomorrow, and its absence is the reason none of them can.

**Deduplication logic is wrong for manual findings.** Platforms deduplicate scanner findings that repeat identically across scans. Manual findings are unique, described in prose, and need the opposite operation: clustering distinct instances into one systemic issue, which no platform does.

**Prioritisation models are built for CVEs.** Risk scoring in this category leans on exploit intelligence, CVSS and exploit-prediction scoring, all of which assume a known vulnerability with a public identifier. A business logic flaw has no CVE and no exploit intelligence, so the entire enrichment pipeline has nothing to work with and falls back to the tester's severity.

**Narrative does not survive the pipeline.** The value of a manual finding is partly in the tester's reasoning — why this matters, what it chains with, what the realistic impact is. Platforms built for scanner rows have no field for it, so it is lost precisely where it would help the receiving engineer most.

**No feedback path to the firm.** Platforms are one-way sinks. The engineer's severity adjustments, which are the most useful signal anyone could give a testing firm, stay inside the client.

**Retest workflow is absent.** Manual findings often need manual verification. Nothing coordinates a retest request back to the firm from the platform tracking the finding.

## Target Customer

The vulnerability management vendors are the natural adapters — Nucleus and Vulcan both position around consolidating many finding sources, and manual testing is the obvious missing one. The work is a schema, an ingestion path, a clustering mode and a narrative field.

The testing firm delivery platforms are the other half of the same bridge and would benefit equally, since structured export makes their findings more actionable and keeps them visible after handover.

The most valuable thing would be a shared open schema neither side owns, which is the kind of thing an industry body or an open-source effort produces faster than a vendor.

## Impact If Solved

The year's best findings stop being handled worst. There is something absurd about an organisation with a sophisticated automated pipeline processing a PDF by hand, and closing it requires a format rather than a technology.

Clustering into systemic issues would change what gets fixed, which is the difference between closing instances and removing causes.

And a feedback path carrying severity adjustments back to the firm would improve the next report at essentially no cost, closing a loop that has never existed in this industry.
