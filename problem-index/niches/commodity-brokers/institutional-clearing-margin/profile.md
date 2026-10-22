# Institutional Clearing & Margin Financing

**Parent Industry:** [[industries/commodity-brokers|Commodity Brokers]]
**Category:** High Market Share
**Contested on:** Every serious competitor in this niche is fighting to give a fund or commercial client the most margin capacity per dollar of the FCM's own capital, through cross-margin offsets, eligible collateral and intraday limits set on the client's real risk, and whoever carries the largest client book per dollar of capital without cutting clients off in a margin spike takes the account.

## Profile
**Market Size:** ~$1.5B a year in clearing technology, margin analytics, collateral and risk services spend at FCMs serving institutional clients (estimate)
**Share of Parent Industry:** ~45% of the industry's technology and services spend (estimate); the CFTC's August 2026 table puts ~66% of segregated customer funds at seven bank FCMs
**Digital Adoption:** High — clearing, margin and collateral run on industrial platforms, though client-level capital allocation decisions are made in committees and spreadsheets
**Target Buyer:** Head of Futures Clearing / Chief Risk Officer of the FCM
**Automation Potential:** High for margin and collateral optimisation, medium for client credit limits

## What Makes This a Distinct Niche
Institutional clearing serves CTAs, hedge funds, asset managers, proprietary trading firms and large commercials, and it is where the money sits: JP Morgan, Goldman Sachs, BofA, Morgan Stanley, SG, Citi and Barclays together held about $248B of the $374B segregation requirement in August 2026. The FCM's own capital requirement rises with customer risk maintenance margin (8% of it), so every client consumes balance sheet. The FCM chooses which clients to carry and on what terms, and the client chooses the FCM that lets it trade most for least. Margin efficiency, cross-margining between products and clearing houses, collateral eligibility (now including tokenized collateral under CFTC Letter 25-39) and intraday limits are the levers.

## Current Tools & Gaps
Back offices on FIS and ION, margin replication of CME SPAN and SPAN 2 and ICE methodologies, collateral optimisation from treasury vendors, and in-house client profitability models. The gaps are three. Capital consumed per client is computed after the fact rather than priced into terms. Intraday limits are set by rule of thumb. And the link between a client's margin, its capital charge and its revenue is rarely visible in one place when the clearing committee meets.

## Problems
- [[niches/commodity-brokers/institutional-clearing-margin/build|🔨 Build: Capital Cost per Client Priced Before the Account Opens]]
- [[niches/commodity-brokers/institutional-clearing-margin/buy|🛒 Buy: Bank Balance-Sheet Allocation Tools Adapted to FCM Capital Rules]]
- [[niches/commodity-brokers/institutional-clearing-margin/fix|🔧 Fix: Intraday Limits Set Once and Never Revisited]]
