# Machine Learning Opportunities — Brand Protection Firms

**Industry:** [[brand-protection-firms|Brand Protection Firms]]
**Derived from:** [[problems/brand-protection-firms/high-impact|High Impact]], [[problems/brand-protection-firms/low-impact-1|Low Impact 1]], [[problems/brand-protection-firms/low-impact-2|Low Impact 2]], [[problems/brand-protection-firms/worker-life-1|Worker Life 1]], [[problems/brand-protection-firms/worker-life-2|Worker Life 2]]

---

## 1. Standing Supply and Operator Survival After Enforcement
#causal-inference #survival-analysis #graph-neural-networks #bayesian-inference #confidence-intervals #hypothesis-testing #evaluation-metrics #revenue-impact

**Problem statement:** Programmes report takedowns, which is an activity measure consistent with both a working programme and an expanding counterfeit operation. The operators return within days under new accounts and the report shows a rising number.

**ML task:** Track standing infringing supply as a stock rather than counting removals, link accounts to operators, and estimate operator survival following each enforcement type
**Input data:** Longitudinal detection records across all monitored surfaces; account creation timing, image reuse, shipping patterns, pricing behaviour and catalogue overlap for operator linkage; enforcement actions with type and date; deliberate enforcement variation across product lines, marketplaces or geographies; the brand's own sales where shared.
**Target:** Volume and price of available infringing supply at a point in time, distinct operator count, and whether an operator continued trading after an action.
**Evaluation metric:** Operator survival after enforcement is the honest effect measure and is directly computable; listing counts are not. Validate operator linkage against confirmed cases from test purchases and platform disclosures. The causal question needs deliberate variation — enforcement intensity varied across comparable product lines for defined periods — which costs a brand something and is the only way to settle a question the whole category has avoided.
**Scope:** Comparing intervention types on operator survival is where this becomes actionable: listing removal, account suspension, payment disruption, logistics interdiction and supply-source action have very different costs and effects, and the current metric makes the expensive-but-effective ones invisible. The commercial obstacle is direct — a vendor paid on notice volume has no reason to build a measure that might show the notices accomplish little. 2-3 ML engineers plus a causal specialist, 9-12 months.
**Data availability:** Detection records are held by the firms longitudinally and are the unused asset. Deliberate variation must be agreed with a brand.

---

## 2. Product-Level Visual and Reference-Level Text Matching
#cnns #contrastive-learning #transformers #bert #dimensionality-reduction #k-nearest-neighbors #transfer-learning #evaluation-metrics

**Problem statement:** Detection matches images against the brand catalogue and keywords against brand names, and the sellers who matter know exactly what that matches on — so they crop, mirror, watermark, misspell, transliterate and describe products without naming them.

**ML task:** Represent products rather than photographs, and brand references rather than strings, so matching survives the standard evasions
**Input data:** The brand's product catalogue with multiple views; listing images across marketplaces and social surfaces; listing text in many languages and scripts; known evasion examples; confirmed counterfeit and confirmed legitimate listings.
**Target:** Whether a listing offers the brand's product, distinct from whether it uses the brand's photograph.
**Evaluation metric:** Evaluate specifically against adversarial transformations — crop, mirror, colour shift, watermark, partial occlusion, photograph-of-genuine-article — rather than on unmodified matching, which is the easy case current systems already handle. For text, evaluate on deliberately obfuscated brand references across scripts. Report recall on the evading subset separately, because that is the population the system exists for and aggregate accuracy will be dominated by the naive listings.
**Scope:** A photograph match is evidence about the photograph, not about the goods, and the distinction matters because the manufacturer's own image appears in legitimate reseller listings. Seller behaviour — price relative to genuine, inventory depth, shipping origin and speed, account age, review velocity, catalogue breadth — is the signal evaders cannot easily remove and should carry substantial weight. 3 ML engineers with vision and multilingual experience, 9-12 months.
**Data availability:** Catalogues and listings are available; confirmed labels come from test purchases and are expensive, which makes label efficiency a design constraint.

---

## 3. Legitimate Use Classification
#bert #transformers #cnns #gradient-boosting #confidence-intervals #contrastive-learning #evaluation-metrics #compliance

**Problem statement:** Automated detection flags legitimate resale, parallel imports, repair services, compatible parts, parody and criticism, and notice processes favour the complainant — so a wrongly-actioned small seller loses income and appeals into a process built for the party with counsel.

**ML task:** Classify flagged listings and accounts by lawful use category, and maintain an enforced allow-list of authorised resellers and distribution partners
**Input data:** Listing text, images and seller attributes; the brand's authorised reseller and distribution records; jurisdictional rules on exhaustion and parallel import; repair and compatible-parts indicators; parody and criticism signals; counter-notice and appeal outcomes as labels.
**Target:** Whether a listing represents a lawful use, adjudicated by counsel review.
**Evaluation metric:** Recall on legitimate use is the safety-critical number here, and it must be reported prominently rather than folded into an accuracy figure — the cost of a false positive is a person's income and the appeal burden falls entirely on them. Report separately by category, because parallel imports, repair and criticism have very different signatures and a system that handles resale well may hit critics hard. Counter-notice rate by detection type is a direct measure of the false positive rate and is a number no firm in this industry publishes.
**Scope:** This must be built into detection rather than bolted on afterwards: a system optimised only for recall will hit all of these, which is not an accident but a modelling choice. The authorised-partner allow-list requiring explicit review before any action removes the most commercially damaging error category outright and is mostly data work. 2 ML engineers plus IP counsel, 6-9 months.
**Data availability:** Reseller records sit with the brand; counter-notice outcomes sit with the firm and are not currently used as labels.

---

## 4. Enforcement Routing Learned From Outcomes
#gradient-boosting #survival-analysis #bert #large-language-models #confidence-intervals #evaluation-metrics #workflow-orchestration #compliance

**Problem statement:** Each platform has its own notice process, evidence standard and repeat-infringer policy, and the enforcement choice is made by whichever lever the platform makes easy rather than by which removes the operator.

**ML task:** Learn which enforcement type succeeds on which platform against which operator profile, at what evidentiary cost and with what effect on operator survival, and assemble platform-specific evidence automatically
**Input data:** Historical notices with platform, type, evidence supplied, outcome and timing; operator profiles and their subsequent behaviour; platform evidence requirements and repeat-infringer policy structures; test purchase results; counter-notice outcomes.
**Target:** Notice success, and operator cessation following the action.
**Evaluation metric:** Success rate alone is the wrong objective and is what produces the current behaviour — route on expected effect on operator survival per unit of evidentiary cost instead. Measure the use of repeat-infringer policies explicitly: most platforms have one, most trigger on accumulation, and sequencing notices to trigger them uses the platform's own mechanism to remove operators rather than listings, which nobody currently plans for.
**Scope:** Evidence assembly in each platform's required format from the detection record is mechanical work that consumes the operations team and scales linearly with volume. Counter-notice handling should be treated as a quality signal rather than an obstacle, which is a change of stance that a volume-priced contract actively discourages. 2 ML engineers, 6-9 months.
**Data availability:** Complete within the firms' notice management systems and not analysed this way.
