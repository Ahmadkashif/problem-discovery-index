# The Network Analyst in Data Month

**Industry:** [[logistics-consultants|Logistics Consultants]]
**Type:** Worker Life Changing
**One-liner:** For four to eight weeks of every network study a junior analyst matches addresses, imputes weights and chases a baseline variance late into the night, doing the part of the job furthest from why they joined.
**Tags:** #large-language-models #k-nearest-neighbors #feature-engineering #evaluation-metrics #worker-facing #automation #data-integration

## The Problem
The analyst on a network study is usually two to four years out of an industrial engineering or supply chain programme. Their first month on the project is data. The client sends a TMS extract with ship-to names typed by hand ("WALMART DC 6094", "Wal-Mart #6094 RDC", "WMT 6094"), an ERP order file keyed on a different customer number, a freight audit file keyed on invoice and pro number, and a warehouse cost spreadsheet built by someone in finance who has since left. The analyst matches them, geocodes thousands of ship-to points and corrects the ones that land on a billing office, fills missing weights and cube from the item master, allocates fuel and accessorials back to shipments, and builds the baseline.

Then the baseline does not tie. The model's total cost is 7% below the general ledger and the partner's readout is on Thursday. The analyst works through the evenings looking for the gap — an unbilled carrier, an intercompany transfer, a month of missing invoices — while the client's data owner answers emails a day late. A traditional study spends one to two of its three to four months on data, and most of that falls on this one person.

## Why It Matters to the Worker
They joined to design networks, and the part of the job that teaches them to — scenario design, reading the results, presenting to a client — arrives only after the data month, compressed. The skills they build in the data month are real but invisible: nobody praises the address matching, and every error in it surfaces later as a wrong answer in front of the client, attributed to them.

The hours are also unpredictable in a way that wears people out. The baseline variance is not a fixed amount of work; it is a search, and it ends when the missing cost is found. Travel to client sites stacks on top. The usual exit is an in-house network or transportation role at a shipper, where the data is at least the analyst's own and they only have to learn it once.

## What a Solution Looks Like
A data intake assistant that reads the client's extracts, proposes the joins between them, clusters ship-to variants into locations with a confidence score, flags geocodes that land on non-receiving addresses, imputes missing weights and cube from the item master with each imputation marked, and drafts the baseline reconciliation — model cost against ledger cost, by cost bucket, with the largest unexplained gaps ranked and the likely causes listed. The analyst reviews and approves rather than builds from nothing, and every decision is logged so the senior modeller can check it in an hour.

## Impact If Solved
Cutting the data month from six weeks to two (estimate) gives each analyst back roughly a month per study, moves that time to scenario work where they learn the craft, and removes most of the late-night variance hunts that drive people out of the work in their first few years.
