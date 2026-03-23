# TSP-Aware Portfolio Management Module

**Niche:** [[niches/wealth-management-rias/military-veteran-advisory/profile|Military & Federal Employee Advisory]]
**Industry:** [[industries/wealth-management-rias|Wealth Management RIAs]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Portfolio management tools like Orion and Black Diamond track client holdings but cannot integrate TSP accounts because TSP does not provide custodial data feeds — leaving a major asset invisible in the advisor's portfolio view.
**Tags:** #data-integration #automation #workflow-orchestration

## The Problem
The Thrift Savings Plan is the largest defined contribution plan in the world (~$800B in assets), yet it operates outside the custodial data feed ecosystem that RIA portfolio management tools rely on. Advisors managing federal/military clients cannot see TSP balances, allocations, or performance alongside the client's other accounts in Orion, Black Diamond, or Advyzon. The advisor must log into my.tsp.gov with the client's credentials (a compliance risk), manually record balances, and maintain a shadow tracking spreadsheet — defeating the purpose of a portfolio management platform.

## What Already Exists
Orion, Black Diamond, and Advyzon provide comprehensive portfolio management with automatic custodian data feeds from Schwab, Fidelity, Pershing, and TD Ameritrade. Account aggregation services like ByAllAccounts and Quovo (now Plaid) pull held-away account data, but TSP integration is unreliable due to TSP's limited API support and multi-factor authentication requirements.

## The Customization Gap
A reliable TSP data integration layer that: (1) securely retrieves TSP balance, allocation, and contribution data without requiring the advisor to store client credentials; (2) maps TSP funds (G, F, C, S, I, L funds) to equivalent asset classes for holistic portfolio analysis; (3) includes TSP-specific features in the portfolio view — contribution limits, catch-up eligibility, loan balances, and Roth vs. traditional split; and (4) enables the advisor to model rebalancing recommendations that span both TSP and non-TSP accounts.

## Target Customer
RIA advisors managing 50+ federal/military client households who currently maintain TSP tracking spreadsheets alongside their portfolio management platform.

## Impact If Solved
Advisors eliminate 30-60 minutes per client per quarter of manual TSP data entry, provide clients with a complete portfolio view that drives better asset allocation decisions, and reduce the compliance risk of storing client TSP login credentials.
