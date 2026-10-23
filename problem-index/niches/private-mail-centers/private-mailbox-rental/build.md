# Renewal Risk Read From the Box's Own Activity

**Niche:** [[niches/private-mail-centers/private-mailbox-rental/profile|Private Mailbox Rental]]
**Industry:** [[industries/private-mail-centers|Private Mail Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A box holder stops collecting, mail piles up, and the store learns they have left when the renewal goes unpaid and six months of remailing begins.
**Tags:** #survival-analysis #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to be the address a small business or household keeps for years, and whoever makes the box work as a full address (every carrier's packages accepted, arrivals visible without a trip, mail forwarded when the holder is away) keeps the renewal and takes the account.

## The Problem
Box holders drift away quietly. Pickup frequency falls, packages wait longer, the holder starts using a virtual mailbox or a new home address, and the store notices only at renewal. A lost holder also leaves an obligation: the DMM requires the store to remail their mail for at least six months after termination, at new postage.

## Why Nobody Has Built This
Stores do not record pickups as data, only rent payments, and a single store has too few departures to model. Point-of-sale vendors have not seen retention as their product.

## What to Build
Log every arrival and every pickup per box (the receiving workflow already touches both), and fit a time-to-departure model on pooled history across a vendor's or franchisor's stores: pickup gaps, package dwell time, mail volume trend, payment pattern, box size and tenure. Flag at-risk holders a few months before renewal and suggest the offer that fits the signal: scanning for a traveller, forwarding for a mover, a smaller box for a fading business.

## Target Customer
Franchisors with mailbox programmes, point-of-sale vendors, and owners of stores with several hundred boxes.

## Impact If Built
Retaining even a small share of departing holders protects recurring revenue at near-zero marginal cost and cuts the six-month remail burden (estimate).
