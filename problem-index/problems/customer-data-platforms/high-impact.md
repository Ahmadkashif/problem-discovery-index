# Identity Resolution Is a Guess Nobody Measures

**Industry:** [[customer-data-platforms|Customer Data Platforms]]
**Type:** High Impact
**One-liner:** Every downstream use of customer data depends on deciding which records are the same person, that decision is probabilistic, and essentially no organisation has measured how often it is wrong or in which direction.
**Tags:** #bayesian-inference #graph-neural-networks #confidence-intervals #gradient-boosting #hypothesis-testing #evaluation-metrics #compliance #k-nearest-neighbors

## The Problem
A customer data platform receives records from many systems: web events with a cookie, app events with a device identifier, orders with an email and a shipping address, loyalty transactions with a card number, support tickets with a phone number, in-store purchases with a partial card token. It must decide which of these belong to the same person.

Deterministic matching on a shared identifier is safe and covers a fraction of the records. The rest is probabilistic — name and address similarity, device and household co-occurrence, temporal patterns, email variants — with a threshold above which records merge. That threshold was set during implementation, often by a vendor's default, and has usually never been revisited.

Both errors are consequential. Over-merging combines two people, which is common in households, at shared devices, with family email accounts, and with common names. The result is one person's purchase history shaping another's recommendations and communications, one person's suppression preference not applying to the other, and in the clearest failure, one person seeing another's order history in an account page fed from the unified profile. Under-merging splits one person into several profiles, which breaks the suppression that a deletion request or an unsubscribe was supposed to apply, double-counts customers in every metric that uses a customer denominator, understates lifetime value, and sends welcome campaigns to people who have been customers for six years.

Nobody knows their rates. There is no dashboard showing merge precision, no alert when a configuration change alters the graph, and no labelled sample to check against. Organisations discover the problem through anecdote — a complaint, an executive who received someone else's recommendations, an auditor's question — and respond by nudging a threshold.

## Why It's Unsolved
There is no ground truth. Knowing whether two records are the same person requires knowing the answer independently, and the whole point of the system is that nobody does. Building a labelled set means manual adjudication of ambiguous pairs by people who can see enough identifying data to decide — which is itself a privacy-sensitive activity requiring controls that most organisations have not thought about.

The evaluation is also genuinely subtle. Precision and recall on random pairs are meaningless because almost all random pairs are non-matches; the interesting performance is entirely in the ambiguous region near the threshold, and sampling that region properly requires deliberate stratified design rather than a random draw.

Incentives do not help. A vendor selling identity resolution has little reason to publish its error rate, and a buyer evaluating vendors has no way to compare them, so the market competes on match rate — the proportion of records merged — which is precisely the metric that improves as over-merging increases. The industry has standardised on a number that rewards the more dangerous error.

And the consequences are asymmetric in a way nobody has priced. An over-merge can be a privacy incident; an under-merge is a marketing inefficiency and a failed deletion. Those are not the same kind of cost and should not be traded at a threshold that treats them symmetrically, which is what a single cut-off does.

## What a Solution Looks Like
Build the evaluation set deliberately. Stratified sampling across the score distribution, concentrated in the ambiguous band, adjudicated under controlled access with a documented rubric for the genuinely hard cases — shared households, a person with two emails, a returned order shipped to a friend. A few thousand adjudicated pairs is enough to estimate error rates with useful precision, and it is a one-off cost that no organisation has paid.

Report both errors separately and continuously. Merge precision and split rate, by segment and by identifier type, tracked over time so a configuration change or an upstream data change is visible immediately rather than after a complaint.

Make the threshold a decision about costs rather than a default. If an over-merge carries privacy exposure and an under-merge carries marketing inefficiency, the operating point should follow from those costs, and it should differ by use: an advertising audience can tolerate a looser merge than a page that displays order history, and most systems apply one graph to both. Use-specific confidence requirements are the practical fix and almost nobody implements them.

Carry confidence downstream. A profile assembled from a marginal merge should be usable for a lookalike audience and refused for anything that exposes personal data back to a user. That requires the match confidence to survive into the activation layer instead of being discarded at the graph boundary, which is a plumbing change with a large safety payoff.

## Impact If Solved
Every personalisation decision, every suppression, every customer count and every privacy request fulfilment rests on this graph, and its error rate is currently unknown at nearly every organisation running one. Measuring it converts a latent and occasionally serious risk into a managed one, lets the merge-versus-split trade be chosen deliberately per use rather than inherited from a default, and gives the category the first honest basis for comparison it has ever had — in a market that currently competes on the metric most improved by the worse error.
