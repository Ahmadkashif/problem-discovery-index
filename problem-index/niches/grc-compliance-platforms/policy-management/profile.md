# Policy & Document Management

**Parent Industry:** [[industries/grc-compliance-platforms|GRC & Compliance Platforms]]
**Category:** Highly Automatable
**Contested on:** Whether the policy set describes how the organisation actually operates, or is a document library maintained because an auditor will ask for it.

## Profile

**Market Size:** ~$450M
**Share of Parent Industry:** ~5%
**Digital Adoption:** Moderate — the mechanics are solved
**Target Buyer:** Compliance operations, HR, legal
**Automation Potential:** Very high — versioning, distribution and attestation are mechanical

## What Makes This a Distinct Niche

Every framework requires documented policies, and every organisation therefore has an information security policy, an access control policy, an incident response plan, a business continuity plan and a dozen others. They must be reviewed annually, distributed to staff, acknowledged, and produced for the auditor with evidence that everyone read them.

The mechanics of this — versioning, distribution, attestation tracking, review reminders — are genuinely solved. Every platform does it and it works.

The contest is over whether the documents mean anything. Policies are frequently generated from templates, approved with light editing, attested by staff who scrolled to the bottom, and never consulted again by anyone except during the next audit. Meanwhile the organisation's actual practice is defined by its technical configuration and its team norms, which may or may not resemble what the policy says. Nothing ever compares them.

It is the most automatable niche in the industry and sits alongside [[niches/grc-compliance-platforms/vendor-risk/profile|⚡ Vendor & Third-Party Risk]] as the mechanical pair. The interesting question in it is not workflow but whether the policy layer could be connected to the control layer at all.

## Current Tools & Gaps

Policy templates supplied by the platforms, editing and approval workflow, versioning, distribution with attestation tracking, review reminders, and evidence packages for auditors. Training modules and acknowledgement records. Document libraries with access control.

The gaps are about meaning rather than mechanism. Policies are not linked to the controls that implement them, so a policy statement and the actual configuration can diverge indefinitely with nothing detecting it. Templates produce documents describing practices the organisation does not follow, which is a latent audit finding and a real liability. Attestation measures scrolling rather than comprehension. Review is an annual date rather than a trigger from changed practice. And the policy set grows monotonically because retiring a document requires someone to argue it is unnecessary.

## Problems

- [[niches/grc-compliance-platforms/policy-management/build|🔨 Build: Policies Bound to Controls]]
- [[niches/grc-compliance-platforms/policy-management/buy|🛒 Buy: Documentation Practice From Engineering]]
- [[niches/grc-compliance-platforms/policy-management/fix|🔧 Fix: The Policy Describes a Company That Does Not Exist]]
