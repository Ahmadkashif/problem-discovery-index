# Design Systems That Decay After Handoff

**Industry:** [[product-design-studios|Product Design Studios]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** A studio delivers a design system as a component library and a documentation site, and it begins drifting from the client's production code the week the studio leaves.
**Tags:** #bert #transformers #large-language-models #change-point-detection #gradient-boosting #evaluation-metrics #automation #data-integration

## The Problem
Design systems are now a standard deliverable: a token set, a component library, usage documentation, and a handover to the client's engineering team. On the day of delivery the Figma library, the code components and the documentation agree with each other.

They begin to diverge immediately. A product team under deadline builds a one-off variant rather than extending the component. A colour is hardcoded. A spacing value drifts. Six months later the production application contains four button implementations, the documentation describes a system that is only partly in use, and the design team is enforcing consistency by review rather than by tooling.

Nobody measures the divergence, so it is discovered as a feeling — the product looks less coherent than it did — and addressed by a periodic audit somebody has to fund. Studios are frequently rehired to do exactly that audit, which is revenue, and is also an admission that the original handover did not hold.

## What Already Exists
The tooling for building design systems is strong. Figma libraries with variables and modes, Storybook for component documentation, Zeroheight and Supernova for the documentation layer, Style Dictionary for token transformation, and Figma's own code connect features linking design components to their implementations. Linting for design tokens exists. Visual regression testing from Chromatic and Percy catches unintended visual change.

## The Customisation Gap
The tools verify that a component matches itself; nothing measures whether the product is actually using the system. The quantity a client needs is adoption: what proportion of rendered UI comes from system components versus bespoke implementations, which parts of the product are drifting fastest, and which components are being worked around most often — because a component that everybody bypasses is a design problem, not a discipline problem.

That is computable from the client's own codebase and render output, and it is not part of any design system product. Measuring it converts an aesthetic complaint into a tracked metric with a trend, which is what makes it fundable.

The second gap is the diagnosis. Workarounds cluster: a component missing a variant everyone needs, an API too rigid for a common case, a documentation gap. Grouping bypasses by cause tells the system's maintainers what to fix, rather than telling them to try harder.

The per-client customisation is the codebase itself — framework, conventions, structure — which is why a generic tool has not appeared and why this has stayed a consulting service delivered by audit.

## Impact If Solved
Design system decay is the mechanism by which most redesign work erodes, and it is invisible until it is expensive. Continuous adoption measurement with cause-level diagnosis turns the periodic audit into a monitored metric and tells maintainers what to change — and for a studio it converts a handover that quietly fails into an ongoing, evidenced relationship.
