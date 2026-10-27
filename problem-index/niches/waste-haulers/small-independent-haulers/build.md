# A Collections Queue Ranked by Who Will Pay Late

**Niche:** [[niches/waste-haulers/small-independent-haulers/profile|Small Independent Haulers]]
**Industry:** [[industries/waste-haulers|Waste Haulers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A small hauler's owner chases overdue accounts in whatever order they come to mind, while the billing history already shows which customers will pay late and which will pay once reminded.
**Tags:** #logistic-regression #gradient-boosting #survival-analysis #automation #revenue-impact #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to run a 2–20 truck hauler's billing and payment collection, and whoever gets the owner's days sales outstanding lowest takes the account.

## The Problem
Service runs before it is paid for. A few hundred households and businesses fall behind each quarter, some because they forgot, some because they are short of cash, some because they have quietly moved. The owner or office manager works through an aging report in the evening, calling and texting whoever is at the top of the list. The accounts that would pay after one reminder get the same attention as the ones that will never pay, and the extras billed late from paper notes push both groups further behind.

## Why Nobody Has Built This
Hauler billing packages stop at invoices and aging reports. Collections and payment-risk tools are priced and designed for utilities, lenders and enterprise receivables teams, and a small hauler's book of a few thousand accounts looks too small to model.

## What to Build
A payment-behaviour model trained across many small haulers' billing histories (invoice timing, payment method, past lateness, seasonality, service changes, extras) that ranks each overdue account by likelihood of paying and by response to a reminder. Each morning it produces a short queue: who gets an automatic text with a pay link, who gets an owner's call, who is offered autopay, and who meets the suspension rule. Extras logged on the driver's tablet are invoiced the same day with the same pay link.

## Target Customer
Owners of 2–20 truck haulers, sold inside or alongside their billing package.

## Impact If Built
Cutting days sales outstanding from ~45 to ~30 days (estimate) frees about two weeks of revenue in cash, ~$60K for a hauler billing $1.5M a year, and gives the owner back the evenings spent on an unranked aging report.
