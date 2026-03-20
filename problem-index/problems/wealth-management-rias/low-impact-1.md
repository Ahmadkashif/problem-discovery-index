# Client-Specific Portfolio Narrative Reports

**Industry:** [[wealth-management-rias|Wealth Management RIAs]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Portfolio reporting tools generate identical charts for every client — but a retiree drawing income needs a completely different explanation than a 35-year-old accumulating aggressively.
**Tags:** #large-language-models #transfer-learning #attention-mechanisms #transformers #entropy-cross-entropy-kl-divergence #automation

## The Problem
Every quarter, RIA operations staff or paraplanners generate portfolio reports through Orion, Black Diamond, or Tamarac. These reports contain accurate performance data, asset allocation breakdowns, and benchmark comparisons. But the narrative section — the part clients actually read — is either a generic market commentary applied to every client or a manually written paragraph the advisor dictates per client. For a 200-client book, personalized narratives take 40-60 hours per quarter.

## What Already Exists
Orion and Black Diamond both offer templated commentary features. Some firms use third-party market commentary services (e.g., Clearnomics, Seven Group). These produce professional, compliant market overviews. However, they cannot explain why *this specific client's* portfolio behaved the way it did relative to *their specific goals* — why the 8% drawdown in international equities matters less for a client with a 20-year horizon than for one withdrawing $15K/month.

## The Customisation Gap
The narrative engine needs access to three data sources simultaneously: the client's portfolio holdings and performance (from the portfolio management system), the client's financial plan and goals (from MoneyGuidePro or eMoney), and the client's risk tolerance and communication preferences (from the CRM). It must generate text that passes SEC advertising rules (no promissory language, no cherry-picked timeframes) while speaking at the client's financial literacy level — some clients want Sharpe ratios, others want "your nest egg grew by $42,000 this quarter."

## Impact If Solved
Paraplanners reclaim 40-60 hours per quarter per advisor. Clients receive reports they actually read and understand, reducing inbound "what does this mean" calls by an estimated 30-40%. Advisors can serve 20-30% more clients without degrading perceived service quality.
