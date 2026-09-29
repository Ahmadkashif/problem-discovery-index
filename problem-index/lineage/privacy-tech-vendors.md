# Lineage: Privacy Tech Vendors

**Industry:** [[industries/privacy-tech-vendors|Privacy Tech Vendors]]
**Wave:** [[series/eras/wave-09-programmatic|9 — Programmatic]]
**The tool:** the TC String of IAB Europe's Transparency & Consent Framework — a base64url bitfield recording, per user, which of up to 24 purposes and which numbered vendors on the Global Vendor List were consented to, passed along the bid request as `gdpr_consent`
**Builder:** IAB Europe
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

A publisher's page in 2017 routinely handed its visitor to dozens of companies the visitor had never heard of — ad server, exchanges, bidders, their data partners — each setting or reading an identifier.

The General Data Protection Regulation, applying from 25 May 2018, required a legal basis for that processing, and for much of it the basis the industry reached for was consent. **The constraint was topological, not legal.** Only the publisher could show the person a question. Every other company in the chain needed proof of the answer, delivered in the few milliseconds of an auction, about a vendor the publisher might not even know was downstream.

The answer had to travel with the impression.

## What Got Built

A string.

IAB Europe announced the Transparency & Consent Framework in November 2017, published its technical standards and policy terms in March 2018, and launched v1.1 on 25 April 2018 — a month before the regulation applied. Version 2.0 followed on 21 August 2019.

The v2 TC String is a big-endian bitfield, base64url-encoded so it survives a URL. Its core segment carries a 6-bit version, 36-bit created and last-updated timestamps, a **12-bit CmpId** naming the consent management platform that collected it, a 12-bit Global Vendor List version, **24 bits for purposes, one bit each**, and then one bit per registered vendor ID, or a range encoding when that is shorter.

Two registries make the bits meaningful: the **Global Vendor List**, a numbered directory of participating ad-tech companies, and the list of registered CMPs. A vendor learns whether it may proceed by checking a single bit at its own ID.

## Who Built It, And Why Them

IAB Europe, the Brussels trade association for the digital advertising industry, with the technical specifications stewarded by IAB Tech Lab's GDPR working group.

The reason it was a trade body and not a vendor is that **the problem was a coordination problem across competitors.** No single exchange could define a consent signal the others would honour; a signal only one bidder reads is worth nothing to a publisher. The association that already convened those companies was the only party that could issue numbered IDs to all of them and make them agree on bit positions.

The shape follows directly from whose revenue was at stake. The string does not describe the person or the page; it describes **the vendors**, because the vendors were the ones who needed permission to keep bidding. Purposes were fixed and enumerated so a machine could check them, not so a person could read them.

And the 12-bit CmpId created an industry. Once the framework needed someone to show the banner, write the string and register an ID, the consent management platform became a registrable product category — the first slot most privacy tech vendors ever filled.

## What It Cost

**Consent became a bit that could be optimised.** The framework standardised what was stored, not what was understood, and a CMP's commercial value to a publisher is measured by how many bits come back set.

The design also broadcast the answer — and so, arguably, the question — to every vendor in the chain. On 2 February 2022 the Belgian Data Protection Authority ruled that the framework failed GDPR on several counts, fined IAB Europe €250,000 and ordered changes; the decision was approved at European Data Protection Board level, and IAB Europe announced an appeal. The standard's owner had become, in the regulator's view, responsible for the processing its string enabled.

## What You Still Touch

The banner with "Accept all" in the bright button and "Manage options" beneath it is the front end of a bitfield; its vendor list is the Global Vendor List made visible.

- [[problems/privacy-tech-vendors/high-impact|🔴 Consent Measured on Acceptance, Never on Understanding]] — the direct descendant of storing consent as a bit
- [[problems/privacy-tech-vendors/low-impact-2|🟡 Knowing What Actually Leaves]] — the string records who was permitted, not who received
- [[niches/privacy-tech-vendors/consent-management/profile|Consent Management]]
- [[niches/privacy-tech-vendors/tag-governance/profile|Cookie & Tag Governance]]

**Sources:** Wikipedia, *Transparency and Consent Framework* (November 2017 announcement, March 2018 publication, Global Vendor List, Belgian DPA ruling of 2 February 2022 and €250,000 fine, EDPB approval, Dutch DPA guidance, appeal); iabeurope.eu TCF page (v1.1 launch 25 April 2018; v2.0 August 2019, v2.1 August 2020, v2.2 May 2023, v2.3 April 2025); GitHub InteractiveAdvertisingBureau/GDPR-Transparency-and-Consent-Framework README (v2.0 released 21 August 2019; IAB Europe oversight, IAB Tech Lab technical stewardship) and the *Consent string and vendor list formats v2* specification (field widths, 24 purposes, base64url, `gdpr_consent` macro, deprecation of the shared `euconsent-v2` cookie in September 2021). WebSearch was unavailable this session (session cap reached); research was by WebFetch on known URLs. ⚠️ **Not established:** the date and holding of the Court of Justice's judgment in case C-604/22 on whether the TC String is personal data — EUR-Lex and curia pages would not render, so it is omitted rather than asserted. No named individual designer of the v1 string could be established.
