# Cross-Channel Takeover Risk for Every SIM and Port Request

**Niche:** [[niches/wireless-carriers/porting-sim-account-security/profile|Number Porting, SIM Changes & Account Takeover Defence]]
**Industry:** [[industries/wireless-carriers|Wireless Carriers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A takeover usually leaves a trail across channels (a password reset online, a call to care, a store visit) that each channel's rules see only in part.
**Tags:** #gradient-boosting #autoencoders #graph-neural-networks #feature-engineering #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to approve every legitimate port-out, eSIM transfer and SIM change in seconds while stopping the takeover attempts hidden among them, and whoever delivers the lowest fraud at the least customer friction takes the account-security budget.

## The Problem
Fraudsters probe accounts through whichever channel is weakest: they phish credentials, call care with partial identity details, visit a store with a fake ID, or request a port with a PIN obtained from the victim. Each channel applies its own checks, so a pattern that is obvious across channels passes each check on its own.

## Why Nobody Has Built This
Channels are owned by different organisations (digital, care, retail, porting operations) with separate systems and metrics. Fraud labels arrive late, from victim complaints and bank notifications, and are recorded inconsistently.

## What to Build
A single risk service scoring every SIM change, eSIM transfer and port-out request from the account's cross-channel event history, device and session signals, linkage between accounts sharing identifiers, and known fraud rings. It decides approve, step up or hold, sends the customer notice the FCC's 2023 order calls for, and learns from confirmed fraud and false positives.

## Target Customer
Heads of fraud and identity at national and regional carriers, and the MVNO hosts that process their partners' requests.

## Impact If Built
Fewer takeovers and the losses and complaints that follow, with fewer legitimate customers stuck in step-up checks, and a documented control ready for the FCC's rules when their compliance date is set.
