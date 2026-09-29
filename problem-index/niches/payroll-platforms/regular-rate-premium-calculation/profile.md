# Regular Rate & Premium Calculation

**Parent Industry:** [[industries/payroll-platforms|Payroll Platforms]]
**Category:** Contested Sub-Niche
**Contested on:** Every serious competitor in wage calculation is fighting to compute the regular rate and every premium correctly for every jurisdiction an employer operates in — and whoever can prove a configuration matches the law takes the account.

## Profile
**Market Size:** ~$3.4B US attributable to earnings rule configuration, overtime and premium calculation
**Share of Parent Industry:** ~11% of payroll revenue
**Digital Adoption:** High as software, low as verified correctness
**Target Buyer:** Payroll and compliance leaders at employers; earnings engine product teams at providers
**Automation Potential:** Very High — the rules are published and the configuration is checkable against them

## What Makes This a Distinct Niche
The regular rate of pay is a legal construct rather than an hourly wage: it includes shift differentials, non-discretionary bonuses, certain incentive payments and on-call compensation, and excludes others, and it is the base on which overtime must be computed. Getting it wrong understates every overtime payment. Around it sit the premiums that vary by jurisdiction — daily overtime, double time after a threshold, seventh consecutive day rules, meal and rest period premiums that are themselves wages in some states and must then enter the regular rate. Employers configure all of this into an earnings engine, usually once, frequently from a general understanding rather than from the specific jurisdictional rules, and the engine applies it forever. The failure is quiet, cumulative, affects every overtime hour, and is among the most commonly litigated wage and hour issues in the country.

## Current Tools & Gaps
Every payroll platform supports earnings codes with configurable inclusion in the regular rate and jurisdiction-specific overtime rules; the larger providers ship jurisdictional defaults. The gaps: defaults are a starting point and employers modify them, after which nothing checks the modification; the interaction between multiple premiums — a differential on an overtime hour on a seventh consecutive day in a state with daily overtime — is where engines and configurations most often diverge and is tested by nobody; meal and rest premium treatment differs by state in ways that catch national employers routinely; and there is no capability anywhere to demonstrate that an employer's configuration is correct, which is precisely what an employer would want to establish before a claim rather than during one.

## Problems
- [[niches/payroll-platforms/regular-rate-premium-calculation/build|🔨 Build: A Provable Configuration]]
- [[niches/payroll-platforms/regular-rate-premium-calculation/buy|🛒 Buy: Property-Based Testing for Earnings Engines]]
- [[niches/payroll-platforms/regular-rate-premium-calculation/fix|🔧 Fix: Premium Interactions Nobody Tests]]
