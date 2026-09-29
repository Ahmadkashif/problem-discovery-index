# Accessibility Tested Once at Launch

**Niche:** [[niches/headless-commerce-vendors/checkout-compliance/profile|Checkout Compliance]]
**Industry:** [[industries/headless-commerce-vendors|Headless Commerce Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** An accessibility audit is commissioned before launch, passes, and is never repeated, while the storefront ships twice a week and every release can reintroduce a barrier.
**Tags:** #compliance #automation #evaluation-metrics #workflow-orchestration #descriptive-statistics #confidence-intervals #quick-win #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to deliver a checkout that is correct in every jurisdiction the retailer sells into, from components that each solve one part — and whoever does that takes the risk off the retailer, because the assembly is where all of it lands.

## The Problem
An external audit before launch finds twelve issues, they are fixed, and a conformance statement is published. Over the following year the storefront ships a hundred and forty times. A modal is added that traps keyboard focus, a component library upgrade changes contrast ratios, a new checkout step is unlabelled for screen readers, and a lazy-loading change breaks the tab order. The conformance statement is still on the site. No further audit is scheduled. The retailer's position is that they are accessible, on the strength of a document describing software that no longer exists, and the exposure is legal as well as ethical.

## Why It's Still Broken
Accessibility is procured as an audit, which is a project with a start and an end, rather than as a control that runs. Automated testing catches a minority of issues, which is used to argue that automation is not worth doing rather than that it should be combined with periodic manual testing. Nobody owns accessibility in a composable stack where the front end, the component library and three embedded vendor widgets all contribute. And the failure is invisible to everybody who is not affected by it.

## What a Fix Looks Like
Test every release and own it explicitly. Run automated accessibility checks in the build pipeline and fail on regressions, which catches the mechanically detectable issues — keyboard traps, missing labels, contrast, heading structure, focus order — and is a fraction of the work that is most of the volume, and is the fix that turns a project into a control. Test with assistive technology on a schedule, since the automated checks miss the experiential failures and the two together are what conformance requires. Include the embedded vendor components, since a payment widget or a chat overlay can break the page and nobody tests them. Test the checkout flow end to end rather than page by page, because the barriers accumulate across steps and a per-page test misses them. Assign ownership, since in a composable stack accessibility falls between the front-end team and three vendors and currently belongs to nobody. Date and version the conformance statement honestly, since an undated statement describing a past release is a misrepresentation. Recruit users of assistive technology for periodic testing, which finds what no audit does. And measure time-to-fix on accessibility regressions, because a regression caught in the pipeline and fixed in a day is a different position from one that lives for a year.

## Who Feels the Pain
Customers who cannot complete a purchase; retailers whose published conformance statement describes software from last year; and developers who introduced a barrier with no check to tell them.

## Impact If Fixed
An audit is a project and accessibility is a property that must hold on every release, of which there are a hundred and forty a year. Pipeline checks cover the mechanically detectable majority, and testing the checkout end to end catches the barriers that accumulate across steps.
