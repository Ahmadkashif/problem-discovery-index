# Lineage: AI Model Evaluation Firms

**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Wave:** [[series/eras/wave-12-transformers|12 — Transformers]]
**The tool:** Chatbot Arena — a public web page that shows a user two anonymous chatbots answering the same prompt, takes a vote on which answer was better, and turns the accumulated votes into an Elo-style leaderboard
**Builder:** LMSYS Org
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A chat model's answer to an open question has no answer key.

The benchmarks inherited from the pre-transformer era — multiple-choice sets, exact-match question answering, reading comprehension — all assume a correct string exists and a program can check it. A general-purpose assistant breaks that assumption twice. Its prompts are open-ended, so there is nothing to match against; and its training data is scraped from the same public web the benchmarks were published on, so a high score may mean the model has seen the test.

The cheap substitute in early 2023 was to ask a stronger model to grade. That is what the Vicuna team did on **30 March 2023**: GPT-4 compared five chatbots over 80 questions and put Vicuna at roughly 90% of ChatGPT. The same post said plainly that the method was "not yet a rigorous or mature approach" and that "building an evaluation system for chatbots remains an open question."

## What Got Built

Chatbot Arena, announced in an LMSYS blog post dated **3 May 2023**.

The mechanic is small. A visitor types any prompt; two randomly chosen models answer side by side with their names hidden; the visitor votes for one, calls a tie, or rates both bad; only then are the names revealed. Each vote is a single match result, and the leaderboard is an Elo rating computed over all of them — the ranking system from chess, borrowed because it turns many noisy pairwise outcomes into one ordered list. At announcement it rated nine models on about 4,700 valid votes, with Vicuna-13B on top.

What the design buys is specific. The test prompts are written live by the public, so no model can have trained on them in advance; and the grader is a human preference, so no answer key is needed. It sidesteps both failures above at once.

## Who Built It, And Why Them

LMSYS — a research collaboration its own site traces to UC Berkeley, Stanford, UC San Diego, Carnegie Mellon and MBZUAI in 2023. The blog post's authors were Lianmin Zheng, Ying Sheng, Wei-Lin Chiang, Hao Zhang, Joseph E. Gonzalez and Ion Stoica.

The commercial logic is that LMSYS was a *vendor* with the problem, not a neutral referee. Five weeks earlier it had shipped Vicuna and needed a defensible claim about how good Vicuna was; its own GPT-4-judge number was one it publicly doubted. The team also already ran a public web demo for Vicuna, so putting two models behind one prompt box was an extension of infrastructure it was paying for anyway. The group best placed to build a live preference leaderboard was the one already paying to serve the contestants.

It then outgrew the lab. LMSYS's site says Chatbot Arena has "graduated"; Wikipedia records incorporation as an independent company in April 2025 and a $100 million seed round in May 2025.

## What It Cost

The Arena measures what a crowd prefers, not what is correct. A fluent, confident, well-formatted wrong answer can win a vote.

It also became a target. Once the leaderboard mattered commercially, labs had reason to tune toward it. *The Leaderboard Illusion* (arXiv, **29 April 2025**) reported 27 private variants tested by Meta ahead of the Llama 4 release and argued that private testing with selective disclosure distorted the rankings. The instrument built to escape benchmark contamination acquired its own form of it.

## What You Still Touch

Every model launch now quotes an Arena rank or a win-rate against a rival, and every commercial evaluation shop runs some version of blind side-by-side human comparison. The questions the Arena deferred — whose preference, how expert, and whether the grader can be trusted — are the ones the industry now sells answers to.

- [[problems/ai-model-evaluation-firms/high-impact|🔴 Benchmark Contamination and Measurement Validity]] — the failure the Arena was designed around, and then reproduced
- [[problems/ai-model-evaluation-firms/low-impact-2|🟡 Human Preference Collection Quality]]
- [[niches/ai-model-evaluation-firms/human-preference-operations/profile|Human Preference Operations]]
- [[niches/ai-model-evaluation-firms/benchmark-integrity/profile|Benchmark Integrity]]
- [[niches/ai-model-evaluation-firms/judge-model-validity/profile|Judge Model Validity]] — the GPT-4-as-judge shortcut the Arena was built to check

**Sources:** LMSYS blog, "Chatbot Arena: Benchmarking LLMs in the Wild with Elo Ratings" (3 May 2023) and "Vicuna: An Open-Source Chatbot Impressing GPT-4 with 90% ChatGPT Quality" (30 March 2023); lmsys.org/about (member universities, "graduated" status); arXiv 2403.04132, Chiang et al., *Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference* (March 2024; 240K+ votes); arXiv 2504.20879, Singh et al., *The Leaderboard Illusion* (April 2025); Wikipedia, *LMArena* (company history, funding). WebSearch was not used; research was by WebFetch on these known URLs. ⚠️ **Discrepancy not resolved:** Wikipedia gives a launch date of **24 April 2023** and names Chiang, Angelopoulos and Stoica as creators; the LMSYS announcement is dated 3 May 2023 with a different author list. I use the dated primary post and treat the earlier date as unconfirmed. The claim that the existing Vicuna demo made the Arena cheap to add is my inference from the two posts, not a statement by LMSYS.
