# Ancillary Services & Specialty

**Parent Industry:** [[industries/home-inspection|Home Inspection]]
**Category:** Low Digitized

## Profile
**Market Size:** $0.5-0.8B
**Share of Parent Industry:** ~12%
**Digital Adoption:** Low — ancillary testing (radon, mold, sewer scope, thermal imaging, WDI/termite) uses specialized equipment with proprietary software that doesn't integrate with the main inspection report. Results are delivered as separate PDFs or lab reports appended to the main report.
**Target Buyer:** Home inspector adding ancillary revenue streams to their standard inspection business
**Automation Potential:** Medium-High — upsell recommendation is a pattern matching task (property characteristics to likely ancillary needs), and test result interpretation for non-specialists is a structured classification problem

## What Makes This a Distinct Niche
Ancillary services are the highest-margin revenue stream for home inspectors. A standard inspection at $400-500 has a 30-40% margin. Adding radon testing ($150, 80% margin), sewer scope ($200-300, 60% margin), mold sampling ($200-300, 50% margin), thermal imaging ($100-200, 70% margin), or WDI/termite inspection ($75-125, 60% margin) can double the per-inspection revenue. The challenge: most inspectors don't know which ancillary services to offer on which properties, and the testing/interpretation for services outside their specialty (radon mitigation thresholds, mold species identification, sewer defect classification) is a knowledge gap that limits adoption. An inspector who adds radon testing without understanding radon geology in their market will over-test in low-risk areas (wasting the customer's money) and under-recommend in high-risk areas (missing the revenue and the safety concern).

## Current Tools & Gaps
Radon testing uses Sun Nuclear or Airthings monitors with companion apps. Sewer scopes use proprietary camera systems (RIDGID, Spartan) with separate recording software. Mold sampling requires third-party lab analysis (EMSL, ProLab). Thermal imaging uses FLIR or InfiRay cameras with separate imaging apps. None of these integrate with Spectora or HomeGauge — the inspector runs the test, receives results in a separate format, and manually attaches them to the main report. No tool recommends which ancillary services to offer based on the specific property's risk profile.

## Problems
- [[niches/home-inspection/ancillary-services-specialty/build|🔨 Build: Ancillary Service Upsell Recommendation Engine]]
- [[niches/home-inspection/ancillary-services-specialty/buy|🛒 Buy: Spectora Ancillary Test Integration]]
- [[niches/home-inspection/ancillary-services-specialty/fix|🔧 Fix: Non-Specialist Test Result Interpretation]]
