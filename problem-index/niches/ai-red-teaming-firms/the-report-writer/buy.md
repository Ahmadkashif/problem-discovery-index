# Structured Findings and Technical Writing Practice

**Niche:** [[niches/ai-red-teaming-firms/the-report-writer/profile|The Report Writer]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Security testing built structured finding formats and report automation years ago, and AI assessment writes prose from notes.
**Tags:** #compliance #automation #workflow-orchestration #data-integration #evaluation-metrics #worker-facing #quick-win #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to get a finding from a researcher's head into two audiences' hands without the researcher writing documents for a week — and whoever does that takes the account, because that week is the industry's most expensive time spent on its least skilled task.

## The Problem
Penetration testing firms faced this and solved it: findings are captured in a structured tool during the test, with a taxonomy, a severity, evidence attached and a recommendation drawn from a library, and the report is generated. The profession also converged on exchange formats so findings flow into a client's tracker rather than being retyped from a document. AI assessment firms capture findings in notes and produce reports in a word processor.

## What Already Exists
Structured finding capture tools used during testing; finding taxonomies with stable identifiers; recommendation libraries mapped to finding classes; report generation from structured data with multiple output formats; findings exchange formats for pushing into issue trackers; and evidence attachment workflows.

## The Customization Gap
The adaptation is to a finding that is probabilistic and whose remedy depends on an architecture. It requires: (1) a finding record carrying a success rate and its interval rather than a binary, since that is the core fact and no existing format has a field for it; (2) evidence as a re-runnable probe rather than a screenshot, which is stronger evidence and is what makes revalidation possible — this connects directly to the revalidation niche; (3) a recommendation library keyed to the client's architecture options rather than to a code fix, since the remedies here are filtering, prompt structure and scoping rather than a patch; (4) regulatory mapping as a maintained artefact, because these clients' primary use of the report is regulatory and the mapping is the part that is redone every engagement; and (5) a finding taxonomy with stable identifiers, which does not exist for this domain and whose absence is why every firm's findings are incomparable.

## Target Customer
Assessment firms, security testing tool vendors for whom this is an adjacent market, and the clients receiving the output.

## Impact If Solved
The structured-capture-and-generate pattern is standard in penetration testing and absent here. A re-runnable probe as evidence is stronger than a screenshot and is what makes revalidation possible, and a maintained regulatory mapping removes work redone in every engagement.
