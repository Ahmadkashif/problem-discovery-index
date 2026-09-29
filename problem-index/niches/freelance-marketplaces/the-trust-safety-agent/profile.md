# The Trust & Safety Agent

**Parent Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Category:** Underserved Audience
**Contested on:** Whether the person deciding an account's fate in fifteen minutes has the evidence assembled, or is assembling it themselves while the queue grows.

## Profile
**Market Size:** ~$1.12B — 8% of platform-intermediated gross services volume
**Share of Parent Industry:** ~8%
**Digital Adoption:** Low — a queue, a policy document and a set of browser tabs
**Target Buyer:** Platform trust & safety operations leadership
**Automation Potential:** High for evidence assembly and case routing; low and deliberately so for the decision itself

## What Makes This a Distinct Niche

An agent reviews a flagged account with fifteen minutes and a policy document, and the decision removes a person's income or lets a fraud continue. The asymmetry is brutal in both directions: a wrong suspension takes away a livelihood from someone with no meaningful appeal, and a wrong clearance leaves a fraudulent operator running against clients who trusted the platform's verification.

The agent has a queue, an account page, a set of related-account links, a message search and a policy document that was written for the cases it anticipated. Assembling the evidence for a decision — the account's history, its network relationships, its client outcomes, the pattern that triggered the flag and whether that pattern has a benign explanation — is manual, repeated for every case, and done under a handle-time target.

The niche is distinct from the gaming-resistance work because that is about detection and this is about adjudication. Detection produces the queue; this is about what happens to the person at the front of it.

## Current Tools & Gaps

Case management systems, queues with priority scoring, account detail views, related-account graphs where they exist, policy wikis and macro libraries. Several platforms run quality assurance sampling on agent decisions for policy adherence. The tooling is comparable to content moderation tooling of a decade ago.

The gaps are consistent with every other adjudication function in this industry: the evidence is not assembled, the decision space is binary when the situation calls for graduated responses, agent agreement is unmeasured, and the feedback loop is broken — an agent who suspends an account rarely learns whether the suspension was right, because the only signal is an appeal, and appeals come disproportionately from the articulate rather than the innocent.

## Problems
- [[niches/freelance-marketplaces/the-trust-safety-agent/build|🔨 Build: Case Assembly and Graduated Response for Account Review]]
- [[niches/freelance-marketplaces/the-trust-safety-agent/buy|🛒 Buy: Trust & Safety Case Tooling Adapted to Livelihood Decisions]]
- [[niches/freelance-marketplaces/the-trust-safety-agent/fix|🔧 Fix: The Agent Never Learns Whether They Were Right]]
