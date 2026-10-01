# Sell-Side Equity Research

## Profile
**Category:** Capital Markets & Investment Research
**Market Size:** ~$8–12B estimated global annual spend by institutional investors on broker research across equities and adjacent credit, with brokers taking roughly 85% of asset managers' research budgets (Substantive Research, 2024); budgets fell for six years after MiFID II and began rising again in 2024
**Tech Maturity:** Medium — publishing, distribution and entitlement are well tooled (BlueMatrix, Bloomberg, FactSet, LSEG Workspace, AlphaSense), but the analytical core is still a per-analyst Excel model, a Word template and a set of habits that leave with the analyst.
**Workforce:** Senior research analysts (FINRA Series 86/87), research associates, supervisory analysts (Series 16) and research compliance staff, editors and production, corporate access teams, research sales and specialist sales, directors of research

## Key Pain Themes
The work runs on a calendar the department does not control. Four times a year every covered company reports inside a few weeks, and the analyst must preview the quarter, read the print at 6:30 a.m., publish a first take before the open, roll the model, take the call and revise estimates and price target by the afternoon — for fifteen to twenty-five names. The deliverable is judgment: which number the stock will trade on, whether management's guide is conservative in the way it usually is, and where consensus is wrong. That judgment lives in one person's model and memory, and a department that loses a senior analyst loses the coverage franchise and the votes attached to it.

Around the analytical work sits a compliance apparatus built after the 2003 Global Research Analyst Settlement: Reg AC certifications, FINRA Rule 2241 conflict disclosures, quiet periods around offerings, restricted and watch lists, price-target basis and risk statements, ratings-distribution tables, and supervisory analyst review of every report before release. And underneath everything is a payment model in flux — unbundled in the EU and UK by MiFID II from 2018, partially rebundled by the FCA from August 2024, still largely commission-funded in the US — in which the department cannot see which of its outputs its clients actually paid for.

## Current Tech Landscape
Reports are authored and distributed through BlueMatrix or in-house publishing systems with compliance disclosure modules, and land in Bloomberg, FactSet, LSEG Workspace, S&P Capital IQ and AlphaSense, which aggregate entitled research for the buy side. Estimates are submitted to LSEG I/B/E/S, FactSet Estimates and Bloomberg, and full models to Visible Alpha. Financial data extraction for models is increasingly bought from Daloopa or Canalyst (now within AlphaSense via Tegus). Corporate access runs on CRM and spreadsheets, readership on platform-provided click logs, and the broker vote arrives as a spreadsheet from each client twice a year. Nothing connects the analyst's forecast history, the department's published views, the client's readership and the vote.

## Problems
- [[problems/sell-side-equity-research/high-impact|🔴 High Impact: The Coverage Franchise That Lives in One Analyst's Head]]
- [[problems/sell-side-equity-research/low-impact-1|🟡 Low Impact: Pre-Publication Compliance Review]]
- [[problems/sell-side-equity-research/low-impact-2|🟡 Low Impact: Spreading the Print Into the Analyst's Own Model]]
- [[problems/sell-side-equity-research/worker-life-1|🟢 Worker Life: The Associate on Earnings Night]]
- [[problems/sell-side-equity-research/worker-life-2|🟢 Worker Life: The Analyst Who Cannot See What Got Paid For]]
- [[problems/sell-side-equity-research/ml-opportunity|🧠 ML Opportunities]]
- [[problems/sell-side-equity-research/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A sell-side research department is a forecasting institution that has never graded its own forecasts. Every estimate, every price target, every rating and every "we think consensus is too low on gross margin" is published, timestamped and archived — and the realised numbers arrive on a schedule, four times a year, in public filings. The labelled dataset is complete and free. What is missing is the join between the department's own forecast history and what happened, at the level of the individual analyst, the individual line item and the individual management team, which is precisely the level at which the tacit judgment that clients pay for actually operates. Automating the mechanical half of the job — spreading the print, rolling the model, clearing the disclosures — is now commodity work; capturing and measuring the judgment half is not, and it is the half that decides who keeps a coverage franchise when the analyst who built it leaves.
