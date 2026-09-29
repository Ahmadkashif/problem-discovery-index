# An Expensive Model on Every Page

**Niche:** [[niches/web-data-extraction-firms/structured-extraction-services/profile|Structured Extraction Services]]
**Industry:** [[industries/web-data-extraction-firms|Web Data Extraction Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Model-based extraction runs a capable model on every page including the nine hundred and ninety that are structurally identical to the ten before them, which is where most of the cost goes.
**Tags:** #convex-optimization #evaluation-metrics #transfer-learning #descriptive-statistics #confidence-intervals #revenue-impact #quick-win #automation
**Contested on:** Every serious competitor in this sub-niche is fighting to return the right fields from a page nobody wrote a parser for, at a cost per page that beats the customer doing it themselves — and whoever does that takes the account, because the alternative is now genuinely available to the buyer.

## The Problem
A crawl collects a hundred thousand product pages from one retailer. They are generated from one template with one layout. Every page is sent to a capable model, which reads the whole document and returns the fields, at a cost per page several orders of magnitude above a selector match. The model produces the same extraction path a hundred thousand times because nothing remembers what it learned on the first page. The resilience that justifies model-based extraction is needed on the handful of pages that deviate, and it is being paid for on all of them.

## Why It's Still Broken
Running the model everywhere is simple, uniform and works, which is a hard combination to argue against during a build. The hybrid requires template learning, template validity checking and a fallback path, which is real engineering against a problem that appears solved. Per-page cost was acceptable when volumes were small and became the dominant line as they grew. And where the firm bills per page, the cost is the customer's.

## What a Fix Looks Like
Learn the template once and use the model where it matters. Induce an extraction template from the model's output on the first pages of a site, then apply it cheaply to structurally matching pages, which is the fix and typically removes most of the cost immediately. Detect template match before extraction, using page structure similarity, so a deviating page is routed to the model and a matching one is not. Verify continuously by sampling template-extracted pages through the model and comparing, which keeps the template honest and doubles as the silent-breakage detector. Escalate automatically on any validation failure, so resilience is preserved exactly where it is needed. Cascade model size, using a small model where it suffices and a capable one only for genuinely hard pages, which is a further large saving and is straightforward to route by confidence. Share templates across customers for the same site, since it is the same page and the second customer should not pay to relearn it. Report cost per extracted record so the saving is visible. And keep the model path always available, because the whole reason to prefer this approach over selectors is that it degrades gracefully when the site changes.

## Who Feels the Pain
Customers paying model prices for template-shaped work; firms whose margin on high-volume sites is far worse than on low-volume ones; and the teams who concluded model-based extraction was uneconomic at scale.

## Impact If Fixed
The resilience justifying model-based extraction is needed on a handful of pages and paid for on all of them. Inducing a template from the model's first outputs and escalating only on structural deviation removes most of the cost while keeping the graceful degradation intact.
