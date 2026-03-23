# AI-Powered Grant-Client Matching Engine

**Niche:** [[niches/grant-writers/opportunity-matching/profile|Grant Research & Opportunity Matching]]
**Industry:** [[industries/grant-writers|Grant Writers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool learns from a grant writer's accept/reject decisions to build an increasingly accurate model of which opportunities match each client — every search starts from zero.
**Tags:** #gradient-boosting #ranking #tabular-ml #recommendation #ai-agent

## The Problem
A grant writer managing 5 clients with different missions monitors 4-5 grant databases weekly, reviews 50-100 new opportunities, and selects 3-5 to pursue per client. The writer's selection criteria are partly explicit (geography, funding range, eligibility) and partly tacit — "this foundation's language suggests they want direct-service programs, not advocacy" or "this federal program funded our competitor last year, so they're unlikely to fund us." Over years, the writer develops a mental model of which opportunities are worth pursuing for each client. This tacit matching knowledge is never captured, never transferred to junior staff, and resets when the writer takes on a new client.

## Why Nobody Has Built This
Existing grant databases (Instrumentl, GrantStation) optimize for breadth of listings, not match quality. They use keyword search and category filters, not learning algorithms. Building a matching engine requires: structured client profiles (mission, geography, budget, service population), structured opportunity profiles (funder priorities, past awards, eligibility criteria), and a feedback loop (accepted/rejected opportunities and win/loss outcomes). No grant database has this feedback loop because writers don't report back on whether they pursued an opportunity or won the award.

## What to Build
A matching engine that: (1) creates structured client profiles from intake information and past proposal data, (2) ingests opportunities from multiple databases (Grants.gov, Foundation Directory, state portals) into a unified format, (3) ranks opportunities by match quality using explicit criteria (geography, eligibility, amount) and learned criteria (funder alignment, competitive landscape, historical win patterns), (4) improves over time as the writer marks opportunities as "pursue," "skip," or "won/lost," (5) surfaces opportunities the writer might miss because they fall outside their usual search patterns but match the client's profile, and (6) provides match explanations ("high match because: geography overlap, funding range match, funder prioritizes direct service, 3 similar orgs funded in past 2 years").

## Target Customer
Grant writing firms managing 5+ clients who spend 10+ hours/week on opportunity research and want to reduce research time while improving match quality.

## Impact If Built
Reduces opportunity research time from 10+ hours/week to 3-4 hours/week, improves match quality by surfacing non-obvious opportunities, and enables junior writers to identify strong matches without senior-level tacit knowledge.
