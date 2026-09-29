# Finding Out From the Client

**Niche:** [[niches/saas-implementation-partners/release-regression/profile|Release Regression Management]]
**Industry:** [[industries/saas-implementation-partners|SaaS Implementation Partners]]
**Type:** Fix (Pain Point)
**One-liner:** The release broke an approval rule and the partner learned about it from an angry support ticket.
**Tags:** #quick-win #automation #evaluation-metrics #workflow-orchestration #change-point-detection #descriptive-statistics #compliance #data-integration
**Contested on:** Every serious competitor in this niche is fighting to establish whether three platform releases a year have broken any of hundreds of client customisations, using manual test scripts — and whoever automates that takes the account.

## The Problem
The partner's first notification of a release breaking something is a client reporting it in production. The release notes were published weeks earlier, the preview environment was available, and nobody had the capacity to check every client against them. The damage is a live business process failing, a support escalation, and a client who concludes the partner is not on top of the platform they were hired for.

## Why It's Still Broken
Nobody reads the release notes against the configurations — a change note describing a platform behaviour means nothing until someone checks which clients depend on that behaviour, and nobody has the list. Testing capacity is fixed. The preview window is short. And the platform vendor is a convenient explanation.

## What a Fix Looks Like
Read the release notes against a list of what clients actually use. Maintain a list of which platform features each client's configuration depends on, which is the fix and is the prerequisite for everything else. Cross-reference each release's change notes against that list to produce a shortlist of clients at risk, which turns an impossible task into a manageable one. Test the shortlist rather than everything, which is what makes the window sufficient. Start from the release preview rather than waiting for production. Notify at-risk clients before the release rather than after the incident, which changes the relationship entirely. Record what actually broke each release, so the risk list improves and becomes evidence. Prioritise by business criticality rather than by configuration complexity. Ask the platform vendor for earlier or better change detail, which partners are entitled to and rarely press for. Reuse the analysis across clients with the same configuration pattern. And publish a release readiness note per client, which is a deliverable clients value and costs little once the analysis exists.

## Who Feels the Pain
Clients with a broken process in production; support teams handling an avoidable escalation; partners whose competence is questioned for a vendor's change; and the managed services margin.

## Impact If Fixed
A change note describing a platform behaviour means nothing until someone checks which clients depend on it, and nobody has the list. A dependency list cross-referenced against release notes turns an impossible task into a shortlist.
