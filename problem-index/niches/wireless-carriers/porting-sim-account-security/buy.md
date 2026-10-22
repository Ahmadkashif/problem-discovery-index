# Payment-Fraud Decisioning Applied to SIM Changes

**Niche:** [[niches/wireless-carriers/porting-sim-account-security/profile|Number Porting, SIM Changes & Account Takeover Defence]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Banks have spent a decade building real-time fraud decisioning for payments; a SIM change is a similar decision that most carriers still handle with static rules.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #compliance #data-integration #automation
**Contested on:** Every serious competitor in this niche is fighting to approve every legitimate port-out, eSIM transfer and SIM change in seconds while stopping the takeover attempts hidden among them, and whoever delivers the lowest fraud at the least customer friction takes the account-security budget.

## The Problem
Carrier SIM and port controls are mostly rules: a PIN, a passcode, a hold period after an address change. Rules are easy for fraudsters to learn and tend to block legitimate customers who trip them.

## What Already Exists
Payment fraud decisioning platforms (NICE Actimize, Featurespace, and others covered under [[industries/payment-fraud-vendors|Payment Fraud Vendors]]) and identity verification vendors under [[industries/identity-verification-vendors|Identity Verification Vendors]].

## The Customization Gap
The adaptation needs carrier event types (SIM change, eSIM transfer, port-out request, number transfer PIN request, device upgrade) as decision points; features from network and device data the carrier alone has; integration with porting systems and care tools; the customer notices the FCC's 2023 order calls for as an action; and fraud labels from victim reports and bank feedback.

## Target Customer
Carrier fraud teams wanting a proven decisioning engine rather than a homegrown one.

## Impact If Solved
Real-time, learning decisions on SIM and port events built on a platform category banks already trust.
