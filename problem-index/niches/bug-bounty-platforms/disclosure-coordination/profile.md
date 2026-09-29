# Disclosure Coordination

**Parent Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Category:** Low Digitized
**Contested on:** Whether disclosure runs on an agreed process with defined timelines and legal protection, or on the goodwill of whoever answers the email.

## Profile

**Market Size:** ~$135M
**Share of Parent Industry:** ~9%
**Digital Adoption:** Low — email, spreadsheets and goodwill
**Target Buyer:** Disclosure and legal staff, vendor security teams, national coordination bodies
**Automation Potential:** Moderate — tracking automates, the negotiation does not

## What Makes This a Distinct Niche

Disclosure is the part of this industry that reaches outside the marketplace. A finding in a third-party component affects every organisation using it. A vulnerability in a vendor's product cannot be fixed by the programme that received the report. A researcher who wants to publish has to negotiate timing with a party who may prefer never. And a researcher reporting to an organisation with no programme at all has no protection whatsoever.

The contest is over whether any of this is governed. Within a bounty programme there is at least a platform, terms and a payment. Outside it — which is where the most consequential findings frequently sit — there is an email address, an unknown response time, no agreed timeline, no guarantee of credit, and in several jurisdictions genuine legal exposure for the person who did the right thing.

Every serious actor in this space is fighting over the same thing: whether disclosure can be made predictable enough that researchers will keep doing it. The alternative to a functioning disclosure process is not silence; it is that findings go to markets where the buyer does not want them fixed.

## Current Tools & Gaps

The `security.txt` convention publishes a contact point. Coordinated vulnerability disclosure policies exist at mature vendors with stated timelines, often ninety days. National coordination bodies handle multi-party cases. CVE assignment provides an identifier and is managed through a numbering authority structure. Platforms offer disclosure coordination as a service tier and manage publication timing for findings in their own programmes. Safe harbour language appears in many programme terms and varies enormously in strength.

The gaps are substantial. Multi-party disclosure — one finding affecting many downstream users of a component — is coordinated by hand, by email, at a scale that regularly defeats it. Timelines are asserted and unenforceable, so a vendor can stall indefinitely and the researcher's only lever is publication. Safe harbour is a contractual statement that does not bind third parties or prosecutors, and researchers reporting outside a programme have none. Credit is discretionary. And nothing tracks whether a disclosed vulnerability was actually fixed downstream, so the same flaw persists in forks and derivatives nobody notified.

## Problems

- [[niches/bug-bounty-platforms/disclosure-coordination/build|🔨 Build: Multi-Party Disclosure That Scales]]
- [[niches/bug-bounty-platforms/disclosure-coordination/buy|🛒 Buy: Coordination Infrastructure From Standards Bodies]]
- [[niches/bug-bounty-platforms/disclosure-coordination/fix|🔧 Fix: Safe Harbour That Does Not Bind Anyone]]
