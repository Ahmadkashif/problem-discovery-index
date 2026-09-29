# Machine Learning Opportunities — Digital Goods Marketplaces

**Industry:** [[digital-goods-marketplaces|Digital Goods Marketplaces]]
**Derived from:** [[problems/digital-goods-marketplaces/high-impact|High Impact]], [[problems/digital-goods-marketplaces/low-impact-1|Low Impact 1]], [[problems/digital-goods-marketplaces/low-impact-2|Low Impact 2]], [[problems/digital-goods-marketplaces/worker-life-1|Worker Life 1]], [[problems/digital-goods-marketplaces/worker-life-2|Worker Life 2]]

---

## 1. Cross-Format Fingerprinting for Redistribution Detection
#cnns #contrastive-learning #transformers #dimensionality-reduction #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance

**Problem statement:** A digital good copies perfectly at zero cost, so redistribution substitutes directly for sales, and enforcement is delegated to solo creators searching for their own products by hand. The platform holds the complete asset corpus that any detection system would need.

**ML task:** Robust fingerprinting across asset formats — perceptual for images and video, structural for code and templates, glyph-level for fonts, parameter-level for presets — plus continuous matching against public sources
**Input data:** The full asset corpus with format and category; confirmed redistribution instances from historical takedowns; crawled public sources including file-sharing sites, forums and competing marketplaces; asset transformations observed in the wild such as re-encoding, cropping and repackaging; per-purchase watermark records where deployed.
**Target:** A match between a publicly available file and a marketplace asset, robust to the transformations redistributors actually apply.
**Evaluation metric:** Recall on confirmed redistribution instances at a precision high enough that automated notices are safe — a false match generates a wrongful takedown against a third party, which carries its own legal exposure. Report robustness separately against each transformation class, since re-encoding, cropping and repackaging defeat naive hashing at very different rates.
**Scope:** The industry assumed fingerprinting meant perceptual hashing and therefore concluded it does not apply to fonts, code, templates and presets — structural and parameter-level signatures for these formats are feasible and essentially unexplored, and they cover the categories where redistribution is most endemic. Per-purchase watermarking is a delivery-path change rather than a modelling one and changes the deterrent structure entirely by making a leaked copy identify its origin. The economics of enforcement, not the technology, are the real obstacle, which is the argument for centralising detection at the platform. 3 ML engineers, 6-7 months.
**Data availability:** The asset corpus is complete. Confirmed redistribution instances exist in takedown records and undercount enormously, since most redistribution is never discovered.

---

## 2. Licence Term Extraction and Usage Verification
#large-language-models #bert #transformers #word-embeddings #transfer-learning #evaluation-metrics #compliance #data-integration

**Problem statement:** Licence terms are prose in a purchase agreement, the delivered file is identical across tiers, and nothing downstream knows what was permitted. Buyers who want to comply cannot determine what they are entitled to, and creators cannot establish what was breached.

**ML task:** Structuring licence terms into machine-readable entitlements, plus detecting usage that exceeds them for asset types where use is observable
**Input data:** Licence agreements and tier definitions per platform; purchase records with buyer, tier and asset; asset fingerprints; publicly observable usage such as fonts on websites and assets in published products; organisational structure where team purchasing exists; historical breach claims and their resolutions.
**Target:** Structured entitlements — permitted uses, seat counts, distribution limits, territory, duration — and detected usage exceeding them.
**Evaluation metric:** Field-level extraction accuracy against legally reviewed agreements, weighted toward the terms that generate disputes: commercial use, distribution and seat count. For usage verification, precision is the binding constraint since a false breach allegation against a paying customer is a serious commercial and legal error.
**Scope:** Licence documents are fairly standardised per platform and highly variable across them, which suits template-aware extraction. The extraction is the precondition for everything else and is bounded. Usage verification is only feasible for observable contexts — fonts on public sites, assets in published apps or games — and should be framed as helping compliant buyers stay compliant rather than as surveillance, since most breach is unintentional and originates in the gap between individual purchase and organisational use. 2 ML engineers plus licensing counsel, 4-5 months.
**Data availability:** Agreements and purchase records are complete. Observable usage requires crawling and is limited to particular asset types. Team and organisational structure is poorly captured, which is where most unintentional breach originates.

