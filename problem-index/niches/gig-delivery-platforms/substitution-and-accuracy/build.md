# Build: Preference-Learned Substitution from Order History

**Niche:** [[niches/gig-delivery-platforms/substitution-and-accuracy/profile|Substitution & Order Accuracy]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Rank substitutions by what this customer has actually accepted before, across their own history and the history of customers like them, instead of by catalogue similarity.
**Tags:** #matrix-decompositions #gradient-boosting #word-embeddings #evaluation-metrics #confidence-intervals #k-nearest-neighbors #automation #worker-facing
**Contested on:** Whether an individual customer's substitution tolerance can be learned well enough to rank alternatives in an aisle.

## The Problem

The substitution list a shopper sees is built from catalogue relationships: same category, similar size, similar price. It knows that oat milk and almond milk are both milk alternatives. It does not know that this customer has rejected almond milk twice, that they accept a larger size at a higher price without complaint, that they have never once accepted a store brand, or that for this particular item they would rather have nothing than the wrong thing.

All of that is in the platform's own record. Every past substitution, whether the customer approved it in chat, whether they refunded it, whether they rated it down, and what they reordered afterwards. The signal is dense — a regular grocery customer generates dozens of these events a year — and it is not consulted at the moment it would matter.

## Why Nobody Has Built This

Substitution has been treated as a catalogue problem rather than a preference problem, and it sits with the merchandising or catalogue team rather than with the personalisation team. That organisational placement explains most of it.

The technical obstacle is the labels, and it is real. An approved substitution in chat is a clean positive. A silent acceptance is ambiguous — the customer may not have noticed, or may have been unwilling to complain. A refund is a clean negative. A low rating is a negative attached to the whole order rather than to the item. Building a usable preference signal from this mix requires deciding carefully what each event means, and it is easy to train a model that learns customer complaint propensity rather than substitution acceptability.

And the cold start is structural: the customers most affected by bad substitutions are often infrequent shoppers with thin histories.

## What to Build

A substitution ranker that combines the customer's own history, the population's behaviour on that specific item pair, and the shopper's judgement.

Start from the item-pair level, which is where the strongest signal is and which requires no personalisation at all. Across all customers, for each out-of-stock item, which substitutions were accepted, refunded or complained about — an acceptance rate per ordered-item-to-substitute-item pair, with volume-weighted confidence. This alone is a large improvement over catalogue similarity and is a group-by over the substitution log.

Add the customer's own history as an update on that prior. Brand loyalty, size tolerance, price tolerance, store-brand acceptance, dietary constraints inferable from their basket, and their specific past reactions to substitutions in the same category. Collaborative structure fills in for thin histories — customers whose baskets resemble this one behave similarly on substitutions.

Model refusal explicitly. For some item-customer pairs the right answer is no substitution, and a ranker that always produces a top choice will produce bad ones. Predicting "this customer would rather have a refund" is a distinct and valuable output, and it is the one that prevents the worst outcomes.

Handle unreachability as the normal case rather than the exception. The current design assumes chat resolves ambiguity; in practice a large share of customers do not respond within the window. The ranker's job is to be right when nobody answers, and it should be evaluated under exactly that condition.

Give the shopper the reason, briefly. "Accepted by this customer before" or "9 in 10 customers accept this" turns a list into a decision they can make in the seconds available, and lets them override sensibly when they can see something the model cannot — the substitute looks poor, the shelf has a better option not in the catalogue.

Evaluate on the outcome that matters: refund rate, item-level complaint rate and repeat ordering, not on offline ranking metrics against historical choices, which were themselves made from a bad list.

## Target Customer

Grocery and retail delivery platforms, where substitution quality is a leading driver of customer retention and of shopper rating volatility. Also the retailers' own e-commerce operations, who face the identical problem in their first-party pickup and delivery and generally solve it no better.

## Impact If Built

The shopper's ninety-second decision is made from evidence instead of a guess, and the customer gets a substitution someone like them has actually accepted. Refunds and complaints fall, which is where the direct business case sits. And the shopper stops absorbing the rating consequence of a catalogue relationship that was never about preference.
