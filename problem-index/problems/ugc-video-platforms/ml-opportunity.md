# Machine Learning Opportunities — UGC Video Platforms

**Industry:** [[ugc-video-platforms|UGC Video Platforms]]
**Derived from:** [[problems/ugc-video-platforms/high-impact|High Impact]], [[problems/ugc-video-platforms/low-impact-1|Low Impact 1]], [[problems/ugc-video-platforms/low-impact-2|Low Impact 2]], [[problems/ugc-video-platforms/worker-life-1|Worker Life 1]], [[problems/ugc-video-platforms/worker-life-2|Worker Life 2]]

---

## 1. Localised, Calibrated Enforcement Decisions
#transformers #cnns #large-language-models #confidence-intervals #bayesian-inference #evaluation-metrics #compliance #worker-facing

**Problem statement:** Enforcement returns a policy category with no indication of which moment, phrase or element triggered it, and no confidence. The creator cannot fix what they cannot locate, the appeal has nothing specific to review, and the platform cannot perform error analysis on its own decisions.

**ML task:** Attribute each enforcement decision to the specific segment and modality that produced it, with a calibrated confidence used to route consequence and review
**Input data:** Video, audio and transcript with timestamps; policy definitions and their labelled examples; classifier outputs at segment level; historical decisions with appeal outcomes; language and content-genre metadata.
**Target:** The segment a trained human reviewer applying the policy would identify as the basis for the decision.
**Evaluation metric:** Localisation agreement with human reviewers, and calibration of the confidence — the latter is what makes routing possible and is the more consequential of the two. Report false-positive rates by policy category, by language and by content genre separately, because aggregate accuracy will look strong while performance on lower-resource languages and on journalism, health education and reclaimed speech is materially worse, which is the documented pattern and the one aggregate metrics conceal.
**Scope:** The circumvention objection is real and usually overstated: naming the thirty seconds beginning at 4:12 is not an evasion manual, and the current practice of providing nothing is the cheapest point on that trade rather than the necessary one. Low-confidence decisions with material economic consequence are where human review should be concentrated, which requires the confidence to be trustworthy. 4 ML engineers plus policy specialists, 12 months.
**Data availability:** Content and decisions are complete. Segment-level human labels for evaluation must be created deliberately and are the project's real cost.

---

## 2. Claim Legitimacy Scoring and Context-Aware Matching
#contrastive-learning #autoencoders #graph-neural-networks #gradient-boosting #confidence-intervals #evaluation-metrics #compliance #transfer-learning

**Problem statement:** Content matching answers whether a fragment corresponds to a reference and never asks whether the claim is a reasonable assertion of rights. Revenue is redirected during disputes, so claiming broadly has upside and no cost.

**ML task:** Score claimant behaviour and match context to route claims rather than act uniformly, and verify reference library submissions proportionally to the enforcement power they confer
**Input data:** Claim histories per claimant with dispute and release outcomes; match characteristics — duration, prominence in the mix, foreground versus background, position in the upload; surrounding content type including whether it is commentary or review; reference library submissions and their provenance; public domain and known-disputed repertoire.
**Target:** Whether a claim is released on dispute or upheld, as a proxy for legitimacy, supplemented by adjudicated samples.
**Evaluation metric:** Precision on flagged illegitimate claims must be high, since wrongly deprioritising a genuine rights holder's claim is a real harm in the other direction. The decisive comparison is against the current uniform treatment: measure revenue correctly retained by creators and genuine claims still enforced, together, since either alone can be gamed. Report performance on the documented failure classes — public domain repertoire, very short fragments, a creator's own original audio.
**Scope:** Claimant behaviour is highly informative and entirely unused today; a claimant with a high release-on-dispute rate across a broad content range is distinguishable from a normal rights holder with simple features. Escrowing disputed revenue rather than paying the claimant removes the incentive for speculative claiming and requires no modelling at all — the cheapest available fix. 2 ML engineers, 6-9 months.
**Data availability:** Complete inside the platform, including years of dispute outcomes that constitute a large labelled set nobody has used this way.

---

## 3. Viewer Regret and Long-Horizon Value
#markov-decision-processes #causal-inference #survival-analysis #bayesian-inference #policy-gradient-methods #confidence-intervals #evaluation-metrics #transformers

**Problem statement:** Recommendation optimises watch time because it is immediate and abundant, and nobody measures whether the viewer was glad afterwards — which is the quantity the entire public argument about these systems concerns.

**ML task:** Estimate per-session and per-recommendation regret from sparse direct survey signals plus behavioural signatures, and evaluate ranking policies against long-horizon viewer value rather than session engagement
**Input data:** Sparse non-intrusive satisfaction responses; session structure including autoplay chains, abrupt terminations and immediate app closures; return patterns over weeks and months; content characteristics; long-run individual engagement trajectories; historical ranking changes as natural experiments.
**Target:** Reported satisfaction where available, and long-horizon retention and session quality where it is not.
**Evaluation metric:** The critical test is that the regret estimate predicts held-out survey responses on viewers whose surveys were withheld — a behavioural proxy validated only against itself is circular, and that failure would be easy to miss. For policy evaluation, long-horizon viewer value measured over months in live experiments, accepting that these experiments are slow and expensive and that there is no shortcut.
**Scope:** The creator-side elasticity belongs in the same programme: what the recommender rewards determines what gets produced, and the effect of a ranking change on the content mix is estimable from the platform's own history of ranking changes. That makes the production consequences of an objective change visible before deployment rather than after it has reshaped a genre. 4 ML engineers plus researchers, 12-18 months.
**Data availability:** Behavioural data is complete. Direct satisfaction signals are sparse by design and are the binding constraint on validation.

---

## 4. Moderator Exposure Reduction and Load Management
#transformers #cnns #large-language-models #gradient-boosting #evaluation-metrics #confidence-intervals #worker-facing #compliance

**Problem statement:** Human reviewers see the most severe material on the internet under throughput targets, and a substantial share of that exposure is avoidable — material presented at full fidelity that could be reduced, whole videos viewed where nine seconds were at issue, and severe categories concentrated on whoever is next in the queue.

**ML task:** Determine what genuinely requires human viewing and at what fidelity, isolate the segment in question, and model cumulative exposure per reviewer to enforce rotation limits
**Input data:** Content with segment-level classifier outputs and severity estimates; historical review decisions and the information actually used to reach them; per-reviewer exposure history by severity category; audit outcomes and reviewer accuracy; queue composition over time.
**Target:** Whether a human decision can be reached correctly from a reduced presentation — blurred, greyscale, muted, thumbnail, transcript summary, or an isolated segment — rather than full-fidelity viewing.
**Evaluation metric:** Decision accuracy under reduced presentation against full-fidelity review is the safety-critical measure: exposure reduction that degrades decision quality has traded one harm for another and must be rejected. Then measure the exposure actually removed — severe items not viewed, minutes of full-fidelity viewing avoided — as the outcome that matters. Track cumulative per-reviewer severe-category exposure as a managed health metric with enforced limits, in the way professions with comparable known risk have long done.
**Scope:** Every unit of exposure removed is a direct reduction in documented occupational injury, which makes this the highest-value application of these platforms' own models to their own operation. Audit incentives need fixing alongside it: quality audits that penalise contextual correctness in favour of literal policy application teach reviewers to stop thinking, and produce exactly the enforcement errors creators experience as inexplicable. Extending these protections to vendor-employed staff on the same terms is a contractual decision, not a technical one. 3 ML engineers plus occupational health input, 9-12 months.
**Data availability:** Complete. Reviewer exposure data exists in workflow systems and is generally not used as a health metric.
