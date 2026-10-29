# Landed Cost and Retailer Cost Changes Under Moving Tariffs

**Industry:** [[consumer-goods-wholesalers|Consumer Goods Wholesalers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** ERPs can compute landed cost; they cannot carry a tariff change from the entry summary to every SKU's cost and into each retailer's cost-change process before the margin is gone.
**Tags:** #monte-carlo-methods #gradient-boosting #large-language-models #feature-engineering #compliance #revenue-impact #automation

## The Problem
A costing analyst at an importer keeps a landed cost for every SKU: factory price, ocean freight, duty, brokerage, inland freight and warehousing. Between February 2025 and July 2026 the duty line changed repeatedly. IEEPA tariffs were imposed and then struck down on 20 February 2026, a 10% Section 122 tariff ran from 24 February to 24 July 2026, and Section 301 forced-labour tariffs of 10% or 12.5% started on 24 July 2026. Each change moved the cost of thousands of SKUs at once. Each one also meant a round of cost-increase requests to every retailer, each with its own forms, notice rules and timing around line reviews. Meanwhile IEEPA refunds have been coming back entry by entry through CBP's refund process, and retailers ask for their share. The analyst works through this in spreadsheets built from the broker's entry reports.

## What Already Exists
ERP landed-cost modules in NetSuite, Acumatica, Dynamics and SAP Business One allocate freight and duty to receipts. Customs brokers file entries and send entry summaries. Trade-content databases such as Descartes CustomsInfo and Thomson Reuters ONESOURCE hold the tariff schedule, and freight forwarders quote rates. The broker side of the same importer is profiled at [[niches/customs-brokers/high-volume-consumer-goods/profile|High-Volume Consumer Goods Imports]].

## The Customisation Gap
The importer needs four things joined. Entry-level duty from the entry summary, line by line, has to flow down to SKU-level cost. Each SKU's cost has to reach each retailer's cost file and cost-change process, with that retailer's notice rules and calendar. Refunds have to be tracked per entry back to the SKUs and the customers who bought them, so the importer knows what it owes and what it keeps. And pending tariff actions need scenario costs, so price requests go in before the duty lands. All of this has to work in the importer's language of item numbers, programmes and accounts, not the broker's language of entries and HTS lines.

## Impact If Solved
For an importer buying ~$40M a year at first cost with a 10-point duty increase (~$4M a year, estimate), getting retailer cost changes accepted one quarter sooner keeps ~$1M of margin (estimate), and a complete per-entry refund record stops refunds being under-claimed or over-shared.
