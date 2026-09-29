# Machine Learning Opportunities — Stock Media Marketplaces

**Industry:** [[stock-media-marketplaces|Stock Media Marketplaces]]
**Derived from:** [[problems/stock-media-marketplaces/high-impact|High Impact]], [[problems/stock-media-marketplaces/low-impact-1|Low Impact 1]], [[problems/stock-media-marketplaces/low-impact-2|Low Impact 2]], [[problems/stock-media-marketplaces/worker-life-1|Worker Life 1]], [[problems/stock-media-marketplaces/worker-life-2|Worker Life 2]]

---

## 1. Training Contribution Attribution and Substitution Measurement
#diffusion-models #contrastive-learning #causal-inference #dimensionality-reduction #confidence-intervals #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** The library is among the most valuable training corpora in existence and its contributors are compensated by a formula — asset count, historical revenue, download share — with no relationship to how much any asset influenced the model. Meanwhile generated imagery competes with the library that trained it, and contributors see their income fall without being told why.

**ML task:** Training data attribution over the marketplace's own model and corpus, plus causal estimation of generative substitution on licensing revenue by category
**Input data:** The training corpus with full provenance; the model's weights and training configuration; generated outputs and their prompts; embedding representations of corpus and outputs; search result composition where generated and library assets compete; licensing revenue by asset, category and period; contributor catalogues and their characteristics.
**Target:** A per-asset influence estimate on model outputs, and the share of a contributor's income decline attributable to generative substitution rather than to other causes.
**Evaluation metric:** Attribution methods are approximate and the honest framing is that an imperfect measured attribution with a published method is a large improvement on a formula with no relationship to contribution at all. Validate by holdout retraining on a corpus subset where feasible — expensive but decisive — and report the method's known failure modes rather than presenting the estimate as settled. For substitution, the credible design uses search result composition: where generated and library results appear in the same result sets, the displacement is measurable.
**Scope:** Output-time similarity is the tractable near-term signal: when a generated image sits close to specific training assets in embedding space, that is a weak but real attribution computable per generation, and it would let compensation follow use rather than inventory. The organisational obstacle should be stated plainly — a marketplace that measures contribution creates an obligation to pay accordingly, and the unsettled legal position makes some participants wary of quantifying anything. That is a reason it has not been done, not a reason it cannot be. 3 ML engineers and 1 researcher, 9 months.
**Data availability:** Uniquely complete at the marketplaces with clean provenance, which is precisely what makes their corpora valuable and makes them the only parties able to attempt this.

---

## 2. Buyer Vocabulary Learning and Demand Gap Reporting
#contrastive-learning #bert #word-embeddings #cnns #k-nearest-neighbors #transfer-learning #evaluation-metrics #revenue-impact

**Problem statement:** Discovery depends on keywords supplied by photographers, who describe what an image is of while buyers search for what it is for. Automatic keywording reads the pixels and hits the same ceiling for the same reason. Meanwhile searches that return nothing satisfying are a direct statement of unmet demand sitting unused in the logs.

**ML task:** Learning the mapping from buyer query vocabulary to asset characteristics from search and licensing logs, plus identification and clustering of unsatisfied demand
**Input data:** Full search query logs with results shown, viewed and licensed; abandoned searches and reformulations; asset content embeddings; contributor-supplied and machine-generated keywords; licensing revenue per asset; result set composition including generated alternatives.
**Target:** Concept and use-case tags learned from revealed buyer behaviour rather than from image content, and a ranked report of demand the catalogue does not satisfy.
**Evaluation metric:** Licensing conversion for assets tagged by the system against those tagged conventionally, measured per category — the point is revenue, not tag agreement, and agreement with existing human keywords would measure conformity to the thing being improved on. For demand gaps, the test is whether contributors who produce against a reported gap achieve above-baseline licensing, which is directly measurable once the reporting exists.
**Scope:** Search logs are the unused asset here and they map buyer vocabulary to asset characteristics directly, which is exactly what contributors cannot infer from a keyword guide. Demand gap reporting is the single most valuable thing a marketplace could give a contributor and nobody does it. Per-asset diagnostics separating a surfacing failure from a click failure from a conversion failure give contributors their first real feedback. 2 ML engineers, 5 months.
**Data availability:** Complete internally and spanning two decades at the established marketplaces, which is unusual depth for a revealed-preference dataset.

