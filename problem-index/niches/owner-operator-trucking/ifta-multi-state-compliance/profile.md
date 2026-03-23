# IFTA & Multi-State Compliance

**Parent Industry:** [[industries/owner-operator-trucking|Owner-Operator Trucking]]
**Category:** Highly Automatable

## Profile
**Market Size:** $5-8B (compliance services)
**Share of Parent Industry:** ~3% (services revenue, but affects 100% of operators)
**Digital Adoption:** Low — Most operators track fuel purchases on paper receipts and hand them to an accountant quarterly; ELD mileage data exists but isn't connected to fuel records
**Target Buyer:** Any OO filing IFTA fuel taxes across 10+ states quarterly
**Automation Potential:** High — IFTA is a pure data problem: miles driven per state + fuel purchased per state = tax owed/refund per state. The data exists in ELDs and fuel card statements but isn't connected.

## What Makes This a Distinct Niche
Every owner-operator who crosses state lines must file IFTA (International Fuel Tax Agreement) quarterly, reporting miles driven and fuel purchased in each jurisdiction. This creates a per-state tax calculation that can result in either taxes owed (drove many miles, bought little fuel in that state) or a refund (bought fuel, drove few miles). The typical OO crosses 15-25 states per quarter, generating hundreds of fuel receipts that must be matched to state-by-state mileage. This process takes 8-20 hours per quarter when done manually, and errors trigger audits with penalties. Yet the data — GPS mileage by state from the ELD, and fuel purchases by location from the fuel card — already exists digitally and could be matched automatically.

## Current Tools & Gaps
ATBS (trucking accounting) handles IFTA filing but requires the operator to organize receipts and provide mileage data — reducing the filing work, not the data collection work. TruckingOffice offers basic IFTA tracking. ELD providers (Motive, Samsara) show miles per state but don't connect to fuel card data. Fuel card providers (EFS, Comdata) show purchase locations but don't connect to ELD mileage. The two datasets exist in separate systems with no bridge.

## Problems
- [[niches/owner-operator-trucking/ifta-multi-state-compliance/build|🔨 Build: Automated IFTA Filing from ELD + Fuel Card Integration]]
- [[niches/owner-operator-trucking/ifta-multi-state-compliance/buy|🛒 Buy: Receipt-Free Fuel Tax Documentation]]
- [[niches/owner-operator-trucking/ifta-multi-state-compliance/fix|🔧 Fix: Quarterly Filing Scramble and Audit Risk]]
