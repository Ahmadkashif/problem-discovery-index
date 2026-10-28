# A Confidential-Billing Router for Every Visit

**Niche:** [[niches/community-health-centers/title-x-family-planning-centers/profile|Title X & Independent Family Planning Centres]]
**Industry:** [[industries/community-health-centers|Community Health Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Family planning centres write off insured visits rather than risk an explanation of benefits reaching a parent or partner, because no system decides per visit whether a confidential claim is possible under the payer's and the state's rules.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #compliance #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to replace unstable grant dollars with insurer payments without breaking Title X confidentiality, and whoever bills the largest share of confidential visits to an insurer takes the account.

## The Problem
A 17-year-old on her parent's plan, or a woman on her husband's employer plan, asks for confidential care. Staff either bill and risk disclosure, or charge the sliding fee and lose the insurer payment. Most choose the second.

## Why Nobody Has Built This
The rules sit in three places: Title X confidentiality requirements, state laws on confidential communications and minor consent, and each payer's EOB and portal behaviour. No billing vendor maps all three, and the market is small.

## What to Build
A per-visit router that takes the patient's confidentiality request, the policyholder relationship, the state and the payer. It decides whether to bill normally, bill with a confidential-communications request, bill a payer that suppresses EOBs for sensitive services, or use the sliding fee. It logs the reason, and outcomes (paid, disclosed, complaint) retrain the payer rules.

## Target Customer
Independent family planning providers and Title X grantees with 5+ sites in states with confidential-EOB laws.

## Impact If Built
If 15% of a centre's 30,000 visits a year are confidential insured visits (estimate) and half could be billed safely at ~$100 each, that is ~$225,000 a year of recovered revenue (estimate).
