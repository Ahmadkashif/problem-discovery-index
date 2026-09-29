# Full-Population Testing

**Parent Industry:** [[industries/soc2-audit-firms|SOC 2 & Attestation Audit Firms]]
**Category:** Contested Sub-Niche
**Contested on:** Whether an auditor examines every item in a control's population, now that the population is sitting in a platform the client already runs.

## Profile

**Market Size:** ~$540M
**Share of Parent Industry:** ~18%
**Digital Adoption:** Very low — evidence is collected, sampling is unchanged
**Target Buyer:** Audit firm leadership, audit technology teams
**Automation Potential:** Very high — it is extraction and rule evaluation

## What Makes This a Distinct Niche

This is the technical half and it is available now. Compliance platforms hold complete, timestamped populations for most of the controls an attestation tests: every access review, every change ticket with its approval, every provisioning event, every configuration state. The auditor samples twenty-five.

It is separable from its sibling in every practical respect. [[niches/soc2-audit-firms/rigour-expression/profile|🎯 Rigour Expression]] requires the report format to change, standards bodies to move, and competitors to accept a comparison they would rather avoid — none of which a firm controls. Full-population testing requires an integration and a method change, nothing from anyone else, and it becomes cheaper than sampling once the connectors exist.

The contest is over whether the extraction can be made reliable enough to rely on. A population pulled from a platform is only as good as the platform's own coverage, and an auditor testing everything in an incomplete population has tested everything in the wrong set. Establishing what the extraction actually covers — and what it misses — is the substantive work, and it is the same coverage problem that runs through the compliance platform category itself.

## Current Tools & Gaps

Audit workpaper platforms recording tests and evidence. Compliance platform integrations at some firms, used to retrieve evidence more conveniently. Audit analytics tooling, mature and largely deployed in financial assurance rather than in attestation. Sampling guidance and sample selection tools.

The gaps are that the available data has not changed the method. Integrations retrieve evidence for a sample rather than extracting the population. Nothing verifies what a platform-derived population actually covers, so the completeness of the extraction is assumed. Control tests are not expressed as rules that could run over a population. Exceptions do not trigger full examination even where the data is present. And no firm has built the reusable connector library that would make full-population testing cheaper than sampling across a client base.

## Problems

- [[niches/soc2-audit-firms/full-population-testing/build|🔨 Build: The Population, Extracted and Tested]]
- [[niches/soc2-audit-firms/full-population-testing/buy|🛒 Buy: Audit Analytics, Already Built]]
- [[niches/soc2-audit-firms/full-population-testing/fix|🔧 Fix: The Integration Fetches Evidence for a Sample]]
