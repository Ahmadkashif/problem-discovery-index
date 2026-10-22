# A Carry-Over Projection That Updates Through the Season

**Niche:** [[niches/community-banks/agricultural-lending/profile|Agricultural Lending]]
**Industry:** [[industries/community-banks|Community Banks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An ag lender projects a farm's year once, at renewal, and learns whether it worked at harvest, when the options for a short year have already closed.
**Tags:** #monte-carlo-methods #time-series-forecasting #bayesian-inference #gradient-boosting #tacit-knowledge-ml #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn a farm borrower's year (acres, yields, contracts, input costs, crop insurance and government payments) into a projected carry-over before the operating line renews, and whoever updates that projection mid-season most reliably takes the account.

## The Problem
A grain operator borrows a seven-figure operating line in February. The lender's projection assumes average yields and a price from the futures curve at the time. By July a dry spell has cut expected yields, prices have moved, the operator has forward-contracted part of the crop, and crop insurance guarantees set a floor. None of it reaches the bank until harvest settlements arrive. A lender carrying ~fifty farm relationships (estimate) cannot rebuild fifty projections in August.

## Why Nobody Has Built This
Farm financial software is built for the farmer's accounting, not the lender's portfolio; ag lending is a small vertical for lending platforms; and the inputs (contract positions, insurance elections, actual acres planted) sit with the farmer, the elevator and the insurance agent.

## What to Build
A portfolio projection that starts from the renewal plan and updates as the season unfolds: county yield estimates and crop condition reports, futures prices, the operator's reported contract and hedge positions, crop insurance guarantees by unit, and programme payment estimates. Monte Carlo over yield and price gives each borrower a probability of a carry-over and its size; the lender sees which operations need a conversation in August rather than December. The senior ag lender's annotations of which operators manage risk well become a prior on the projection.

## Target Customer
Senior ag lenders and chief credit officers at rural community banks with agricultural loans above a quarter of the book.

## Impact If Built
Earlier restructuring of short years, better-timed collateral reviews, and an ag book the board and examiner can see in-season rather than after harvest.
