# Machine Learning Opportunities — Esports Organizations

**Industry:** [[esports-organizations|Esports Organizations]]
**Derived from:** [[problems/esports-organizations/high-impact|High Impact]], [[problems/esports-organizations/low-impact-1|Low Impact 1]], [[problems/esports-organizations/low-impact-2|Low Impact 2]], [[problems/esports-organizations/worker-life-1|Worker Life 1]], [[problems/esports-organizations/worker-life-2|Worker Life 2]]

---

## 1. Unified Attention Measurement Across Fragmented Surfaces
#cnns #causal-inference #bayesian-inference #confidence-intervals #gradient-boosting #hypothesis-testing #evaluation-metrics #revenue-impact

**Problem statement:** Essentially all revenue comes from sponsors buying attention that is spread across a broadcast the organisation does not control, a dozen player streams on three platforms, short-form clips that travel without attribution, and social accounts — with incompatible metrics and no outcome data returned.

**ML task:** Construct a consistent attention unit across surfaces — weighted by prominence and likely notice — and attribute delivery per sponsorship placement rather than per deal
**Input data:** Broadcast video with logo and mention detection including size, duration and screen position; stream viewership with concurrency and session structure; short-form clip performance including derivative uploads identified by watermark or audio fingerprint; social engagement; sponsor-returned outcome signals where negotiated — codes, links, app installs.
**Target:** Attention-seconds delivered per placement, and where outcome data exists, the sponsor-side effect.
**Evaluation metric:** The critical discipline is refusing to sum incomparable things: a logo visible in a corner during a replay and a thirty-second integrated read are not the same unit, and an aggregate that treats them alike is the impressive meaningless number the sector already produces. Publish the weighting methodology and its uncertainty. Validate the prominence weighting against attention research where it exists, and state plainly where the weights are assumptions rather than measurements.
**Scope:** A smaller defensible number with a published method is worth more to a sceptical sponsor than a larger indefensible one, which is the opposite of the sector's instinct and is the product decision this stands or falls on. Pooling sponsor-returned outcomes across deals would build the first genuine evidence base about what esports sponsorship does. 2-3 ML engineers with video experience, 9-12 months.
**Data availability:** Fragmented across parties who have no obligation to help, which is the core difficulty. Broadcast video, stream metrics and social data are obtainable; derivative clip tracking requires fingerprinting infrastructure.

---

## 2. Context-Adjusted Player Contribution and Patch Robustness
#gradient-boosting #bayesian-inference #graph-neural-networks #confidence-intervals #transfer-learning #causal-inference #hypothesis-testing #evaluation-metrics

**Problem statement:** Rosters are the largest controllable cost and are assembled on statistics shaped by patch, meta, role, teammates and league strength — so a player's numbers on one team are a poor guide to their contribution on another, and multi-year contracts are signed on that basis.

**ML task:** Estimate individual contribution adjusted for role, teammates, patch and league strength, and identify traits that persist across metas — including adaptation rate measured in the weeks after each patch
**Input data:** Event-level match data from publisher APIs and demo parsing; role assignment and team structure; patch versions with change content; teammate identity and quality; league and opponent strength; historical transfers with before-and-after performance.
**Target:** Performance after a transfer, which is the decision the evaluation is for — not performance in the observed context, which is what current statistics describe.
**Evaluation metric:** Prediction of post-transfer performance on held-out transfers is the only test that matters, and it is the test the sector has never run on its own scouting. Report calibrated intervals: competitive samples are small, seasons are short, and a confident point rating on forty matches overstates the evidence, particularly for the young players whose signings carry the most risk. Evaluate adaptation rate separately, since it is the trait most likely to transfer and is essentially never computed.
**Scope:** Each title's data is different enough that nothing transfers between them, so this is built per title — which is why it has not been built generally and why a title-specific build is defensible. Roster fit and synergy is the extension where most of the money is lost and requires modelling the team as a structure rather than as a set of individuals. 2 ML engineers per title plus an analyst, 6-9 months.
**Data availability:** Rich for major titles through publisher APIs and demo parsing. Transfer outcome history is public and is the label set nobody uses.

---

## 3. Game-State-Aware Highlight Detection and Cross-Platform Routing
#cnns #transformers #contrastive-learning #large-language-models #gradient-boosting #evaluation-metrics #automation #transfer-learning

**Problem statement:** Content is now where the revenue comes from, hundreds of hours of stream footage are reviewed by hand each week, and the automated tooling detects chat spikes — which finds loud moments rather than good ones and misses quiet skill, narrative beats and anything that happened when few people were watching.

**ML task:** Detect clip-worthy moments from game state combined with audio, player reaction and chat, tuned to this organisation's audience, and route each clip to the platform where its kind of moment performs
**Input data:** Stream video and audio; game state through the same publisher APIs the performance analysts already use; chat activity; player voice and reaction; the organisation's own posting history and per-platform performance; platform format conventions.
**Target:** Whether a moment, once clipped and posted, performs above the organisation's own baseline for that platform.
**Evaluation metric:** Compare against the chat-spike baseline directly, since that is the incumbent and the claim is that game state adds something it cannot see. Measure recall on moments the community clipped and the organisation missed — those are labelled misses sitting in public and are the cheapest available evaluation set. Per-platform routing is evaluated by whether the same clip does better on the recommended surface than on the default one.
**Scope:** Game state is the unused signal and is available through infrastructure the organisation already runs for coaching. Tuning to the organisation's own voice — which players, what tone, what kind of moment — is what separates useful automation from a firehose. Clip attribution through watermarking and audio fingerprinting feeds directly into item 1, which makes these one programme. 2 ML engineers, 6-9 months.
**Data availability:** Complete. Stream archives, game state and posting performance are all held by the organisation.

---

## 4. Practice Load, Injury Risk and Honest Decline Detection
#survival-analysis #change-point-detection #gradient-boosting #time-series-forecasting #confidence-intervals #hypothesis-testing #evaluation-metrics #worker-facing

**Problem statement:** Practice regimes of ten to fourteen hours a day have been standard for a decade with no analysis of what they do to performance or to injury rates, and performance decline is noticed when results drop — at which point the contract conversation is already adversarial.

**ML task:** Relate practice load, input volume, break patterns and sleep timing to performance and to reported injury; and separate genuine decline from form variance and meta mismatch
**Input data:** Practice and scrim hours with timing; input volume and rate where instrumented; competitive performance over time; reported injuries and their timing; patch history and role changes; sleep and travel schedules; age and tenure.
**Target:** Performance outcomes and injury incidence as a function of load; and the distinction between temporary form variance, meta mismatch and durable decline.
**Evaluation metric:** For load, the finding that matters is whether a threshold exists beyond which additional practice degrades performance — established decades ago in other competitive disciplines and never tested here. Report it with intervals and with the confounding acknowledged, since teams that practise more may differ in other ways. For decline, measure how early a durable decline is distinguishable from a dip, because the entire value is protecting players from being released for the wrong reason and organisations from releasing players they should keep.
**Scope:** This should be built with player representatives involved rather than only for organisations, because a load model in the hands of one party is a management tool and in the hands of both is evidence. Injury data requires medical reporting that most of the sector does not collect and is the gating input. 2 ML engineers plus sports science input, 9-12 months.
**Data availability:** Practice logs exist unevenly. Competitive performance is public. Injury and medical data is largely uncollected, which is itself the finding.
