# Feasibility — Section 301 / Section 232 Tariff Exclusion Monitoring and Application

**Industry:** [[customs-brokers|Customs Brokers]]
**Problem:** [[problems/customs-brokers/low-impact-2|Section 301 / Section 232 Tariff Exclusion Monitoring and Application]]
**Problem type:** Low Impact

**Problem summary:** Generic trade compliance databases list tariff exclusions, but don't proactively match a broker's import portfolio against newly-published exclusions, calculate the retroactive duty savings, and draft the exclusion application or refund claim for the broker's clients.

## Solution Approach
Monitor Federal Register/CBP exclusion publications, normalize them to HTS lines, and match them against each client's import portfolio to flag eligibility and prepare draft applications/refund claims. Keep brokers in the loop with clear audit trails and savings estimates.

## Open Source Data
Federal Register notices, Section 301/232 exclusion lists, and the HTS schedule are public; matching and ROI calculations require proprietary entry data and supplier/part mappings.

## Worth Solving?
Medium — worthwhile as a customization/efficiency lever once a clear sponsor and data owner are identified.
