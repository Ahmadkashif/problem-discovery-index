# Order-to-Activation & Zero-Touch Provisioning

**Parent Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to turn an online order into working service without a human touch — serviceability answer, port assignment, ONT or modem activation and install slot — and whoever closes the most orders without a call or a second visit takes the account.

## Profile
**Market Size:** ~$2.5B a year in install labour avoidable through self-install, provisioning and order-management software, and order-handling staff (estimate)
**Share of Parent Industry:** ~0.8% of industry receipts (estimate)
**Digital Adoption:** Medium-High at large operators, Low-Medium in the long tail where orders still pass by email between sales, engineering and the install scheduler
**Target Buyer:** VP of Customer Operations or Director of Provisioning
**Automation Potential:** Very high for the order flow; medium for self-install success

## What Makes This a Distinct Niche
Between "check my address" and "it works" sit a serviceability lookup, a credit check, a port or tap assignment, equipment shipping or a truck, activation of the ONT or modem, and the first-week experience. Each manual step costs money and loses some customers. The defining automation questions are whether the address is really serviceable today and whether this order can be self-installed or needs a technician. The fibre record problem upstream is the separate [[niches/wired-broadband-providers/fiber-network-records/profile|Fibre Network Records & As-Built Inventory]] niche.

## Current Tools & Gaps
BSS and OSS suites (CSG, Amdocs at scale; Sonar, gaiia, Powercode in the long tail), e-commerce checkouts, Calix and other vendors' activation platforms, field service scheduling. Gaps: serviceability answers drawn from records that don't match the field; self-install offered by rule rather than by predicted success; and failed activations discovered when the customer calls.

## Problems
- [[niches/wired-broadband-providers/order-to-activation/build|🔨 Build: Self-Install Success Prediction]]
- [[niches/wired-broadband-providers/order-to-activation/buy|🛒 Buy: E-Commerce Order Orchestration Adapted to Serviceability]]
- [[niches/wired-broadband-providers/order-to-activation/fix|🔧 Fix: The Address That Says Serviceable and Isn't]]
