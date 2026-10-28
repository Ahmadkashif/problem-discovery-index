# Virtual PPA Settlement Reconciled in Spreadsheets

**Industry:** [[renewable-power-producers|Renewable Power Producers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Energy trading systems already settle financial contracts, but every corporate virtual PPA carries its own negative-price, curtailment, settlement-point and certificate-delivery terms, so the month-end invoice is rebuilt in Excel and argued over with the buyer.
**Tags:** #descriptive-statistics #large-language-models #data-integration #automation #workflow-orchestration #revenue-impact #quick-win

## The Problem
A virtual PPA is a contract for differences. Each settlement interval, the project and the buyer exchange the difference between a market price at an agreed settlement point (a hub or the project's node) and the fixed strike price, multiplied by the contracted volume, whether that is as-generated output or a fixed shape. Corporate buyers negotiate the details: no settlement in intervals where prices fall below zero or below a floor, deemed energy paid for some curtailment and not for other kinds, basis risk allocated one way or another, and renewable energy certificates transferred in M-RETS, WREGIS or PJM-GATS within a set number of days of issuance.

At month end, the commercial settlement analyst pulls ISO settlement statements, revenue-meter data, interval prices and curtailment instructions, rebuilds each contract's calculation in a spreadsheet, and sends an invoice. The buyer's adviser runs a shadow settlement and disputes the difference. ISOs then resettle the same days weeks and months later with revised meter data, so the same month is recalculated several times. A portfolio of 25 contracts means 25 rule sets, and the analyst who built each workbook is the only person who knows its quirks.

## What Already Exists
Energy trading and risk management systems such as Allegro and ION's Endur book and settle physical and financial power trades for utilities and trading desks. ISO shadow-settlement software checks market charges against statements. Analytics firms such as REsurety sell shadow-settlement and revenue analytics to project owners and buyers (named from recall), and the certificate registries record each transfer.

## The Customisation Gap
Trading systems assume standard instruments and a trading desk to configure them; a corporate virtual PPA is a bespoke contract administered by a two-person commercial team. The industry-specific logic is: a term library per contract that turns negative-price, floor, curtailment and shape clauses into executable rules; classification of each curtailment interval as an ISO reliability instruction, an economic self-curtailment or an outage, mapped to how that contract treats it; alignment of every recalculation to each ISO's resettlement calendar; certificate delivery matched to registry issuance and transfer records; and a buyer-ready invoice with the interval-level working that pre-empts the shadow settlement.

## Impact If Solved
In a portfolio settling ~$150M a year, a 2% disputed share leaves ~$3M in argument at any time (estimate). Automated reconciliation could cut ~3 analyst days per contract per month to a few hours and shorten disputes from months to one billing cycle.
