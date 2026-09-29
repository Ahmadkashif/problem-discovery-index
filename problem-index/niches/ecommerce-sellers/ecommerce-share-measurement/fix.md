# Category Definitions Are Rebuilt Per Client

**Niche:** [[niches/ecommerce-sellers/ecommerce-share-measurement/profile|E-Commerce Share Measurement Providers]]
**Industry:** [[industries/ecommerce-sellers|E-Commerce Sellers]]
**Type:** Fix (Pain Point)
**One-liner:** Two competing brands ask what their share of the same category is, receive different denominators, and the firm cannot explain the difference because neither definition was recorded.
**Tags:** #word-embeddings #bert #k-means-clustering #dimensionality-reduction #descriptive-statistics #evaluation-metrics #tacit-knowledge-ml #data-integration #workflow-orchestration #compliance

## The Problem
A category is not a fact; it is a boundary somebody drew. Whether a product belongs in a client's competitive set depends on judgments about form, use occasion, price tier, and channel that analysts make per engagement, frequently in consultation with the client who has a view about who their competitors are. Those judgments determine the denominator and therefore the share. They are recorded nowhere. So the same category has several definitions across the client book, two competing brands receive irreconcilable numbers, and when one of them challenges a figure the firm defends it with a methodology description rather than with the actual inclusion rules.

## Why It's Still Broken
Client-specific category definition is a genuine feature — a brand's competitive set really is a strategic judgment, and forcing everyone onto one taxonomy would produce numbers nobody found useful. That legitimate flexibility has been allowed to mean no definition is recorded at all. The delivery system stores outputs, and the analysis lives in queries where the inclusion logic is embedded in code. And because clients see only their own numbers, the inconsistency surfaces rarely and dramatically rather than continuously and manageably.

## What a Fix Looks Like
Category definitions as versioned, structured objects attached to every delivered number: the inclusion and exclusion rules, the reason for each non-obvious call, whether the definition was client-specified or house-standard, and which engagements use it. Recorded as the work is done. A house-standard definition per category exists alongside client variants, so the firm can always answer both what the client's number is and what the standard number is, and quantify the gap — which converts an embarrassing discrepancy into a documented, defensible choice. A consistency layer flags where two definitions of the same category diverge without a recorded reason, which is the accidental case that should be fixed rather than the deliberate one that should be explained. And because definitions are versioned, a client's trend line can state whether a movement reflects the market or a definitional change, which is currently indistinguishable.

## Who Feels the Pain
Analysts reconstructing definitional decisions colleagues already made; account teams caught between two clients comparing figures; the research director accountable for consistency with no instrument; and the firm's credibility, which rests on numbers being explicable.

## Impact If Fixed
Turns the most common client dispute into a documented choice, and makes longitudinal share claims defensible. The house-standard definition library is also a genuine asset — it is the accumulated category judgment of the firm, which is what a client is really buying and what currently exists only in analysts' heads.
