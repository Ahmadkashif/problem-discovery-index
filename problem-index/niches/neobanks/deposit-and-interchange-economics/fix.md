# The Direct Deposit That Never Started

**Niche:** [[niches/neobanks/deposit-and-interchange-economics/profile|Deposit & Interchange Economics]]
**Industry:** [[industries/neobanks|Neobanks]]
**Type:** Fix (Pain Point)
**One-liner:** The customer intended to move their pay across, could not find the right form in their employer's portal, put it off, and the account went dormant.
**Tags:** #workflow-orchestration #automation #evaluation-metrics #descriptive-statistics #quick-win #revenue-impact #data-integration #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to become the account a customer's wages arrive into rather than the card they use occasionally — and whoever does that earns from a relationship instead of from a transaction.

## The Problem
A customer opens an account intending to make it their main one. To do that they must change their direct deposit, which means finding the payroll portal, locating the right screen, entering a routing and account number they have to go and find, sometimes printing and submitting a form, and possibly waiting a pay cycle to confirm it worked. Most people attempt this once, get interrupted, and never return to it. The account receives a small funding transfer, a few card purchases, and then nothing. The single most valuable action in the customer lifecycle is an administrative errand at a third party, and the institution's contribution is a screen showing the account number.

## Why It's Still Broken
The action happens outside the institution's product, at an employer's system it does not control, which makes it feel like the customer's problem — the ownership ends at the boundary and so does the effort. Switching services exist and are used inconsistently. Nobody measures the abandonment rate of the setup attempt. And the customer who gave up does not complain, they simply stop using the account.

## What a Fix Looks Like
Own the errand. Integrate with payroll providers to change the deposit directly where possible, which is the fix and removes the errand entirely for the large share of customers whose employers use a major provider. Use the available switching mechanisms for the rest, rather than showing an account number and wishing the customer luck. Instrument the attempt so the abandonment is visible, since the institution currently cannot see who tried and stopped and this is the most valuable funnel in the business. Prompt at the right moment, which is when the customer is engaged rather than on a fixed schedule after signup. Prefill everything the institution knows and reduce what the customer must find. Confirm success by detecting the arriving deposit and telling the customer, which closes the loop and is currently left to them to notice. Follow up specifically on the customers who started and stopped, since they declared intent and are the highest-return audience the institution has. Offer partial switching, because a customer who will move some of their pay is a real outcome and the all-or-nothing framing loses them. Support the employers who use small or paper-based payroll, which is a substantial minority and is currently unsupported entirely. And report attempt and completion rates, because the single most valuable action in the business is currently unmeasured.

## Who Feels the Pain
Customers who meant to switch and did not; institutions whose most valuable customers were lost to a portal; and growth teams whose acquisition spend produces dormant accounts.

## Impact If Fixed
Ownership ends at the product boundary and so does the effort, leaving the business's most valuable action as an errand at a third party. Payroll integration removes it for a large share of customers, and instrumenting the attempt makes the most valuable funnel in the business visible for the first time.
