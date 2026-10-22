# The 1% Cash Remittance Tax at the Counter

**Industry:** [[money-service-businesses|Money Service Businesses]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Since January 2026 every transmitter must decide, transfer by transfer and at thousands of agent counters, whether the sender paid with a physical instrument, collect 1%, refund it on cancellation and deposit it semi-monthly — and tax engines built for sales tax do not know what a funding method is.
**Tags:** #decision-trees #logistic-regression #evaluation-metrics #data-integration #compliance #automation #workflow-orchestration

## The Problem
The One Big Beautiful Bill Act created a 1% excise tax under new IRC §4475 on outbound remittance transfers made on or after 1 January 2026 when the sender funds the transfer with cash, a money order, a cashier's check or a similar physical instrument. Transfers funded from a US bank account or a US-issued debit or credit card are outside it. The transmitter collects the tax at the point of transfer, makes semi-monthly deposits and files quarterly on Form 720; the IRS gave penalty relief for the first three quarters of 2026 in Notice 2025-55 and issued proposed regulations in April 2026.

For an app-based transmitter funded by cards and bank transfers this is a small edge case. For an agent-network transmitter it is the majority of volume. The funding method is captured, if at all, by a clerk pressing a button on a terminal: cash, money order, or "other". A sender who hands over a cashier's check, pays part in cash and part by card, or cancels and resends the next day creates a case the terminal was never designed to classify. The tax must also appear correctly on the consumer's prepayment disclosure and receipt under the CFPB's remittance rule, and be refunded when a transfer is cancelled within the rule's window.

## What Already Exists
Sales and use tax engines such as Avalara and Vertex compute jurisdictional taxes on transactions. Payment platforms tag card and bank funding. Agent terminals and send platforms already print Reg E disclosures. Tax departments file Form 720 for other federal excise taxes.

## The Customisation Gap
What the transmitter needs is a funding-method determination layer, not a rate table: rules for mixed and ambiguous instruments as the proposed regulations define them; validation of clerk-entered funding codes against other signals (cash drawer reconciliation, sweep amounts, receipt images) so systematic miscoding at a given agent is caught; tax-inclusive disclosure and receipt templates per corridor and language; cancellation and refund logic tied to the Reg E cancellation window; and a deposit and Form 720 reconciliation from transfer-level data to the semi-monthly liability. Agent-level exceptions — a store that never records cash although it sweeps cash-heavy amounts — are an audit and agent-oversight signal as much as a tax one.

## Impact If Solved
A transmitter can collect and deposit the tax correctly before penalty relief ends, avoid over-collecting on card-funded transfers (a pricing disadvantage in a market priced to the cent) and under-collecting on cash (a liability the provider carries), and turn miscoded funding methods into an early warning about agents whose cash records do not add up.
