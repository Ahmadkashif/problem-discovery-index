# Conduct Monitoring

**Parent Industry:** [[industries/embedded-finance-platforms|Embedded Finance Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in this niche is fighting to infer how a programme treats its customers from the API calls it makes — and whoever detects a problem before the bank's examiner does defines what oversight from this layer can mean.

## Profile
**Market Size:** ~$1.1B US
**Share of Parent Industry:** ~14% of category revenue
**Digital Adoption:** Low — bank rules applied to programmes
**Target Buyer:** Platform risk and data leadership
**Automation Potential:** Very High — an inference problem with a comparison set

## What Makes This a Distinct Niche
This contest is detection. The platform sees account creations, transfers, card authorisations, fee postings, reversals and closures, per programme, at scale. From that it must infer whether customers are being treated fairly — whether fees are being applied in ways the disclosures would not support, whether onboarding is failing disproportionately for some populations, whether accounts are being closed in patterns that suggest a problem, whether a product's economics depend on customer confusion. It is an inference problem with a natural comparison set across programmes, and it has nothing in common with producing evidence for a bank partner.

## Current Tools & Gaps
Transaction monitoring rules inherited from bank retail contexts, programme-level thresholds, and incident-driven investigation. The gaps: alerts calibrated for one product applied to all; conduct signals not modelled at all; the cross-programme comparison unused; onboarding and closure patterns unexamined; and detection that happens when something has already gone wrong.

## Problems
- [[niches/embedded-finance-platforms/conduct-monitoring/build|🔨 Build: Inferring Conduct From API Calls]]
- [[niches/embedded-finance-platforms/conduct-monitoring/buy|🛒 Buy: Conduct Risk Practice]]
- [[niches/embedded-finance-platforms/conduct-monitoring/fix|🔧 Fix: One Calibration for Every Product]]
