# Teller Cross-Sell Pressure During Member Transactions

**Industry:** [[credit-unions|Credit Unions]]
**Type:** Worker Life Changing
**One-liner:** Tellers get their transaction window back — instead of awkwardly pitching products during a 90-second deposit, they receive a single contextually relevant suggestion only when the member's account data indicates genuine fit, transforming cross-sell from a compliance checkbox into a natural conversation.
**Tags:** #gradient-boosting #recommendation #tabular-ml #worker-facing

## The Problem

Credit union tellers are evaluated on cross-sell metrics — the number of product referrals generated per member interaction. Branch managers track referral counts weekly, and tellers who consistently fall below targets face coaching conversations and performance plan escalation. The problem is that tellers process 80-120 transactions per shift with an average interaction time of 60-90 seconds, during which they must complete the transaction accurately, verify member identity, and — in the remaining seconds — identify and pitch a relevant product. Most tellers resort to scripted prompts ("Have you considered our auto loan rates?") delivered without context, which members find annoying and tellers find demoralizing. The referral conversion rate on untargeted teller pitches is 1-3%, meaning 97-99% of the uncomfortable interactions produce nothing except friction.

## Why It Matters to the Worker

Tellers describe cross-sell pressure as the single most stressful aspect of their job. The dissonance between "serve the member" and "sell to the member" creates daily emotional friction. New tellers, particularly those who chose CU work over bank work specifically because of the member-service mission, burn out on the sales pressure within 12-18 months. Annual teller turnover at CUs averages 25-30%, and exit interviews consistently cite sales expectations as a top-three departure reason. The teller who genuinely wants to help members manage their finances is forced into a transactional sales role that undermines the relationship the CU's model depends on.

## What a Solution Looks Like

A recommendation model that analyzes each member's account data in real time as they approach the teller window — current product holdings, recent transaction patterns, life event signals (address change, payroll increase, new joint account holder) — and generates either zero or one contextually relevant suggestion displayed on the teller's screen. The suggestion includes a one-sentence rationale ("Member's auto loan at another institution has a 7.9% rate; CU auto refi rate is 5.4%") so the teller can make a genuine, informed recommendation rather than a scripted pitch. When no relevant suggestion exists, the screen shows nothing — the teller simply processes the transaction without sales pressure. The model learns from referral outcomes: which suggestions lead to applications, which are dismissed, which member segments respond to which product recommendations.

## Impact If Solved

Referral conversion rate increases from 1-3% to 8-15% because suggestions are contextually relevant. Total referral volume decreases (fewer pitches per shift) but qualified referral volume increases. Tellers report reduced stress because the suggestion is genuinely helpful when it appears and absent when it isn't. Teller retention improves — even a 5-point reduction in annual turnover (from 28% to 23%) saves $3,000-$5,000 per avoided replacement in hiring and training costs.
