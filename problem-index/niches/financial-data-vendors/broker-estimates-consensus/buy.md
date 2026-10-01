# Reading a Broker's Model Like a Filing

**Niche:** [[niches/financial-data-vendors/broker-estimates-consensus/profile|Broker Estimates & Consensus]]
**Industry:** [[industries/financial-data-vendors|Financial Data Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Spreadsheet extraction tools can read a workbook's cells; they cannot tell which row of a broker's idiosyncratic model is the segment KPI a client wants in consensus.
**Tags:** #large-language-models #transformers #graph-theory #k-nearest-neighbors #evaluation-metrics #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to hold the broadest set of contributed broker estimates at line-item detail and to clean them into a consensus clients trust — and whoever gets both the contributions and the hygiene right owns the number earnings surprises are measured against.

## The Problem
Detailed consensus — segment revenue, unit volumes, KPIs — comes from broker models contributed as workbooks, each laid out in the analyst's own style. Mapping rows to standardised line items is done by hand, per broker, per company, and redone when the analyst restructures the model.

## What Already Exists
Generic spreadsheet parsing and table extraction, and LLM-based document extraction services.

## The Customization Gap
A broker-model mapper must use the formula graph as well as labels, learn each analyst's layout from prior contributions, align KPI definitions across brokers who define them differently, and refuse to map a row when its definition differs from the standard rather than forcing it in.

## Target Customer
Detailed-estimates product teams at consensus vendors.

## Impact If Solved
Detailed consensus is where the estimates contest has moved, and its cost is per-model mapping labour. Learning layouts from history makes breadth affordable.
