# Break Prediction Before the Cutoff

**Niche:** [[niches/trust-companies/institutional-custody-asset-servicing/profile|Institutional Custody & Asset Servicing]]
**Industry:** [[industries/trust-companies|Trust Companies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Custody operations find breaks when the reconciliation runs, after the cutoff pressure has started, though most breaks follow patterns visible hours earlier.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #time-series-forecasting #automation #workflow-orchestration #data-integration
**Contested on:** Every serious competitor in this niche is fighting to deliver each client's positions, cash and corporate-action entitlements without breaks before the client's own NAV and settlement cutoffs, and whoever has the fewest unresolved breaks at the cutoff takes the account.

## The Problem
A custody bank reconciles millions of positions and cash movements a day against investment managers, fund accountants, sub-custodians and depositories. Breaks — a late trade instruction, a mismatched settlement amount, an income entitlement booked at the wrong rate, a corporate action applied on the wrong date — surface when the reconciliation runs, and analysts then race the client's NAV or settlement deadline to resolve them.

## Why Nobody Has Built This
Reconciliation tools are built to match, not to forecast. Break histories are coded with inconsistent reason codes across teams and acquired platforms, so the labelled history is messy. And operations teams are measured on breaks cleared, not breaks prevented.

## What to Build
A model that scores every expected settlement, income event and corporate action for break risk hours before the cutoff, from features such as counterparty, market, instruction timing, security type, event complexity and the history of similar items. High-risk items are worked proactively: the instruction chased, the rate confirmed, the event interpretation checked. A root-cause classifier standardises reasons on resolved breaks so recurring causes can be fixed upstream.

## Target Customer
Heads of asset servicing and reconciliation operations at global and regional custody banks.

## Impact If Built
Preventing even ~20% of breaks (estimate) before they occur reduces the number of items still open at the client's cutoff, which is the metric clients notice, and frees analysts for the complex events that need them.
