# 42 CFR Part 2 Compliant Safety Communication

**Niche:** [[niches/non-emergency-medical-transport/behavioral-health-transport/profile|Behavioral Health Transport]]
**Industry:** [[industries/non-emergency-medical-transport|Non-Emergency Medical Transport]]
**Type:** Fix (Pain Point)
**One-liner:** Behavioral health facilities cannot share clinically relevant transport safety information with NEMT providers because 42 CFR Part 2 substance use confidentiality rules create a legal barrier that no technology currently navigates.
**Tags:** #compliance #data-integration #worker-facing

## The Problem
42 CFR Part 2 imposes stricter confidentiality protections on substance use disorder (SUD) treatment records than HIPAA applies to general health information. When a substance use treatment facility needs to communicate transport safety information to an NEMT provider ("patient is in early recovery from opioid use, do not transport past patient's former dealer's neighborhood"), the disclosure may violate Part 2 without explicit, narrowly-scoped patient consent. Facilities err on the side of sharing nothing, which means drivers arrive with no safety context. Alternatively, social workers share information verbally and informally, creating unauditable disclosure practices that put the facility at legal risk. The result: either the driver has no safety information (creating transport risk) or the facility shares information without proper consent (creating legal risk).

## Why It's Still Broken
42 CFR Part 2 was designed to protect patients from the stigma of substance use disorder, not to impede safe transport. But the regulation was written before digital health information exchange and NEMT coordination existed, and the consent framework (requiring written, specific, and time-limited patient authorization for each disclosure to each recipient) is impractical for routine transport coordination. The 2020 CARES Act Part 2 revisions aligned some protections with HIPAA but did not resolve the specific challenge of sharing safety-relevant information with non-healthcare transportation providers. No technology platform has built a Part 2-compliant consent and disclosure workflow for NEMT.

## What a Fix Looks Like
A compliant disclosure platform that: (1) captures patient consent specifically authorizing the sharing of transport-relevant safety information (not clinical records) with their NEMT provider, (2) translates clinical safety assessments into transport-actionable safety needs (avoiding clinical terminology and diagnosis disclosure), (3) scopes the disclosure to the minimum necessary information for safe transport (e.g., "patient may experience anxiety in enclosed spaces" rather than "patient has PTSD from a specific trauma"), (4) maintains an auditable consent and disclosure log for regulatory compliance, and (5) automatically expires disclosures per the consent terms. The platform gives facilities a legally defensible way to share what drivers need to know.

## Who Feels the Pain
Behavioral health facility social workers who spend 15-30 minutes per patient negotiating informal information sharing with NEMT providers, NEMT drivers who transport behavioral health patients with no safety context, and facility compliance officers who know that current verbal disclosure practices violate Part 2 but have no alternative.

## Impact If Fixed
Enables safe behavioral health transport with compliant information sharing, reduces transport safety incidents by 40-60% through informed driver preparation, and protects facilities from Part 2 violation liability (penalties up to $500 per violation per day). Opens the behavioral health NEMT segment to providers who currently avoid it due to information-sharing complexity.
