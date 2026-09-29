# Source Content Readiness

**Industry:** [[localization-services|Localization Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Half the defects that surface as translation problems were created in the source content, and nobody checks the source before it enters the pipeline.
**Tags:** #bert #transformers #large-language-models #gradient-boosting #evaluation-metrics #automation #workflow-orchestration #data-integration

## The Problem
Content arrives for localization in whatever state it was written. Strings concatenated at runtime so that a translator sees fragments without knowing what sentence they form. Placeholders with no indication of what they contain. Idioms and culturally specific references. Text embedded in images. Dates, currencies and units hardcoded. UI strings with no context about where they appear or how much space they have. Ambiguous source sentences that have several valid readings.

Each of these produces the same downstream sequence: the linguist raises a query, the query waits for a response from someone at the client who did not write the string, the deadline slips, and if the query goes unanswered the linguist guesses. The guess is sometimes wrong, and the resulting defect is recorded as a translation error.

This is well understood by everyone in the industry and is nobody's job to fix. The content authors are measured on shipping, the localization vendor is engaged after authoring, and the internationalisation review that would catch it happens at neither point.

## What Already Exists
Internationalisation linting exists in some development workflows, catching hardcoded strings and format issues. Style guides and content guidelines for translatable content are well documented and inconsistently followed. Translation management systems support context screenshots and character limits where someone supplies them. Some continuous localization integrations surface string context automatically from the codebase. Query management workflows are standard and are a workflow around the problem rather than a fix.

## The Customisation Gap
Readiness is checkable at authoring time and is checked nowhere. Concatenation, missing placeholder documentation, idiom use, ambiguity, unexplained abbreviations, text that will expand beyond its container in known languages, and culturally specific references are all detectable in source text before it is ever sent — and the feedback has to reach the author while they are writing, not the linguist three weeks later.

The valuable output is predictive: which strings will generate queries. A vendor with years of query history can learn what source characteristics produce them, and flagging those strings to the client before the handoff removes the delay from the critical path entirely.

Expansion is a specific and tractable case. Text length changes predictably by language pair, and a UI string that fits in English and will overflow in German or Finnish is identifiable at authoring time from the string and its container constraints, which is far cheaper than discovering it in a localised build.

The customisation is per-client register and per-product constraint — a marketing team writing for adaptation needs different guidance from an engineering team writing UI strings, and a generic content linter serves neither.

## Impact If Solved
Source readiness defects consume linguist time, generate query cycles that dominate schedule slippage, and produce errors attributed to translation that originated in authoring. Checking at the point of writing, with query prediction to route the remainder before handoff rather than after, addresses the largest controllable source of both cost and delay in a localization programme — and does it upstream, where the fix is a sentence rewrite rather than a thirty-language rework.
