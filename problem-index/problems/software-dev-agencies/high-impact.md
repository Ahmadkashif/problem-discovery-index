# Project Scoping & Estimation Accuracy

**Industry:** [[software-dev-agencies|Software Development Agencies]]
**Type:** High Impact
**One-liner:** Agencies stop bleeding margin on every project because estimates finally reflect actual build complexity instead of optimistic guesses.
**Tags:** #gradient-boosting #bert #transformers #feature-engineering #cross-validation #evaluation-metrics #word-embeddings #transfer-learning #bias-variance-tradeoff #tacit-knowledge-ml #revenue-impact

## The Problem
Software development agencies systematically underestimate projects by 30-50%, and the error compounds on fixed-bid contracts where every extra hour comes directly out of margin. The root cause is that estimation relies on senior leads pattern-matching against past projects in their heads — they read a client brief, sense which "simple" features hide architectural landmines (undefined integrations, ambiguous data models, unstated performance requirements), and adjust upward. But their adjustments are still anchored to the written scope, which is always incomplete. Junior PMs and less experienced leads lack this pattern library entirely, producing estimates that are functionally fictional.

## Why It's Unsolved
Historical project data is scattered across Jira boards, Google Docs, Slack threads, and individual memories — there is no structured dataset linking "what the client asked for" to "what it actually took." The features that predict blowups are linguistic and contextual: vague requirement language ("the system should handle payments"), missing technical specifics, references to third-party integrations without API documentation, and scope items that sound simple but require cross-cutting architectural changes. No off-the-shelf PM tool models this because the signal is in the text of the brief, not in the task list. The tacit knowledge challenge is severe — experienced leads often cannot articulate why they sense a project will blow up; they just "know" from the shape of the requirements.

## What a Solution Looks Like
A model that ingests a client brief (requirements doc, RFP, SOW) alongside structured metadata (tech stack, team size, integration count, client history) and outputs a calibrated effort estimate with confidence intervals and flagged risk areas. The system highlights specific passages in the brief that correlate with historical overruns — "this sentence pattern has been associated with 2.5x scope expansion in past projects." It does not replace the lead's judgment; it gives them quantitative backing to push back on timelines and price accordingly.

## Impact If Solved
A 20% improvement in estimation accuracy on a $2M/year agency translates to $200-400K in recovered margin annually. Across the industry, this addresses the single largest driver of agency failure — not lack of clients, but inability to deliver profitably.
