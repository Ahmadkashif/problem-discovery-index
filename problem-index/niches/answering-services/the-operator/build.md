# Practice Calls for Every Account Before the First Live One

**Niche:** [[niches/answering-services/the-operator/profile|The Answering Service Operator]]
**Industry:** [[industries/answering-services|Telephone Answering Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** New operators learn each client's rules on live callers, at night, with real stakes; a simulator that plays realistic callers for each account would let them make their mistakes on practice calls.
**Tags:** #large-language-models #transformers #evaluation-metrics #worker-facing #tacit-knowledge-ml #automation
**Contested on:** Every serious competitor in this niche is fighting to make an operator two weeks out of training handle any of hundreds of client accounts correctly on the first call, and whoever gets new operators account-accurate fastest takes the account.

## The Problem
Training covers the platform and call etiquette. The accounts (which pediatric group pages for what, which contractor's emergency rule uses outdoor temperature, how the funeral home wants first calls taken) are learned when the call comes in. The first time an operator meets a hard call on an account is a real caller.

## Why Nobody Has Built This
Building realistic practice calls for hundreds of accounts by hand is impossible, and generic contact-centre simulators use a few standard scenarios. Voice models capable of playing a convincing frightened parent or angry tenant are recent.

## What to Build
A voice simulator that generates practice callers from each account's rule table and from anonymised patterns of real hard calls. It plays them to the trainee, scores the trainee's questions and disposition against the rules and against what experienced operators did, and certifies the operator per account or per vertical before live routing. Supervisors assign drills on the accounts a trainee will be routed to that week.

## Target Customer
Training and operations managers at answering services with 20+ operators and high turnover.

## Impact If Built
Time to account-accurate shrinks, first-month errors on live callers fall, and the experienced operators' handling of hard calls becomes training material instead of folklore.
