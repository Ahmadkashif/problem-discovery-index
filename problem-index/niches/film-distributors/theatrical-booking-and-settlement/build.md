# A Settlement Record Per Engagement and Per Film Buyer

**Niche:** [[niches/film-distributors/theatrical-booking-and-settlement/profile|Theatrical Booking & Settlement]]
**Industry:** [[industries/film-distributors|Film Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A distributor negotiates film rent with the same circuit buyers on every release and keeps no record of how each one settles against the terms it agreed.
**Tags:** #gradient-boosting #feature-engineering #evaluation-metrics #large-language-models #data-integration #revenue-impact #workflow-orchestration
**Contested on:** Every serious competitor in this niche is fighting to settle every engagement at the terms actually agreed within days of the run ending, and whoever settles fastest with the fewest write-downs keeps exhibitors booking its films and producers trusting its statements.

## The Problem
Terms are agreed per engagement before the film opens. When the run ends, the circuit's film buyer proposes a settlement, often below terms if the film underperformed or the holdover was weak. The booker accepts, pushes back or escalates, from memory of how that buyer behaved last time. Across hundreds of engagements a year the gap between terms and settlement is real money, and nobody measures it.

## Why Nobody Has Built This
Specialty distributors are small, exhibitor systems record only the exhibitor's side, and the large studios' in-house systems aren't for sale. Terms confirmations live in email, so the data never existed in structured form.

## What to Build
An engagement ledger populated from terms emails and exhibitor statements, read by a language model and confirmed by the booker. Each engagement records the agreed terms, reported grosses, the settlement proposed and the settlement accepted. On top sits a buyer-level history: average settlement against terms by circuit, by film type and by performance band. A model then predicts each engagement's likely settlement before the negotiation opens, so the booker knows when a proposal is out of line.

## Target Customer
Heads of theatrical sales and distribution finance at specialty and independent distributors, and the outside booking agents they hire.

## Impact If Built
Evidence in every settlement negotiation, a forecastable theatrical receipt for the CFO, and producers' statements built on settlements the distributor can defend.
