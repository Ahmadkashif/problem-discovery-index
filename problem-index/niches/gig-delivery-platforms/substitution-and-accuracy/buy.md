# Buy: Retail Recommendation Engines Adapted to a Forced Choice

**Niche:** [[niches/gig-delivery-platforms/substitution-and-accuracy/profile|Substitution & Order Accuracy]]
**Industry:** [[industries/gig-delivery-platforms|Gig Delivery Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Recommendation engines suggest what a customer might also want; substitution asks what they will accept instead of the thing they chose and cannot have.
**Tags:** #matrix-decompositions #word-embeddings #gradient-boosting #evaluation-metrics #confidence-intervals #k-nearest-neighbors #automation #data-integration
**Contested on:** Whether a recommender optimised for discovery can serve a decision where the customer has already stated exactly what they wanted.

## The Problem

Retail recommendation is a mature, heavily invested field. Collaborative filtering, item embeddings, session-based recommendation and complement-versus-substitute modelling are well developed, and grocery e-commerce platforms run good versions of them for cross-sell and basket building.

Substitution looks superficially like the substitute-item half of that problem and is not. A recommender proposes an addition to a basket that the customer will evaluate and may ignore at no cost. A substitution replaces a specific stated intent with something else, chosen by a third party, delivered without further review, with a refund and a rating on the line. The optimisation target, the tolerance for error and the decision-maker are all different.

## What Already Exists

Collaborative filtering and matrix factorisation libraries. Item2vec-style embeddings trained on basket co-occurrence, which learn substitute relationships reasonably well. Commercial recommendation platforms serving retail. Product catalogue and attribute data from retailers and from data providers. Session recommendation models. All of this is available and much of it is already deployed inside these platforms for discovery.

## The Customization Gap

**Substitutes and complements are confused by co-occurrence.** Embeddings trained on baskets learn that two items appear together, which identifies complements strongly and substitutes weakly — genuine substitutes rarely co-occur, which makes them look unrelated. Substitution needs relationships learned from substitution events themselves, a different training corpus that only the delivery platform holds.

**The target is acceptance, not engagement.** Recommenders optimise click, add-to-basket or revenue. Here the target is whether the customer kept the item without complaint or refund — a label the recommender stack has no path to and that arrives a day later, attached to a fulfilment event rather than a session.

**Refusal has to be a first-class prediction.** No recommender is built to output "recommend nothing". For substitution, predicting that the customer would prefer a refund is frequently the correct and highest-value answer, and it requires an abstention mechanism the products do not offer.

**The consumer is a worker under time pressure, not a browsing customer.** The output is consumed in an aisle in seconds by someone who is not the person with the preference. It needs to be a short ranked list with a one-line reason and a confidence, not a personalised carousel. It also needs to degrade gracefully when the shopper can see the shelf and the model cannot.

**Real-time inventory is the input nobody has.** Recommenders assume the catalogue is available. Grocery stock accuracy is poor, so a substitution suggestion for an item that is also out of stock wastes the shopper's scarcest resource. Joining suggestion ranking to live shelf-level availability — and learning which feeds are trustworthy at which stores — is an integration problem outside the recommender entirely.

## Target Customer

Grocery delivery platforms already operating a recommendation stack for discovery, who need to know why pointing it at substitution underperforms. Also retail technology vendors serving first-party grocery e-commerce, where the same gap exists and the substitution event data is thinner.

## Impact If Solved

The embedding and serving infrastructure gets reused and the five adaptations make it a substitution engine: trained on substitution outcomes, targeting acceptance, able to say no, shaped for a worker in an aisle, and joined to what is actually on the shelf. The measurable result is fewer refunds and fewer shoppers rated down for someone else's guess.
