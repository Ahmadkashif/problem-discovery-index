# Introducing Broker Commission and Statement Reconciliation

**Industry:** [[commodity-brokers|Commodity Brokers]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every introducing broker rebuilds, each month and by hand, the same reconciliation from its clearing FCM's statements to what each of its brokers is owed, because accounting software understands invoices and does not understand round turns, fee pass-throughs and give-ups.
**Tags:** #large-language-models #feature-engineering #gaussian-mixture-models #decision-trees #data-integration #automation #quick-win

## The Problem
An introducing broker cannot hold customer money, so its revenue arrives as a monthly commission payment from the FCM that clears its accounts. The IB then has to split that payment among its associated persons, often on per-broker schedules: a share of net commission after exchange, clearing and NFA fees, with different splits for hedge accounts, house accounts and accounts inherited from a departed broker. The source data is the FCM's daily and monthly statements and a commission report, delivered as PDFs, CSV extracts or a portal download in the FCM's own layout. An IB that clears through two FCMs, or moved its book after a merger such as StoneX's 2025 purchase of R.J. O'Brien and its roughly 300 IBs, has two layouts to reconcile.

The work is done in Excel by the principal or an office manager over the first days of the month. Errors show up as broker complaints: a missed adjustment, a fee charged twice, a trade booked to the wrong AP number.

## What Already Exists
QuickBooks or Xero hold the IB's own books. Generic reconciliation tools such as BlackLine or Duco match ledgers. The clearing FCM supplies a back-office portal built on FIS or ION platforms, and some FCMs offer IB reporting dashboards. Commission-management software exists for insurance agencies and securities broker-dealers.

## The Customisation Gap
The missing logic is specific to futures. It has to parse each FCM's statement and commission formats into one model of trades, round turns, fees and adjustments. It has to apply per-AP, per-account and per-product split schedules, including half-turn conventions, option premium commissions and give-up fees. It has to handle exchange and clearing fee pass-throughs, which change several times a year (estimate). And it has to flag anomalies against the IB's own history (a fee per contract outside its normal band, a commission rate that does not match the account's agreement) before the payout is made. Supervision under NFA Rule 2-9 also needs the same trade record viewed per broker, so the reconciled book doubles as the supervisory one.

## Impact If Solved
A principal who spends two to four days a month reconciling (estimate) gets most of that time back. Broker payout disputes, which are among the reasons APs move their books (estimate), are caught before they happen. And the IB gains a clean per-account history it can carry to a new clearing FCM rather than rebuilding from PDFs.
