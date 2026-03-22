# Automated Estate Plan Assembly Pipeline

**Niche:** [[niches/estate-planning/basic-wills-poa/profile|Basic Wills & POA]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Clients answer a guided questionnaire, the system generates a complete estate plan package (will, POAs, healthcare directive, trust if needed), and the attorney reviews and signs — reducing per-plan attorney time from 3-5 hours to 30 minutes.
**Tags:** #large-language-models #transformers #decision-trees #feature-engineering #automation #workflow-orchestration #revenue-impact

## The Problem
A basic estate plan requires 4-6 documents: a will (or revocable trust with pour-over will), financial power of attorney, healthcare power of attorney / advance directive, and potentially a certificate of trust and assignment of personal property. Each document must be internally consistent (same named fiduciaries, same asset references, same contingent provisions). Currently, the attorney or paralegal conducts a 60-90 minute intake meeting, enters data into a document assembly tool, generates each document separately, cross-checks for consistency, reviews the package, schedules a signing ceremony, and delivers the final plan. Total attorney/paralegal time: 3-5 hours per plan at a flat fee of $1,500-$3,000, making margins thin and throughput limited to 4-6 plans per week per attorney.

## Why Nobody Has Built This
The end-to-end pipeline crosses multiple software categories: client intake (form builder), document assembly (legal drafting), practice management (scheduling/billing), and document delivery (e-signature/portal). No single vendor spans all four. Document assembly vendors (WealthDocx, HotDocs) focus on drafting quality and leave intake and delivery to others. Practice management vendors (Clio) focus on billing and calendaring and leave document generation to others. Building the full pipeline requires integrating across these categories or building a vertical stack — both expensive for a market of small law firms with $1,500 average transaction values.

## What to Build
A vertical SaaS platform for basic estate planning that covers: (1) a client-facing intake questionnaire with branching logic (married/single, children/no children, blended family, own a business), (2) automated document generation producing a complete, internally consistent plan package from the questionnaire responses using state-specific templates, (3) an attorney review interface highlighting decision points and provisions that need human judgment, (4) integrated e-signature and document delivery, and (5) a client portal for accessing their plan documents post-signing. The system uses an LLM to flag questionnaire responses that suggest the client may need more complex planning (e.g., mention of a disabled child, assets over $5M, real estate in multiple states) and routes those clients to a full consultation rather than the automated pipeline.

## Target Customer
Solo and small-firm estate planning attorneys (1-3 attorneys) handling 10-20 basic plans per month who are losing price-sensitive clients to LegalZoom and spending too much time on routine document assembly.

## Impact If Built
Reduces per-plan attorney time from 3-5 hours to 30-45 minutes of review. Enables a solo attorney to handle 30-40 plans per month instead of 10-15, tripling throughput at the same staffing level. Competes with DIY services on speed and convenience while preserving the attorney review that DIY lacks.
