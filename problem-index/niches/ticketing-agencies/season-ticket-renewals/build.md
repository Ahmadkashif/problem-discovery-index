# Renewal Risk From Scans and Resale Behaviour

**Niche:** [[niches/ticketing-agencies/season-ticket-renewals/profile|Season-Ticket & Membership Ticketing]]
**Industry:** [[industries/ticketing-agencies|Ticketing & Reservation Agencies]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every season-ticket account leaves a game-by-game trail of scans, transfers and resales that predicts non-renewal months ahead, and most teams score renewal risk only when the invoice goes out.
**Tags:** #survival-analysis #gradient-boosting #logistic-regression #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this sub-niche is fighting to tell a team which season-ticket members will not renew while there is still time to save them, and whoever's renewal forecast holds up at the renewal deadline takes the account.

## The Problem
A team's service reps each carry a book of several hundred season-ticket accounts (estimate). They learn who is unhappy when the renewal invoice goes unpaid. By then the member has decided. Earlier signals are logged but unused: how many games the account scanned, how often it transferred tickets to friends, how many seats it listed on resale and at what price, and whether the team lost.

## Why Nobody Has Built This
Scan data sits with the ticketer, resale data partly with marketplaces, and renewal outcomes in the team's CRM. Each vendor builds a dashboard for its own slice. Teams' analytics staff are small, and season-ticket bases are a few thousand to tens of thousands of accounts, small enough that models need pooling across seasons.

## What to Build
A time-to-churn model per account, refreshed after every home game, that combines attendance, transfer and resale behaviour, seat location and price changes, tenure and on-field results. Each rep gets a ranked weekly list with the reason each account is at risk and the save actions that worked for similar accounts before.

## Target Customer
VPs of ticketing and retention at major-league and minor-league teams; college ticket offices facing rising seat-donation requirements.

## Impact If Built
A few points of renewal rate on a base of 10,000 accounts is worth millions in ticket revenue a season (estimate), and reps spend their calls on accounts that can still be saved.
