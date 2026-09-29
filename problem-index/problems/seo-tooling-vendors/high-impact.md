# Rank Stopped Being a Proxy for Anything

**Industry:** [[seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** High Impact
**One-liner:** The entire measurement stack reports position in a list of links, at a moment when the answer sits above the list, is generated fresh each time, and cites whoever it cites.
**Tags:** #large-language-models #bert #causal-inference #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #monte-carlo-methods

## The Problem
A search results page that once returned ten links now frequently returns a generated answer occupying the first screen, with citations, above a set of links that a minority of sessions reach. For informational queries the click is often unnecessary: the answer was the point, and the searcher has it. Publishers and brands across categories have reported substantial organic traffic declines on queries where their rankings did not move at all.

Rank tracking still works perfectly. It reports position three, accurately, for a query whose position three now sits below the fold beneath something that answered the question. The number is correct and has stopped corresponding to the thing the customer is paying to influence.

Measuring the replacement is genuinely hard in a way ranking never was. Generated answers are non-deterministic — the same prompt returns different text and different citations on different runs. They are personalised by account, history, location and device. They are produced by several systems at once: Google's AI Overviews and AI Mode, ChatGPT's search, Perplexity, Copilot, and whatever assistant is embedded in the customer's own market. None offers an API for measurement, and several forbid automated querying in their terms. And the query itself has changed shape — people ask assistants long conversational questions, so the keyword list a decade of tooling is organised around no longer describes the input.

The current answer from the vendor layer is a tab that samples a few thousand prompts on a schedule and counts brand mentions. That produces a number that moves, which customers buy, and whose relationship to reality has not been established by anyone.

## Why It's Unsolved
There is no ground truth available. With ten blue links, position was observable and near-deterministic, so a crawler could measure it and everyone agreed on the measurement. With generated answers there is no canonical result to observe: there is a distribution over outputs, conditioned on a user context the measurer does not have, from a model that changes without notice. Any measurement is a sample from a distribution whose shape is unknown and whose conditioning variables are unobservable.

The sampling problem compounds. Which prompts should be sampled, in what proportion, from what population of users, to represent a brand's actual exposure? That requires knowing what people actually ask assistants about a category, and no vendor has that distribution — the assistants do, and will not share it.

Access is adversarial. Automated querying of these interfaces is rate-limited and contested, and building a business on scraping systems whose operators object is a fragile foundation that also sits on unsettled legal ground.

And the causal question is worse than before. Under the old model, an SEO could at least correlate a change they made with a ranking movement. Under the new one, whether a brand is cited in a generated answer depends on training data, retrieval, and a model's synthesis behaviour, and the lag between publishing something and any of that changing is unknown and probably long.

## What a Solution Looks Like
Measure it as a distribution and say so. Repeated sampling across prompt variants, contexts and time produces an inclusion rate with an interval, not a position. A vendor that reports *cited in 34% of sampled answers for this question cluster, interval 28-41, from 400 samples across 6 phrasings* is telling the truth; one that reports a visibility score of 61 is not. The measurement design — how many samples, across what variation, with what stability over time — is the actual product and the thing nobody has published.

Build the prompt population properly rather than from the keyword list. What people ask an assistant is a different distribution from what they type into a search box, and it can be approximated from conversational query data where available, from customer support and site search logs, from community question corpora, and from the customer's own audience. Organising visibility around question clusters rather than keywords is the structural change the category has not made.

Treat the citation decision as something to model, not just to count. Which sources get cited is a function of observable properties — how directly the page answers the question, its structure, whether the claim is stated plainly and attributably, corroboration across sources, entity clarity. Modelling that is what turns a monitoring product into an actionable one, and the training data is the vendor's own crawl plus the sampled answers.

And keep the old surface honestly. Links have not disappeared and transactional queries still convert; the useful version reports the two surfaces separately with their actual contribution, rather than blending them into one score that hides which half moved.

## Impact If Solved
The category's core metric has been deprecated by the market it serves, and the first vendor with a defensible measurement of generative visibility defines how an entire industry reports its results — the position rank tracking held for fifteen years. The customer's need is acute and immediate: marketing leaders are being asked why organic traffic fell and have no instrument that explains it. And the modelling of what gets cited is the first genuinely new thing this category could sell since the backlink index.
