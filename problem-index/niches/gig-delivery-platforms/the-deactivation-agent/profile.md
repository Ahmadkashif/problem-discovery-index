# The Deactivation Review Agent

**Parent Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Category:** Underserved Audience
**Contested on:** Whether the person deciding within minutes whether someone keeps their income has the evidence assembled and any response available between nothing and permanent removal.

## Profile
**Market Size:** ~$5.4B — 6% of US gross order value
**Share of Parent Industry:** ~6%
**Digital Adoption:** Low — a flag, a policy, a queue and a handle-time target
**Target Buyer:** Platform trust & safety operations leadership
**Automation Potential:** High for evidence assembly and routing; deliberately low for the decision

## What Makes This a Distinct Niche

Someone lost their income because an automated system flagged their account, and an agent with a policy and a queue decides within minutes whether they get it back. For a full-time courier a deactivation is the loss of a job, delivered by an automated system, with no employment protections because the classification is contractor — a classification that remains genuinely contested in law and varies by jurisdiction.

The agent is the only human in that chain and is set up to fail. The flag arrives with a reason code and thin context. The evidence — the customer complaint, the GPS trace, the delivery photo, the account's full history, the base rate for that complaint type — is spread across systems and assembled by hand. The action space is binary. The appeal, if there is one, routes to a similar queue.

It is a distinct niche from the platform's fraud detection because detection produces the flag and this is about what happens to the person behind it, and from courier-facing problems because the underserved party here is the reviewer.

## Current Tools & Gaps

Case management with queues and reason codes, account detail views, policy documents, macro libraries and some quality assurance sampling for policy adherence. Appeals processes exist and are generally thin. A few jurisdictions have introduced deactivation protections requiring stated reasons, notice periods and genuine appeal, and the systems built to satisfy them show what is feasible.

The gaps mirror every adjudication function in this batch. Evidence is not assembled. Complaint base rates are not surfaced, so an agent cannot tell whether two complaints in six hundred deliveries is unusual. The action space has no middle. Inter-agent agreement is unmeasured. And the outcome feedback loop is broken — an agent learns they were wrong only via an appeal, and appeals come disproportionately from the articulate and the persistent.

## Problems
- [[niches/gig-delivery-platforms/the-deactivation-agent/build|🔨 Build: Case Assembly, Base Rates and a Graduated Response]]
- [[niches/gig-delivery-platforms/the-deactivation-agent/buy|🛒 Buy: Trust & Safety Tooling Adapted to Deactivation]]
- [[niches/gig-delivery-platforms/the-deactivation-agent/fix|🔧 Fix: Two Complaints in Six Hundred Deliveries, With No Baseline]]
