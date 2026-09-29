# Purchase Data Through a Generic Propensity Model

**Niche:** [[niches/retail-media-networks/offsite-audience-extension/profile|Offsite Audience Extension]]
**Industry:** [[industries/retail-media-networks|Retail Media Networks]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every network now sells offsite audiences built from purchase data, using generic propensity tooling and clean rooms that answer questions weeks after the campaign they were about has ended.
**Tags:** #gradient-boosting #matrix-decompositions #survival-analysis #evaluation-metrics #confidence-intervals #revenue-impact #time-series-forecasting #transformers
**Contested on:** Every serious competitor in this niche is fighting to turn purchase data into an offsite audience that actually performs and can be measured before the campaign ends — and whoever does that turns a commodity segment business into a measurable one.

## The Problem
A retailer has the complete purchase history of twenty million households: what they buy, how often, in what combinations, with what substitutions, at what price sensitivity, across years. They use it to build a segment called category buyers, last ninety days, exported to a demand-side platform as a list of identifiers. That segment is a recency filter over the richest consumer behavioural dataset in existence. The brand buys it because it is better than nothing, the network sells it because it is easy, and the structure that would make it genuinely valuable — the sequence, the basket, the trajectory — is discarded at the first step.

## Why Nobody Has Built This
Segment exports were the fastest route to revenue and became the product before anyone examined what was being thrown away. The demand-side platforms accept lists, so a list is what gets built, and the interface shaped the product. Measurement is weak enough that a better audience cannot demonstrate its value, which removes the incentive to build one. And clean rooms are positioned as the answer to measurement while being far too slow to inform anything.

## What to Build
Use the structure in the data. Model purchase trajectories rather than filtering on recency — the sequence of what a household buys, the intervals, the substitutions and the life-stage transitions are what predict a future purchase, and a ninety-day flag captures almost none of it. Predict the moment as well as the person, since a household's replenishment cycle says when a message will land and offsite advertising currently ignores timing entirely. Build audiences against the brand's actual objective — switching, trial, lapsed recovery, basket growth — rather than shipping a category segment for every brief, because these need different households and are currently served identically. Measure match rate honestly and report the audience the brand actually reached, which erodes substantially in transit and is usually invisible. Close the loop from offsite exposure back to in-store and online purchase, which the retailer can do and almost nobody else can, and which is the category's genuine advantage. Deliver measurement during the campaign rather than after it, which is the fix note's subject and is what makes the data actionable. Feed offsite outcomes back into audience construction, so the models improve rather than being rebuilt per brief. Price audiences on measured performance rather than on scarcity, which is the only way the good ones become distinguishable. Handle the privacy constraints as a design input rather than as a compliance step afterwards, since it determines what can be built at all. And evaluate against the brand's alternatives, since the comparison with a platform's own targeting is the purchase decision.

## Target Customer
Retail media networks selling offsite, brand media teams buying purchase-based audiences, and the clean room and identity vendors sitting between them.

## Impact If Built
A ninety-day recency filter over the richest consumer dataset in existence discards the sequence, the basket and the trajectory that actually predict purchase. Modelling trajectories and predicting the moment, then closing the loop to in-store purchase, is the advantage only the retailer has.
