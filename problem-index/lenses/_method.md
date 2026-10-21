# Three Lenses — Method

Every industry (257) and sub-niche (3,973) in the vault is scored on three lenses. Each lens
is the mean of 4–5 factors scored 1–5, rescaled to 0–100: `score = (mean − 1) / 4 × 100`.
The lenses are scored **independently**. AI-proof is not derived from clarity, so where
the two disagree is a finding.

Horizon for AI-proof: **5 years, to 2031**.

## What gets scored

- **Industry:** the core work of the industry's typical operator, as the industry profile
  describes it.
- **Sub-niche:** the work the sub-niche itself describes, which may differ from its parent:
  - A customer segment (e.g. church group charters): score the work of serving that segment.
  - A function (e.g. appointment and deposit management): score that function.
  - An insight pocket (a data vendor, publisher, regulator or association): score that
    organisation's work.

## Lens 1 — AI-proof (5 = most protected)

| Factor | 1 | 5 |
|---|---|---|
| `physical`: value is delivered by hands or bodies, on site | entirely on screens | entirely hands-on, unstructured places |
| `liability`: a licensed or accountable human must do it or sign it | no licence, no personal liability | licensed professional must act personally and carries the liability |
| `trust`: the buyer pays for a specific person or relationship | commodity, any provider will do | the relationship is the product |
| `judgment`: decisions are novel, ambiguous, adversarial or high-stakes, with slow feedback | routine, each case like the last | each case novel and consequential |
| `durability`: buyers will still pay a firm or person for this in 2031, rather than doing it themselves with AI or getting it from AI-native software | AI substitutes the product directly | demand unaffected or grows because of AI |

## Lens 2 — Value clarity (5 = clearest)

| Factor | 1 | 5 |
|---|---|---|
| `what`: the deliverable is well defined and success is measurable and agreed | "good" is a matter of taste | an exact, checkable deliverable |
| `how`: the method can be written down and experts agree on the steps | each expert does it differently, by feel | a codified procedure or rulebook |
| `repetition`: the same kind of task recurs with little variation | every job is one-off | thousands of near-identical cases |
| `feedback`: correctness can be checked quickly and objectively | outcome known years later, if ever | instant, objective pass or fail |

The working hypothesis behind this lens is that high clarity predicts replacement by AI
or automation. Scoring it apart from AI-proof lets the vault test that.

## Lens 3 — Digital nature (5 = most digital)

| Factor | 1 | 5 |
|---|---|---|
| `input`: what the work starts from | physical things, places or bodies | data, documents, code, media |
| `production`: where the value-adding work happens | by hand, in person | on a screen |
| `delivery`: what the customer receives | a physical result or in-person service | a digital output or online service |
| `buying`: how customers find, buy from and talk to providers | local, face to face, needs presence | fully remote; a provider abroad is normal |

## Anchors

These were scored by hand first and given to every scorer as calibration. The scores are
factor values in the order listed above.

| Item | AI-proof (phys, liab, trust, judg, dur) | Clarity (what, how, rep, fb) | Digital (in, prod, deliv, buy) |
|---|---|---|---|
| plumbing-contractors | 5, 4, 3, 3, 5 | 4, 3, 3, 4 | 1, 1, 1, 2 |
| funeral-homes | 4, 4, 5, 2, 5 | 3, 4, 4, 2 | 1, 1, 1, 2 |
| childcare-centers | 5, 5, 5, 3, 5 | 3, 3, 4, 2 | 1, 1, 1, 2 |
| tattoo-studios | 5, 2, 5, 3, 5 | 2, 2, 2, 2 | 1, 1, 1, 2 |
| crop-farming | 5, 2, 1, 3, 5 | 4, 3, 3, 1 | 1, 1, 1, 2 |
| private-equity-firms | 1, 3, 5, 5, 4 | 3, 2, 2, 1 | 4, 3, 3, 2 |
| personal-injury-law | 1, 5, 4, 4, 4 | 4, 3, 3, 2 | 4, 4, 3, 2 |
| penetration-testing-firms | 1, 3, 3, 4, 4 | 3, 3, 3, 3 | 5, 5, 5, 5 |
| software-dev-agencies | 1, 1, 3, 3, 2 | 3, 4, 3, 4 | 5, 5, 5, 5 |
| tax-prep-firms | 1, 3, 3, 2, 2 | 5, 5, 5, 4 | 4, 5, 5, 3 |
| medical-billing | 1, 2, 2, 2, 2 | 5, 4, 5, 4 | 5, 5, 5, 4 |
| seo-tooling-vendors | 1, 1, 2, 3, 1 | 3, 2, 3, 3 | 5, 5, 5, 5 |
| localization-services | 1, 1, 2, 2, 1 | 4, 4, 5, 3 | 5, 5, 5, 5 |
| data-labeling-services | 1, 1, 1, 2, 2 | 5, 5, 5, 4 | 5, 5, 5, 5 |
| tattoo-studios/appointment-deposit-mgmt (function) | 1, 1, 2, 1, 2 | 5, 5, 5, 5 | 4, 4, 4, 4 |
| charter-bus-operators/driver-risk-data-providers (insight pocket) | 1, 3, 2, 2, 4 | 4, 4, 5, 3 | 5, 5, 5, 5 |

## Checks

- `_state/verify.py` confirms every one of the 4,230 items has every factor, as an integer
  from 1 to 5.
- A blind re-score of a random sample, by a scorer that never saw the first scores,
  measures agreement per lens. The result is recorded in `_overview.md`.
