# Plan Loss Ratio Decomposed by Cohort and Decision

**Niche:** [[niches/professional-employer-organizations/master-health-plan-pricing/profile|Master Health Plan Pricing & Underwriting]]
**Industry:** [[industries/professional-employer-organizations|Professional Employer Organizations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When a PEO's master plan runs ten points over target, nobody can say how much came from groups admitted this year, how much from renewals priced too low, and how much from three cancer claims.
**Tags:** #bayesian-inference #causal-inference #monte-carlo-methods #descriptive-statistics #evaluation-metrics #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor in this niche is fighting to keep a PEO's master health plan at its target loss ratio while still undercutting what small employers would pay on their own. But that is two contests with different winners: selecting and pricing prospects from a census and a few morbidity flags before a broker's quote deadline, which new-business underwriters and scoring vendors win, and setting each in-force client's renewal so low-claim groups stay and the plan does not spiral, which renewal actuaries and account teams win. Decomposed into contested sub-niches below.

## The Problem
A PEO's plan result is reported as one number: claims over premium for the plan, perhaps by region. Behind it sit thousands of small clients admitted in different years by different underwriters at different prices, renewed at different rates, some leaving and some staying. When the number goes wrong, as it did for Insperity in 2025, management debates causes without evidence. Sales blames underwriting, underwriting blames trend, and actuaries blame the large claims.

## Why Nobody Has Built This
Claims data in fully insured plans arrives from the carrier at plan level or in standard reports, not keyed to the PEO's own quote and renewal records. The two decisions live in different teams' systems. And small groups' results are so noisy that a naive cohort table misleads more than it informs.

## What to Build
A plan attribution model. Each client is tagged with its admission cohort, underwriter, broker, price relative to manual and every renewal action. The plan's deviation from expected is then decomposed into selection (new-business cohorts running above or below their priced loss ratio), renewal pricing (rate actions versus credible client experience), mix and retention (which clients left), trend, and large-claim randomness, with simulation bands showing what chance alone could produce.

## Target Customer
Chief underwriting officers, chief actuaries and CFOs at PEOs with master plans covering 20,000+ members, and the boards asking them why the plan missed.

## Impact If Built
The PEO acts on the cause rather than raising every client's rate. A deviation traced to one year's new business, one channel or one renewal policy can be fixed in the next quote season instead of after two more bad years.
