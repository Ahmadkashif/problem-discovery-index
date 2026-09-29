# The Submittal Register Read From the Specification

**Niche:** [[niches/construction-tech-platforms/submittal-rfi-routing/profile|Submittal & RFI Routing Content]]
**Industry:** [[industries/construction-tech-platforms|Construction Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The document that says exactly which submittals are required, from whom, to whom and by when is stored in the platform as a PDF, and a project engineer spends three weeks per project reading it and typing the answer into a register.
**Tags:** #large-language-models #bert #transformers #word-embeddings #evaluation-metrics #confidence-intervals #automation #workflow-orchestration
**Contested on:** Every serious competitor in document workflow is fighting to read the specification and decide who a submittal or RFI should go to, in what sequence, and by when — and whoever routes most accurately against the spec takes the account.

## The Problem
A project engineer receives a 1,400-page project manual. Over the next three weeks, between other duties, she reads every technical section, extracts every submittal requirement — product data, shop drawings, samples, certifications, test reports, closeout documents — records which subcontractor owes it and which consultant reviews it, applies the turnaround from the general conditions, and builds a register of several hundred line items. It is careful, valuable work, and it is transcription. She will do it again on the next project, from a manual that is 80% the same because it came from the same architect's office.

## Why Nobody Has Built This
The vendors' product management has been oriented around workflow rather than content, and content extraction was genuinely unreliable until recently — specifications are long, inconsistently formatted, delivered as PDFs of varying quality, and full of cross-references and exceptions that a naive extractor mangles. There is also a liability shadow: a missed submittal requirement is a real construction consequence, so a vendor asserting a register takes on a responsibility that a vendor providing an empty register does not. That shadow is the reason to design for review rather than a reason to leave it manual.

## What to Build
An extraction pipeline over the project manual that produces a proposed register: every submittal requirement located to its specification section and paragraph, classified by type, with the responsible party inferred from the section's trade scope, the reviewer inferred from the section's designated consultant, and the turnaround taken from the general conditions. Every line cites the passage it came from, so the project engineer verifies rather than transcribes, and verification of a cited line takes seconds. Confidence is per line, and low-confidence lines are surfaced first rather than buried. Because most specifications are assembled from a limited set of master texts, the system improves sharply with volume — a section it has seen from this architect before is nearly free — which is the compounding property that makes this a platform capability rather than a service.

## Target Customer
Construction platform vendors who own the document workflow, general contractors and construction managers staffing project engineers, and the third-party firms currently selling register creation as a service.

## Impact If Built
Three weeks of project engineering per project, largely recovered, at a moment in the job when that engineer's attention is worth more elsewhere. The register also becomes complete rather than best-effort, which matters because the requirements most often missed are in the sections read last, under time pressure — and a missed submittal surfaces as a delay months later, when it is expensive.
