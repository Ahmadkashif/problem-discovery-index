# Machine Learning Opportunities — Localization Services

**Industry:** [[localization-services|Localization Services]]
**Derived from:** [[problems/localization-services/high-impact|High Impact]], [[problems/localization-services/low-impact-1|Low Impact 1]], [[problems/localization-services/low-impact-2|Low Impact 2]], [[problems/localization-services/worker-life-1|Worker Life 1]], [[problems/localization-services/worker-life-2|Worker Life 2]]

---

## 1. Market Outcome Measurement for Localised Content
#causal-inference #hypothesis-testing #confidence-intervals #transformers #bert #evaluation-metrics #gradient-boosting #revenue-impact

**Problem statement:** Translation quality is scored by reviewers against error typologies, which describes the artefact. Whether the localised page converted, whether the interface was understood, whether market search terms were used — the things the client is buying — are never measured.

**ML task:** Run translation variants as within-locale experiments on high-traffic surfaces and estimate the effect of translation choices on conversion, comprehension proxies and support contact
**Input data:** Variant assignment within locale; per-locale conversion, engagement and support contact data; search query data in the target market; the translation variants themselves with their linguistic characteristics; review scores for comparison; locale-level confounders such as pricing, payment methods and competition.
**Target:** Conversion or task completion for the localised surface, attributable to the translation variant rather than to the market.
**Evaluation metric:** Within-locale randomised comparison is the only design that separates translation quality from market effects, and the headline result is the correlation between review score and measured outcome — which is the number that would tell this industry whether its entire quality apparatus predicts anything. Expect it to be weak on some content types and report it honestly rather than pooling until it looks acceptable.
**Scope:** Measurement is feasible only on high-traffic surfaces — landing pages, product pages, onboarding, top support articles — and any programme claiming to measure everything is overreaching. Terminology reconciliation against actual market search language is the most immediately actionable output and frequently contradicts the client's approved glossary. 1-2 data scientists plus a locale analyst, 9-12 months.
**Data availability:** Requires client analytics access per locale, which procurement-managed per-word relationships do not currently include. This is a contracting change.

---

## 2. Post-Editing Effort Measurement and Difficulty-Based Pricing
#gradient-boosting #confidence-intervals #transformers #hypothesis-testing #evaluation-metrics #probability-distributions #worker-facing #revenue-impact

**Problem statement:** Post-editing is paid at a flat discount against translation on the assumption that editing is proportionally less work, the workforce disputes it, and nobody has measured the actual relationship between machine output quality and editing effort.

**ML task:** Model effort per segment from editing telemetry, and use segment-level quality estimation to price and route by difficulty rather than applying a flat per-word rate
**Input data:** Keystroke, timing and pause data per segment; edit distance between machine output and final; segment characteristics — length, domain, terminology density, source ambiguity, entity and number content; machine output quality estimation scores; linguist identity and experience; final quality outcomes.
**Target:** Actual time and cognitive effort per segment, with edit distance as a weak proxy and timing as the primary signal.
**Evaluation metric:** The distribution is the finding, not the mean — the industry's pricing assumes proportionality and the reality is that most segments are light and a minority require more work than translating from scratch. Report the proportion of segments where post-editing exceeds translation effort, since that single number addresses the dispute directly. Validate effort models against held-out linguists, because per-person speed differences will otherwise dominate.
**Scope:** The collection design is an ethical requirement rather than a detail: telemetry gathered on a freelance workforce can be used for pricing or for surveillance, and the difference is transparency, linguist access to their own data, and whether it sets rates or monitors people. Built without that, this makes the problem worse. 1-2 data scientists, 4-6 months.
**Data availability:** Editing telemetry is generated continuously in every translation editor and almost universally discarded.

---

## 3. Source Readiness Checking and Query Prediction
#bert #transformers #large-language-models #gradient-boosting #evaluation-metrics #automation #workflow-orchestration #feature-engineering

**Problem statement:** Concatenated strings, undocumented placeholders, idioms, ambiguity and text that will overflow its container generate query cycles that dominate schedule slippage, and every one of them is detectable in the source before handoff.

**ML task:** Classify source strings for localization readiness, predict which will generate linguist queries, and estimate length expansion by target language
**Input data:** Source strings with their context and container constraints; historical query logs linked to the strings that generated them; string characteristics — concatenation, placeholders, idiom, ambiguity, abbreviation, cultural reference; realised translation lengths by language pair; UI layout constraints.
**Target:** Whether a string generated a query, and the realised length ratio per language pair.
**Evaluation metric:** Query prediction recall at a precision that authors will tolerate — a readiness checker that flags a third of strings will be disabled within a week, so precision governs adoption and recall governs value. Measure the reduction in query volume and in query-driven schedule slippage as the outcome. Expansion prediction is straightforwardly evaluated against realised lengths and is the easiest win here.
**Scope:** The feedback must reach the author while they are writing, not the linguist three weeks later, which makes this an authoring-tool integration rather than a localization-tool feature. Guidance must differ by content type — marketing copy written for adaptation and UI strings have different readiness criteria and a single linter serves neither. 1-2 engineers, 4-6 months.
**Data availability:** Query histories exist in every translation management system and are rarely linked back to the source strings that caused them.

---

## 4. Context-Aware Memory Retrieval and Asset Health
#contrastive-learning #bert #word-embeddings #k-nearest-neighbors #transformers #evaluation-metrics #data-integration #dimensionality-reduction

**Problem statement:** Translation memories match on strings while applicability depends on context and currency, and both memories and glossaries degrade until linguists stop trusting them and work around the leverage the client is paying for.

**ML task:** Retrieve memory matches by contextual and semantic similarity with recency and approval weighting, detect contradictory and stale entries, and validate terminology against live client content and market usage
**Input data:** Translation memory entries with provenance, date, project and context; the segment's context — surface type, surrounding content, character constraints; linguist acceptance and rejection of offered matches; terminology database; the client's published content in each locale; market search language.
**Target:** Whether a linguist accepts an offered match, and whether a terminology entry is consistent with current approved usage.
**Evaluation metric:** Match acceptance rate at a fixed offer volume is the direct measure, and it should be compared against the incumbent fuzzy threshold rather than in isolation. For asset health, precision on flagged contradictions against reviewer adjudication, since the remediation is manual. Terminology conflicts with live content are checkable outright and are the most immediately convincing output.
**Scope:** Thresholds and register expectations must be per-client and per-content-type — what counts as a usable match differs completely between a medical device manual and a consumer app. Rejection patterns are the strongest available signal of memory decay and are logged nowhere. 2 engineers, 4-6 months.
**Data availability:** Memories, glossaries and client published content are all accessible. Linguist acceptance data requires editor instrumentation.
