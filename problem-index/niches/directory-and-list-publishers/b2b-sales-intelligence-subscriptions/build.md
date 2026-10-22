# Two Products Sold Under One Seat

**Niche:** [[niches/directory-and-list-publishers/b2b-sales-intelligence-subscriptions/profile|B2B Sales Intelligence Subscriptions]]
**Industry:** [[industries/directory-and-list-publishers|Directory & List Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A sales intelligence subscription bundles a contact product and an account-universe product, and nobody measures either on the customer's own territory, so neither the vendor nor the buyer knows which half is failing.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #feature-engineering #data-integration #revenue-impact
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every serious competitor is fighting to be the database a revenue team works from — but sales development teams buy the contact that connects this week, while marketing and revenue operations buy the complete, correctly sized universe of accounts they target and carve into territories, and those are two contests with different winners. Decomposed into contested sub-niches below.

## The Problem
A mid-market software company buys seats on a B2B data platform for its sales development team and its marketing operations team. The SDR manager sees connect rates falling and blames the data; the marketing operations lead finds hundreds of duplicate and defunct accounts in the last territory build and blames the data too. They are describing different failures in different products, but the vendor reports one number — database size — and the renewal is negotiated as one thing.

## Why Nobody Has Built This
Vendors have little incentive to publish measures that could show half their product underperforming in a customer's segment. Buyers lack the outcome data in one place: dial outcomes sit in the dialer, bounces in the email platform, dead accounts in the CRM's lost-reason fields.

## What to Build
A measurement layer that joins the customer's own outcomes back to the vendor records they came from and reports two separate scorecards on the customer's territory: reachability (connects to the named person, deliverable emails, by seniority and industry) and universe correctness (dead, duplicate and mis-banded accounts found in a sample, with confidence intervals). It runs continuously, so a vendor can show improvement and a buyer can compare vendors on a trial.

## Target Customer
Revenue operations leaders at companies spending six figures a year on contact and company data, and the vendors who want an honest renewal argument.

## Impact If Built
Renewals and vendor bake-offs get decided on measured performance in the buyer's own market, and vendors learn which half of their product is losing the account.