---

## 3. Rights Detection and Release Correspondence
#object-detection #cnns #semantic-segmentation #bert #large-language-models #evaluation-metrics #compliance #automation

**Problem statement:** Commercial licensing depends on model releases, property releases and the absence of problematic trademarks, artworks and designs, verified by a person looking at the image and the paperwork in seconds. Wrongly clearing an asset exposes everyone to a claim; wrongly restricting one silently destroys most of its earning potential and the contributor is not told why.

**ML task:** Detection and localisation of faces, logos, landmarks, artworks and protected designs, with recognisability scoring and document-level release correspondence checking
**Input data:** Asset images and video frames; submitted release documents as photographs in multiple languages; historical rights classifications and their review outcomes; known infringement claims and their causes; jurisdictional rules on property releases, editorial restrictions and trademark treatment.
**Target:** Localised detections with a recognisability estimate, a correspondence check between visible people and submitted releases, and a licensing classification recommendation with the reasoning.
**Evaluation metric:** Recall on detection is the binding requirement, since a missed logo or recognisable face becomes a downstream claim against the buyer, the contributor and the marketplace. Recognisability should be reported as a score with the reasoning shown rather than as a decision, because it is a spectrum on which no two reviewers agree and consistency is the achievable improvement. Release correspondence is measured on whether it correctly identifies incomplete or mismatched documentation against a labelled sample.
**Scope:** Encoding jurisdictional rules — which vary by territory for property releases, editorial restrictions and trademark treatment — turns reviewer knowledge into referenced rules and is more valuable than any single detector. Telling contributors specifically why an asset was restricted to editorial, with the remedy named, converts an invisible earning penalty into a fixable defect. 2 ML engineers, 5 months.
**Data availability:** Assets and historical classifications are complete internally. Release documents are unstructured photographs of variable quality, which is the main processing difficulty.

---

## 4. Submission Triage by Objective Quality and Catalogue Saturation
#cnns #contrastive-learning #k-nearest-neighbors #object-detection #dimensionality-reduction #evaluation-metrics #worker-facing #automation

**Problem statement:** Reviewers assess very large daily submission volumes in seconds each for technical quality, similarity, rights and policy, using reason codes that rarely describe the actual issue. A contributor rejected because the catalogue already holds two thousand similar assets receives "technical quality" and cannot act on it.

**ML task:** Objective technical quality measurement, near-duplicate clustering within and across batches, and catalogue saturation estimation by visual concept
**Input data:** Submitted assets with technical measurements of focus, noise, exposure, compression artefacts and aberration; the existing catalogue with embeddings; historical accept and reject decisions with reason codes; appeal outcomes; downstream licensing performance of accepted assets.
**Target:** An objective technical assessment, batch clusters with a best-of-cluster selection, and a saturation figure for the concept the asset occupies.
**Evaluation metric:** Consistency is the goal more than accuracy: the contributor complaint that two similar images were treated differently is a variance problem, and automating objective measures fixes variance directly. Measure decisions per reviewer hour and appeal rate, since appeals are the visible symptom of unexplained decisions. Track whether accepted assets subsequently licensed, which is the outcome feedback reviewers have never received and the only route to calibrating a standard that currently drifts informally.
**Scope:** Similarity clustering turns forty near-identical frames from one shoot into a single decision and is a direct application of embedding similarity that no reviewer workflow should be without. Catalogue saturation is the real reason behind a large share of rejections and is computable, and showing it makes both the decision and the reason code honest. Specific, actionable rejection reasons — which region is soft, which logo needs removing, how saturated the concept is — are what convert a rejection into a correction. 2 ML engineers, 4 months.
**Data availability:** Complete internally. Historical decisions provide supervision, though reason codes are coarse enough that the labels need care.
