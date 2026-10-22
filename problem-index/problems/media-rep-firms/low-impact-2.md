# Commission Statements, Splits and Contract Buyouts

**Industry:** [[media-rep-firms|Media Representative Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Sales-commission software calculates what a company owes its own salespeople; a rep firm has to calculate what hundreds of stations owe it, on net collected revenue, with buyouts and house-account carve-outs, and reconcile it every month.
**Tags:** #large-language-models #descriptive-statistics #feature-engineering #data-integration #automation #compliance

## The Problem
A rep firm's revenue is a commission on media sold for each station, recognised when the spot airs. For a firm representing hundreds of stations, the monthly close means several things. The firm takes each station's billing for national business, removes agency commission and anything excluded under the contract, applies the contracted rate, and handles business the station sold directly or that sits on the station's house-account list. It deals with political, digital and network business that may carry different rates, and with collections that came in short. The result is a commission statement each station's business office checks line by line against its own traffic and billing data, and disputes are common.

Contracts add a layer. Representation agreements are multi-year; the largest firm describes terms of up to ten years. When a station or group changes rep, the incoming rep has traditionally bought out the remaining term of the outgoing rep's contract, and termination fees can be material: iHeartMedia reported nonrecurring contract termination fees earned by Katz in 2024. Tracking those liabilities and their schedules station by station is its own accounting problem.

## What Already Exists
Commission platforms such as Xactly, CaptivateIQ and Spiff calculate incentive pay for a company's own sales staff from CRM bookings. Station traffic and billing systems such as WideOrbit produce the invoices and payment records. General ledgers and revenue-recognition modules handle the accounting.

## The Customisation Gap
Incentive-pay tools model one company paying its employees on bookings. A rep firm is paid by many counterparties on net collected media revenue, under contracts whose terms differ station by station. The rep-specific layer needs several pieces. Contract terms have to be extracted from representation agreements: rates by revenue type, exclusions, house accounts and term. Station billing has to be ingested from several traffic systems and matched to orders the rep placed. Short payments must be handled against the agency's payment, with the industry's long-running dispute over sequential versus joint liability for agency non-payment behind them. Buyout liabilities need modelling over the remaining term. And the firm needs a statement each station can audit against its own records without a phone call.

## Impact If Solved
A monthly commission close that reconciles automatically frees rep-firm and station business-office staff from line-by-line disputes. It surfaces under-billed commission the rep is owed. It also gives a station group's CFO a clean answer to the question it asks at renewal: what did we pay the rep, for which business?
