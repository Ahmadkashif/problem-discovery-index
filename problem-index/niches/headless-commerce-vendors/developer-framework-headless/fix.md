# A Starter That Does Not Scale to a Real Catalogue

**Niche:** [[niches/headless-commerce-vendors/developer-framework-headless/profile|Developer-Framework Headless]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The starter template performs beautifully with two hundred products and falls apart at forty thousand, which is a discovery made after the storefront is built rather than while it is being chosen.
**Tags:** #evaluation-metrics #time-series-forecasting #confidence-intervals #descriptive-statistics #automation #convex-optimization #quick-win #data-integration
**Contested on:** Every serious competitor in this sub-niche is fighting to get a developer from nothing to a working storefront faster than they could write it themselves, and to still be worth using in month six — and whoever does that takes the adoption, because the decision is made before anybody is paid.

## The Problem
The framework's demonstration store has two hundred products, three categories and no personalisation. It renders instantly. The developer's actual catalogue has forty thousand products across nine hundred categories with variant-level pricing, and the same patterns produce a category page that fetches too much, a search results page that waterfalls, and a build time that makes deployment impractical. Every one of those is a consequence of a data-fetching pattern the starter template established, discovered after the storefront was built against it.

## Why It's Still Broken
Starter templates are marketing artefacts optimised to look fast in a demonstration, and a realistic catalogue makes the demonstration worse. Performance characteristics at scale are not published because they are less flattering. The developer has no way to test at their own scale before committing to the patterns. And the failure appears as their implementation being wrong rather than as the template teaching a pattern that does not scale.

## What a Fix Looks Like
Demonstrate at realistic scale and publish the characteristics. Ship a large-catalogue starter alongside the small one, with the patterns that actually work at scale, which is the fix — the template is what teaches the patterns and a small template teaches patterns that fail. Publish performance characteristics against catalogue size, category depth and variant count, so a developer can see where their situation sits before they build. Provide a scale test harness the developer can run against their own catalogue in an afternoon, which is the fully convincing version. Warn in development when a pattern will not scale — an unbounded fetch, a waterfall, an unpaginated query — since the framework can detect these and the developer cannot see them at demonstration scale. Document the data-fetching model explicitly, since it is the source of almost all of these failures and is currently implicit in the templates. Support incremental and partial builds, since build time at catalogue scale is a hard blocker that demonstrations never encounter. Provide a migration path from the small-catalogue patterns, because developers who already built against them need a route that is not a rewrite. And test the framework's own releases against a large catalogue, so regressions at scale are caught by the maintainer rather than by the user.

## Who Feels the Pain
Developers rebuilding a storefront whose patterns came from the template they were given; retailers whose launch slips on performance; and framework maintainers losing production references at exactly the point of commitment.

## Impact If Fixed
The starter template teaches the patterns and a two-hundred-product template teaches patterns that fail at forty thousand. Development-time warnings on unbounded fetches and waterfalls catch what a developer cannot see at demonstration scale.
