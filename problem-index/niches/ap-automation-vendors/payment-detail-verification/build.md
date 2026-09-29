# Corroboration the Attacker Cannot Forge

**Niche:** [[niches/ap-automation-vendors/payment-detail-verification/profile|Payment Detail Verification]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The control against a six-figure wire fraud is a phone call to a number the fraudster may have supplied.
**Tags:** #graph-theory #gradient-boosting #change-point-detection #compliance #evaluation-metrics #confidence-intervals #automation #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to confirm that a bank detail change is genuine using evidence an attacker cannot forge — and whoever replaces the callback to a number from the email itself removes the category's largest concentrated loss.

## The Problem
An email arrives, apparently from a known supplier, saying their banking has changed. It is convincing, it references a real invoice, it may come from a genuinely compromised mailbox. The procedure says call the supplier to confirm — and the number on file may have been updated by the same attacker, or the person calling uses the number in the signature. The payment goes out. This attack has been running unchanged for a decade against an industry that knows about it and has answered with training.

## Why Nobody Has Built This
The callback is a procedural control, so the problem was assigned to policy and training rather than to product — and a control that exists on paper deflects the pressure to build a real one. Verification requires evidence outside the customer's own systems, which no single customer has. Losses are embarrassing and therefore under-reported, which keeps the aggregate invisible. And the platform processes the payment without owning the verification.

## What to Build
Corroborate against the network. Verify a proposed bank detail against what every other buyer of that supplier is paying, which is the core and is evidence the attacker cannot touch — a supplier's genuine account is the one hundreds of other buyers are already paying. Score every change for risk from its context: how it arrived, who requested it, the timing relative to an invoice, whether the account is newly opened, whether it is in an unexpected jurisdiction. Confirm through a channel independent of the request, since the whole failure is confirming through the attacker's channel. Verify the account holder name against the supplier identity, which is a direct check and is increasingly available through payment infrastructure. Detect the social engineering pattern rather than the individual message, because urgency, a new contact, a changed domain and a payment deadline together are the signature. Hold the first payment to a changed account and confirm receipt with the supplier, as that single delay converts a loss into a recoverable near miss. Alert every other buyer of that supplier when a change is detected as fraudulent, which is the network's compounding defence and does not exist. Test the control by simulation, since a procedure never tested is a belief. Record attempted fraud even when it fails, because the pattern data is valuable and is currently discarded. And measure how many changes are verified independently rather than by callback, which is the honest control metric.

## Target Customer
Risk and payment operations leadership, finance leaders who have suffered or fear this loss, insurers pricing the exposure, and payment fraud vendors without the cross-buyer view.

## Impact If Built
Assigning the problem to policy and training deflected the pressure to build a real control. A supplier's genuine account is the one hundreds of other buyers already pay, which is corroboration no attacker can manufacture.
