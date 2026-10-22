# Exhibit Drawings That Don't Know the Show Rules

**Industry:** [[specialty-design-studios|Specialty Design Studios]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Exhibit designers draw in general-purpose CAD that knows nothing about the exhibitor manual, so height limits, sightline rules, rigging, flame-retardancy and labour estimates are checked by a project manager reading PDFs.
**Tags:** #large-language-models #transformers #gradient-boosting #feature-engineering #compliance #automation #data-integration

## The Problem
A custom trade show exhibit is designed once and then has to comply, show by show, with each venue's and each show's rules. An island booth may build to a height limit set by the show; a peninsula booth must keep its back wall below a certain height for a set distance so it does not block the neighbours' sightlines; hanging signs need rigging points the venue approves and a deadline for the rigging order; covered areas and double-deck structures can trigger smoke-detector, sprinkler or structural review; and every fabric must carry an NFPA 701 certificate or face testing by the fire marshal. The exhibitor manual that holds these rules is a hundred-page PDF that differs for every show, and the general service contractor's order deadlines sit in a separate portal.

The same booth is then estimated for installation and dismantle labour, drayage by weight, and shipping crates. A rendering that looks simple can take several times the planned labour hours on the floor, at union rates and on straight-time or overtime clocks the client did not budget for. A custom exhibit for a 30x50 booth can cost $150,000+ and is expected to last about twenty shows, so the same design is re-checked against twenty different rule sets.

## What Already Exists
Vectorworks (with Spotlight), SketchUp, AutoCAD and Rhino handle drawing and rendering well. Exhibit house management systems handle job costing, inventory and property tracking. Show organisers publish manuals; general service contractors such as Freeman and GES publish order portals and deadlines. CEIR's research shows exhibit space alone takes 40.5% of exhibitor spend, so the rest of the budget — design, build, shipping, labour — is under constant pressure.

## The Customisation Gap
The exhibit-specific layer is a rules engine fed by the exhibitor manual: extract each show's height limits, sightline setbacks, rigging, fire, electrical and labour-jurisdiction rules from the PDF, and check the 3D model against them before the design review rather than at the marshalling yard. It also needs a labour and drayage estimator trained on the house's own past installs — component counts, connection types, crate weights and actual hours billed — so the estimate reflects how this house's booths actually go up. And it needs a property record linking each reusable component to the shows it has been to, its condition and its certificates, so a redesign reuses what exists.

## Impact If Solved
Catching a sightline or height violation in design rather than on the floor avoids the most expensive class of on-site rework, and a labour estimate grounded in the house's own install history keeps the client's show budget honest — which, for an exhibit house, is the difference between a renewed programme and a lost account.
