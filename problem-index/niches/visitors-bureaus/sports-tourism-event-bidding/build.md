# Roster-to-Hotel Matching for Every Tournament

**Niche:** [[niches/visitors-bureaus/sports-tourism-event-bidding/profile|Sports Tourism & Event Bidding]]
**Industry:** [[industries/visitors-bureaus|Convention & Visitors Bureaus]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A tournament's true room nights could be counted by matching team rosters to hotel stays, and nobody does it systematically.
**Tags:** #k-nearest-neighbors #logistic-regression #feature-engineering #data-integration #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to prove how many room nights a tournament actually generated, and whoever counts the teams that booked outside the stay-to-play block most completely takes the account.

## The Problem
A youth volleyball tournament brings 300 teams. The housing company reports 4,000 room nights booked through stay-to-play. Teams that booked direct, used vacation rentals or stayed with relatives do not appear. The sports commission estimates the rest, or does not, and the grant and the economic impact claim rest on that figure.

## Why Nobody Has Built This
Hotels, housing companies and tournament operators each hold part of the data, and none is paid to join it. Matching names across hotel folios requires hotel cooperation and care with personal data.

## What to Build
A privacy-preserving matching service: team and roster lists from the tournament platform, matched against participating hotels' reservation records by team name, coach contact and dates, with fuzzy matching and a confidence score per match; plus a model estimating unmatched leakage from team origin, distance and rate gaps. The output is a counted figure and an estimated figure, labelled separately.

## Target Customer
Sports commission directors in cities that host recurring youth tournaments.

## Impact If Built
Grants and bids priced on counted stays, and a stronger case to rights-holders that the city delivers rooms.
