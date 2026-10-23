# A Payer-Specific Continued-Stay Writer With Days-at-Risk Tracking

**Niche:** [[niches/skilled-nursing-facilities/ma-authorization-denials/profile|Medicare Advantage Authorisation & Continued-Stay Reviews]]
**Industry:** [[industries/skilled-nursing-facilities|Skilled Nursing Facilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Each MA plan wants the same clinical progress in its own format on its own day, and the facility rewrites it by hand for every resident every week.
**Tags:** #large-language-models #transformers #gradient-boosting #workflow-orchestration #revenue-impact #automation #ai-agent
**Contested on:** Every serious competitor in this niche is fighting to keep every MA resident's authorised days matched to clinical need through weekly updates and appeals, and whoever wins the most continued-stay days that hold up on plan and QIO appeal takes the account.

## The Problem
A building with 20–30 MA residents (estimate) may deal with a dozen plans and their delegated managers. A nurse or MDS coordinator compiles therapy progress, functional scores and nursing needs into each plan's template, uploads it to the portal before its deadline, and logs the days approved. A missed deadline or thin update ends coverage while the resident still needs care.

## Why Nobody Has Built This
Plan requirements differ and change. EHR vendors avoid payer-specific workflows, and billing outsourcers work after the fact on claims. The clinical writing needed LLMs to automate credibly.

## What to Build
An agent that knows each plan's update schedule, template and criteria. It drafts each update from the week's therapy notes, Section GG changes and nursing documentation, with cited sources, and submits it through the portal or, as plans adopt it, the CMS-0057-F prior authorisation API. It maintains a days-at-risk board and predicts which stays are likely to be cut, so the team prepares peer-to-peer evidence in advance.

## Target Customer
VPs of revenue cycle and managed care at chains in high-MA markets; administrators of buildings with large MA censuses.

## Impact If Built
Each update takes ~10 minutes instead of ~45 (estimate). At 20–30 MA residents a building (estimate) that returns ~15 staff hours a week, fewer covered days are lost to missed deadlines or thin documentation, and denials are anticipated rather than discovered.
