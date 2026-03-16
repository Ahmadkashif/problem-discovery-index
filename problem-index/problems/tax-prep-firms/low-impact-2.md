# Tax Planning Scenario Modeling for Advisory Upsell

**Industry:** [[tax-prep-firms|Tax Prep Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Financial planning tools model investments and retirement but cannot simulate tax-specific scenarios like entity restructuring, Roth conversions, or QBI deduction optimization that tax preparers need to sell advisory services.
**Tags:** #gradient-boosting #regression #tabular-ml #revenue-impact

## The Problem
Tax prep firms earn $200-500 per return during filing season but could earn $1,000-3,000 per client annually through year-round tax planning engagements — entity selection (S-corp vs. LLC vs. sole prop), retirement contribution optimization, Roth conversion laddering, timing of capital gains harvesting, QBI deduction threshold management, and estimated tax payment scheduling. Most small firms do not offer these services because they lack tools to quickly model scenarios and present clear "Option A saves $4,200 vs. Option B saves $6,800" comparisons to clients. Preparers who attempt it use spreadsheets that take 2-3 hours per client and are error-prone.

## What Already Exists
Holistiplan and Corvee offer tax planning software, and tools like BNA Income Tax Planner (Bloomberg) provide scenario modeling. Financial planning platforms (eMoney, RightCapital) include tax projections. However, these tools are priced for advisory firms ($3,000-8,000/year), require extensive manual data entry separate from the tax software, and do not integrate with Drake/Lacerte/UltraTax workflows. A preparer who just finished a return in Drake cannot click a button to model "what if this client elected S-corp status next year" — they must re-enter all the data into a separate tool.

## The Customisation Gap
A tax-prep-native planning module needs to pull completed return data directly from the preparation software, model specific tax code scenarios (entity election, income timing, deduction bunching, AMT triggers, NIIT thresholds, state-specific impacts), generate client-facing comparison reports in plain language, and price the engagement as a deliverable the firm can sell. The model should incorporate multi-year projections using regression on the client's income trajectory and flag planning opportunities automatically when return data reveals them (e.g., "this client's QBI deduction phases out at $182K — they are at $168K and trending up").

## Impact If Solved
Enables a 500-return firm to convert 10-15% of clients to planning engagements at $1,500 average, generating $75,000-112,500 in off-season revenue. Reduces scenario modeling time from 2-3 hours to 20-30 minutes per client. Transforms seasonal firms into year-round practices.
