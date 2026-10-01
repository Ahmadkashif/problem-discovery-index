# Recruiting-Industry Candidate Matching

**Niche:** [[niches/expert-networks/custom-call-brokerage/profile|Custom Call Brokerage]]
**Industry:** [[industries/expert-networks|Expert Networks]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Recruiting technology has spent a decade building semantic matching between job descriptions and candidates, and an expert network solves a near-identical problem with a keyword search and a screener.
**Tags:** #transformers #word-embeddings #k-nearest-neighbors #gradient-boosting #evaluation-metrics #automation
**Contested on:** This niche is not terminal — finding an expert for a fund that covers the same tickers every quarter and finding forty experts on a private target inside a two-week deal clock are different contests with different winners, and they are stated separately in the sub-niches.

## The Problem
An expert request is a job description for one hour: a role, an employer type, a time window, a decision the person must have owned. Associates translate it into keyword searches and read results by hand.

## What Already Exists
Recruiting platforms offer semantic matching of candidates to roles, skills inference from profiles, outreach sequencing with response-rate optimisation, and candidate rediscovery from an applicant database.

## The Customization Gap
The adaptation needs: (1) matching on a decision rather than a skill — the expert must have owned a specific choice at a specific time, which is closer to event extraction from a career history than to skills matching; (2) a time window, since knowledge decays and the client often wants a specific period; (3) compliance as a hard filter applied before ranking, varying by client; (4) outcomes in hours rather than months, so the model can be retrained on call ratings continuously; and (5) screener design as part of the product, since the question set determines what evidence of fit is collected.

## Target Customer
Heads of operations and product at expert networks; vendors of recruiting technology looking for an adjacent market.

## Impact If Solved
Recruiting has solved most of the generic matching problem; the expert-network version is narrower, faster-feedback and higher-value per match, and the adaptation is mostly about decisions, time windows and compliance.
