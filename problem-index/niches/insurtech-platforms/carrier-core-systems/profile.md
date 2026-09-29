# Carrier Core Systems

**Parent Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Category:** High Market Share
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor is fighting to let a carrier change what it sells and how it handles claims without a multi-year programme — but policy administration and claims are different contests with different buyers. Decomposed into contested sub-niches below.

## Profile
**Market Size:** ~$6.1B US carrier core systems — policy, billing and claims
**Share of Parent Industry:** ~38% of insurtech revenue
**Digital Adoption:** High investment and slow change — implementations run for years
**Target Buyer:** CIOs, transformation leads and the operations organisations that live with the result
**Automation Potential:** High in specific places and constrained by the surrounding programme culture

## What Makes This a Distinct Niche
Core systems are where the industry's money and its inertia both sit. Guidewire and Duck Creek run policy, billing and claims for a large share of US carriers, with Socotra, EIS and others competing on configurability and speed. Implementations are multi-year programmes with costs measured in tens of millions, and the recurring complaint is identical across carriers: the system was bought to make change faster and change is still slow. What the category label conceals is that "change" means two different things to two different organisations inside the same carrier. To the product and underwriting organisation it means getting a new product, a rate change or a form revision into production across the states it is filed in. To the claims organisation it means handling a claim better — reserving it correctly, routing it to the right adjuster, and closing it without leakage. Those are different problems, and the decomposition below treats them as such.

## Current Tools & Gaps
The incumbents are deeply embedded with extensive configuration capability and large implementation ecosystems; the newer platforms compete on time-to-market and cloud delivery. The gap that spans both halves is analytical rather than functional: these systems administer transactions and were never designed to answer questions about them. The chain from submission to decline reason to quote to bind to loss experience exists inside them and is not queryable without a data warehouse programme of its own. Testing and release confidence is the other shared gap — a configuration change's downstream effects on billing, reporting and reinsurance are established by manual regression testing, which is why change is slow regardless of how configurable the system is.

## Problems
- [[niches/insurtech-platforms/carrier-core-systems/build|🔨 Build: The Submission-to-Loss Chain as a Queryable Asset]]
- [[niches/insurtech-platforms/carrier-core-systems/buy|🛒 Buy: Software Release Engineering Practice for Configuration Change]]
- [[niches/insurtech-platforms/carrier-core-systems/fix|🔧 Fix: The Data Conversion Nobody Validates Clinically]]
