# Bordereaux That Arrive in Forty Layouts

**Niche:** [[niches/reinsurers/programme-quota-share-oversight/profile|MGA & Programme Quota Share Oversight]]
**Industry:** [[industries/reinsurers|Reinsurers]]
**Type:** Fix (Pain Point)
**One-liner:** Every MGA sends its bordereau in its own layout, so the reinsurer's analysts spend their month mapping columns instead of reading the business.
**Tags:** #large-language-models #feature-engineering #data-integration #automation #quick-win #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to see a delegated-authority programme's underwriting drift in its monthly bordereaux before the loss ratio shows it, and whoever detects drift early enough to reprice or exit at the next renewal takes the account.

## The Problem
Column names, class codes and date conventions differ by MGA and change without notice. Analysts remap each file monthly, and a silent layout change can hide a shift in the business for a quarter.

## Why It's Still Broken
Reinsurers lack the leverage to impose a template on MGAs whose fronting carrier sits between them, and mapping work is spread thin across underwriting assistants.

## What a Fix Looks Like
Language-model mapping of each incoming bordereau to a standard schema, using the previous month's confirmed mapping, with only new or changed columns sent for confirmation and every layout change logged.

## Who Feels the Pain
Programme analysts and underwriting assistants; underwriters who need the numbers for renewal; finance teams booking ceded premium.

## Impact If Fixed
Mapping drops from days to minutes per bordereau, and layout changes stop hiding business changes.
