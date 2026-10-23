# Photo Identification for Breakers, Lamps and Fittings

**Niche:** [[niches/electrical-distributors/branch-counter-sales/profile|Branch Counter Sales to Contractors]]
**Industry:** [[industries/electrical-distributors|Electrical Distributors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An electrician holds up a breaker from a 1970s panel, and whether the counter gets it right depends on who is on shift.
**Tags:** #tacit-knowledge-ml #cnns #contrastive-learning #k-nearest-neighbors #large-language-models #worker-facing #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to get an electrician out of the branch with the right part during the early-morning rush, and whoever clears the 6:30 a.m. line with the fewest wrong-part return trips takes the account.

## The Problem
Old and obsolete electrical parts arrive at the counter as physical samples, photos or descriptions: a breaker with a faded label, a panel nameplate, a ballast, a lamp base, a fitting. The veteran recognises the manufacturer, era and type, knows the current or classified replacement and its limits, and knows which ones the inspector will accept. Others look it up slowly or guess.

## Why Nobody Has Built This
Manufacturer cross-reference tools cover current part numbers, not worn physical samples, and nobody has collected labelled images of what electricians bring to counters.

## What to Build
A counter app that photographs the part or label, retrieves matching items by image and text embeddings over the catalogue, manufacturer compatibility tables and IDEA attributes, and returns ranked candidates with the reason and the limits (panel models, voltage, fault rating). Each confirmation becomes a labelled example. An engineer can demo it in two weeks on public catalogue images and phone photos of common breakers and lamp bases.

## Target Customer
Branch and regional managers at chains and independents with residential and service contractor customers.

## Impact If Built
If hard lookups fall from ~5–15 minutes to under one and wrong-part return trips fall by about half (estimate), each avoided trip saves an electrician ~an hour of billable time, the line moves, and the veteran's recognition stays when they retire.
