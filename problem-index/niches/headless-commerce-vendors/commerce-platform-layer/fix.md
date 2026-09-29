# Extensibility That Becomes a Fork

**Niche:** [[niches/headless-commerce-vendors/commerce-platform-layer/profile|Commerce Platform Layer]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Every retailer has business rules the platform does not model, they are implemented in custom services around it, and within two years the deployment is a bespoke system with a vendor logo on it.
**Tags:** #workflow-orchestration #compliance #data-integration #evaluation-metrics #automation #descriptive-statistics #quick-win #graph-theory
**Contested on:** Not terminal — the contest differs by whether the buyer is an architecture committee or a developer, and the decomposition is recorded in the profile.

## The Problem
The retailer prices differently for trade customers in one country, applies a loyalty rule the platform's promotion engine cannot express, and has an approval step in the order flow for high-value accounts. None fit the platform's model, so each is implemented as a service that intercepts and modifies. Two years later the composition contains eleven such services, the platform's own promotion engine is bypassed, upgrades require regression-testing custom logic nobody documented, and the retailer is running a bespoke commerce system that they license a platform for. The extensibility mechanism worked exactly as designed and the outcome is the thing composable architecture was meant to avoid.

## Why It's Still Broken
Extensibility hooks are the vendor's answer to every unmet requirement, which makes them a sales tool as well as an architecture. Each individual extension is reasonable and the accumulation is nobody's decision. The vendor has no visibility into what customers have built around them, so the pattern is invisible at the point where it could inform the roadmap. And the resulting brittleness appears as upgrade cost years later.

## What a Fix Looks Like
Model the common extensions rather than hooking them. Instrument what customers actually build around the platform, which requires asking or observing and is the input the roadmap has never had — the extensions cluster heavily and the recurring ones are product gaps wearing a customisation costume. Bring the recurring patterns into the platform as configurable capability, since a rule that eleven customers implemented separately should be a feature. Make the extension mechanism composable rather than interceptive, so an extension declares its effect rather than rewriting a response, which preserves the platform's ability to reason about the outcome. Report extension footprint per deployment as a health metric, so both the retailer and the vendor can see a deployment drifting toward bespoke. Provide upgrade compatibility testing for extensions, which is what makes an extended deployment maintainable. Publish a reference set of well-implemented extensions for the recurring patterns, since the quality of an extension depends on the integrator and there is no reference. Warn when an extension bypasses a platform capability rather than adding to it, because that is the specific pattern that produces the fork. And measure customer upgrade lag against extension footprint, which will show the relationship and is the evidence for the investment.

## Who Feels the Pain
Retailers whose licensed platform became a bespoke system; integrators maintaining eleven interceptors; and vendors whose customers cannot upgrade and whose roadmap is blind to what they needed.

## Impact If Fixed
Extensions cluster heavily and the recurring ones are product gaps, and the vendor has never had visibility into what customers build. A declarative rather than interceptive extension mechanism preserves the platform's ability to reason about the outcome, which is what the fork destroys.
