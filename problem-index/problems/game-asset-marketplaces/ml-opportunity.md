# Machine Learning Opportunities — Game Asset Marketplaces

**Industry:** [[game-asset-marketplaces|Game Asset Marketplaces]]
**Derived from:** [[problems/game-asset-marketplaces/high-impact|High Impact]], [[problems/game-asset-marketplaces/low-impact-1|Low Impact 1]], [[problems/game-asset-marketplaces/low-impact-2|Low Impact 2]], [[problems/game-asset-marketplaces/worker-life-1|Worker Life 1]], [[problems/game-asset-marketplaces/worker-life-2|Worker Life 2]]

---

## 1. Compatibility and Integration Cost Prediction
#gradient-boosting #graph-neural-networks #bert #transfer-learning #confidence-intervals #k-nearest-neighbors #evaluation-metrics #feature-engineering

**Problem statement:** The listing shows a thumbnail and a price, and the cost that determines whether the purchase was worthwhile is the integration work — engine version, render pipeline, rig structure, dependency graph, performance budget — none of which is visible before buying.

**ML task:** Extract technical properties from the asset files and predict fit and integration hours against a specific buyer's project configuration
**Input data:** The asset files themselves — geometry, materials, shaders, textures, rigs, audio, code and its dependency graph; declared and inferred engine version and pipeline targets; the buyer's project configuration including engine version, pipeline, platform targets, package set and performance budget; historical refunds, reviews mentioning integration, and observed post-purchase usage.
**Target:** Integration effort in hours with a range, and the specific expected friction points.
**Evaluation metric:** Predicted hours against reported or observed actual integration effort, and — more usable in practice — precision on the specific friction predictions, because "may require material rebuild for your pipeline" is actionable and a compatibility score is not. Measure refund rate and abandonment among purchases made with and without the prediction available; those are the outcomes the marketplace cares about and they are directly observable.
**Scope:** Property extraction from files is the foundation and is deterministic engineering rather than modelling; the prediction layer sits on top of it. The compatibility surface is genuinely multidimensional and needs maintaining as engines release, which is work the marketplace can do once instead of every buyer doing it by purchase and trial. 2-3 engineers with engine expertise plus 1 ML engineer, 9-12 months.
**Data availability:** Every file is already stored by the marketplace. Buyer project configuration requires an integration buyers would grant readily. Integration effort labels are the weak point and must be bootstrapped from reviews and refunds.

---

## 2. Content-Based Asset Retrieval With Style Matching
#contrastive-learning #cnns #transformers #autoencoders #dimensionality-reduction #k-nearest-neighbors #evaluation-metrics #bert

**Problem statement:** Search runs on creator-written titles and tags optimised for discoverability, so finding an asset depends on guessing the word the creator used — and the property buyers most need, whether it sits stylistically with what they already have, is captured by no keyword.

**ML task:** Learn representations from asset content — geometry, materials, textures, audio, code — supporting retrieval by what the asset is and by style similarity to a buyer's existing project
**Input data:** Asset files across the catalogue; rendered views from consistent viewpoints rather than creator-chosen thumbnails; extracted technical properties; the buyer's existing project assets as a query; purchase and usage signals.
**Target:** Whether a retrieved asset is purchased and retained rather than refunded or abandoned.
**Evaluation metric:** Retention-weighted retrieval quality rather than click-through, since surfacing an appealing asset that does not fit is the failure this is meant to remove. Evaluate the long tail explicitly — the value is in making unfindable catalogue findable, and an aggregate metric will be dominated by the well-marketed listings that already sell. Style matching should be validated by whether technical artists judge the retrieved set as coherent, which requires human evaluation and has no automatic substitute.
**Scope:** Representations must come from the asset rather than the thumbnail: two models with identical geometry can have entirely different renders, and two similar renders can be a game-ready asset and a film-quality one unusable in real time. Set-level retrieval — assembling a coherent collection spanning creators, matched on style, scale, budget and pipeline — is the buyer's actual task and is a different query from ranking individual listings. 2-3 ML engineers with 3D and multimodal experience, 9-12 months.
**Data availability:** Complete. The catalogue is the training set.

