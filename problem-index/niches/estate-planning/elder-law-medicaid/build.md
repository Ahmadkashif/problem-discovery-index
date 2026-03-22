# Medicaid Eligibility & Spend-Down Strategy Modeler

**Niche:** [[niches/estate-planning/elder-law-medicaid/profile|Elder Law & Medicaid Planning]]
**Industry:** [[industries/estate-planning|Estate Planning]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Elder law attorneys input a client's assets and the system models multiple pathways to Medicaid eligibility — comparing irrevocable trusts, Medicaid-compliant annuities, caregiver agreements, and direct spend-down — with timeline and cost projections for each strategy.
**Tags:** #gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #tacit-knowledge-ml #compliance #revenue-impact

## The Problem
When a family walks in with an 82-year-old parent who needs nursing home care and has $400K in countable assets, the elder law attorney must determine: How long until Medicaid eligibility under each possible strategy? What is the total cost of care during the spend-down period? Which assets are countable vs. exempt under this state's rules? Are there prior transfers within the 5-year look-back that create penalty periods? What is the optimal combination of strategies (e.g., purchase a Medicaid-compliant annuity for $200K, establish a caregiver agreement for $50K, spend down $150K on exempt home modifications)? Experienced elder law attorneys develop deep intuition for which strategy combinations work best for specific client profiles — a form of tacit knowledge that takes years of practice and familiarity with local Medicaid agency interpretations to develop. New attorneys in this field make costly mistakes because they lack this pattern recognition.

## Why Nobody Has Built This
Medicaid rules are state-administered with 50+ different rule sets. Each state defines countable assets differently (some count IRAs, some don't; home equity caps range from $688K to $1,033K in 2024). Penalty period divisors (the daily cost of care used to calculate transfer penalties) vary by state and change annually. Community spouse resource allowances differ. Income rules use different methodologies (income-cap states vs. medically needy states). Building a comprehensive rule engine requires encoding and maintaining 50+ state rule sets that change annually — a maintenance burden that deters commercial software development for a relatively small market of elder law specialists.

## What to Build
A state-specific Medicaid planning platform where the attorney inputs: client's state, age, marital status, asset inventory (type, value, ownership), income sources, existing transfers within the look-back period, and current care needs. The system applies that state's Medicaid rules and models: (1) direct spend-down timeline and cost, (2) irrevocable trust with 5-year wait, (3) Medicaid-compliant annuity conversion, (4) caregiver agreement with family member, (5) combination strategies. Output shows: months to eligibility, total out-of-pocket cost during spend-down, assets preserved for the community spouse, and penalty exposure from prior transfers. An ML layer trained on case outcomes from participating firms learns which strategies experienced attorneys select for similar profiles, flagging the tacit knowledge patterns that distinguish veteran elder law attorneys from generalists.

## Target Customer
Elder law attorneys handling 5-15 Medicaid planning cases per month who currently spend 2-4 hours per case on manual eligibility calculations and strategy comparisons using state Medicaid manuals and custom spreadsheets.

## Impact If Built
Reduces per-case analysis time from 2-4 hours to 20-30 minutes. Prevents strategy selection errors that can cost families $50K-$200K in unnecessary spend-down. Enables general estate planning attorneys to offer Medicaid planning services with confidence, expanding the addressable market.
