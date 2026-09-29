# Localization Services

## Profile
**Category:** Digital Professional Services
**Market Size:** ~$27B global language services, with RWS, Lionbridge, TransPerfect and Keywords at the top and a long tail of regional agencies and freelance linguists beneath them
**Tech Maturity:** Restructured by machine translation, unmeasured at the outcome. Translation memory, terminology management and MT integration are mature, and post-editing of machine output is now the dominant production model. What no part of the chain measures is whether the localised content performed — whether the translated page converted, whether the localised product was understood, whether the support article resolved anything.
**Workforce:** Translators and post-editors, reviewers and language leads, terminologists, localization project managers, engineers handling file formats and integrations, vendor managers

## Key Pain Themes
Quality is measured internally, by linguistic review scores against error typologies, and never externally by whether the content worked in market. A translation can score well and convert badly; a translation that reads awkwardly to a reviewer can outperform a fluent one because it uses the terms buyers actually search for. The industry has an elaborate internal quality apparatus and no outcome loop at all.

The second theme is the economics of post-editing. Machine translation quality improved to the point that the standard production model became editing machine output rather than translating, and the rate structures moved with it — post-editing is typically paid at a fraction of translation rates on the assumption it is proportionally less work. Linguists widely dispute that the effort scales the way the discount implies, particularly on difficult segments where fixing a fluent-sounding but wrong machine output takes longer than translating from scratch. Nobody measures actual effort per segment, so the rate remains a negotiated assumption.

The third is that the content arriving for translation is frequently not ready. Source text written without localization in mind — concatenated strings, hardcoded formats, idioms, missing context — generates queries, delays and defects that surface as translation problems and originate upstream.

## Current Tech Landscape
Translation management systems from Phrase, Smartling, XTM, Lokalise and memoQ handle workflow, translation memory and terminology. Neural MT from DeepL, Google, Microsoft and the large language model providers is integrated everywhere, with custom-trained engines for large accounts. Quality estimation — predicting segment quality without a reference — exists commercially and is used mainly for routing. Linguistic quality assurance runs on MQM and DQF error typologies. Continuous localization integrations connect directly to repositories and content systems.

## Problems
- [[problems/localization-services/high-impact|🔴 High Impact: Quality Is Scored by Reviewers and Never by the Market]]
- [[problems/localization-services/low-impact-1|🟡 Low Impact: Terminology and Translation Memory Leverage]]
- [[problems/localization-services/low-impact-2|🟡 Low Impact: Source Content Readiness]]
- [[problems/localization-services/worker-life-1|🟢 Worker Life: The Post-Editor Paid by the Discount]]
- [[problems/localization-services/worker-life-2|🟢 Worker Life: The Project Manager Coordinating Thirty Languages]]
- [[problems/localization-services/ml-opportunity|🧠 ML Opportunities]]
- [[problems/localization-services/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
Localization is one of the few professional services with a genuinely rich internal quality framework and no external validation of it whatsoever. Error typologies, review scores and quality estimation all describe the translation as an artefact; the question the client is buying — does this work in this market — is answered by conversion, comprehension, support volume and search behaviour in the target locale, all of which sit in the client's systems and none of which return. The consequence is an industry that competes on price and internal quality scores, and a production model whose central economic assumption about post-editing effort has never been measured against what post-editing actually takes.
