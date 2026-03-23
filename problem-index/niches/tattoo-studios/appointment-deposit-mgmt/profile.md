# Appointment & Deposit Management

**Parent Industry:** [[industries/tattoo-studios|Tattoo Studios]]
**Category:** Highly Automatable

## Profile
**Market Size:** Cross-segment (applies to all tattoo studios)
**Share of Parent Industry:** Cross-cutting operational function
**Digital Adoption:** Medium — Some studios use generic booking tools, but tattoo-specific deposit logic (non-refundable, credited toward session, forfeited on no-show) is handled manually.
**Target Buyer:** Any studio owner or artist losing revenue to no-shows and last-minute cancellations
**Automation Potential:** High — Deposit collection, reminder sequences, no-show enforcement, and waitlist management are all rule-based and automatable.

## What Makes This a Distinct Niche
No-shows are the tattoo industry's biggest single operational problem, with rates running 15-25% at studios that don't collect deposits and 5-10% at those that do. But deposit management in tattooing is unique: deposits are typically non-refundable, credited toward the session cost (not an add-on fee), subject to rescheduling policies that vary by studio and by deposit amount, and frequently collected via informal channels (Venmo, CashApp) with no connection to the booking system. The rules around deposits — when to charge, how much, what happens on cancellation, how to handle partial forfeiture — are studio-specific and complex enough that generic booking tools can't model them.

## Current Tools & Gaps
Studios that collect deposits do so through Venmo/CashApp with manual tracking in spreadsheets or notebooks. Generic booking tools (Vagaro, Square) support pre-payments but don't model the tattoo-specific deposit lifecycle: partial forfeiture on late cancellation, rollover to rescheduled date, split deposits across multi-session projects, or studio-specific grace period policies. The deposit and the booking live in separate systems.

## Problems
- [[niches/tattoo-studios/appointment-deposit-mgmt/build|🔨 Build: Tattoo-Specific Deposit Lifecycle Manager]]
- [[niches/tattoo-studios/appointment-deposit-mgmt/buy|🛒 Buy: Automated Reminder & Waitlist System]]
- [[niches/tattoo-studios/appointment-deposit-mgmt/fix|🔧 Fix: No-Show Revenue Leakage]]
