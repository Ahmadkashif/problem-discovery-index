# Investigative Case Research and Fact Consistency Platform

**Niche:** [[niches/podcasting-networks/true-crime-networks/profile|True Crime Networks]]
**Industry:** [[industries/podcasting-networks|Podcasting Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform helps true crime producers maintain a structured case database with timeline, evidence, source references, and cross-episode fact consistency — ensuring that claims made in Episode 15 don't contradict evidence presented in Episode 3.
**Tags:** #llm #named-entity-recognition #nlp #data-integration #ai-platform

## The Problem
A true crime series covering a complex case (multi-season, 20–50 episodes) generates thousands of facts: dates, locations, witness statements, forensic evidence, legal proceedings. The producer and writers track these in Google Docs, personal notes, and memory. As the series progresses, factual inconsistencies creep in — a date mentioned in Episode 5 doesn't match the timeline in Episode 22. A witness statement quoted in Season 1 is paraphrased differently in Season 3. When listeners (who are obsessively detail-oriented) catch these inconsistencies, they flood social media and damage the show's credibility. The producer spends hours re-listening to old episodes to verify facts before scripting new ones.

## Why Nobody Has Built This
True crime podcasting is a relatively new format — the genre exploded after Serial (2014). The research workflow resembles investigative journalism, but newsroom tools (DocumentCloud, Aleph) are designed for text-based reporting, not audio production. The fact-checking workflow for a 30-episode audio series has no precedent in traditional media. And the market is concentrated: perhaps 200–500 true crime shows are large enough to justify production tooling, making it a small addressable market for a standalone product.

## What to Build
A case management platform where producers build a structured case file: (1) a timeline of events with source attribution (court record, interview, public document), (2) a character/entity database (victim, suspect, witnesses, investigators) with all statements attributed by source and episode, (3) an evidence registry linking physical evidence, forensic reports, and expert testimony to timeline events, (4) a fact-checking layer that highlights potential contradictions when new script content references established facts, and (5) episode-level annotation that marks exactly where in each published episode specific facts were stated. LLM-powered transcript analysis can auto-populate the fact database from existing episode transcripts, giving producers a retroactive case file for shows already in production.

## Target Customer
Executive producers and showrunners at true crime podcasts and networks producing serialized investigative content with 10+ episodes per series.

## Impact If Built
Eliminates 5–10 hours per episode of fact-verification time (re-listening to old episodes, searching documents). Prevents factual errors that generate listener complaints and social media backlash — each major error costs 2–5% of audience in the following episodes. Enables producers to take on more complex cases (multiple suspects, decades-long timelines) that would be unmanageable with current ad-hoc tracking.
