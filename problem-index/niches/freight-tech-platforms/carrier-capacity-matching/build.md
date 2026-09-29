# Acceptance Probability Learned From Every Tender Ever Sent

**Niche:** [[niches/freight-tech-platforms/carrier-capacity-matching/profile|Carrier Capacity Matching]]
**Industry:** [[industries/freight-tech-platforms|Freight Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A brokerage has logged every load it ever offered, to whom, at what rate, and whether they took it — which is a complete record of carrier price sensitivity by lane — and covers tomorrow's loads by calling down a list.
**Tags:** #logistic-regression #gradient-boosting #graph-neural-networks #confidence-intervals #evaluation-metrics #cross-validation #revenue-impact #tacit-knowledge-ml
**Contested on:** Every serious competitor in load matching is fighting to cover a load on the first carrier contacted, at a rate that carrier will accept — and whoever holds first-tender acceptance rate highest takes the account.

## The Problem
A rep has a load from Laredo to Memphis on Thursday. She works a list: carriers who have run it before, carriers who said they liked the lane, carriers who answered last time. Most decline — wrong direction, no equipment available, rate too low, driver out of hours. It takes twenty-six calls. The brokerage's system contains every tender it has ever sent, the rate offered, and the response, across years and thousands of carriers, which is a direct observation of which carriers accept what on which lanes at which prices. It is used to populate a call log.

## Why Nobody Has Built This
Carrier sales is a relationship business and the industry's instinct has been that relationships resist modelling — which is half true and has been used to justify not trying. Digital brokerage's difficulties reinforced the view, though its matching was generally built on static carrier attributes and declared preferences rather than on observed acceptance behaviour, which is a different and much stronger signal. The data is also messy in specific ways: a decline may reflect the rate, the timing, the equipment, or that the dispatcher was busy, and the log usually does not distinguish them — which is a data capture problem with an easy fix, as the note below describes.

## What to Build
An acceptance model per carrier per lane shape, estimated from the brokerage's own tender history: probability of acceptance as a function of rate, lead time, equipment, origin and destination, and the carrier's recent activity. Carrier position matters more than anything else and is available where visibility data exists — a carrier delivering into a market tomorrow is the best candidate for freight out of it, and that is knowable rather than guessable. Output is a ranked tender list with an acceptance probability and a recommended rate per carrier, so the rep calls three carriers instead of twenty-six and knows what to offer. The rate recommendation must be honest about what it is optimising: covering at the lowest rate a carrier will accept and covering reliably are different objectives, and a brokerage that quietly optimises the first while telling carriers it is matching them well will lose the relationships the business runs on.

## Target Customer
Freight brokerages of all sizes, load boards who could offer matching rather than search, and the carrier-side dispatch services on the other end of the same calls.

## Impact If Built
Carrier sales is the largest labour line in a brokerage and most of it is spent on declines. Raising first-tender acceptance materially reduces cost per load and shortens coverage time, which is also what shippers experience as service. The carrier's side benefits too when the matching is honest: fewer irrelevant calls, and offers on lanes they actually want.
