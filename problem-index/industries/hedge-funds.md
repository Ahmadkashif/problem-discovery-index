# Hedge Funds

## Profile
**Category:** Capital Markets & Investment Research
**Market Size:** ~$5T in global hedge fund assets (HFR put industry capital at a record ~$5.15T at end-2025), generating an estimated ~$100B+ a year in management and performance fees; investment managers spent an estimated ~$2.8B on alternative data in 2025 (Neudata), most of it from hedge funds
**Tech Maturity:** High at the edges, manual at the core — systematic funds run some of the most sophisticated research infrastructure in any industry, while the discretionary side (long/short equity pods, credit, event-driven, macro) still runs on Excel models, a research management system nobody fully uses, a Bloomberg terminal, and the analyst's own memory of why a position is on.
**Workforce:** Portfolio managers, fundamental analysts and associates (typically organised in pods at multi-manager platforms), quantitative researchers and data scientists, alternative-data sourcing and data engineering teams, risk managers, compliance officers and MNPI control staff, investor relations, and operations

## Key Pain Themes
A hedge fund's product is a sequence of decisions — buy, short, size, add, cut — and the research that justifies each one is written down unevenly and almost never joined to what happened next. Profit and loss is attributed to positions and factors with great precision; it is not attributed to the thesis, the analyst note, the expert call or the dataset that produced the position, so the fund cannot say which parts of its research process carry information. At multi-manager platforms the problem is sharper: pods are cut on drawdown, analysts move between platforms every two or three years, and the judgement that made a coverage list profitable leaves with the person who held it.

Around the decision sits a research workflow under a hard external clock. Earnings season compresses forty companies' quarters into three weeks, each requiring the model updated, the call heard and the thesis re-checked before the open. Alternative datasets arrive as trials with a 30–90 day window to prove they carry signal on the fund's own universe. And every input — an expert call, a channel check, a dataset, a conversation with a company's investor relations team — must be cleared by compliance for material non-public information risk, a review that is mostly manual and is the binding constraint on how fast research can move.

## Current Tech Landscape
Market data and fundamentals come from Bloomberg, FactSet and S&P Capital IQ; consensus and model data from Visible Alpha and Daloopa; search across filings, transcripts and expert calls from AlphaSense (which absorbed Sentieo and Tegus). Research notes live in research management systems such as Bipsync or in OneNote, Evernote and email. Alternative data is sourced directly or through brokers and evaluated by in-house data teams; risk runs on MSCI Barra or Axioma factor models; e-communications surveillance on Global Relay or Smarsh. Each tool is competent within its boundary. The research record — thesis, evidence, conviction, outcome — spans all of them and is owned by none.

## Problems
- [[problems/hedge-funds/high-impact|🔴 High Impact: The Thesis Nobody Grades]]
- [[problems/hedge-funds/low-impact-1|🟡 Low Impact: Alternative Data Trial Evaluation]]
- [[problems/hedge-funds/low-impact-2|🟡 Low Impact: MNPI Clearance of Research Inputs]]
- [[problems/hedge-funds/worker-life-1|🟢 Worker Life: The Pod Analyst Through Earnings Season]]
- [[problems/hedge-funds/worker-life-2|🟢 Worker Life: The Data Scientist Serving Twenty PMs]]
- [[problems/hedge-funds/ml-opportunity|🧠 ML Opportunities]]
- [[problems/hedge-funds/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Hedge funds are the purest decision businesses in the economy: every position is a dated, sized prediction, and its outcome is marked to market every day. The outcome data is perfect. The decision data is not — the reasoning behind a position lives in notes, models and the analyst's head, and is rarely recorded in a form that can be joined to the P&L it produced. That makes the industry's most valuable research question unusually tractable and unusually neglected: which of our research activities carries information? The obstacles are organisational (portfolio managers resist having their judgement scored), legal (every research input passes through an MNPI filter) and structural (analysts leave, and their pattern recognition goes with them). For research-workflow automation the useful finding is that the hard part is not producing more research — LLMs already summarise transcripts and filings — but recording the research decision so it can be graded, reused and handed over, and clearing research inputs fast enough that compliance stops being the bottleneck. Note that the hedge fund itself is a poor buyer for a research-insight engine under the Pass 2 rubric — its insight is monetised through trading, not invoiced, and MNPI is a live procurement gate — so the strongest commercial pockets sit around it, in the firms that sell research to funds.
