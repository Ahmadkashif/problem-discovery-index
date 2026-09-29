# Monitoring an Agency That Changes Policy Without Publishing a Rule

**Niche:** [[niches/immigration-law/immigration-legal-research-publishers/profile|Immigration Legal Research Publishers]]
**Industry:** [[industries/immigration-law|Immigration Law Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The change that reshapes thousands of live filings arrives as an edited paragraph on a web page with no notice and no version history.
**Tags:** #anomaly-detection #ocr #data-integration #named-entity-recognition #automation

## The Problem
Immigration policy does not mostly move through the Federal Register. It moves through policy manual edits, memoranda posted to an agency site, updated form instructions, revised processing time pages, and field guidance that surfaces when practitioners start seeing it applied. A paragraph changes and thousands of pending petitions are affected.

The publisher's promise is that subscribers hear about it immediately and correctly. Meeting that promise means watching agency web properties continuously, catching edits that carry no announcement, and working out what changed and what it means — under time pressure, because subscribers are filing today.

Detection is substantially manual and substantially social: editors watch what they can, and hear about the rest from practitioners who noticed a filing behave differently.

## What Already Exists
Web change monitoring is a mature commodity — Visualping, ChangeTower, and the enterprise media monitoring platforms all detect page changes and alert. Regulatory tracking services cover the Federal Register comprehensively and well.

## The Customization Gap
The generic tools detect that something changed. Everything that matters here is what changed and whether it signifies.

**Semantic diffing, not character diffing.** A policy manual page changes constantly for formatting, navigation, and boilerplate. The signal is a substantive change to a legal standard, and it may be a single word — "may" to "must", a threshold number, an added exception. Character diffs bury that in noise; nothing generic distinguishes substance from formatting.

**Silent retroactive edits.** The agency edits published pages without version markers, so the previous text simply ceases to exist. The monitoring system must be the version history nobody else maintains — archiving every state of every watched page so a change can be characterized after the fact. This is an archival obligation, not an alerting feature.

**Impact scoping at detection.** An edit to a provision matters differently depending on which petition types depend on it. If provisions are linked to the publisher's own guidance and to petition categories, a detected change immediately names what it affects — which is the difference between an alert and a usable advisory.

**Sources beyond text pages.** Processing time tables, form editions, fee schedules, and appointment availability all carry policy signal and are structured data on web pages, not prose. Their changes need parsing rather than diffing.

**High recall, aggressively triaged.** A missed change is the failure the subscription exists to prevent, so detection must be over-inclusive, which makes editorial triage the constraint. Ranking candidate changes by likely significance is the piece that makes over-inclusive detection survivable.

## Target Customer
VP of Content or Head of Legal Research at an immigration publisher, where being second to notice a policy change is a competitive loss and being wrong about one is worse.

## Impact If Solved
Immediacy is the product. An agency that changes policy silently on a web page is a genuinely hostile monitoring target, and every publisher in this space is partly relying on practitioners to tell them. Systematic semantic monitoring with an archived history turns the core claim into something the publisher controls, and the archive itself becomes an asset — the version history of US immigration policy, which the agency does not keep.
