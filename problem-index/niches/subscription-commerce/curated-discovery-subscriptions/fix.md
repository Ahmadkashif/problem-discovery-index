# A Quiz Taken Once, Before Anything Arrived

**Niche:** [[niches/subscription-commerce/curated-discovery-subscriptions/profile|Curated Discovery Subscriptions]]
**Industry:** [[industries/subscription-commerce|Subscription Commerce]]
**Type:** Fix (Pain Point)
**One-liner:** A subscriber's preferences are captured in a sign-up quiz answered before they had received anything, and every box for the next two years is selected from those answers.
**Tags:** #bayesian-inference #evaluation-metrics #confidence-intervals #descriptive-statistics #k-nearest-neighbors #worker-facing #quick-win #gradient-boosting
**Contested on:** Every serious competitor in this sub-niche is fighting to choose contents a subscriber will be pleased to receive without them having asked for anything specific — and whoever does that keeps the subscriber, because the alternative is a customer who decides they would rather choose for themselves.

## The Problem
The quiz asks about style, size, preferences and dislikes. The customer answers as best they can, guessing at categories they have no strong view on, before receiving a single item. Eight boxes later the company knows nothing more about them than it did on day one, despite having sent them forty items and observed which were kept, returned, worn, complained about or ignored. The richest preference dataset any commerce business could ask for is generated every month and discarded, and the selection still runs on the guesses.

## Why It's Still Broken
The quiz is part of the sign-up flow owned by acquisition, and updating preferences is part of the account owned by nobody. Per-item feedback is asked for in a form nobody completes, so the conclusion drawn is that customers will not give feedback rather than that the form is wrong. Returns are processed as logistics rather than as signal. And the selection rules were built against the quiz fields, so using richer signal means rebuilding them.

## What a Fix Looks Like
Update the preference from what happens. Treat every delivery as an experiment that produces evidence, and update the subscriber's preference model from what they kept, returned, rated, re-ordered or complained about — which is a continuous stream and makes the sign-up quiz merely the prior rather than the answer. Make feedback one tap per item and put it where the customer already is, which changes the response rate by an order of magnitude and is the difference between having the signal and not. Read returns as preference, since a return is the strongest possible statement about an item and is currently a warehouse event. Ask a single targeted question when the model is uncertain about something that matters, rather than a long form nobody completes. Show the subscriber what the company thinks it knows and let them correct it, which is both accurate and reassuring — a customer who sees their profile understands why the boxes are what they are. Re-ask the quiz questions that have gone stale rather than the whole thing. Report preference model confidence per subscriber, so a low-confidence subscriber gets a safer box and an exploration item rather than a risky guess. And measure box satisfaction against the model's prediction, since that is the only way the selection improves.

## Who Feels the Pain
Subscribers receiving boxes selected from answers they gave before knowing anything; merchandisers selecting from a profile they know is stale; and operators discarding the best preference data in commerce every month.

## Impact If Fixed
Forty observed items per subscriber are discarded in favour of eight guesses given on day one. One-tap per-item feedback in the place the customer already is changes the response rate by an order of magnitude, and a return is the strongest preference statement available and is processed as a warehouse event.
