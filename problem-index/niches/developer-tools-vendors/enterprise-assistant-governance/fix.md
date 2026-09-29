# Secrets and Proprietary Context Leaving in Prompts

**Niche:** [[niches/developer-tools-vendors/enterprise-assistant-governance/profile|Enterprise Assistant Governance]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The context an assistant sends is assembled automatically from surrounding code, which regularly includes credentials, customer data in test fixtures and proprietary algorithms, and nobody measures what left.
**Tags:** #bert #word-embeddings #logistic-regression #descriptive-statistics #evaluation-metrics #confidence-intervals #compliance #quick-win
**Contested on:** Every serious competitor here is fighting to make an assistant approvable by a security and legal function — provenance, licence exposure, data boundaries and audit — and whoever does that takes the enterprise, because a blocked tool has no adoption to win.

## The Problem
A developer works in a file whose neighbours include a test fixture containing real customer records, a configuration file with an API key that should have been in a secret store, and the implementation of a pricing algorithm the company regards as its core intellectual property. The assistant assembles context from the surrounding code and sends it. No policy was violated by anybody: the developer did nothing unusual, the assistant did what it is designed to do, and the organisation has no record of what was transmitted. The security function's concern about these tools is precisely this, and it is met with a contractual assurance about retention rather than a control.

## Why It's Still Broken
Context assembly optimises for suggestion quality, which means including as much relevant surrounding code as fits, and sensitivity is not one of the criteria. Scanning what is about to be sent adds latency to the path that must be fastest, which is a real trade-off resolved silently in favour of speed. There is no log of transmitted context in most deployments, so the exposure is not merely uncontrolled but unmeasured. And the credentials and customer data that cause the worst instances are themselves policy violations that predate the assistant, which makes the exposure a compounding of two problems rather than a new one.

## What a Fix Looks Like
Inspect and record what leaves. Scan assembled context before transmission for credentials, tokens and keys, which is fast, well-understood pattern-and-entropy work and catches the worst category outright. Detect personal and customer data in fixtures and sample files, which is the second largest category and is equally detectable. Let the organisation mark sensitive paths — a directory containing proprietary algorithms, a fixture directory — and exclude them from context assembly with the developer told it happened, since silent exclusion produces confusing suggestion quality. Log what was sent, at least in summary form with file paths and detection results, so the exposure is measurable and an incident can be investigated. Report the aggregate, which will identify the specific fixtures and configuration files responsible for most of the exposure and is a short remediation list. And treat a detected credential as an incident in its own right, since it was already exposed in the repository before any assistant saw it.

## Who Feels the Pain
Security functions asked to approve a tool whose data flows they cannot observe; organisations with credentials and customer data in repositories that are now being transmitted; and developers whose tools are blocked because the control does not exist.

## Impact If Fixed
Credential and personal data scanning on the outbound path is fast and mature, and it addresses the specific concern that blocks approval. The transmitted-context log is what converts an unmeasured exposure into a managed one, and the aggregate report usually names a handful of files responsible for most of it.
