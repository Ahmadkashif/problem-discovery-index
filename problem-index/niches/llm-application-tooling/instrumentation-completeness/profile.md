# Instrumentation Completeness

**Parent Industry:** [[industries/llm-application-tooling|LLM Application Tooling]]
**Category:** Low Digitized
**Contested on:** Every serious competitor in this niche is fighting to make the trace contain the thing you need at the moment you need it — and whoever does that takes the account, because a trace missing the decisive context is indistinguishable from no trace at all.

## Profile
**Market Size:** ~$190M US
**Share of Parent Industry:** ~11% of category revenue
**Digital Adoption:** Low — traces missing the decisive context
**Target Buyer:** Platform and applied AI teams
**Automation Potential:** High — completeness is checkable automatically

## What Makes This a Distinct Niche
Tracing libraries are mature and standards-compliant, and the traces most applications emit are missing exactly the context needed to debug the failure in front of you. The model call is recorded and the retrieval that fed it is not; the response is recorded and the user's reaction to it is not; the prompt template is recorded and the variables substituted into it are not; the request is recorded and the application state that shaped it is not. Each omission is a deliberate-looking choice made by a developer instrumenting quickly and is discovered months later in an investigation that cannot proceed. Completeness is checkable automatically and nothing checks it.

## Current Tools & Gaps
Automatic instrumentation for supported libraries, manual span creation, and context propagation. The gaps: no measure of trace completeness; no checking that a trace contains what a debugging session needs; automatic instrumentation covers the framework and not the application logic around it; user reactions are in a different system; and no guidance on what to instrument, so it is learned by failing to debug.

## Problems
- [[niches/llm-application-tooling/instrumentation-completeness/build|🔨 Build: Traces Missing Exactly What You Need]]
- [[niches/llm-application-tooling/instrumentation-completeness/buy|🛒 Buy: Auto-Instrumentation and Context Propagation]]
- [[niches/llm-application-tooling/instrumentation-completeness/fix|🔧 Fix: The User's Reaction in a Different System]]
