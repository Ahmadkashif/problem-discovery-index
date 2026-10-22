# Assets That Arrive Without Cost Basis

**Niche:** [[niches/trust-companies/trust-account-acceptance-onboarding/profile|Trust Account Acceptance & Onboarding]]
**Industry:** [[industries/trust-companies|Trust Companies]]
**Type:** Fix (Pain Point)
**One-liner:** Securities transferred in from a prior trustee or custodian often arrive without lot-level cost basis, and the gap surfaces at the first sale or the first tax return.
**Tags:** #large-language-models #data-integration #feature-engineering #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn a signed trust instrument and a transfer of assets into a correctly coded, KYC-cleared account in days, and whoever onboards fastest without an acceptance error takes the account.

## The Problem
Basis may be carried over, stepped up at a death, or split across lots, and prior trustees supply it unevenly, sometimes as statements rather than data. Accounts open with placeholder basis, and an officer later diversifies a position without knowing the tax cost.

## Why It's Still Broken
Nobody owns basis at transfer: operations moves the assets, tax needs the basis months later, and the prior trustee has no incentive to help.

## What a Fix Looks Like
Basis captured as part of acceptance: extract lots from whatever the prior holder supplies, flag positions with missing or implausible basis, apply date-of-death valuations where the instrument and facts call for them, and chase the gaps before the account is marked open.

## Who Feels the Pain
Investment officers deciding on diversification; tax preparers reconstructing basis at year-end; beneficiaries facing unexpected gains.

## Impact If Fixed
Every account opens with usable basis, investment decisions account for tax cost from day one, and year-end reconstruction disappears.
