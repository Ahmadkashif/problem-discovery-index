# Bills of Materials Nothing Consumes

**Industry:** [[software-supply-chain-security|Software Supply Chain Security]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** SBOM generation is standardised, automated and increasingly mandated, and the documents are produced, filed and never read — because the tooling generates them and nothing consumes them.
**Tags:** #graph-theory #bert #word-embeddings #k-nearest-neighbors #evaluation-metrics #compliance #data-integration

## The Problem
A software bill of materials lists the components in a piece of software. Formats are standardised, generation is automated in most build systems, and federal procurement increasingly requires them.

The generation problem is solved. The consumption problem does not have a product. An organisation receiving SBOMs from its vendors accumulates documents in a repository, and when a new vulnerability appears in a widely used component the question everyone asks — are we affected, and in what — cannot be answered from them without a project.

The reasons are ordinary and specific. SBOMs vary in depth, with some listing direct dependencies only. Component naming is inconsistent, so the same library appears under several identifiers across documents. Version specifications are ambiguous. They are point-in-time and go stale as vendors ship updates. And there is no shared identifier scheme reliable enough to join them.

So the document is filed for compliance, the compliance requirement is satisfied, and the organisation's actual exposure question is answered the way it always was: by asking around and grepping.

## What Already Exists
SPDX and CycloneDX are mature, well-specified formats. Generation is built into most build tools and CI systems. SBOM repositories and exchange mechanisms exist. Vulnerability databases can be joined to component lists in principle. The Package URL specification provides a naming scheme that helps where adopted. Some vendors offer SBOM management platforms.

## The Customisation Gap
Component identity resolution across documents is the foundational missing layer. The same library appears with different names, different version formats and different granularity across SBOMs from different vendors, and joining them is entity resolution over a messy identifier space — exactly the pattern that recurs throughout this vault.

Currency is the second gap. An SBOM describes a version that shipped and does not describe what is deployed now, and nothing tracks which version of which vendor product is actually running where.

Depth normalisation matters because a shallow SBOM listing direct dependencies only creates a false sense of coverage, and the recipient cannot tell a thorough document from a superficial one without inspecting it.

Query is what would make the whole thing useful: given a newly disclosed vulnerability, which products, in which versions, deployed where, contain the affected component — answerable in minutes rather than as a project, which is the entire reason the mandate exists.

## Impact If Solved
SBOMs are mandated, generated at scale and functionally inert, because the ecosystem built generation and never built consumption. Identity resolution and a query layer are what would let an organisation answer its exposure question in minutes, which is the outcome the regulation was written to produce and currently does not.
