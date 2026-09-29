# Distributed Tracing Standards

**Niche:** [[niches/headless-commerce-vendors/cross-vendor-observability/profile|Cross-Vendor Observability]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The tracing standard, the propagation format and the collectors are all mature and vendor-neutral, and the one thing missing is adoption across a commercial boundary.
**Tags:** #graph-theory #data-integration #automation #compliance #evaluation-metrics #workflow-orchestration #descriptive-statistics #quick-win
**Contested on:** Every serious competitor in this niche is fighting to make one trace span six companies' systems — and whoever does that solves the category's acknowledged weak point, because the standard exists and stops at every vendor boundary.

## The Problem
Vendor-neutral instrumentation, a standard propagation header, semantic conventions for common domains and collectors that route to any backend are all mature and widely adopted. The entire technical problem of joining a trace across service boundaries is solved, deployed at scale, and free. What has not happened is two companies agreeing to propagate the header across the boundary between them, which requires no engineering and a paragraph in a contract.

## What Already Exists
Vendor-neutral instrumentation libraries and collectors; standard trace context propagation headers; semantic conventions for common domains with a governance process; backend-agnostic export; sampling strategies for high-volume paths; and the multi-tenant considerations already worked through for service providers.

## The Customization Gap
The adaptation is to propagation between companies with a commercial relationship. It requires: (1) an agreement rather than an implementation, since the technical work is a header and the barrier is that neither party has asked — making it a standard clause in commerce vendor contracts is the whole unlock and is a procurement action; (2) a trust model for what a vendor returns, since a vendor will not expose internal service names and a coarse span with their total processing time is both acceptable and sufficient; (3) commerce semantic conventions so spans from different vendors describe comparable operations, which the standards process supports and which this domain has not defined; (4) sampling coordinated across parties, since independent sampling decisions break traces and a shared rule is required; and (5) a neutral collection point, since neither the retailer nor any vendor is an acceptable custodian for all parties and an independent one is the commercial position.

## Target Customer
Retail platform engineering, commerce vendors, observability vendors, and the open telemetry community for whom cross-company propagation is an unaddressed case.

## Impact If Solved
The technical problem is solved, free and deployed, and the barrier is that two companies have not agreed to propagate a header. A standard clause in commerce vendor contracts is the whole unlock, and a coarse vendor span with total processing time is sufficient without exposing anything.
