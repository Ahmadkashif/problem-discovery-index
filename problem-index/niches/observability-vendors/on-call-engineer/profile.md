# The On-Call Engineer

**Parent Industry:** [[industries/observability-vendors|Observability Vendors]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor that takes this seriously is fighting to make on-call sustainable — fewer pages, better ones, fairly distributed, with the context attached — and whoever does that takes the engineering organisation, because on-call burden is a leading cause of the attrition that leadership actually feels.

## Profile
**Market Size:** ~$680M US incident response, paging and on-call tooling
**Share of Parent Industry:** ~6% of category revenue
**Digital Adoption:** Low — the human side of on-call is unmeasured and unowned
**Target Buyer:** Engineering leadership; the beneficiaries are the people on the rota
**Automation Potential:** High — page load, distribution and outcomes are all recorded

## What Makes This a Distinct Niche
The on-call engineer is the person the entire category exists to help, and is mostly not helped. They are woken by an alert that says a number crossed a threshold, with no indication of whether anyone is affected, whether it is the same thing as last week, what changed, or whether it could have waited until morning. The organisational side is equally unattended: page load is distributed very unevenly across a rota, the same services page repeatedly without anyone acting on the cause, handover between shifts loses context, and the cumulative human cost is one of the most cited reasons experienced engineers leave. This is a distinct contested surface because the product is about the person rather than the system — page quality, load distribution, context at wake-up, handover, and the sustainability of the rota — and because everything needed to measure it is already recorded and reported by nobody.

## Current Tools & Gaps
Paging and on-call scheduling platforms with rotations, escalation policies and incident timelines; runbooks in wikis; postmortem templates. The gaps: page quality is unmeasured, so an alert that woke somebody for nothing is indistinguishable from one that mattered; load is not reported per person, so the uneven distribution is invisible; repeat pages are not identified as repeats; the page carries a threshold breach rather than context, so the engineer starts from nothing at the worst hour; handover is a message; and nothing measures the sustainability of a rota until somebody resigns.

## Problems
- [[niches/observability-vendors/on-call-engineer/build|🔨 Build: Woken at Three by a Number]]
- [[niches/observability-vendors/on-call-engineer/buy|🛒 Buy: Shift Work Research and Workload Distribution]]
- [[niches/observability-vendors/on-call-engineer/fix|🔧 Fix: Nobody Measures Who Carries the Rota]]
