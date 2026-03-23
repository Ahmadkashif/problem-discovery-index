# Benefits Cliff Visibility

**Niche:** [[niches/nonprofits-social-services/benefits-eligibility-screeners/profile|Benefits Eligibility Screeners]]
**Industry:** [[industries/nonprofits-social-services|Nonprofits Social Services]]
**Type:** Fix (Pain Point)
**One-liner:** Benefits navigators cannot show clients how a $2/hour raise might cost them $6,000/year in lost benefits because no screening tool models the effective marginal tax rate across all active benefit programs.
**Tags:** #regression #tabular-ml #automation #revenue-impact #worker-facing

## The Problem
Benefits cliffs occur when a small increase in income causes a disproportionate loss of benefits — a family earning $35,000 might receive $12,000 in benefits (SNAP, Medicaid, childcare subsidies, LIHEAP), but earning $38,000 could reduce benefits by $8,000, making the raise a net loss. Navigators intuitively know these cliffs exist but cannot quantify them for each client's specific benefit portfolio. Clients make employment decisions (taking a raise, increasing hours, switching jobs) without understanding the financial consequences, and navigators lack the tools to advise them.

## Why It's Still Broken
Modeling benefits cliffs requires calculating the phase-out rates of 5-10 active benefits simultaneously, each with different income thresholds, phase-out slopes, and categorical boundaries. The interaction effects are non-linear — losing Medicaid doesn't just remove health coverage, it may also remove categorical eligibility for other programs. No screening tool models this because it requires maintaining benefit calculation formulas (not just eligibility thresholds) for every program in every state, which is an order of magnitude more complex than eligibility screening alone.

## What a Fix Looks Like
A benefits cliff calculator that takes a client's current income, household composition, and active benefits, then models the net financial impact of income changes in $1,000 increments — showing exactly where the cliffs are. The output is a simple chart: "At $35K you keep $47K (income + benefits). At $38K you keep $42K. You need to reach $44K before you're better off." Navigators use this to counsel clients on employment decisions, and clients can see the math themselves.

## Who Feels the Pain
Benefits navigators who watch clients take raises or overtime only to lose benefits that cost them more than they gained — and feel helpless because they couldn't warn the client with specific numbers.

## Impact If Fixed
Enables informed employment decisions for 2M+ households near benefits cliffs, prevents the estimated $3,000-$8,000 annual net income loss per family caused by uninformed cliff crossings, and gives navigators a concrete tool to support economic mobility counseling.
