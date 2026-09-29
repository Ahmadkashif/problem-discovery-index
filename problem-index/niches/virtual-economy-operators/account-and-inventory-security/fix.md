# Password Changed and Everything Gone in Four Minutes

**Niche:** [[niches/virtual-economy-operators/account-and-inventory-security/profile|Account & Inventory Security]]
**Industry:** [[industries/virtual-economy-operators|Virtual Economy Operators]]
**Type:** Fix (Pain Point)
**One-liner:** The attacker reset the password and transferred the entire inventory before the notification email had been read.
**Tags:** #quick-win #automation #change-point-detection #compliance #evaluation-metrics #workflow-orchestration #descriptive-statistics #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to protect inventories worth real money with security that was designed for game logins — and whoever raises that floor takes the account.

## The Problem
The standard theft sequence takes minutes: compromise the email or the credentials, reset the password, log in from a new device, and transfer every valuable item out before the account holder sees any notification. There is no delay between gaining access and being able to move assets. The notification arrives after the loss. Every step of this is well known and the timeline is unchanged because nothing interrupts it.

## Why It's Still Broken
Nothing separates access from transfer — an account where logging in immediately confers the power to move every asset gives the attacker the entire window, and the notification is a record rather than a control. Holds add friction. The email account is outside the operator's control. And the loss is the user's.

## What a Fix Looks Like
Insert a delay between access and transfer. Hold all transfers for a period after a password, email or device change, which is the fix and breaks the sequence outright at very low cost. Notify through a channel the attacker has not compromised, since email notification to a compromised email is worthless. Let the holder cancel a pending transfer during the hold, which is what makes the hold protective rather than merely annoying. Scale the hold duration to the value being moved so ordinary trading is unaffected. Lock on rapid liquidation of a whole inventory, as that pattern is unmistakable and never legitimate. Require a second factor for transfers above a threshold rather than only at login. Show the holder recent security events prominently on their next visit. Make recovery after a compromise evidence-based rather than knowledge-based. Warn holders of valuable inventories who have no protection enabled, which is a direct and effective message. And apply the hold by default rather than as an opt-in setting, since the people most at risk are the least likely to find it.

## Who Feels the Pain
Holders who lost everything in minutes; support teams handling unrecoverable cases; operators absorbing the reputational cost; and honest traders whose market is supplied with stolen goods.

## Impact If Fixed
An account where logging in immediately confers the power to move every asset gives the attacker the entire window, and the notification is a record rather than a control. A post-change transfer hold breaks the sequence outright.
