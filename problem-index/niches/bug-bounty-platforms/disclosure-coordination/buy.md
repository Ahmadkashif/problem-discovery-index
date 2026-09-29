# Buy: Coordination Infrastructure From Standards Bodies

**Niche:** Disclosure Coordination
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The vulnerability identifier and advisory ecosystem is mature and machine-readable, and the coordination process that produces an advisory is still email and a spreadsheet.
**Tags:** #graph-theory #evaluation-metrics #compliance #data-integration #workflow-orchestration #automation #confidence-intervals
**Contested on:** Whether disclosure runs on an agreed process with defined timelines and legal protection, or on the goodwill of whoever answers the email.

## The Problem

The output end of disclosure is well built. CVE identifiers, the numbering authority structure, the National Vulnerability Database, OSV, GitHub Security Advisories, the CSAF advisory format and VEX for expressing whether a product is actually affected — a genuine ecosystem of machine-readable vulnerability information with broad adoption.

The process that produces those artefacts is not built at all. Getting from a researcher's report to a coordinated advisory involves notifying the right parties, agreeing an embargo, tracking readiness, negotiating extensions and publishing together — and every one of those steps is performed manually by whoever has taken on the coordination.

The result is an ecosystem with excellent outputs and no throughput. Coordination capacity, not identifier availability or advisory format, is what limits how many multi-party vulnerabilities get handled well.

## What Already Exists

Identifiers and databases: CVE and the CNA structure, NVD, OSV for open-source ecosystems, GitHub Security Advisories with an integrated reporting and advisory workflow, and the various national vulnerability databases.

Formats: CSAF for machine-readable advisories, VEX for affected-status statements, CVRF as its predecessor, and SBOM formats — SPDX and CycloneDX — which describe what is in a product and are the key input for determining who is affected.

Coordination bodies: CERT/CC and its VINCE platform, which is the closest existing thing to purpose-built coordination tooling, national CSIRTs, and sector-specific coordination centres.

Dependency data: package registries, dependency graph services at the code hosts, and the SBOM tooling ecosystem.

Platform-side: the bounty platforms' own disclosure workflow, which handles publication timing within a programme.

## The Customization Gap

**VINCE exists and is underused outside its own orbit.** CERT/CC built coordination tooling with case management and multi-party communication. It is not widely adopted by the broader ecosystem, and understanding why — reach, integration, awareness — matters more than building another one.

**SBOM data is not wired to notification.** SBOMs describe what is in a product. Determining who to notify about a component vulnerability is exactly the query SBOMs answer, and nobody has built the join. This is the single clearest available integration.

**Advisory formats describe the outcome, not the process.** CSAF and VEX express the finished advisory. There is no format for the coordination state — who was notified, who acknowledged, what the current embargo date is — which means coordination cannot be shared between systems or handed over.

**VEX solves the downstream question and is not fed back.** VEX lets a vendor state whether a product is actually affected. Collecting VEX statements during coordination would tell the coordinator who still needs to act, and the format is currently used for post-publication communication only.

**Identifier assignment is decoupled from coordination timing.** CVE assignment and embargo management are separate processes, and reserving an identifier early is good practice that nothing enforces or tracks against the embargo state.

**Nothing tracks propagation.** Once an advisory publishes, the ecosystem has no mechanism for tracking which downstream packages and distributions actually shipped the fix, even though the dependency data to compute it exists in the same registries that hosted the advisory.

## Target Customer

CERT/CC and the coordination bodies, extending VINCE with SBOM-driven notification and propagation tracking, which would raise the capacity constraint that limits how many cases get coordinated properly.

GitHub and the code hosts are the other credible home: they hold the dependency graphs, the advisory database and the maintainer relationships, and already run a disclosure workflow that stops at single-repository scope.

Open-source foundations as the demand side, since they face multi-party coordination constantly and have the least tooling.

## Impact If Solved

Wiring SBOM and dependency data to notification would mechanise the step that currently limits coordination throughput — working out who needs to know — and would particularly help the downstream parties who are most often missed.

Shared coordination state in a standard format would let cases be handed between coordinators and would give every participant the same view, removing the most common cause of embargo failure.

And propagation tracking would close the gap between an advisory being published and the fix actually reaching the systems running the vulnerable code, which is where the real exposure persists long after everyone has declared the vulnerability handled.
