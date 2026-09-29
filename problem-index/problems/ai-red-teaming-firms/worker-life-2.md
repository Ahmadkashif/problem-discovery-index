# Report Writer Translating Findings

**Industry:** [[ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Worker Life Changing
**One-liner:** The most experienced researchers spend the end of every engagement writing documents, translating what they found into something an engineering team can act on and a compliance team can file.
**Tags:** #large-language-models #transformers #bert #word-embeddings #evaluation-metrics #transfer-learning #automation #worker-facing

## The Problem
An engagement ends with a report. It must serve several audiences at once: an engineering team that needs reproducible technical detail, a security leader who needs severity and prioritisation, a compliance function that needs mapping onto a regulatory framework, and an executive who needs a summary.

Writing it falls to the researchers, usually the most senior ones, and takes a significant share of the engagement — commonly a fifth or more of the total time.

The content is largely reconstruction. The researcher worked through the assessment with notes and transcripts, and now writes up what they did, why it worked, how to reproduce it, and what to do about it. The reproduction steps in particular are painstaking because a probe involving a specific conversational sequence must be documented exactly.

The remediation guidance is the hardest part and the most valuable. Saying what a client should actually change requires understanding their architecture, and the researcher writes it under deadline pressure at the end of an engagement when they are already committed to the next one.

## Why It Matters to the Worker
Senior researchers are the scarce resource in this industry and a fifth of their time goes to documentation. The work that requires their expertise is finding vulnerabilities, and they are producing prose.

The audience conflict makes it worse. The same finding must be written three ways, and a report that satisfies the engineers frustrates the executives and vice versa. Researchers cycle through revisions responding to feedback about tone and framing rather than substance.

Deadline compression is structural. The report is due at the end of the engagement, findings accumulate throughout, and the writing therefore concentrates into the final days alongside the last testing — which is when the most interesting findings usually emerge.

And it is a genre most researchers were never trained in. They are technical people producing compliance documentation, and the mismatch shows in both directions.

## What a Solution Looks Like
Capture during the engagement rather than reconstruction after it. The probes, responses, configurations and outcomes are all logged; assembling a technical finding from them is largely mechanical, and a draft that exists before the writing week changes the whole shape of the work.

Reproduction steps generated from the actual session. The exact sequence is in the log, and turning it into documented steps is a transformation rather than an act of memory.

Audience-specific rendering from one structured finding. Severity, technical detail, remediation and regulatory mapping should be facets of a single record rather than four separately written documents.

Remediation drawn from the firm's own history. The same vulnerability class has been remediated many times across clients, and what actually worked is knowledge the firm holds and does not reuse.

Framework mapping automated. Aligning findings to the EU AI Act, the NIST framework or a sector standard is a lookup once findings are structured, and it is currently done by hand and inconsistently.

## Impact If Solved
Report writing consumes a fifth of the scarcest capacity in the industry and produces documents that are reconstructions of records already held. Generating drafts from session logs and rendering per audience returns senior researchers to research, and the accumulated remediation history is a genuine asset the firms have never assembled.
