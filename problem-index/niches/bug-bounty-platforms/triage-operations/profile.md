# Triage Operations

**Parent Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Category:** High Market Share
**Contested on:** Whether a qualified analyst's attention is spent on submissions that might be real, or spread evenly across a queue that is mostly not.

## Profile

**Market Size:** ~$375M
**Share of Parent Industry:** ~25%
**Digital Adoption:** Moderate — good workflow, manual judgement
**Target Buyer:** Platform triage leadership, programme managers
**Automation Potential:** High for filtering and routing, low for validation

## What Makes This a Distinct Niche

Triage is the largest operational cost in this industry and the reason many organisations run private programmes or none at all. A public programme receives a large majority of submissions that are duplicates, out of scope, scanner output or plain non-issues, and every one must be read by somebody qualified to tell a real finding from a plausible-looking one.

That qualification is the expensive part. Distinguishing a genuine authorisation bypass from a confidently written description of intended behaviour requires the same skill as finding the bypass. So the industry employs people capable of doing security research to read, mostly, submissions that are not security research — and the consequence of a misjudgement in the other direction is that a real vulnerability is closed as informative and stays in production.

Every serious competitor is fighting over the same thing: how much analyst attention each valid finding costs. A platform that could route its analysts' time toward the submissions most likely to be real, and away from the ones a machine can confidently dismiss, would have a structurally better cost position in a business whose margin is triage.

## Current Tools & Gaps

Submission workflow with state tracking, duplicate flagging by manual search, reputation-weighted queue ordering at some platforms, canned responses for common invalid categories, and escalation paths to the programme. Managed triage is sold as a service tier. Some automated detection of scanner output exists and is shallow.

The gaps are large. Duplicate detection is largely manual — an analyst searches prior submissions by keyword, which fails on the same finding described differently. Nothing predicts the probability a submission is valid, so queue order is by age or reputation rather than by expected value. Scope checking is manual, which is why out-of-scope submissions consume analyst time at all. Reproduction is done by hand from the researcher's prose rather than from anything executable. And nothing measures analyst calibration, so the rate of real findings closed as invalid — the most expensive error in the system — is unknown everywhere.

## Problems

- [[niches/bug-bounty-platforms/triage-operations/build|🔨 Build: Triage by Expected Value]]
- [[niches/bug-bounty-platforms/triage-operations/buy|🛒 Buy: Support Triage Tooling With a Higher Bar]]
- [[niches/bug-bounty-platforms/triage-operations/fix|🔧 Fix: The Real Finding Closed as Informative]]
