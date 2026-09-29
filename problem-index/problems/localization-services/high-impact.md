# Quality Is Scored by Reviewers and Never by the Market

**Industry:** [[localization-services|Localization Services]]
**Type:** High Impact
**One-liner:** The industry runs an elaborate apparatus for scoring translations against error typologies and has no idea which translations actually worked in the market they were made for.
**Tags:** #evaluation-metrics #causal-inference #hypothesis-testing #confidence-intervals #transformers #bert #revenue-impact #gradient-boosting

## The Problem
Translation quality is assessed by linguistic review. A reviewer samples segments, categorises errors against a typology — accuracy, fluency, terminology, style, locale convention — assigns severities, and produces a score. The score gates delivery and feeds vendor scorecards.

It describes the artefact. Whether the localised page converted, whether the localised interface was understood without support contact, whether the translated documentation resolved the question, whether the market search terms were the ones used — none of that is in scope, and all of it is what the client is actually buying.

The two come apart in specific and known ways. A terminologically consistent translation using the client's approved glossary can systematically miss the words buyers in that market actually type, which is a search and conversion problem invisible to any reviewer. A fluent rendering of source copy written for a different market can be perfectly accurate and commercially inert. Conversely a translation flagged for style deviations may be exactly the register the local audience responds to.

The absence of outcome data also makes the industry's central economic argument unresolvable. Whether a higher-priced human translation outperforms post-edited machine output commercially — not in review scores, but in conversion and comprehension — is an empirical question that would settle a decade of pricing arguments, and nobody has run it at scale.

For the vendor the effect is competitive. With no outcome evidence, localization is procured on price per word and internal quality scores, which are comparable across vendors and unrelated to value. That is the exact dynamic that has compressed margins across the industry and driven the shift to post-editing economics.

## Why It's Unsolved
Outcome data is in the client's analytics, per locale, and localization vendors are rarely given access. The relationship is procurement-managed and priced per word, which does not naturally include a measurement clause.

Attribution is genuinely difficult in a way that is particular here. A locale's conversion rate differs from another's for reasons of market, competition, pricing, payment methods, logistics and brand recognition, and translation quality is one contributor among many. Isolating it requires comparing translation variants within a locale, which means running experiments on localised content — technically straightforward, organisationally novel, and something almost no company does.

There is also a quality-definition problem underneath. Review typologies were designed to make quality assessable and consistent, and they succeeded at that. Redefining quality as market outcome would invalidate a large apparatus of scorecards, certifications and service level agreements that the industry's commercial relationships are built on, which is a substantial institutional obstacle to even asking the question.

And the volume works against it. A large account translates millions of words across dozens of locales continuously; outcome measurement at segment level is impossible and at content-item level is only feasible for the high-traffic surfaces, which means any programme must be deliberately scoped to where the stakes are rather than applied everywhere.

## What a Solution Looks Like
Measure where it matters and accept it cannot be measured everywhere. High-traffic surfaces — landing pages, product pages, onboarding flows, top support articles — carry most of the commercial consequence, and instrumenting those per locale is tractable.

Run translation variants as experiments. Two renderings of the same page, served randomly within a locale, is a clean test of whether translation choices affect outcome, and it is the only way to separate translation quality from market effects. This is the single highest-value practice the industry does not have.

Bring market language into the process. The terms buyers actually search for in a locale are observable from search data and are frequently not the approved glossary terms. Reconciling terminology with market usage — and being able to show a client the cost of insisting on their glossary — turns a recurring argument into an evidenced decision.

Feed outcomes back to linguists. A translator who learns that their rendering of a landing page outperformed the alternative has information nobody in this industry currently receives, and it is the only mechanism by which craft judgement could be calibrated against results rather than against review scores.

## Impact If Solved
This would give localization the evidence base it has never had, at the moment its pricing model is under maximum pressure. A vendor that can demonstrate commercial outcome rather than review scores competes on something other than price per word — which is the only escape from the compression the industry has experienced — and clients get an answer to a question they have been unable to ask about a spend that runs to millions across locales.
