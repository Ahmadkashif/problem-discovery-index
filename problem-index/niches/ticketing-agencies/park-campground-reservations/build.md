# A Fairness Audit for Campsite Release

**Niche:** [[niches/ticketing-agencies/park-campground-reservations/profile|Public Park & Campground Reservations]]
**Industry:** [[industries/ticketing-agencies|Ticketing & Reservation Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A park agency cannot say what share of its peak-season campsites go to scripts, repeat power users or resellers, so it cannot tell whether a new release rule or lottery helped.
**Tags:** #causal-inference #hypothesis-testing #gradient-boosting #monte-carlo-methods #evaluation-metrics #compliance
**Contested on:** Every serious competitor in this niche is fighting to allocate scarce campsites, permits and timed entries so that people rather than bots and cancellation scrapers get them, and whoever can show the agency the lowest share of bookings captured by automated tools takes the account.

## The Problem
When a state park changes its booking window from six months to a rolling release, adds a lottery or limits nights per account, the change is judged by complaints. The data to judge it properly exists in booking logs: request timing, account histories, cancellations and rebookings, who checked in.

## Why Nobody Has Built This
Reservation vendors are paid per transaction and judged on uptime, not allocation quality. Agencies lack analysts, and the booking data sits in the vendor's system under the agency's contract.

## What to Build
An audit service that classifies bookings by likely automation and power-user concentration from timing, account and device patterns, and estimates the share of peak sites going to first-time and occasional campers. It runs simulations and A/B tests of release rules and lottery designs before they go live, and reports to the agency each season.

## Target Customer
State parks reservation and revenue directors, and federal programme managers who oversee Recreation.gov's contract.

## Impact If Built
Agencies can choose release and lottery rules on evidence and put a measured fairness target into their next reservation contract.
