# Defect Triage Practice

**Niche:** [[niches/seo-tooling-vendors/site-audit-and-prioritisation/profile|Site Audit & Impact Prioritisation]]
**Industry:** [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Software engineering triages defects by impact and cost as routine practice, and SEO audits ship a severity word applied to every site identically.
**Tags:** #workflow-orchestration #gradient-boosting #evaluation-metrics #convex-optimization #descriptive-statistics #confidence-intervals #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to rank a site's issues by what fixing them would do for that site — and whoever does that turns an eleven-thousand-row export into a ticket an engineering team will actually take.

## The Problem
Engineering organisations triage defects as a matter of routine: severity assessed against user impact for this product, priority set against cost and business consequence, duplicates merged, and a backlog ordered so the next thing worked on is the most valuable thing. Static analysis tools that produce thousands of undifferentiated findings are widely criticised for exactly the failure SEO audit tools exhibit, and the better ones have responded with contextual severity and noise suppression. SEO tooling has not.

## What Already Exists
Defect triage frameworks separating severity from priority; static analysis with contextual suppression and ranking; duplicate detection and grouping; backlog prioritisation against cost and value; and integration into engineering workflow systems.

## The Customization Gap
The adaptation is to a defect whose consequence is a traffic change rather than a user-visible fault. It requires: (1) impact estimated from an external and delayed signal rather than from a crash report, so the severity depends on ranking and traffic consequences that unfold over weeks — this makes impact estimation statistical where software triage is mostly observational; (2) the consequence differing wildly by page value, which means the same defect on two pages of the same site has different priorities and no software triage model treats identical defects differently by location; (3) the requester having no authority over the backlog, since the SEO is petitioning engineering rather than owning the queue, which changes the output from a priority to an argument; (4) grouping by template rather than by symptom, as thousands of occurrences are usually one change; and (5) verification through subsequent traffic rather than through a test, which is slow and noisy.

## Target Customer
Technical SEO teams, engineering organisations receiving SEO requests, and audit tooling vendors whose outputs go unactioned.

## Impact If Solved
Software triage was forced to solve the thousand-undifferentiated-findings problem and SEO audits still produce it. Impact that is statistical and delayed, and differs by page value for identical defects, is what the software model does not handle.
