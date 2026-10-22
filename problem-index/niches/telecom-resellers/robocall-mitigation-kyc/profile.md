# Robocall Mitigation, KYC & Traceback Response

**Parent Industry:** [[industries/telecom-resellers|Telecom Resellers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche (STIR/SHAKEN signing vendors, call-analytics firms, customer-vetting tools and compliance consultants) is fighting to give a provider records that show the FCC and downstream carriers no illegal traffic originates on or passes through its network, and whoever catches the bad customer before the first traceback takes the account.

## Profile
**Market Size:** ~$400M a year in robocall compliance tooling, signing, analytics, consultants and staff time at resellers, VoIP and wholesale providers (estimate)
**Share of Parent Industry:** ~0.7% of a ~$60B resale economy (estimate)
**Digital Adoption:** Medium — call signing and analytics are automated; customer vetting, traceback responses and mitigation plans are documents and email
**Target Buyer:** Compliance Officer or Head of Network Abuse at a wholesale, SIP-trunk or CPaaS provider
**Automation Potential:** High for dossiers, traceback assembly and filing upkeep; human judgement for terminations

## What Makes This a Distinct Niche
Every voice provider, intermediate provider and gateway provider must certify its robocall mitigation in the FCC's database. The new rules effective February 5, 2026 add annual recertification by March 1, updates within 10 business days of any change, and fines of $10,000 per false filing and $1,000 per missed update. Every provider must answer traceback requests within 24 hours, and the Industry Traceback Group ran 3,606 of them in 2024. Calls must be signed with the provider's own SPC token, because the third-party authentication shortcut ended in 2025. Removal is fatal and frequent: more than 1,200 providers were removed in August 2025 and 14 more in September 2026. Most of the work is repeatable evidence assembly, and that is what makes the niche automatable.

## Current Tools & Gaps
STIR/SHAKEN signing services (TransNexus and others), call-analytics labelling, CDR search in the softswitch, onboarding forms, and consultant-drafted mitigation plans. The gaps: customer vetting recorded as a checklist rather than evidence; traceback responses assembled by hand from logs; and mitigation plans that describe the company as it was when the consultant wrote them.

## Problems
- [[niches/telecom-resellers/robocall-mitigation-kyc/build|🔨 Build: The 24-Hour Traceback Workbench]]
- [[niches/telecom-resellers/robocall-mitigation-kyc/buy|🛒 Buy: Bank AML Monitoring Adapted to Voice Traffic]]
- [[niches/telecom-resellers/robocall-mitigation-kyc/fix|🔧 Fix: The Mitigation Plan That Describes a Different Company]]
