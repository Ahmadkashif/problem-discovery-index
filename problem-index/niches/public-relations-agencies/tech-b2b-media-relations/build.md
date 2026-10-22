# Angle-to-Reporter Matching From What Reporters Actually Ran

**Niche:** [[niches/public-relations-agencies/tech-b2b-media-relations/profile|Technology & B2B Media Relations]]
**Industry:** [[industries/public-relations-agencies|Public Relations Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Tech PR teams choose angles and reporters separately, when the coverage decision is a match between the two that every reporter's published record already reveals.
**Tags:** #tacit-knowledge-ml #transformers #word-embeddings #gradient-boosting #evaluation-metrics #revenue-impact #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to turn client news that reporters treat as interchangeable (another AI launch, another funding round, another survey) into a data- or customer-led story that a named beat reporter will run, and whoever matches angle to reporter best takes the account.

## The Problem
A software client is announcing a product with a survey of 1,000 IT buyers attached. The account team drafts three possible angles (the survey finding, a named customer's result, the chief executive's view on a market trend) and then builds one list. Senior publicists know that one enterprise reporter only runs survey stories with a methodology note and an exclusive, that another wants a customer on the record, and that a third covers the trend but never single-vendor news. Juniors pitch all three angles to everyone, or one angle to all.

## Why Nobody Has Built This
Media databases sell contacts and beats, which are coarse labels. The fine-grained signal (which formats and angles each reporter has actually run in the last six months) sits in public articles that nobody has represented at the angle level, and the response signal sits in each agency's outreach logs.

## What to Build
Represent each reporter by embeddings of their recent articles, segmented by story type (data story, customer story, funding, trend piece, product review) and by sources they quote. Represent each candidate angle the same way. Rank reporter–angle pairs by fit, re-weighted by the agency's own reply and coverage history, and show the evidence (the three most similar pieces each reporter ran). Capture the senior's keep and drop choices to train the ranker over time.

## Target Customer
Practice leads and media relations directors at technology agencies of 20–300 staff, and in-house tech communications teams running frequent launches.

## Impact If Built
Fewer, better-matched pitches per announcement, higher tier-one hit rates per launch, and juniors who pitch the right angle to the right reporter from their first month.
