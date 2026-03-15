# AI-Assisted RFE Response Generation and Approval Strategy

**Industry:** [[immigration-law|Immigration Law Firms]]
**Type:** High Impact
**One-liner:** Immigration attorneys who currently spend 8-20 hours assembling RFE responses — pulling policy memos, drafting legal arguments, gathering supporting documents — cut that to 2 hours of review and refinement, processing twice as many RFEs with the same team without sacrificing quality.
**Tags:** #llm #text-generation #named-entity-recognition #nlp #tacit-knowledge-ml #revenue-impact

## The Problem
A Request for Evidence is USCIS notifying the petitioner that their application is deficient — the agency needs additional documentation or legal argument before it can approve. RFEs arrive with a strict response deadline (typically 87 days) and require a substantive response that addresses every point raised. The response must cite USCIS policy memos, AAO decisions, and case law; present supporting evidence (employer letters, expert opinions, expert witness declarations for specialized skills claims); and make a legal argument for why the petitioner meets the relevant standard. An experienced immigration attorney can write a persuasive RFE response, but it takes hours of research and drafting — work that must be redone largely from scratch for each unique RFE even when the legal arguments are structurally similar.

## Why It's Unsolved
Two related problems make this hard. First, the relevant precedent for immigration RFEs is scattered across USCIS policy manuals, Policy Alerts, AAO non-precedent decisions, and Board of Immigration Appeals decisions — a corpus that is not well-indexed in general legal research tools and changes frequently with new USCIS guidance. Second, and more importantly, the most valuable input to a strong RFE response is not the legal research — it's the experienced attorney's judgment about which arguments USCIS adjudicators at a specific field office are currently accepting, which evidence formats carry the most weight, and how to frame a borderline case. This institutional knowledge is tacit and cannot be captured by a general-purpose LLM trained on public data.

## What a Solution Looks Like
A system with two components: (1) an RFE parsing engine that reads the USCIS RFE document, identifies each deficiency raised, classifies the deficiency type (specialized occupation, employer-employee relationship, specialty occupation standards, etc.), and retrieves the relevant policy memo sections, AAO decisions, and successful argument patterns from a curated immigration law knowledge base; (2) an LLM drafting layer that generates the response structure with section-by-section argument drafts, cites specific precedent, and identifies the specific additional evidence needed. The attorney reviews, adds client-specific context, strengthens the legal argument where needed, and finalizes. The output is an RFE response that reflects the firm's legal standards, not a generic template.

## Impact If Solved
Reduces RFE response preparation from 8-20 hours to 2-4 hours per response. An immigration firm handling 20 RFEs per month saves 120-320 attorney and paralegal hours — equivalent to 1-2 full-time staff members. Firms can take on higher case volumes, improve RFE approval rates by surfacing stronger precedent, and reduce the risk of missing response deadlines due to workload.
