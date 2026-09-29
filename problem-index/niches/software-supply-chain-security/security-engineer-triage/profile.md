# The Security Engineer

**Parent Industry:** [[industries/software-supply-chain-security|Software Supply Chain Security]]
**Category:** Underserved Audience
**Contested on:** Every serious competitor that takes this seriously is fighting to stop an application security engineer establishing that findings do not apply, one at a time, in a queue the scanner regenerates nightly — and whoever does that takes the function, because that is currently the job.

## Profile
**Market Size:** ~$260M US attributable to application security triage operations
**Share of Parent Industry:** ~9% of category revenue
**Digital Adoption:** None — triage is manual, repetitive and has no memory
**Target Buyer:** Application security leadership; the beneficiary is the engineer
**Automation Potential:** Very High — the determinations are repetitive and are discarded

## What Makes This a Distinct Niche
Application security engineers spend their weeks establishing that findings do not apply, one at a time, in a queue the scanner regenerates every night. The work has a specific and demoralising shape: each determination requires real expertise — reading the advisory, locating the usage, reasoning about reachability and configuration — and produces a conclusion that is discarded, repeated across every service using the same component, and regenerated after every version bump. The engineers are among the most skilled people in the organisation and are performing a lookup. The predictable consequences follow: the work that would prevent findings — threat modelling, architectural review, developer education — is displaced by triage, the engineers leave for roles where they can do it, and the function's headcount grows in proportion to the scanner's output rather than to the organisation's risk.

## Current Tools & Gaps
Vulnerability management platforms with ticketing, suppression files, and severity-based filtering. The gaps: determinations are not durable, portable or reusable, which is the core waste; the same component appears in forty services and is assessed forty times; nothing proposes a determination based on prior identical assessments; the queue's composition is not analysed, so nobody knows what proportion is repeat work; the engineer's expertise is applied to a lookup; and the preventive work that would reduce the inflow has no time allocated.

## Problems
- [[niches/software-supply-chain-security/security-engineer-triage/build|🔨 Build: Establishing That It Does Not Apply, Nightly]]
- [[niches/software-supply-chain-security/security-engineer-triage/buy|🛒 Buy: Case Management and Determination Reuse]]
- [[niches/software-supply-chain-security/security-engineer-triage/fix|🔧 Fix: The Same Component Assessed Forty Times]]
