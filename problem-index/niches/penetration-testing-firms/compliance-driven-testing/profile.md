# Compliance-Driven Testing

**Parent Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Category:** Highly Automatable
**Contested on:** Whether the engagement is scoped to find problems or to produce the artefact an auditor will accept, and whether anyone is willing to say which.

## Profile

**Market Size:** ~$360M
**Share of Parent Industry:** ~6%
**Digital Adoption:** Moderate — scanning plus manual validation
**Target Buyer:** Compliance and audit functions, procurement, vendor risk teams
**Automation Potential:** Very high — the scope is defined by a framework

## What Makes This a Distinct Niche

A large share of testing is procured to satisfy a requirement. SOC 2 mentions penetration testing. PCI DSS specifies it. Customer security questionnaires ask whether annual testing is performed. Cyber insurance applications ask the same. The buyer in these cases needs a dated report from a credible firm, and the security value is a secondary benefit rather than the purchase driver.

This shapes everything about the engagement. Scope tends toward what is auditable rather than what is risky. Depth is whatever the framework's language can be read to require, which is usually not much. Price falls toward the cost of the thinnest acceptable deliverable, because a buyer who needs a document is rationally indifferent between a thorough test and a sufficient one.

It is a distinct market because the buyer, the success condition and the economics all differ from risk-driven testing. And it is the reason the whole industry's pricing is under pressure: firms doing genuinely deep work compete in the same procurement process against firms producing an artefact, with nothing in the deliverable that lets a buyer tell them apart. That is the same measurement absence that runs through [[niches/penetration-testing-firms/assessment-assurance/profile|🔵 Assessment Assurance]], seen from the commercial end.

## Current Tools & Gaps

Automated scanning platforms with a manual validation layer, delivered as a fixed-price package against a defined framework scope. Compliance automation platforms — Vanta, Drata, Secureframe — manage the surrounding evidence and increasingly partner with or resell testing. Audit firms accept reports on largely undocumented criteria. Questionnaire platforms collect the artefact as a yes-or-no attestation.

The gaps are mostly about honesty and specification. No framework states what depth of testing satisfies it, so the requirement is met by whatever an auditor accepts, which varies by auditor. Nothing distinguishes a compliance-scoped engagement from a risk-driven one in the artefact, so a thin report and a deep one are interchangeable in a questionnaire. Automated coverage is not reported, so the buyer cannot see how much of the engagement was a scan. And the compliance buyer has no way to purchase more depth deliberately, because there is no vocabulary for depth to buy.

## Problems

- [[niches/penetration-testing-firms/compliance-driven-testing/build|🔨 Build: The Honest Compliance Package]]
- [[niches/penetration-testing-firms/compliance-driven-testing/buy|🛒 Buy: Compliance Automation Extended Into Testing]]
- [[niches/penetration-testing-firms/compliance-driven-testing/fix|🔧 Fix: Nobody Will Say What the Requirement Requires]]
