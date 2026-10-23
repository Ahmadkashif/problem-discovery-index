# A Reissue Calculator for Net Fares

**Niche:** [[niches/travel-agencies/diaspora-vfr-agencies/profile|Diaspora & VFR Fare Agencies]]
**Industry:** [[industries/travel-agencies|Travel Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** When a family's plans change, the agent works out the change cost on a net fare by reading fare rules and calling the consolidator, while the family waits on WhatsApp.
**Tags:** #large-language-models #bert #gradient-boosting #evaluation-metrics #automation #compliance
**Contested on:** Every serious competitor in this niche is fighting to change or refund a family's net-fare ticket the day their plans change without triggering a debit memo, and whoever reissues changes fastest under the consolidator's rules takes the account.

## The Problem
A family of five bought tickets to Lagos for a wedding; a grandmother falls ill and two of them must fly a week earlier. The agent has to find the fare rules for a private net fare, work out the change penalty, fare difference and residual value, check what the consolidator allows the agency to do itself, and quote a price the family will accept. It can take hours and a phone call, and a miscalculation surfaces weeks later as a debit memo.

## Why Nobody Has Built This
Net fares are private contracts between airlines and consolidators, so their rules are not in the public fare tools agencies use, and the segment's agencies are too small for GDS vendors to court.

## What to Build
A reissue assistant for consolidator-issued tickets: it reads the ticket and the net-fare rule text, classifies the change conditions, computes the options and their total cost, flags any step that would breach the consolidator's or airline's rules, and drafts the quote in the customer's language. Historical debit memos train a risk check on each reissue before it is submitted.

## Target Customer
Consolidators, which could offer it to their agency networks, and multi-location diaspora agencies.

## Impact If Built
Changes quoted in minutes rather than hours, fewer debit memos, and the agency keeps the family that would otherwise call a competitor while waiting.
