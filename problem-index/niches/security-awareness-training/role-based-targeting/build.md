# Build: Exposure-Based Assignment

**Niche:** Role-Based Risk Targeting
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Derive each person's actual exposure from access, transaction authority and observed targeting, and assign content and simulation difficulty accordingly rather than uniformly.
**Tags:** #gradient-boosting #graph-theory #evaluation-metrics #confidence-intervals #k-means-clustering #data-integration #automation #worker-facing
**Contested on:** Whether the programme reflects what a person is actually exposed to and what they already know.

## The Problem

Assignment is by department, which is a poor proxy for exposure. A finance department contains people who approve large payments and people who process expenses. An engineering department contains people with production access and people who do not. A sales department contains a handful of people whose calendars are public and who are named on the website.

The signals that would actually describe exposure are available and unused. The identity system knows what each person can access, including the small number with broad privilege. The finance system knows who can authorise payments and to what value. The public web presence shows who is externally visible. Email metadata shows who receives external mail at volume. And the organisation's own incident and reporting history shows which roles attackers have actually gone for.

Combining these produces a genuine exposure profile — this person can authorise payments, is publicly named, receives high external mail volume, and roles like theirs have been targeted twice in the last year — and it is a far better basis for assignment than a department code.

The consequence of not doing it is that the programme is simultaneously too much for most people and too little for the few who matter.

## Why Nobody Has Built This

**The platform sits outside the systems that know.** Identity, finance and incident data live elsewhere, and awareness platforms integrate with HR for the org chart and little else.

**Uniform assignment is defensible for compliance.** Everyone receiving the same training is easy to evidence. Differentiated assignment invites the question of why some people got less.

**The awareness manager cannot obtain the data.** Access and transaction authority data are held by teams the awareness function does not command.

**Targeting individuals as high-risk is sensitive.** Identifying a small group as high-exposure and treating them differently raises fairness and privacy questions that need handling, particularly where works councils are involved.

**Vendors sell libraries, not targeting.** The commercial product is content breadth, and targeting reduces the volume of content consumed.

**Nobody measures the mismatch.** Nothing reports how much of the assigned content is irrelevant to the recipient, so the waste is invisible.

## What to Build

**Derive exposure from access and authority.** Privilege level from the identity system, payment authority from finance, data access from the data platform, external visibility from the public web presence, external mail volume from the gateway. Each is a signal and together they are a profile.

**Add observed targeting.** Which roles this organisation's actual attackers have gone for, from the reporting stream and the incident record. This is the strongest signal and it is entirely local.

**Assign content to exposure, not to department.** Payment authorisers receive payment fraud content in depth; people with no such authority do not receive it at all. This shortens the programme for most and deepens it for the few.

**Vary simulation difficulty by exposure.** A high-exposure individual should be tested against the sophistication a real attacker would use on them, which is far higher than the organisational average. Uniform simulation under-tests exactly the people who matter.

**Assess prior knowledge and skip accordingly.** Someone who demonstrably knows the material should not sit through it. A short diagnostic would shorten the programme for a substantial share of the workforce and improve its standing considerably.

**Handle the high-exposure group properly.** The small number of genuinely targeted individuals warrant something other than a module — a briefing, a conversation, specific technical controls. Treating them as the top of a content assignment scale under-serves them.

**Govern the differentiation.** Identifying people as high-exposure needs a stated basis, transparency to the individual, and a framework agreed with HR, because it is a judgement about people that will be visible to them.

## Target Customer

Security leadership at organisations with clearly differentiated risk — financial services, organisations with high-value payment flows, any business where executive impersonation is a live threat.

Awareness managers, for whom exposure-based assignment is the change most likely to improve the programme's standing with the workforce by removing irrelevant content.

Vendors, for whom targeting is a genuine differentiator and requires integrations rather than more content.

## Impact If Built

Attention concentrates where exposure is, which is a large reallocation given how skewed real targeting is toward a small number of roles.

Shortening the programme for the majority by removing irrelevant content would improve its standing with the workforce more than any content refresh, and it is the main reason the annual module is resented.

And testing high-exposure individuals at the difficulty a real attacker would use on them addresses the specific failure where the people most likely to be targeted are tested with the same generic lure as everyone else.
