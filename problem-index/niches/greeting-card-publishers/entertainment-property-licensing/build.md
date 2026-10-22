# Property Demand Forecast for Minimum-Guarantee Bids

**Niche:** [[niches/greeting-card-publishers/entertainment-property-licensing/profile|Entertainment Property Licensing & Approvals]]
**Industry:** [[industries/greeting-card-publishers|Greeting Card Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A licensing VP commits a minimum guarantee on a character property a year before the cards ship, judging from release slates and buzz, with no forecast of what the property will sell on a card rack when it gets there.
**Tags:** #gradient-boosting #time-series-forecasting #survival-analysis #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to bid minimum guarantees on the film, TV, game and character properties that will still be selling when the cards reach the shelf a year later, and to get licensor approvals through inside the print window, and whoever picks and clears properties best takes the licensed pockets.

## The Problem
Licensed cards are concentrated in a few pockets where children choose: kids' birthday, Valentine's classroom packs, party-adjacent designs. A property that peaks with a film release can be dead by the time the card ships, while an evergreen character sells for years. Minimum guarantees are owed regardless, so an overbid is a direct loss.

## Why Nobody Has Built This
The data is scattered: the publisher's own sales of past licensed cards, public signals (release dates, streaming charts, search interest, toy sales rankings), and the licensor's own figures, which it shares selectively. Few publishers bid on many properties, so the problem looks too small to model.

## What to Build
A property demand model trained on the publisher's past licensed card sales by property age and type (film franchise, preschool series, toy-led, game-led), joined to public attention signals, that predicts sell-through at the planned shelf date and the probability of meeting the minimum guarantee. It recommends bid ceilings and flags properties whose attention curves look like fads.

## Target Customer
VPs of licensing at card, gift wrap and party publishers bidding on several properties a year.

## Impact If Built
Fewer guarantees that never earn out and a portfolio tilted towards properties that last, measured against each season's actual results.
