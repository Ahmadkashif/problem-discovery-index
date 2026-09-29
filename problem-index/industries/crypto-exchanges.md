# Crypto Exchanges

## Profile
**Category:** Fintech
**Market Size:** ~$15B US revenue across centralised trading venues, custody and staking, concentrated in a small number of licensed operators
**Tech Maturity:** World-class matching engines attached to compliance processes that run on vendor scores and manual review — Coinbase, Kraken, Gemini, Crypto.com and Binance.US operate exchanges capable of enormous throughput, and make their most consequential customer decisions (freeze this deposit, close this account, file this report) from a third-party address risk score and an analyst's judgement.
**Workforce:** Exchange and matching engineers, blockchain and protocol engineers, transaction monitoring and BSA analysts, listings and token due diligence teams, market operations, support, legal and licensing staff

## Key Pain Themes
The defining operational problem is deposit screening. Funds arrive from an on-chain address; a blockchain analytics vendor assigns that address and its transaction history a risk characterisation; above a threshold the exchange holds the funds and investigates. The customer, who may have received the coins from a service several hops removed from anything illicit, discovers that their deposit is frozen and receives very little explanation.

Ground truth almost never returns. Occasionally law enforcement confirms a case. Occasionally the customer produces a provenance that satisfies an analyst. In the overwhelming majority of instances the exchange never learns whether the funds were actually criminal proceeds, which means the screening threshold has been set and adjusted for years without anyone measuring its precision. That is the same missing join that runs through the rest of financial services, with an additional difficulty: the taint propagates through a public ledger by heuristics that are themselves contested.

Around it sit token listing due diligence, tax reporting and cost basis across transfers, a 24/7 market operations function, and a support queue dominated by locked accounts and missing deposits.

## Current Tech Landscape
Chainalysis, TRM Labs and Elliptic supply address attribution and risk scoring; their clustering heuristics and sanctions mappings are effectively the industry standard and are proprietary. Transaction monitoring on the fiat side runs on conventional tooling. Identity is handled by the usual vendors plus chain-specific checks. Tax reporting is moving under the 1099-DA regime, which requires per-transaction basis reporting that most exchanges cannot compute for assets transferred in from elsewhere. Custody is split between internal systems and specialists. Market surveillance for manipulation is thinner than in equities, largely because the regulatory requirement has been thinner.

## Problems
- [[problems/crypto-exchanges/high-impact|🔴 High Impact: Deposit Screening Without Ground Truth]]
- [[problems/crypto-exchanges/low-impact-1|🟡 Low Impact: Token Listing Due Diligence]]
- [[problems/crypto-exchanges/low-impact-2|🟡 Low Impact: Cost Basis and Tax Reporting]]
- [[problems/crypto-exchanges/worker-life-1|🟢 Worker Life: The Transaction Monitoring Analyst Tracing Hops]]
- [[problems/crypto-exchanges/worker-life-2|🟢 Worker Life: Market Operations at Three in the Morning]]
- [[problems/crypto-exchanges/ml-opportunity|🧠 ML Opportunities]]
- [[problems/crypto-exchanges/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
An exchange holds something unusual: a public, complete, permanent transaction ledger on one side, and verified real-world identity on the other, joined at the deposit and withdrawal address. That junction is the most informative position in the entire crypto data landscape and is where the analytics vendors' attribution ultimately comes from. The exchanges generate the labels and buy them back as a scored feed, with the vendor accumulating the cross-exchange picture and each exchange retaining only its own slice. The interesting and unexploited asset is the exchange's own history of screening decisions and their few resolved outcomes — a small, expensive, genuinely labelled dataset about the thing the whole industry claims to measure and nobody evaluates.
