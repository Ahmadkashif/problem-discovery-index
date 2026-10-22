# Self-Install Success Prediction

**Niche:** [[niches/wired-broadband-providers/order-to-activation/profile|Order-to-Activation & Zero-Touch Provisioning]]
**Industry:** [[industries/wired-broadband-providers|Wired Broadband Providers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Operators offer self-install by blanket rule, so some customers who needed a technician fail and call, while others who could have plugged in are sent a truck.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #automation #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn an online order into working service without a human touch — serviceability answer, port assignment, ONT or modem activation and install slot — and whoever closes the most orders without a call or a second visit takes the account.

## The Problem
Self-install saves a truck roll, but a failed self-install costs a support call, a truck anyway and sometimes the customer. The decision is made by rule (existing outlet, prior service at address) with no estimate of success.

## Why Nobody Has Built This
The outcome — success, call, truck, cancel — is spread across order, support and field systems that are rarely joined at order level.

## What to Build
A model predicting self-install success per order from the address's service history, outlet and drop records, telemetry from previous equipment at the address, neighbouring signal health, building type and the customer's channel, used to route each order to self-install, assisted self-install (video help) or a technician, with thresholds tuned to cost.

## Target Customer
Customer operations leaders at cable operators and fibre ISPs with self-install programmes.

## Impact If Built
More orders completed without a truck and fewer failed self-installs, each worth a technician visit and often a customer.
