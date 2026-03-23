# Automated Government Meeting Coverage Pipeline

**Niche:** [[niches/news-media-local/rural-news-deserts/profile|Rural News Deserts]]
**Industry:** [[industries/news-media-local|Local News Media]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool automatically monitors rural county and municipal meeting agendas, transcribes meetings, extracts newsworthy decisions, and generates publishable summaries — the foundational civic coverage that news deserts lack.
**Tags:** #llm #speech-recognition #text-generation #nlp #automation #ai-agent

## The Problem
The most immediate consequence of a news desert is that nobody covers government meetings. County commissions, school boards, planning commissions, and water districts make decisions affecting thousands of people with zero public scrutiny. A single reporter cannot physically attend 10-15 meetings per month across a rural county where government bodies meet in different towns 40 miles apart. Most meetings now record audio or video (many since COVID), but nobody has time to watch 3-hour meeting recordings to extract the 4 newsworthy decisions.

## Why Nobody Has Built This
Government meetings are technically challenging to process: audio quality varies enormously (echoey community centers, muffled speakers), proceedings follow Robert's Rules loosely (motions aren't always clearly stated), and extracting "what's newsworthy" requires understanding local context (a zoning change that sounds routine might be the first step toward a controversial development). Existing transcription services (Otter, Rev) produce raw transcripts but don't identify decisions, votes, or newsworthy moments. The per-market revenue is too low for enterprise tools to care.

## What to Build
A pipeline that: (1) ingests meeting audio/video from YouTube, Zoom recordings, or uploaded files, (2) transcribes with speaker identification, (3) identifies formal actions (motions, votes, approvals) using procedural language patterns, (4) extracts newsworthy items based on configurable criteria (budget changes over $X, zoning decisions, personnel actions), and (5) generates draft meeting summary articles that a human editor reviews and publishes. Target accuracy: 95% on formal action extraction, human review required for editorial framing.

## Target Customer
Nonprofit news startups, community information hubs, and community foundations funding civic coverage in counties that have lost their newspaper.

## Impact If Built
Enables a single part-time editor to provide civic coverage across an entire rural county (10-15 government bodies) — coverage that currently doesn't exist at all — at a cost of $200-500/month in software rather than $40K-60K/year in reporter salary.
