# Licence Obligation Analysis Beyond Identification

**Niche:** [[niches/open-source-commercial-vendors/enterprise-procurement-compliance/profile|Enterprise Procurement & Compliance]]
**Industry:** [[industries/open-source-commercial-vendors|Open Source Commercial Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software composition analysis identifies which licences are present, which is the easy half, and the question every legal reviewer actually asks is what those licences require given how the software is being used.
**Tags:** #bert #large-language-models #graph-theory #word-embeddings #evaluation-metrics #confidence-intervals #compliance #cross-validation
**Contested on:** Every serious competitor here is fighting to get open-source software through an enterprise's legal, security and procurement review without a three-month project — and whoever does that takes the enterprise adoption, because the review is where it currently stops.

## The Problem
Composition analysis tools scan a codebase and report the licences present, with a risk rating per licence. A legal reviewer's question is different: given that we link this library dynamically in a service we operate but do not distribute, what must we actually do? The answer depends on the licence, the linking mode, whether the software is distributed, and whether it is modified — a small number of dimensions producing a small number of outcomes, determined identically for every organisation and computed by a lawyer every time.

## What Already Exists
Software composition analysis with comprehensive licence identification; machine-readable licence metadata standards; software bill-of-materials formats; the published licence compatibility analyses maintained by several organisations; dependency graph extraction; and language models that read licence text accurately. The identification layer is entirely solved.

## The Customization Gap
The adaptation is from identification to obligation. It requires: (1) a usage model as an input — distributed or hosted, linked statically or dynamically, modified or not, embedded in a product or used internally — since the obligations turn on these and a tool that ignores them can only report a licence name; (2) obligation output rather than a risk rating, meaning the specific actions required such as attribution, source availability or notice, which is what the reviewer needs to act on and what a red-amber-green rating conceals; (3) transitive analysis through the dependency tree, since the obligation frequently arrives from a dependency of a dependency and the relevant question is the effective obligation of the whole graph; (4) explicit uncertainty where the position is genuinely contested, because some licence questions have no settled answer and a tool that asserts one is worse than one that flags it for counsel; and (5) reviewable provenance for every conclusion, since a legal function will not adopt a conclusion they cannot trace to the text it came from.

## Target Customer
Software composition analysis vendors, enterprise legal and open-source programme offices, and the open-source vendors supporting enterprise reviews.

## Impact If Solved
Identification is solved and obligation is what the reviewer needs, which is a one-layer gap absorbing an enormous amount of legal time. A usage model as an explicit input and obligation-shaped output are the two changes that turn a scan result into an answer.
