# Two Contacts Counted, One Problem

**Niche:** [[niches/customer-support-platforms/support-channels/profile|Support Channels]]
**Industry:** [[industries/customer-support-platforms|Customer Support Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Support measures contacts, so a customer who needed three interactions across two channels to solve one problem appears as three units of work successfully handled.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #graph-theory #quick-win #automation #worker-facing
**Contested on:** *Not terminal as stated* — see the sub-niches for the two distinct forms this contest takes.

## The Problem
A customer chats, is told to email, emails, receives a reply asking for information they already gave, calls, and is resolved. The organisation records four contacts, four handle times, three satisfaction surveys and one resolution. Every one of its operational metrics improved. The customer's experience was four interactions to solve one problem and the measurement system cannot see that, because the unit is the contact. Every incentive in the function — agent throughput, channel cost per contact, deflection rate — is computed on a unit that does not correspond to the thing the customer experienced.

## Why It's Still Broken
The ticket is the natural record for an operational system and the contact is the natural unit of work, so the metrics followed. Reconstituting an issue from several contacts requires the identity resolution and the linking this niche describes, which nobody has built. And changing the unit is uncomfortable: an organisation that starts measuring issues rather than contacts will see its resolution rate fall and its per-issue cost rise, with no underlying change, which is a reporting discontinuity that requires an explanation to an executive.

## What a Fix Looks Like
Define the issue and measure on it. Contacts are grouped into issues by customer, subject and time proximity, which is a clustering problem over records the platform already holds and is tractable even without perfect identity resolution. Report contacts per issue, channel switches per issue, and time to resolution measured from the customer's first attempt rather than from the ticket that eventually resolved it — which is the customer's actual experience and is currently invisible. Keep the contact-level operational metrics for staffing and capacity, where they are the right unit, and use issue-level metrics for anything describing service quality. Report the transition matrix between channels, since a high rate of chat-to-phone escalation on a particular topic is a specific, fixable failure in the chat experience and is currently averaged away. And publish the change honestly when the metric shifts, because the new number is the true one and the old one was flattering.

## Who Feels the Pain
Customers who needed four interactions; agents handling contacts that should never have been necessary; and support leaders optimising a system against a unit that hides its worst outcomes.

## Impact If Fixed
Issue-level measurement is a clustering exercise over existing records and immediately reveals the repeat-contact and channel-switching patterns that contact-level reporting conceals. The channel transition analysis is the most actionable output, since it points at specific topics where an automated or self-service path is failing and sending people to the phone.
