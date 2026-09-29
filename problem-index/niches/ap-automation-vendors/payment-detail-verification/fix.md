# Calling the Number in the Email

**Niche:** [[niches/ap-automation-vendors/payment-detail-verification/profile|Payment Detail Verification]]
**Industry:** [[industries/ap-automation-vendors|AP Automation Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The procedure says verify by phone and does not say which number, so people use the one in front of them.
**Tags:** #compliance #quick-win #worker-facing #automation #evaluation-metrics #workflow-orchestration #descriptive-statistics #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to confirm that a bank detail change is genuine using evidence an attacker cannot forge — and whoever replaces the callback to a number from the email itself removes the category's largest concentrated loss.

## The Problem
The control is written as "call the vendor to verify". In practice the person calls the number in the email signature, or the number the requester supplied, or the number on the vendor record that was updated last week by the same request. The control is defeated not by sophistication but by the absence of a specified source for the number. Everyone in the process believes they followed the procedure, and the wire goes to the fraudster.

## Why It's Still Broken
The procedure was written as a training instruction rather than as a system control, so it specifies an action and not its inputs — and an instruction that cannot be enforced is followed in whatever way is easiest. The verified number is not distinguished in the vendor record. Nobody tests whether the control works. And the failure is rare enough per company to feel like bad luck.

## What a Fix Looks Like
Specify the number and lock it. Mark a verified contact number on each vendor record, which is the fix and turns an ambiguous instruction into a specific one. Lock the verified number against change through the same channel that requests a bank change, as that single rule breaks the attack's most common form. Present the verified number in the verification step so the person does not have to look for one, since convenience determines behaviour. Record the source of the number used and require it to be selected, because an unauditable control cannot be assessed. Show the record's recent change history during verification, as a number changed last week alongside a bank change request is the whole story. Require a second approver for bank changes, which is standard and inconsistently applied. Hold the first payment and confirm receipt separately, since it is the cheapest effective backstop. Flag requests arriving by email at all, because a supplier portal submission is far stronger evidence than a message. Run a simulated attack, as most organisations have never tested this and the result changes the conversation immediately. And report how many changes were verified against a locked number, which is the only meaningful measure of whether the control is real.

## Who Feels the Pain
The person who authorised the payment and will be blamed; finance teams facing an unrecoverable loss; suppliers accused of a change they never requested; and companies whose control existed only on paper.

## Impact If Fixed
The procedure was written as a training instruction, so it specifies an action and not its inputs. Marking and locking a verified contact number turns an ambiguous instruction into an enforceable control.
