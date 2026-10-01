# Alternative Data Trial Evaluation

**Industry:** [[hedge-funds|Hedge Funds]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every fund runs the same 30–90 day trial process on every alternative dataset — map it to tickers, backtest it against reported KPIs, clear its provenance — and rebuilds that process by hand for each vendor.
**Tags:** #feature-engineering #linear-regression #time-series-forecasting #evaluation-metrics #hypothesis-testing #data-integration #compliance #automation

## The Problem
A data vendor offers a trial: card transaction panel, app usage, web traffic, job postings, satellite counts, shipping manifests. The fund's data team has a window — commonly one to three months — to decide whether to pay a licence that can run to six or seven figures a year. In that window they must load the files, map the vendor's company or merchant names to the fund's securities, build point-in-time history, test whether the series predicts reported KPIs or returns on the names the fund actually trades, and get compliance to sign off on how the data was collected.

Most trials die not because the data is bad but because the evaluation never finishes. Entity mapping takes weeks; the backtest is rushed; the vendor's history has been revised in ways that make it look better than it was in real time; and the conclusion is a data scientist's judgement presented to a PM who wanted a yes or no.

## What Already Exists
Data catalogues and pipeline tools (Snowflake, Databricks, dbt, and data delivery platforms such as Crux), alternative-data discovery services such as Neudata, and broker marketplaces analysed in [[data-marketplace-brokers|Data Marketplace Brokers]]. Vendors often supply their own backtest decks. Industry due-diligence questionnaires exist for data provenance.

## The Customisation Gap
The generic tools move and store data; they do not answer the fund's question. The fund-specific logic is: symbology mapping from merchant and brand names to tradable securities, with corporate actions and subsidiaries; point-in-time reconstruction that refuses revised history; KPI-level evaluation against the fund's own coverage universe and its own consensus source; panel-bias diagnostics (does this panel over-represent one demographic or region); and a provenance record compliance can rely on for MNPI and consent purposes. Each fund builds this per dataset, and the vendor's backtest deck answers a different question from the one the fund's PMs ask.

## Impact If Solved
A standard, repeatable trial harness turns evaluation from a bespoke six-week project into a few days, lets a data team evaluate several times more datasets per year, and produces a written verdict PMs and compliance can both rely on — which is the difference between alternative data as a research input and alternative data as an expensive experiment.
