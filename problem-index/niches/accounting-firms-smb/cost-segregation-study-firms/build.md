# Component Classification Engine Grounded in Firm Precedent

**Niche:** [[niches/accounting-firms-smb/cost-segregation-study-firms/profile|Cost Segregation Study Firms]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A classification engine built on the firm's own decided studies, so that a component in a new medical office building is classified against the eighty times the firm has classified that same component — with the reasoning and any examination history attached.
**Tags:** #gradient-boosting #cnns #transfer-learning #feature-engineering #evaluation-metrics #cross-validation #tacit-knowledge-ml #compliance #revenue-impact

## The Problem
A cost segregation study requires hundreds of individual classification decisions, each defensible against published asset class precedent. Building types repeat heavily — medical office, multifamily, quick-service restaurant, light industrial — and so do their components, which means a firm doing 800 studies a year has classified the same categories of dedicated plumbing, specialty electrical, decorative finishes, and site improvements thousands of times. Every one of those decisions was reasoned through and documented. None of it is retrievable as precedent. A new engineer classifies from training and judgment, a senior engineer classifies from personal recall, and the two produce different answers on the same facts. The inconsistency is invisible internally and expensive externally: it surfaces as an adjustment on examination, on a study delivered years earlier.

## Why Nobody Has Built This
Prior studies are archived as delivered PDFs and spreadsheets organized by client and property. The classification decisions inside them are structured data trapped in document layout — a component description, an allocated cost, an assigned life, and usually a short justification, repeated across hundreds of rows and thousands of files. Extracting that into a queryable precedent base was a data engineering problem no firm had reason to fund, because the cost was visible and the benefit was diffuse. It is also genuinely firm-specific: two firms may take different defensible positions on the same component, and a shared industry database would be worse than useless because it would blur the position the firm has actually been defending.

## What to Build
An engine that parses the firm's study archive into a component-level precedent base — component description, building type, allocated cost, assigned class life, stated justification, and where recoverable, examination outcome. For a new study, the engineer's takeoff is matched against that base and each line returns the firm's prior treatment of the same component in comparable buildings, with the distribution of past decisions, the reasoning used, and any history of challenge. Where the firm has been consistent, the classification is proposed with high confidence and the engineer confirms. Where the firm has been inconsistent — the genuinely valuable output — the system surfaces the split explicitly and asks for a decision that then becomes precedent. A second pass runs across the completed study to flag internal contradictions before delivery: a component classified one way on floor two and another way on floor three is the kind of error that is trivial to catch mechanically and nearly impossible to catch by review.

## Target Customer
Directors of engineering and practice leaders at cost segregation firms producing 200+ studies annually, and national specialty tax directors at regional CPA firms with an in-house cost segregation group.

## Impact If Built
Makes classification consistent across engineers and across time, which is the firm's actual exposure on examination. Compresses the classification pass — the most engineer-intensive stage of the study — and lets less experienced staff work at closer to senior standard with the precedent in front of them. The precedent base becomes a defensible institutional position rather than a set of individual opinions, which is directly usable in examination defense.
