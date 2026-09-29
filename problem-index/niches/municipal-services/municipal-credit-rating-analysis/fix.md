# Analyst Judgment About a Community Is Recorded as a Notch

**Niche:** [[niches/municipal-services/municipal-credit-rating-analysis/profile|Municipal Credit Rating & Public Finance Analysis]]
**Industry:** [[industries/municipal-services|Municipal Services]]
**Type:** Fix (Pain Point)
**One-liner:** An analyst who has covered a state for a decade knows which governments will actually raise taxes when they need to, and the rating shows a letter.
**Tags:** #tacit-knowledge-ml #text-classification #large-language-models #worker-facing #compliance

## The Problem
Municipal credit turns on things that are not in the financial statements. Whether a council has the political capacity to raise rates. Whether a state will support a distressed local government or let it fail. Whether a manager's projections have historically been realistic. Whether a labour contract cycle is about to reset the cost base. How a particular state's oversight regime actually behaves when a city gets into trouble.

An analyst covering a state for a decade knows all of it, and it is often the difference between two credits with identical ratios. That knowledge shapes the rating and appears in the rating as a letter and a paragraph of published rationale written for an external audience.

The internal record — why the analyst weighted governance the way they did, what they expect this issuer to do under stress, which of their assessments have been borne out — is not captured in any structured form. Analysts cover regions for years and then move, and the successor inherits a book of credits with published rationales and none of the understanding behind them.

## Why It's Still Broken
The published rationale is a regulated document written to a template, and everything about the process points at producing it. Post-crisis regulation emphasized transparency of criteria and consistency of application, which pushed the organization toward documenting method rather than judgment.

There is also a genuine caution: internal analyst notes about a government's political capacity or a manager's credibility are sensitive, and could be sought in litigation or by the issuer.

That is an argument for careful design, not for having no record. The alternative in place is that the most valuable analytical asset in the business exists only in individual memory.

## What a Fix Looks Like
Capture the qualitative assessment as structured, internal, dated records.

**Typed issuer assessments.** Governance capacity, management credibility, political willingness to act, state oversight posture, revenue-raising flexibility — recorded with evidence and a confidence level, separate from the published rationale.

**Record the expectation.** What the analyst expects this issuer to do under a defined stress, stated at the time. This is what makes the assessment testable, and checking those expectations against outcomes over years is the only way anyone learns which analysts' judgments are reliable and on what.

**State and regional context notes.** How a state's oversight regime behaves in practice, which is knowledge that applies across every credit in that state and is currently rebuilt by each analyst who covers it.

**Retrieval at surveillance.** An analyst picking up a credit — especially a new analyst inheriting a book — should see the accumulated assessment history rather than starting from the last published rationale.

**Internal by design.** These are the agency's own analytical working records with a defined status, which is a policy decision the organization can make deliberately rather than by keeping nothing.

## Who Feels the Pain
Analysts inheriting coverage, rebuilding a decade of regional understanding. Senior analysts, who are the agency's real capability and cannot be replicated. Criteria teams, who cannot see which qualitative factors actually predicted anything. And issuers, whose rating depends partly on who covers them.

## Impact If Fixed
The qualitative assessment is where municipal credit analysis adds value beyond the ratios, and it is entirely undocumented in a workforce with normal turnover. Structuring it makes coverage consistent through transitions, gives criteria development an evidence base, and — by recording expectations that can be checked — is the only route to knowing whether the judgment the whole business rests on is any good.
