# Mobile Churn Analytics Adapted to Fixed Broadband

**Niche:** [[niches/wired-broadband-providers/residential-retention-and-migration/profile|Residential Retention & Migration]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Mobile carriers have run churn and next-best-offer analytics for two decades; fixed broadband churn is driven by different things and the models don't transfer as they are.
**Tags:** #gradient-boosting #survival-analysis #causal-inference #feature-engineering #revenue-impact #data-integration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor is fighting to keep a household's broadband revenue when its current connection stops being its best option, but for cable operators that is a pricing contest at promo roll-off against fixed wireless and fibre, and for telcos it is an operational contest to move households off copper before the wire center is retired. Decomposed into contested sub-niches below.

## The Problem
Fixed operators buy churn tooling built for mobile, where churn follows device upgrade cycles, contract ends and coverage complaints. Broadband churn follows promotion expiry, moves, outages and the arrival of an alternative at the address.

## What Already Exists
Churn prediction and next-best-offer modules in telecom BSS suites (Amdocs, CSG) and customer data platforms, proven at mobile carriers with uplift testing and campaign management.

## The Customization Gap
Fixed broadband needs: features for promo and price-lock calendars per account; address-level competitive availability rather than coverage complaints; outage and repeat-ticket history from the network; move detection (address change is the largest single churn event and a retention opportunity if the new address is serviceable); household-level rather than line-level modelling; and, for telcos, copper retirement status per wire center.

## Target Customer
Retention and customer analytics leads at operators already licensing a BSS suite with churn modules.

## Impact If Solved
Operators get usable broadband churn models from tools they already pay for, without a separate data science build.
