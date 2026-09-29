# Rules Engines and Query Optimisation

**Niche:** [[niches/b2b-commerce-platforms/entitlement-and-price-resolution/profile|Entitlement & Price Resolution]]
**Industry:** [[industries/b2b-commerce-platforms|B2B Commerce Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Rules engines, materialised views and authorisation systems each solve part of this, and B2B pricing is implemented as customer group overrides and custom code.
**Tags:** #graph-theory #convex-optimization #data-integration #automation #evaluation-metrics #compliance #dynamic-programming #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to resolve one customer's correct price and entitlement for any product at any quantity in milliseconds — and whoever does that takes the account, because that resolution is what a B2B storefront is and everything else in the category is built on it.

## The Problem
Evaluating a rule set fast is what rules engines do, with efficient matching algorithms designed for exactly the case where many rules apply to many facts. Precomputing an expensive query result and maintaining it incrementally is what materialised views do. Deciding what a principal may see is what authorisation systems do, including the filtered-retrieval problem of returning only permitted records efficiently. All three are mature and all three map directly onto pieces of this problem, and the category implements it as overrides and bespoke services.

## What Already Exists
Production rule engines with efficient many-rule matching; materialised view maintenance with incremental refresh; authorisation systems with relationship-based models and filtered listing; policy engines with decision caching; and query optimisation with precomputation and indexing strategies.

## The Customization Gap
The adaptation is to a rule set that is a commercial agreement and a result that is money. It requires: (1) correctness treated as contractual rather than best-effort, since a wrong price is a billing dispute and a caching strategy that occasionally serves stale prices is not acceptable in the way a stale product description is — that difference governs the whole design; (2) the rule set authored by commercial staff rather than by engineers, which means an expression model a pricing administrator can use and is where most implementations fail; (3) effective dating throughout, since agreements start and end and a historical order must be reprice-able against the agreement in force at the time; (4) entitlement as filtered retrieval integrated with search rather than as post-filtering, which the authorisation literature addresses and the platforms do not; and (5) explainability, since a buyer and a rep both need to know why a price is what it is and no rules engine surfaces its derivation by default.

## Target Customer
Platform vendors, distributor and manufacturer engineering teams, and the rules engine and authorisation communities for whom commercial pricing is an unserved application.

## Impact If Solved
Three mature technologies each solve a piece and the category uses overrides and custom code. Treating correctness as contractual governs the caching design, and an expression model a pricing administrator can author is where implementations currently fail.
