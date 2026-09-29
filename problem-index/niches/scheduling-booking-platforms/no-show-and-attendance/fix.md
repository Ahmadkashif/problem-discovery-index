# The Deposit Setting That Is On or Off

**Niche:** [[niches/scheduling-booking-platforms/no-show-and-attendance/profile|No-Show & Attendance]]
**Industry:** [[industries/scheduling-booking-platforms|Scheduling & Booking Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Deposits are the most effective anti-no-show measure available and are configured as a single switch, so operators either add friction to every booking or forgo the lever entirely.
**Tags:** #descriptive-statistics #logistic-regression #hypothesis-testing #confidence-intervals #evaluation-metrics #revenue-impact #quick-win #automation
**Contested on:** Every serious competitor in this niche is fighting to predict which bookings will not be honoured and intervene on the ones worth intervening on — and whoever raises attendance takes the account, because the slot cannot be sold twice and the operator counts the loss every week.

## The Problem
An operator loses meaningful revenue to no-shows. The platform offers deposits. They turn it on, booking volume drops because new customers abandon at the payment step, and they turn it off again a fortnight later. They now have neither the deposits nor the data to know whether it was working — the drop in bookings was visible immediately and the improvement in attendance was not measured at all. Both outcomes were recorded by the platform and neither was reported.

## Why It's Still Broken
Deposit collection was built as a payments feature with a boolean, because that is the simplest thing to ship and because differentiating by customer requires knowing something about the customer. Vendors do not report the attendance effect of the setting, so operators evaluate it on the one number they can see — bookings — which is the one that moves against it. And there is a genuine reluctance to charge regular customers a deposit, which is correct and is exactly what a differentiated policy would avoid.

## What a Fix Looks Like
Make the deposit conditional and measure it. Condition on what is already known without any modelling: first-time customers, bookings made far ahead, customers with a prior no-show, high-value services, and peak slots — a rules-based policy an operator can understand, agree with and explain to a customer, which matters because they will be asked. Exempt returning customers in good standing explicitly, which removes the objection operators actually have. Report both sides of the trade in the same place: bookings abandoned at the payment step against no-shows avoided, in money, over the same period — which is a straightforward calculation from data the platform holds and is the report that would let anyone evaluate the feature at all. Offer alternatives with lower friction for the middle of the distribution: card-on-file with a stated policy, or a confirmation that requires a tap, both of which recover part of the effect at a fraction of the abandonment. And let the policy be tried on a sample rather than the whole book, so the operator learns before committing.

## Who Feels the Pain
Operators losing recoverable revenue because the only available lever is too blunt to use; customers asked for a deposit at a business they have visited for years; and vendors whose most effective feature is switched off nearly everywhere.

## Impact If Fixed
A rules-based conditional deposit needs no model and addresses the operator's actual objection, and the two-sided report is a calculation over existing data that nobody produces. Both are small changes to a feature that is currently abandoned after a fortnight almost everywhere it is tried.
