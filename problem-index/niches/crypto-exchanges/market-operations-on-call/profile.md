# Market Operations On Call

**Parent Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Category:** 🟣 Underserved Audience
**Contested on:** Every serious competitor in this niche is fighting to page a human only when the market's behaviour is actually a system fault — and whoever separates a violent but ordinary market from a broken exchange makes a permanently staffed function survivable.

## Profile
**Market Size:** ~$1.2B US
**Share of Parent Industry:** ~8% of category revenue
**Digital Adoption:** Medium — strong engineering, naive alerting
**Target Buyer:** Exchange engineering leadership
**Automation Potential:** High — modelling market regimes into alerting

## What Makes This a Distinct Niche
Crypto markets do not close. Someone is always responsible for liquidity, matching, custody operations, deposits and withdrawals, and incidents. The alerting that pages them was built on thresholds that cannot distinguish a thirty percent move — which is a Tuesday — from a pricing feed that has stalled, and cannot distinguish a withdrawal queue backing up because of a network event from one backing up because of a bug. The person on the other end of the page is the audience nobody has designed for.

## Current Tools & Gaps
Standard observability stacks, threshold alerts, runbooks, and a rotation. The gaps: alerting that does not model market regime; no distinction between market conditions and system faults; volatility events and system events indistinguishable; no rota design for a market with no natural quiet period; and burnout treated as attrition rather than as a design outcome.

## Problems
- [[niches/crypto-exchanges/market-operations-on-call/build|🔨 Build: Alerting That Knows the Market]]
- [[niches/crypto-exchanges/market-operations-on-call/buy|🛒 Buy: Exchange Operations From Traditional Markets]]
- [[niches/crypto-exchanges/market-operations-on-call/fix|🔧 Fix: Paged by a Bull Run]]
