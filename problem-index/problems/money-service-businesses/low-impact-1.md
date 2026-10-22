# Fifty-State Licence Maintenance on NMLS

**Industry:** [[money-service-businesses|Money Service Businesses]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every licensed money transmitter keeps the same evidence current for every state — net worth, surety bonds, permissible investments, quarterly call reports, change-of-control filings — and rebuilds it by hand because generic compliance tools do not model money transmission law.
**Tags:** #large-language-models #transformers #feature-engineering #data-integration #compliance #workflow-orchestration #automation #quick-win

## The Problem
A transmitter operating nationally holds a licence in nearly every state (estimate: 49 plus DC and territories), managed through NMLS. Each licence carries continuing obligations. The NMLS MSB Call Report is due within 45 days of each quarter end, with a financial condition section, transaction activity by state, a permissible-investments schedule and an annual destination-country section; a late report can block renewal, and some states fine per late filing (Georgia charges $1,000). Each state sets a minimum net worth and a surety bond that scales with volume. Permissible investments must cover outstanding transmission obligations at all times, not just at quarter end. Any change in control, key individual or agent count triggers filings with deadlines that differ by state.

The licensing team — often two to six people at a mid-sized transmitter (estimate) — keeps this in spreadsheets, the NMLS portal, a calendar and email with outside counsel. Every multistate examination begins with a request list that asks for the same evidence in a slightly different form.

## What Already Exists
GRC platforms such as AuditBoard, LogicGate and ServiceNow's risk and compliance module track obligations, controls and evidence generically; see [[grc-compliance-platforms|GRC & Compliance Platforms]]. Regulatory intelligence services publish state-by-state requirement summaries. NMLS itself provides the filing portal and the call report template. Licensing law firms and consultancies sell application and maintenance services.

## The Customisation Gap
The generic tools know that a control exists; they do not know money transmission. The industry-specific layer is: a state-by-state rule model distinguishing states that have adopted the Money Transmission Modernization Act (35 in full or in part by August 2026) from those still on legacy statutes, with each state's net worth formula, bond schedule and permissible-investment definitions; a daily permissible-investment calculation against outstanding obligations by state, not a quarter-end snapshot; call report preparation that reconciles state transaction totals back to the ledger before submission; change-of-control and key-individual workflows with each state's notice period; and an exam evidence library mapped to the multistate examination request list. NMLS holds the filings but not the reasoning or the reconciliations behind them.

## Impact If Solved
A licensing team stops rebuilding the same reconciliations four times a year and before every exam, catches a permissible-investment shortfall on the day it opens rather than at quarter end, and answers an examiner's request list from a maintained library instead of a scramble — removing perhaps a third of a small licensing team's recurring work (estimate) and most of its late-filing risk.
