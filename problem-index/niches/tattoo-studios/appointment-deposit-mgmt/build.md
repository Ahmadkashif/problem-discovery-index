# Tattoo-Specific Deposit Lifecycle Manager

**Niche:** [[niches/tattoo-studios/appointment-deposit-mgmt/profile|Appointment & Deposit Management]]
**Industry:** [[industries/tattoo-studios|Tattoo Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool models the full tattoo deposit lifecycle — collection, crediting toward session, partial forfeiture on late cancellation, rollover on reschedule, and split tracking across multi-session projects.
**Tags:** #workflow-orchestration #automation #data-integration #revenue-impact

## The Problem
Tattoo deposits are unlike any other service industry deposit. They're non-refundable but credited toward the session cost (so the client doesn't pay more — they pay early). They have studio-specific forfeiture rules: some studios forfeit 100% for any cancellation under 48 hours, others offer one free reschedule. Multi-session projects complicate things further — does the initial deposit cover all sessions, or just the first? When a 4-session back piece client cancels session 3, what happens to the original deposit? No booking tool handles this logic.

## Why Nobody Has Built This
Generic booking platforms model deposits as simple prepayments with binary refund policies. The tattoo deposit lifecycle has too many edge cases for horizontal platforms to support: partial forfeiture, rolling credit, multi-session allocation, and the common practice of collecting deposits via informal payment apps that don't integrate with booking systems. Building this requires deep understanding of how studios actually operate — which varies significantly shop to shop.

## What to Build
A deposit management system that lets studio owners configure their specific policies (forfeiture windows, reschedule limits, multi-session rules) and then automates enforcement. Deposits are collected at booking via integrated payment (card, Venmo, CashApp), tracked through the session lifecycle, and automatically credited at checkout. The system handles edge cases: late cancellation triggers forfeiture notification with studio policy cited, reschedules roll the deposit to the new date, and multi-session projects track deposit allocation per session.

## Target Customer
Studios collecting deposits manually (Venmo + spreadsheet) who lose $500-2,000/month to inconsistent enforcement, forgotten deposits, and clients disputing forfeiture because there's no documented policy trail.

## Impact If Built
Reduces deposit-related revenue leakage by 80-90%, eliminates 2-3 hours per week of manual deposit tracking, and provides a professional, dispute-proof record of every deposit transaction.
