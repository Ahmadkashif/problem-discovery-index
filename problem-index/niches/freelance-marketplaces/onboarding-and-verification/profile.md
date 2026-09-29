# Onboarding & Verification

**Parent Industry:** [[industries/freelance-marketplaces|Freelance Marketplaces]]
**Category:** Highly Automatable
**Contested on:** Whether a new freelancer's stated capability can be established well enough to give them a first contract, without a verification process that turns away the people the marketplace needs.

## Profile
**Market Size:** ~$560M — 4% of platform-intermediated gross services volume
**Share of Parent Industry:** ~4%
**Digital Adoption:** Moderate — identity verification is automated; skill verification is a quiz or nothing
**Target Buyer:** Platform trust & safety and supply growth teams
**Automation Potential:** Very high for identity; genuinely difficult for capability

## What Makes This a Distinct Niche

Every marketplace faces the same opening problem: a person arrives with a profile claiming skills, and nothing in the system knows whether the claim is true. The ranking runs on outcome history that this person does not have. Clients hire on reputation that does not exist. The platform's answer is to let them bid and let the market sort it out, which means the first contract is allocated essentially at random among the unproven — and the cost of the sorting is borne by whichever client draws badly.

The two halves of the problem behave completely differently. Identity verification — is this a real, unique person who is who they say — is a solved commodity, and the vendor market for it is mature. Capability verification — can this person actually do the work they claim — is genuinely hard, badly served, and the thing the marketplace most needs.

The niche is distinct because it sits before every other mechanism in the industry: a freelancer with no history is invisible to the ranking, unrateable by the reputation system, and unpredictable to the bid model. Everything else compounds from whatever happens here.

## Current Tools & Gaps

Identity verification is bought — Persona, Onfido, Jumio, Veriff — and works. Document checks, liveness, duplicate detection and sanctions screening are automated and reliable enough that it is not where the difficulty lies.

Skill verification is where platforms have tried and mostly retreated. Multiple-choice tests were widely deployed and widely gamed, and several platforms deprecated them. Portfolio review is manual and does not scale. Certification partnerships cover a narrow slice of skills. What remains is self-declared skill tags plus whatever a client infers from a profile, which is why first contracts are a lottery and why the whole supply side has a cold-start problem that never fully resolves for people who do not get lucky early.

## Problems
- [[niches/freelance-marketplaces/onboarding-and-verification/build|🔨 Build: Capability Evidence for Freelancers Without History]]
- [[niches/freelance-marketplaces/onboarding-and-verification/buy|🛒 Buy: Identity Verification Adapted to a Population That Cannot Be Turned Away]]
- [[niches/freelance-marketplaces/onboarding-and-verification/fix|🔧 Fix: The First Contract Is a Lottery]]
