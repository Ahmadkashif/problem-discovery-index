# Supplier Commission Reconciliation

**Industry:** [[travel-agencies|Travel Agencies]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every agency has to match thousands of bookings to commission payments from hundreds of suppliers that pay late, in different formats and often not at all, and generic accounting tools don't know what a commission should have been.
**Tags:** #large-language-models #k-nearest-neighbors #survival-analysis #evaluation-metrics #data-integration #automation #revenue-impact

## The Problem
A leisure agency or host books hotels, cruises, tours, insurance and rail with hundreds of suppliers. Each owes a commission on its own schedule: hotels after checkout, often through a commission clearing house that batches payments from thousands of properties; cruise lines at or after final payment; tour operators on their own statements; insurers monthly. The agency's back office must work out what each booking should have paid after cancellations, date changes, rate changes and non-commissionable fees, match the payment to the booking, apply the host or advisor split, and chase the gap. Hotel commissions are the worst: ASTA now keeps a watch list of properties that fail to pay 45 days after a completed stay, and recovery firms take 50% of what they collect on claims from 180 days after checkout.

The work is mostly matching. Payment statements identify bookings by confirmation number, guest surname or arrival date, frequently misspelled or truncated, and a single payment may cover dozens of bookings across properties in a chain. Small agencies reconcile in spreadsheets once a quarter; larger hosts employ commission teams who spend their days on supplier portals and email.

## What Already Exists
General accounting and AR tools (QuickBooks, Xero, NetSuite) record payments but have no idea what was owed. Agency back-office systems such as Trams and ClientBase track expected commissions from booking data and can match some electronic statements. Newer tools such as Tern have added hubs that match expected to received commissions, and recovery services such as Commtrak chase aged hotel claims on contingency.

## The Customisation Gap
The industry-specific logic is: rules for what each supplier type should pay (commissionable versus non-commissionable components, cruise fare versus port charges and fees, hotel room revenue versus resort fees and taxes); booking-change history that alters the expected amount; fuzzy matching of payment lines to bookings when the only shared keys are a guest name and an arrival date; the host-advisor split and its 1099 consequences; supplier-specific payment behaviour (which chains pay through which clearing house, typical delay, how often they underpay); and the timing of when to chase and through which route — the property, the brand's agency desk, ASTA's reporting tool, or a contingency firm. Generic AR tools lack all of it.

## Impact If Solved
A host with ~$100-300M in bookings (estimate) that recovers even ~2-3% more of earned hotel commission, and cuts its commission team's matching time by half, gains hundreds of thousands of dollars a year; the independent advisor gets paid for work done months earlier instead of writing it off.
