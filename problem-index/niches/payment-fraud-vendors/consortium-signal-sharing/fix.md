# The Blocklist Entry From Three Years Ago

**Niche:** [[niches/payment-fraud-vendors/consortium-signal-sharing/profile|Consortium Signal Sharing]]
**Industry:** [[industries/payment-fraud-vendors|Payment Fraud Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** A device or an email was flagged once, years ago, possibly wrongly, and it has been declined everywhere ever since.
**Tags:** #compliance #quick-win #evaluation-metrics #descriptive-statistics #automation #confidence-intervals #graph-theory #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to make the network signal worth more than the sum of its members' own data — and whoever proves the consortium's marginal contribution can charge for it instead of asserting it.

## The Problem
A negative signal entered the consortium: a device fingerprint, an email, a shipping address. Perhaps it was a genuine fraudster, perhaps a chargeback from a confused customer, perhaps a shared computer or a reassigned address. It has no expiry. Every merchant on the network declines that identifier indefinitely, the person affected has no idea why they are declined everywhere, and there is no route for them to contest a record they cannot see.

## Why It's Still Broken
Negative signals were designed to accumulate, so nothing in the system expires them — a list built to remember has no mechanism for forgetting, and the cost of remembering falls entirely on the person listed. Removing an entry risks readmitting a fraudster, which is visible, while keeping it costs a stranger nobody counts. The affected person has no visibility and no channel. And nobody measures how many entries are old, unconfirmed or singleton.

## What a Fix Looks Like
Give negative signals a lifespan and a burden of proof. Expire entries on a schedule appropriate to the signal type, which is the fix and is standard practice in adjacent disciplines. Require corroboration before a single event creates a network-wide negative, since one merchant's chargeback is weak evidence for a permanent global block. Report the age and confirmation count of entries actually driving declines, which will show how much of the list is stale singletons. Decay confidence over time rather than treating a three-year-old signal as current. Re-evaluate an entry when contradicted by subsequent good behaviour, as a person transacting successfully elsewhere is evidence. Distinguish shared and reassigned identifiers — household devices, recycled addresses, corporate networks — because they generate systematic and permanent harm. Provide a contest route through the merchant, since the affected person currently has none anywhere. Measure how many declines trace to a single unconfirmed entry, as the number will make the case. Tell merchants when a decline rests on a stale network signal, so they can override for a customer they know. And review the policy against consumer protection expectations, because a permanent secret blocklist is exactly what draws regulatory attention.

## Who Feels the Pain
People declined everywhere with no explanation and no appeal; merchants losing customers to another merchant's old chargeback; and vendors carrying a consumer protection exposure nobody has examined.

## Impact If Fixed
A list built to remember has no mechanism for forgetting, and the cost of remembering falls entirely on the person listed. Expiry, corroboration before listing, and confidence decay are standard elsewhere and absent here.
