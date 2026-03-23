# Reg F Contact Frequency Limit Tracking Gaps

**Niche:** [[niches/collections-agencies/compliance-audit-automation/profile|Compliance Audit Automation]]
**Industry:** [[industries/collections-agencies|Collections Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Reg F limits contact attempts to 7 per phone number per 7-day rolling period, but most collection platforms track attempts per account, not per phone number — creating systematic over-contact that violates the rule.
**Tags:** #compliance #automation #data-integration #worker-facing

## The Problem
CFPB Regulation F, effective November 2021, limits collection call attempts to 7 per phone number per 7-day rolling period, with a presumption of harassment at higher frequencies. This is a per-number limit, not a per-account or per-debtor limit. A debtor with 3 phone numbers on file has 3 separate counters. Most collection platforms track contact attempts at the account level — they count "we called this account 5 times this week" but do not track "we called phone number (555) 123-4567 exactly 4 times and phone number (555) 987-6543 exactly 1 time." Dialers that manage phone number rotation do not necessarily track cumulative attempts per number against the 7-in-7 threshold.

## Why It's Still Broken
The Reg F contact frequency rule was a new regulatory requirement that collection platforms were not designed to track at the phone-number level. Platform vendors have been slow to implement per-number tracking because it requires a schema change (contact attempts indexed by phone number, not just account ID) and integration with the dialer's call log at a granularity that many dialers do not export. Agencies that attempt manual tracking use spreadsheets that agents are supposed to update — an error-prone process that adds overhead to every call.

## What a Fix Looks Like
A contact frequency tracking module that sits between the dialer and the collection platform, indexing every contact attempt by phone number with a rolling 7-day counter. Before the dialer places a call, the module checks the target phone number's attempt count and blocks the call if it would exceed the 7-in-7 limit. The module provides real-time visibility to agents (showing remaining attempts per number) and generates compliance reports for audits documenting that no number was contacted more than 7 times in any 7-day period.

## Who Feels the Pain
Compliance officers who cannot demonstrate Reg F contact frequency compliance because their platform does not track attempts at the phone-number level, and agency principals who face $1K per violation in statutory damages plus attorney fees in private FDCPA/Reg F lawsuits.

## Impact If Fixed
Eliminates Reg F contact frequency violations that currently expose agencies to $100K-$1M in annual litigation risk. Provides audit-ready documentation of per-number contact compliance. Optimizes agent time by preventing wasted calls to numbers that have already reached the contact limit.
