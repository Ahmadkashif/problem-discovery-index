# Bespoke API Connectivity

**Parent Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor here is fighting to get a non-engineer connected to an internal system nobody has written a connector for, in the session where they need it — and whoever does that takes the builder, because the alternative is a hand-rolled HTTP block and a lost afternoon.

## Profile
**Market Size:** ~$740M US attributable to long-tail and custom integration within the category
**Share of Parent Industry:** ~12% of category revenue
**Digital Adoption:** Low — the tail is served by generic HTTP blocks and hand-written code
**Target Buyer:** The builder, in the moment; the platform vendor, structurally
**Automation Potential:** Very High — the specification describes almost everything required

## What Makes This a Distinct Niche
Every organisation of any size has systems that no connector marketplace will ever cover: the internal service the platform team built, the industry vertical product with a few hundred customers nationally, the acquired company's legacy system, the departmental tool with an API added as an afterthought. These are exactly the systems that hold the data the app needs, because they are the systems the business runs on. The contest here is time-to-connected for a person who cannot read an API specification and should not have to: whoever can take whatever description of the system exists — a specification file, a documentation page, an example request someone pasted in a chat, or the traffic itself — and produce a working, authenticated, typed connection in the same session wins the builder, and the builder is the person who chooses the platform.

## Current Tools & Gaps
Generic HTTP request blocks, custom connector authoring frameworks aimed at developers, community connector repositories, and integration platforms with their own custom connector tooling. The gaps: everything available assumes someone who can read a specification, which excludes the category's actual user; authentication is the single biggest failure point and is handled as a configuration form rather than as a recognised pattern; the connector a builder hand-rolls is invisible to the platform, so it cannot be monitored, reused or maintained; and nothing is reusable across builders in the same company, so three people connect to the same internal system three times.

## Problems
- [[niches/no-code-app-builders/bespoke-api-connectivity/build|🔨 Build: Connected in the Session, Not the Sprint]]
- [[niches/no-code-app-builders/bespoke-api-connectivity/buy|🛒 Buy: Specification Inference From Documentation and Traffic]]
- [[niches/no-code-app-builders/bespoke-api-connectivity/fix|🔧 Fix: Three People Connected to the Same System Three Times]]
