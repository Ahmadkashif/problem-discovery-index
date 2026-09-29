# Benefits, Leave & Local Entitlements

**Parent Industry:** [[industries/remote-work-infrastructure|Remote Work Infrastructure]]
**Category:** Low Digitized
**Contested on:** Whether a worker receives what their own country entitles them to, or what the client's global policy offers.

## Profile
**Market Size:** ~$880M — 11% of US remote work infrastructure spend
**Share of Parent Industry:** ~11%
**Digital Adoption:** Low — dozens of regimes maintained by reading and administered by email
**Target Buyer:** Platform compliance and benefits operations; clients; workers
**Automation Potential:** High — entitlement calculation and accrual are mechanical

## What Makes This a Distinct Niche

Statutory entitlements differ enormously by country — annual leave, sick pay, parental leave, notice, public holidays, mandatory health coverage, pension contributions, thirteenth-month payments — and they are not optional. An employer of record must provide at least the local statutory minimum regardless of what the client's global policy says.

The tension is structural. The client has a policy designed around their home market and wants consistency; the local law sets a floor that may be well above or oddly different from it; and the worker frequently knows neither. The platform sits between, obliged to the law and selling to the client.

The niche is distinct because entitlement is where local law is most detailed, most frequently updated and most immediately felt by the worker — and because the failure mode is quiet: a worker who receives less than their statutory minimum usually does not know.

## Current Tools & Gaps

Leave tracking in the platform with per-country configuration. Benefit packages assembled per jurisdiction, often through local brokers. Statutory minimums encoded in the payroll rules. Client-side policy layered on top. Local counsel for questions.

The gaps are accrual correctness, policy interaction and worker visibility. Accrual rules are intricate and jurisdiction-specific — carryover, expiry, proration, public holiday interaction, sickness during leave — and are frequently simplified into a generic model that is wrong at the edges. The interaction between the client's policy and the statutory floor is resolved case by case. And the worker is rarely told what they are actually entitled to under their own law, as distinct from what the policy offers.

## Problems
- [[niches/remote-work-infrastructure/benefits-and-entitlements/build|🔨 Build: Statutory Entitlement as a Computed Floor]]
- [[niches/remote-work-infrastructure/benefits-and-entitlements/buy|🛒 Buy: Leave and Benefits Administration Adapted to Sixty Statutory Regimes]]
- [[niches/remote-work-infrastructure/benefits-and-entitlements/fix|🔧 Fix: The Worker Does Not Know What They Are Entitled To]]