---

## 3. Style Vocabulary Induction from Query-Purchase Behaviour
#contrastive-learning #cnns #transformers #word-embeddings #dimensionality-reduction #k-nearest-neighbors #evaluation-metrics #gradient-boosting

**Problem statement:** Buyers search for a feeling, an era or a compatibility requirement, and there is no shared vocabulary for aesthetic qualities. Creator-supplied tags are inconsistent and aspirational, similarity search requires a starting example the buyer often lacks, and work that is not found earns nothing.

**ML task:** Learning a joint embedding between natural language descriptions and asset appearance, with a style vocabulary induced from what buyers search and subsequently purchase
**Input data:** Search queries with subsequent clicks and purchases — millions of pairs encoding exactly the language-to-asset mapping; asset files and imagery; creator tags as a weak prior; category structure; buyer purchase histories; refund and review text indicating mismatch.
**Target:** The asset a buyer purchased following a query, and an induced vocabulary of aesthetic descriptors grounded in that behaviour.
**Evaluation metric:** Purchase conversion on surfaced results rather than click-through, since a click on an asset that turns out to be wrong produces a refund and a poor review. Report results separately for new creators, since discovery for unfound work is where the supply-side value concentrates and aggregate metrics are dominated by established sellers.
**Scope:** The query-to-purchase corpus is the asset here — it is the only place a grounded aesthetic vocabulary could come from, and it exists only inside these marketplaces. Compatibility should be extracted from files rather than from creator descriptions: engine versions, application requirements, glyph coverage and format support are readable directly and are a hard filter that currently fails softly, producing refunds. Bundle coherence — assets that work together — is a distinct objective from individual relevance. 2-3 ML engineers, 5 months.
**Data availability:** Query and purchase logs are complete and large. Asset files are held. Refund reasons indicating discovery mismatch are captured inconsistently and are a useful negative signal.

---

## 4. Originality Assessment and Claim Triage
#contrastive-learning #cnns #bert #dimensionality-reduction #confidence-intervals #hypothesis-testing #evaluation-metrics #compliance

**Problem statement:** Reviewers decide copyright and originality questions in minutes, at volume, between two creators who both earn from the platform, on evidence consisting of two files and two assertions. The asymmetry between liability and creator harm drives liberal removal.

**ML task:** Similarity measurement on the specific elements at issue, corpus-wide common-convention detection, and triage separating clear cases from the genuinely contested middle
**Input data:** Claimed and accused assets with upload timestamps and creation history; both creators' prior catalogues; the full marketplace corpus for convention baselines; historical claim decisions and their reasoning; appeal outcomes; claim patterns between creators.
**Target:** The claim decision as confirmed after any appeal, which is a more honest label than the initial decision.
**Evaluation metric:** Precision and recall reported separately for upheld and rejected claims, since the costs fall on different parties and a single accuracy figure hides which way errors go. Appeal overturn rate is the operational quality measure and the only signal that the removal threshold is miscalibrated.
**Scope:** Common-convention detection is the genuinely useful contribution: where similarity between two assets is explained by a pattern widespread across the corpus, that is directly relevant to whether the shared elements are protectable, and it is measurable against the whole catalogue in a way no individual reviewer can approximate. Tactical claim detection — patterns of claims between competing creators — protects the party being targeted and is visible in the claim graph. This assists a legal judgement and must not make one. 2-3 ML engineers plus counsel, 5-6 months.
**Data availability:** Assets, timestamps and decisions are complete. Appeal outcomes are recorded inconsistently and are the most valuable label since they indicate where the initial decision was wrong.
