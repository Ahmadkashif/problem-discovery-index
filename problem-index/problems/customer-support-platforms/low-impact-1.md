# Macro and Canned Response Maintenance

**Industry:** [[customer-support-platforms|Customer Support Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Macros are a universal, well-implemented feature and every mature support organisation has eight hundred of them, of which agents use forty and the rest are wrong.
**Tags:** #bert #word-embeddings #k-means-clustering #dbscan #large-language-models #evaluation-metrics #automation #worker-facing

## The Problem
Macros — saved replies with variable substitution and optional ticket actions — are one of the oldest and most useful features in support software. Every platform has them and every organisation uses them heavily.

They accumulate without limit. Someone creates a macro for a situation, a colleague creates a near-duplicate because they could not find the first, a policy changes and one of the two is updated, a product is renamed and neither is. After a few years a mature help desk has hundreds, they overlap, several contradict each other, and nobody has a mandate to prune them.

New agents are the ones harmed most. They are told to use macros, they search the library, they find four plausible options with no indication which is current, and they pick one. Sometimes it is the deprecated one that references a plan tier that no longer exists.

Meanwhile the genuinely useful signal — which responses agents actually write repeatedly, freehand, because no macro covers it — is invisible, so the library grows in the wrong direction.

## What Already Exists
Macro and canned response management is standard in Zendesk, Salesforce, Intercom, Freshdesk and every other platform, with folders, permissions and usage reporting. Some platforms report macro usage counts. Dynamic content and variable substitution work well. Knowledge base article suggestion in the agent workspace is common.

## The Customisation Gap
Usage counts exist and nobody acts on them, because a count does not tell you whether a macro is wrong or merely narrow. What is missing is quality signal: macros followed by a customer reply that indicates the answer did not land, macros associated with reopened tickets, macros whose text contradicts the current knowledge base or another macro.

Duplicate detection is the obvious absent feature. Near-identical macros are trivially detectable by text similarity, and no platform surfaces them, so the library's redundancy grows unchecked.

Induction from agent behaviour is the more valuable direction. Agents writing the same response freehand dozens of times are showing exactly which macro should exist, and clustering outbound agent replies reveals it directly. The library should grow from observed behaviour rather than from whoever thought to create one.

Contradiction detection across macros and against the knowledge base is the third gap and matters more under generative deflection, since an automated system drawing on a corpus containing two contradictory statements will pick one.

## Impact If Solved
Macro libraries are how support organisations encode their answers, and they degrade into contradictory sprawl that new agents navigate blind. Pruning, deduplicating and inducing from behaviour turns a decaying artefact into a maintained one, using signals already in the platform.
