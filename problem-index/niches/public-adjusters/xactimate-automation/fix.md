# Estimate Inconsistency Across Adjusters

**Niche:** [[niches/public-adjusters/xactimate-automation/profile|Xactimate Estimate Automation]]
**Industry:** [[industries/public-adjusters|Public Adjusters]]
**Type:** Fix (Pain Point)
**One-liner:** Two PAs inspecting the same property produce estimates that differ by 15-30% because Xactimate offers multiple valid ways to scope the same damage, and no standard exists for item selection, waste factors, or overhead-and-profit inclusion.
**Tags:** #anomaly-detection #gradient-boosting #tabular-ml #compliance

## The Problem
Xactimate contains over 10,000 line items with overlapping categories. The same damage can be estimated using different line items (e.g., "remove and replace drywall" versus "patch drywall" versus "skim coat and paint"), different waste factors (10% versus 15% versus 20%), different overhead-and-profit treatment (included versus excluded versus partially included), and different scope decisions (replace the whole wall versus just the damaged section). Two competent PAs will produce different estimates for the same property — and carriers exploit this inconsistency to challenge estimates line by line.

## Why It's Still Broken
There is no industry-standard scoping guide that defines "for this damage type, use these line items with these quantities." Xactimate training teaches software operation, not scoping methodology. Each PA develops their own approach through trial and error, adjusting based on which carriers accept which items. Firms lack the tools to enforce consistent scoping across their team — they review estimates manually, catching inconsistencies only when the firm owner's experience flags them.

## What a Fix Looks Like
A firm-level estimate standards engine that defines preferred scoping patterns for common damage types: "For wind-damaged 3-tab shingle roof, use these line items, apply 15% waste, include O&P on all contractor items." When an adjuster writes an estimate that deviates from firm standards — using different line items, unusual waste factors, or non-standard scope — the system flags the deviation for review before submission. Over time, the system learns the firm's standards from approved estimates and becomes more accurate in flagging true deviations versus acceptable variations.

## Who Feels the Pain
PA firm owners who review every estimate for consistency and catch scoping differences that would undermine carrier negotiations. Junior adjusters who learn bad habits from inconsistent feedback.

## Impact If Fixed
Reduces estimate revision rate by 40-50% (fewer carrier challenges based on non-standard line items). Improves firm-wide estimate quality consistency, enabling faster carrier negotiations. Reduces firm owner review time by 30-40% by flagging only true deviations.
