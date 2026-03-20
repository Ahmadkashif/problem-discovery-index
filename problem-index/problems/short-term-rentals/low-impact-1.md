# Guest Screening and Problem Booking Detection

**Industry:** [[short-term-rentals|Short-Term Rentals]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic identity verification tools confirm who a guest is, but don't predict which bookings are likely to result in parties, property damage, or rule violations — the behavioral signals in the booking pattern and communication that experienced hosts recognize before check-in.
**Tags:** #gradient-boosting #logistic-regression #word-embeddings #feature-engineering #cross-validation #evaluation-metrics #conditional-probability-and-bayes-theorem #automation

## The Problem

STR hosts lose significant revenue and bear repair costs from problem guests: house parties that damage property and generate neighbor complaints, guests who smoke inside, leave excessive damage beyond the security deposit, or invite unauthorized guests. Airbnb's review system provides backward-looking signals only — a guest with zero reviews is either a first-time guest or someone who created a new account after previous issues.

Experienced hosts recognize risk patterns in bookings: same-day bookings for weekend nights with no prior reviews; bookings for properties near the host's home address that mention "a few friends"; guests whose first message asks about "local nightlife." These patterns are probabilistic, not deterministic, but accumulate into meaningful risk signals.

## What Already Exists

Superhog, Autohost, and Safely provide STR guest verification and screening services. These services confirm identity but don't predict problematic behavior from booking pattern signals.

## The Customisation Gap

A problem booking detection tool needs: (1) booking features — lead time, day of week, guest review history, group size vs. property capacity, message content (NLP on the initial inquiry); (2) property features — property type (house vs. apartment, proximity to nightlife), local event calendar overlap; (3) a binary classification model trained on outcomes (party/damage event vs. normal stay) from the host's or a consortium's booking history. The NLP on guest inquiry language is the differentiating signal — guests who ask "how close are you to downtown?" vs. "what are the quiet hours?" send different signals.

## Impact If Solved

Reducing problem bookings by 20-30% on a portfolio of 20 properties at one incident per 6 months per property saves $15,000-$30,000 in damage costs and host time annually. More importantly, it protects the property's review rating — the single most important revenue driver in STR.
