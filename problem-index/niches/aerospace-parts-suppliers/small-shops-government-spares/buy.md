# Bid-Board Tools That Learn the Shop's Win Rate

**Niche:** [[niches/aerospace-parts-suppliers/small-shops-government-spares/profile|Small Shops Bidding Government Spare Parts]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Bid-board tools surface solicitations and past awards; they don't learn from the shop's own wins and losses which items and prices it actually wins.
**Tags:** #logistic-regression #gradient-boosting #feature-engineering #evaluation-metrics #revenue-impact #automation
**Contested on:** Every serious competitor in this niche is fighting to put a small AS9100 shop's quotes on the government solicitations it can actually win, and whoever lifts the shop's awards per quote submitted takes the account.

## The Problem
Shops subscribe to a tool that alerts them to solicitations and shows award history. They still quote by gut feel, and a lost quote leaves no lesson because nobody records the winning price against their own.

## What Already Exists
SalesPatriot, SAM Search, BidPulsar, Starbridge, Cleat.ai and HigherGov provide solicitation search, AI summaries and award history. SalesPatriot cites a 283% bid-volume increase at its customer Echelon Supply & Service (vendor figure).

## The Customization Gap
A win-rate layer that records every quote and its outcome, pulls the award price and winner, models win probability by NSN family, quantity, set-aside and price relative to history, and feeds that back into which items to quote and at what price. It should also bring in the shop's job actuals so a winning price is checked against cost before the quote goes out.

## Target Customer
Shops already subscribed to a bid-board tool that want it to raise awards, not just alerts.

## Impact If Solved
Quoting fewer, better-chosen items at prices calibrated to award history could lift awards per quote from ~1 in 10 to ~1 in 5 (estimate).
