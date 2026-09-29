# Technical Audits That Return Four Thousand Issues

**Industry:** [[seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every crawler produces a prioritised list of site issues, prioritised by a severity label the vendor assigned in general, not by what fixing it would do for this site.
**Tags:** #gradient-boosting #causal-inference #change-point-detection #k-nearest-neighbors #evaluation-metrics #confidence-intervals #feature-engineering #automation

## The Problem
A technical SEO audit crawls a site and returns findings: duplicate titles, thin content, broken internal links, redirect chains, missing canonicals, slow templates, orphaned pages, crawl budget waste. A large site produces thousands. Each carries a severity — high, medium, low — from the vendor's fixed taxonomy.

The output is unactionable at that volume, and the prioritisation is generic. A redirect chain flagged high severity might affect forty pages nobody visits. A thin-content warning might sit on a template producing a third of the site's conversions, where the fix is a quarter of an engineering roadmap. The audit cannot distinguish these because it does not know the site's traffic, revenue or engineering cost, and the severity label was assigned by someone writing a rule for all sites.

So the practitioner does the prioritisation by hand: export to a spreadsheet, join to analytics, estimate effort, argue for engineering time. Most audits produce a document that is read once. The recurring complaint from in-house SEOs is not that they lack findings — it is that they cannot get anything fixed, because they cannot state what a fix is worth.

## What Already Exists
Screaming Frog is the practitioner default and is genuinely excellent at finding things. Semrush, Ahrefs, Sitebulb, Lumar and OnCrawl all run cloud crawls with issue taxonomies and trend tracking. Google's Search Console reports indexation and Core Web Vitals from real user data. Lumar and OnCrawl in particular integrate log files and analytics, which is the closest anyone comes. Several tools now estimate a traffic-opportunity figure per issue, generally by multiplying an affected page's current impressions by an assumed click-through improvement.

## The Customisation Gap
Prioritisation requires a causal estimate — what happens to this site's outcomes if this class of issue is fixed on these pages — and the industry uses a severity label plus a multiplication. The data to do better exists: these vendors hold longitudinal crawl histories for millions of sites, and therefore millions of natural experiments in which a site fixed a specific issue class on a specific page type and something did or did not happen afterwards. That corpus can support effect estimates by issue class, page type, site size and vertical, with intervals.

The second half is the site's own economics. The value of a fix is traffic change times conversion rate times value, and the cost is engineering effort, both of which live on the customer's side. A prioritisation that ranks by expected value net of effort is a fundamentally different artefact from one that ranks by severity, and it is the artefact an SEO needs to win an engineering argument.

And issues should be grouped by cause, not enumerated by instance. Four thousand findings are usually a few dozen template or system defects; reporting the defect with its blast radius, rather than every page it touches, is what makes the output readable and is mostly a clustering problem over the crawl.

## Impact If Solved
The binding constraint on technical SEO is not detection, it is getting engineering time, and that argument is won or lost on whether the SEO can state the value of a fix with a defensible number. Effect estimates drawn from a cross-site natural-experiment corpus are the only credible source for that number, and no customer can build it alone — which makes it the clearest case in this category for something only a vendor can sell.
