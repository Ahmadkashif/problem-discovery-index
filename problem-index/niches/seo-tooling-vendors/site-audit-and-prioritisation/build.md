# Eleven Thousand Rows Sorted by a Word

**Niche:** [[niches/seo-tooling-vendors/site-audit-and-prioritisation/profile|Site Audit & Impact Prioritisation]]
**Industry:** [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every crawler produces a prioritised list of site issues, prioritised by a severity label the vendor assigned in general, not by what fixing it would do for this site.
**Tags:** #gradient-boosting #causal-inference #evaluation-metrics #confidence-intervals #revenue-impact #descriptive-statistics #workflow-orchestration #convex-optimization
**Contested on:** Every serious competitor in this niche is fighting to rank a site's issues by what fixing them would do for that site — and whoever does that turns an eleven-thousand-row export into a ticket an engineering team will actually take.

## The Problem
The audit reports four hundred critical issues, three thousand high and eight thousand medium. The critical ones include missing meta descriptions on pages nobody visits and a canonical problem on a template that generates most of the site's organic traffic. Both are labelled the same because the label was assigned to the issue type, not to this occurrence on this site. The SEO now has to work out which rows matter, which they do by intuition, and then persuade an engineering team to take them — a team that will reasonably ask what the business impact is, and receive an answer that begins with the word probably.

## Why Nobody Has Built This
Severity labels are assigned per issue type because that is what a crawler can do without knowing anything about the site's traffic or revenue, and nobody joined those inputs. Estimating the effect of a fix requires a causal model the category has not built. Vendors compete on issues detected, which rewards volume over prioritisation. And the SEO's difficulty persuading engineering is not the vendor's problem.

## What to Build
Prioritise by estimated effect. Estimate the traffic and revenue consequence of fixing each issue occurrence, using the page's own traffic, its position in the site's structure and the observed effect of similar fixes across the corpus — which is the core and is what turns a label into a number an engineer can act on. Draw on the longitudinal record of what actually happened when sites fixed things, connecting to the causal work, since millions of observed fixes across a decade is the evidence nobody uses. Weight by page value rather than by page count, so an issue on one high-value template outranks the same issue on eight thousand dead pages. Estimate engineering cost as well as benefit, because prioritisation without cost is only half a ranking and is why the list loses to other work. Group occurrences into a single actionable change, since eleven thousand rows are usually a few dozen template fixes and the row-level presentation obscures that. Produce a ticket in the engineering team's own system with the estimate attached, which is what makes the work get done. Predict, then measure after deployment, which is the only way the estimates improve and the only way the SEO builds credibility. Flag issues that are not worth fixing, which is genuinely useful and which no audit tool will say. Account for the generative surface, since some classic issues matter less now and some structural ones matter more. And report the estimated value of the backlog, because that number is what gets engineering capacity allocated.

## Target Customer
Technical SEO teams, the engineering organisations who receive their requests, and audit tooling vendors whose output is an export.

## Impact If Built
Severity is a property of the issue type and the label was assigned without knowing the site, so a dead page and a core template score identically. Estimating effect per occurrence from the corpus of observed fixes produces the number engineering asks for and currently never receives.
