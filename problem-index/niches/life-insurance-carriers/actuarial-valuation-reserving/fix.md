# Assumption Tables With No Version History

**Niche:** [[niches/life-insurance-carriers/actuarial-valuation-reserving/profile|Actuarial Valuation, Reserving & Quarter Close]]
**Industry:** [[industries/life-insurance-carriers|Life Insurance Carriers]]
**Type:** Fix (Pain Point)
**One-liner:** Mortality, lapse and expense tables are copied between pricing, valuation and reinsurance models as files, and nobody can say for certain which version produced last quarter's reserve.
**Tags:** #data-integration #descriptive-statistics #compliance #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to close each quarter's statutory, principle-based and LDTI reserves on the filing calendar with every movement attributed to a driver the auditor accepts, and whoever delivers an attributed close with the fewest overnight reruns takes the account.

## The Problem
An assumption update approved by the committee is loaded into one model and missed in another. An analyst fixes a typo in a lapse table and saves over the file. LDTI makes every assumption change an income-statement item that auditors trace, and PBR requires documented margins on each one, yet the tables live in shared drives.

## Why It's Still Broken
Each projection engine stores assumptions its own way, and governance has grown up as a committee process, not a data system. Building a repository is nobody's budget line until an audit finding makes it one.

## What a Fix Looks Like
One governed repository of assumption tables with versions, approvals, the experience study behind each change and the models that consume it. Loads into every engine come from the repository, and a check before each run confirms the expected versions.

## Who Feels the Pain
Valuation actuaries reconstructing what changed; assumption committees; auditors; appointed actuaries signing opinions.

## Impact If Fixed
Assumption errors are caught before runs rather than after filings, and the audit trail for every reserve change exists without a scramble.
