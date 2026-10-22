# The Hardship Agent With Ninety Seconds to Choose a Plan

**Industry:** [[credit-card-issuers|Credit Card Issuers]]
**Type:** Worker Life Changing
**One-liner:** An early-stage collections agent hears a cardholder's job loss, divorce or medical bill and has seconds to pick a hardship programme from a menu, with no way of knowing whether the choice will cure the account or just postpone the charge-off.
**Tags:** #gradient-boosting #survival-analysis #causal-inference #large-language-models #worker-facing #workflow-orchestration #revenue-impact

## The Problem
In-house collections at a card issuer works accounts from the first missed payment until charge-off at about 180 days. Agents make or take calls through a dialer, and a large share of the conversations are with people in real trouble: a lost job, a reduced shift, a hospital stay, a separation. The agent's screen shows the balance, days past due, payment history and a list of programmes the cardholder may be eligible for — a temporary APR reduction, a fixed payment plan with the card closed, a skip-a-payment, a re-age after three on-time payments, a settlement offer at later stages. Policy sets eligibility; the agent chooses.

The choice is made in about the time it takes to read the screen, and the agent rarely learns how it turned out. An account placed on a plan it cannot sustain breaks the plan two months later and charges off anyway, now with months of lost recovery; an account given a deeper concession than it needed costs the issuer interest it would have collected. Minimum-only payment behaviour rose to 15% of general-purpose and 20% of private-label cardholders in 2024 (CFPB), so the queue of stretched customers is not shrinking.

## Why It Matters to the Worker
The calls are heavy. Agents spend a shift hearing hard stories and are measured on promises to pay, right-party contacts and dollars collected — numbers that reward pushing a payment over finding the arrangement that will hold. Experienced agents develop a sense for which cardholders will keep a plan and which are buying time, and new agents do not have it; turnover in collections floors is high, so most calls are taken by the people with the least feel for them. Agents also carry the compliance exposure: issuer call caps of one to four a day per account (CFPB), state creditor-collection rules, and every word recorded for review.

## What a Solution Looks Like
At the moment the agent opens the account, a recommendation ranks the eligible programmes by their estimated chance of curing this account — trained on years of the issuer's own plan assignments and their outcomes, adjusted for which cardholders were offered what — with the two or three facts that drive it. During the call, a transcript assistant captures the hardship reason and expected duration in the cardholder's own words, fills the notes and checks the offer against policy. After the call, the agent sees, weeks later, whether the plans they set held.

## Impact If Solved
Agents spend the call on the conversation rather than on the menu, new agents make choices closer to those of veterans, and an issuer that cures even a few more accounts in every hundred placed on plans recovers balances that would otherwise charge off — while the agent finally gets feedback on the part of the job that matters most to the cardholder.
