# Build: Standing Capacity Before the Crisis

**Niche:** Low-Resource Language Moderation
**Industry:** [[industries/content-moderation-services|Content Moderation Services]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A standing, pre-built moderation capability for high-risk low-resource languages — labelled data, trained reviewers, coded-term tracking — assembled before the crisis rather than scrambled during it.
**Tags:** #bert #transfer-learning #large-language-models #word-embeddings #evaluation-metrics #confidence-intervals #data-integration #compliance
**Contested on:** Whether moderation capability is allocated to where the offline consequences of failure are most severe, or to where the training data and the advertising revenue already are.

## The Problem

Moderation capability in a given language is built during or after the emergency that reveals its absence. The pattern repeats: a platform grows quickly in a market, becomes a primary communication channel there, a political crisis or ethnic conflict escalates, coordinated incitement spreads in a language with no classifier and three reviewers, harm follows, and capability is assembled urgently over the following year under intense scrutiny.

Building it during the crisis is close to the worst possible time. Reviewers cannot be recruited, security-cleared, trained on policy and calibrated in weeks. Labelled data cannot be collected retrospectively at the volume a classifier needs. Coded terminology — the vocabulary that emerges specifically to evade moderation and that changes weekly during an escalation — cannot be tracked by people who arrived last month. And the local knowledge that distinguishes a threat from a reference from a joke takes years to develop and cannot be procured on demand.

Everything about the response is late because nothing about the preparation exists. There is no standing capacity, no pre-built corpus, no trained bench, and no measure that would have identified the language as high-risk before the risk materialised.

## Why Nobody Has Built This

**Nobody pays for capability before the incident.** Standing capacity in a language with low volume is a cost with no current return. Platforms fund moderation against volume and revenue, and the languages that need this most have little of either at the point when preparation would matter.

**The incentive arrives only after the harm.** Investment follows the crisis reliably and precedes it almost never, because the counterfactual — the incident that did not happen — is unprovable and therefore unbudgetable.

**Data collection is hard before there is anything to collect.** A classifier needs examples of violating content in that language, and in a pre-crisis market the volume is genuinely low. Building the corpus means deliberate collection, partnership with local organisations and synthetic augmentation, none of which any vendor is funded to do.

**Local recruitment is structurally hard.** These are markets where the vendor has no presence. Finding speakers of the right dialects, with the cultural and political literacy to read charged material correctly, who can be employed, cleared and retained, is a real operational problem that takes a year and is nobody's current objective.

**Political exposure cuts against involvement.** Moderating politically charged content in a contested environment guarantees accusations of bias from every side. A commercial vendor's rational instinct is to avoid the work, which is part of why the specialist tier is thin.

**Risk assessment is nobody's product.** No standing measure exists of which languages are underserved relative to the offline risk in their markets. Without the measure there is no list, and without a list there is nothing to prepare for.

## What to Build

**A language risk index, published.** Platform penetration as a communication medium, growth rate, political volatility and conflict indicators, existing classifier coverage, and reviewer headcount per unit of volume — combined into a standing assessment of which languages are most underserved relative to consequence. This is the artefact that makes the case for everything else, it can be built largely from public data and platform disclosures, and its existence creates the pressure that budget alone never will.

**Pre-build the corpus deliberately.** Partnership with local civil society organisations, academic linguists and diaspora communities to assemble labelled examples of the categories that matter, in the registers people actually use — code-switched, transliterated, dialect-heavy. Augmented with careful synthetic generation and with transfer from related languages. Started years before it is needed, at a cost that is trivial next to the cost of the crisis response.

**A trained, retained bench.** Reviewers recruited and certified in advance, working part-time on adjacent queues to stay calibrated, available to surge. The hard part is retention and calibration during the quiet period, which argues for a consortium model where several platforms share a standing capability none of them would fund alone.

**Track coded terminology continuously.** Evolving vocabulary detected from usage shifts rather than from a glossary someone updates, with local reviewers confirming meaning. This changes weekly during an escalation and is the single fastest-degrading piece of moderation capability.

**Design for the transfer gap explicitly.** Multilingual models transfer usefully into mid-resource languages and poorly into low-resource ones and their real registers. Measure the gap per language rather than assuming it, and route to humans where the model is known to be unreliable — which is the honest version of coverage.

**Fund it as shared infrastructure.** No single platform will pay for standing capacity in a low-volume language. A consortium, a levy, or a regulatory requirement is the realistic funding structure, and the risk index is what makes the allocation argument tractable.

## Target Customer

Platform regional and integrity leadership, though the honest position is that internal budget will not fund this ahead of the incident. The realistic buyers are consortium arrangements, regulators implementing systemic risk obligations, and the civil society and academic funders who already work on this.

Specialist vendors with genuine regional depth are the natural operators, and a standing capability is a defensible position in a market where the large generalists compete on cost.

## Impact If Built

Capability arrives before the harm rather than after it, which is the only version of this that helps anyone. Every retrospective on these failures reaches the same conclusion, and nothing in the industry's structure acts on it.

The risk index alone would change the conversation. A public, methodologically defensible list of which languages are most underserved relative to consequence is the kind of artefact that reallocates resources, because it makes an invisible allocation visible.

And the corpus is durable. Labelled data in a low-resource language, collected carefully, retains value for years and benefits every platform and every researcher working in that language — which is precisely why it should be built as shared infrastructure rather than as one company's asset.
