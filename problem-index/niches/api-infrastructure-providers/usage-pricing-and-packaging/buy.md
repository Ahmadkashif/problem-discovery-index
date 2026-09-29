# Pricing Science From Every Other Consumption Business

**Niche:** [[niches/api-infrastructure-providers/usage-pricing-and-packaging/profile|Usage Pricing & Packaging]]
**Industry:** [[industries/api-infrastructure-providers|API Infrastructure Providers]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Telecoms, utilities and cloud infrastructure have decades of tariff design, elasticity estimation and bill-shock research, and API pricing is set by looking at a competitor's pricing page.
**Tags:** #gradient-boosting #logistic-regression #survival-analysis #bayesian-inference #hypothesis-testing #confidence-intervals #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor here is fighting to tell an API business what to charge for, at what tier, with what overage behaviour — and whoever answers that takes the commercial side of the category, because metering is solved and the pricing decision is guessed at by everybody.

## The Problem
Designing tariffs for metered consumption is an old discipline. Telecoms spent decades on tier design, bundling, overage behaviour and the customer consequences of bill shock, with a research literature and regulatory attention. Utilities have rate design. Cloud infrastructure has commitment discounts and burst pricing. API businesses, which are metered consumption businesses in every respect, set prices by analogy.

## What Already Exists
Tariff design methodology from telecoms and utilities; price elasticity estimation; customer lifetime value modelling; churn modelling with survival methods; cluster-based segmentation for packaging; and the bill-shock literature, which is directly relevant to overage design and is entirely unread in this category.

## The Customization Gap
The adaptation is to a developer-mediated purchase with very high usage dispersion. It requires: (1) handling extreme skew, since API usage distributions are far more dispersed than telecoms minutes, with the largest consumer often thousands of times the median, which breaks tier designs imported naively; (2) recognising that the buyer and the user differ — an engineer generates the usage and a finance function receives the invoice, which is precisely the bill-shock structure and makes overage behaviour a relationship question rather than a revenue one; (3) elasticity estimation without experiments, since a provider cannot easily randomise prices across consumers, which pushes toward quasi-experimental designs using historical changes and cohort comparison; (4) cost-to-serve attribution as an input, because unlike telecoms the marginal cost varies enormously by request type and a uniform unit hides it; and (5) migration design for existing consumers, since almost all the practical difficulty of a pricing change is moving the current book and the literature on that is thin.

## Target Customer
Metering and billing vendors, API businesses, and the pricing consultancies who currently serve this need with judgement rather than data.

## Impact If Solved
Decades of tariff design exist next door and are unread in a category doing exactly the same thing. Extreme usage skew and the buyer-user split are the two adaptations, and the second is what makes overage behaviour the highest-stakes decision in the structure.
