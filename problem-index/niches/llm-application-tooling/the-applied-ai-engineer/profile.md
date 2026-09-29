# The Applied AI Engineer

**Parent Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor in this niche is fighting to tell an engineer which of five simultaneously-moving things caused a quality change — and whoever does that takes the account, because that attribution is most of the job and nothing supports it.

## Profile
**Market Size:** ~$170M US in loaded engineering cost
**Share of Parent Industry:** ~9% of category revenue equivalent
**Digital Adoption:** None — bisecting a stack that moves underneath
**Target Buyer:** Applied AI engineering teams and their leads
**Automation Potential:** Very High — every moving part is recordable

## What Makes This a Distinct Niche
An applied AI engineer investigating why answers got worse must separate their own prompt changes from a provider's silent model update, a retrieval change, a data change and ordinary sampling noise, with no reliable baseline anywhere. Four of those five move without announcement, three of them belong to other teams or other companies, and the fifth is large enough to hide a real regression. The engineer bisects by hand, re-running samples through configurations they reconstruct from memory, on a stack where the ground moves between measurements. This is the recurring core of the role in every organisation running one of these applications, and nothing in the category addresses it.

## Current Tools & Gaps
Traces, prompt version history, and whatever the engineer remembers. The gaps: no versioned record of all five components together; no continuous baseline against which change is measured; no detection of provider-side model changes; no statistical treatment, so noise is chased and real regressions dismissed; and no attribution of a quality change to a cause.

## Problems
- [[niches/llm-application-tooling/the-applied-ai-engineer/build|🔨 Build: Five Things Moved and One of Them Was Yours]]
- [[niches/llm-application-tooling/the-applied-ai-engineer/buy|🛒 Buy: Change Attribution and Continuous Benchmarking]]
- [[niches/llm-application-tooling/the-applied-ai-engineer/fix|🔧 Fix: The Model That Changed Without Telling Anyone]]