---

## 3. Asset Fingerprinting for Resale and Component Provenance
#contrastive-learning #autoencoders #cnns #dimensionality-reduction #k-nearest-neighbors #graph-neural-networks #compliance #evaluation-metrics

**Problem statement:** Work taken from another marketplace, a game, a repository or an artist's portfolio is relisted under a new name, detected reactively when the original creator notices. Separately, assets bundle components — textures, libraries, samples — whose licences may not permit resale, and nobody checks.

**ML task:** Fingerprint assets robustly to the transformations resellers apply, match submissions against the full catalogue and known external corpora, and detect bundled components from licensed or public sources
**Input data:** Geometry, material structure, texture content and audio waveform across the catalogue; known external corpora — public repositories, other marketplaces where cooperation exists, licensed libraries; submission history and account relationships; confirmed takedown cases as labels.
**Target:** Whether a submission is derived from existing work, and whether it contains components from identifiable sources.
**Evaluation metric:** Robustness to the specific transformations that matter — retopology, retexturing, rescaling, format conversion, pitch shifting — tested adversarially rather than on unmodified copies, which is the easy case and the one reverse image search already handles. Precision at the enforcement threshold must be very high, because a false accusation against a legitimate creator is a serious harm and the appeal burden falls on them. Report recall separately so the marketplace knows what it is missing rather than assuming coverage.
**Scope:** The marketplace holds every file, which makes it the only party able to check a submission against the whole corpus; cross-marketplace checking on a shared index is the extension that would matter most and requires competitors to cooperate. On generative provenance, the honest position is that detection is unreliable and degrading, so the defensible design is strong disclosure, verifiable process evidence where creators can supply it, and clear statements to buyers about what has not been established — rather than a verification claim that will be wrong in both directions. 2 ML engineers, 9-12 months.
**Data availability:** Catalogue is complete. External corpora are partial. Confirmed cases exist in takedown history.

---

## 4. Convention Normalisation and Performance Budget Estimation
#gradient-boosting #cnns #transfer-learning #graph-neural-networks #confidence-intervals #evaluation-metrics #automation #feature-engineering

**Problem statement:** Assets from many creators arrive with different scale, pivot placement, naming, texture packing, material structure and level-of-detail conventions, and a technical artist converts each by hand. Separately, the performance implications accumulate invisibly until the project misses its frame budget near ship.

**ML task:** Identify an incoming asset's conventions and transform it to the project's, and estimate its contribution to geometry, texture memory, material count and draw call budgets on the target platform
**Input data:** Asset files with geometry, pivots, hierarchy, naming, texture channel usage and material graphs; the project's own convention specification inferred from its existing content; target platform characteristics; historical profiling data linking asset properties to measured cost.
**Target:** Correctly normalised assets, and predicted runtime cost on the target platform validated against profiling.
**Evaluation metric:** For normalisation, correctness verified by a technical artist on a sample — this transformation is destructive if wrong, so it should produce a reviewable diff rather than apply silently. For budget estimation, accuracy against measured profiling on the target platform, reported per platform since the relationship between asset properties and cost differs substantially between them. The operational metric is how much late-stage optimisation work is avoided, which is the cost this addresses.
**Scope:** Convention detection is the interesting part and is learnable from the variety across a marketplace catalogue; the transformations themselves are deterministic once the source convention is identified. Surfacing budget impact at import rather than at profiling turns the end-of-project optimisation crunch into a running constraint. 2 engineers with technical art expertise plus 1 ML engineer, 6-9 months.
**Data availability:** Assets are available; project conventions are inferable; profiling data requires instrumentation studios usually have and rarely retain in a linkable form.
