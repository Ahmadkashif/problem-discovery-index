# Tax Research and Position Documentation

**Industry:** [[accounting-firms-smb|SMB Accounting Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** CPAs get definitive, citation-backed answers to client-specific tax questions in minutes instead of the 45-90 minute manual research cycle through CCH and RIA.
**Tags:** #large-language-models #transformers #attention-mechanisms #transfer-learning #entropy-cross-entropy-kl-divergence #evaluation-metrics

## The Problem
When a client asks "Can I deduct my home office if I also rent a coworking space?" or a preparer encounters an unusual K-1 allocation from a client's partnership interest, the CPA must research the position, find supporting authority (IRC sections, Treasury regulations, revenue rulings, court cases), and document the rationale in a tax memo that survives IRS scrutiny. A mid-complexity research question takes 45-90 minutes using traditional tools, and a typical firm encounters 5-15 such questions per week during tax season. The research must be precise — citing the wrong revenue ruling or missing a recent Tax Court decision creates malpractice exposure.

## What Already Exists
CCH AnswerConnect, Thomson Reuters Checkpoint, and Bloomberg Tax are the dominant research platforms. They provide full-text search across the Internal Revenue Code, regulations, rulings, and case law. AI-assisted tools like Blue J Tax offer predictive analytics on audit outcomes. General-purpose LLMs (ChatGPT, Claude) can discuss tax concepts but hallucinate citations and miss recent guidance, making them dangerous for position documentation.

## The Customisation Gap
The gap is between "search engine for tax law" and "research assistant that understands accounting firm workflow." A CPA needs a tool that takes a fact pattern as input, identifies the relevant IRC sections and regs, finds the most current and controlling authority (prioritizing circuit court jurisdiction matching the client's location), drafts a tax position memo in the firm's standard format, and rates the confidence level (should-level vs. more-likely-than-not vs. substantial authority). The tool must be grounded exclusively in authoritative sources with verifiable citations — no generated text without traceable provenance. It must also integrate with the firm's workpaper system (CCH Axcess, GoFileRoom) so the memo becomes part of the permanent file.

## Impact If Solved
A firm saves 15-30 hours per week during tax season on research tasks, freeing senior staff for client-facing advisory. Standardized memo quality reduces malpractice exposure and improves IRS examination outcomes. The firm can profitably handle more complex returns without adding senior headcount.
