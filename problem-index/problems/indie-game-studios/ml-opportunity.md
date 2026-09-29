# Machine Learning Opportunities — Indie Game Studios

**Industry:** [[indie-game-studios|Indie Game Studios]]
**Derived from:** [[problems/indie-game-studios/high-impact|High Impact]], [[problems/indie-game-studios/low-impact-1|Low Impact 1]], [[problems/indie-game-studios/low-impact-2|Low Impact 2]], [[problems/indie-game-studios/worker-life-1|Worker Life 1]], [[problems/indie-game-studios/worker-life-2|Worker Life 2]]

---

## 1. Launch Outcome Forecasting From Pre-Release Trajectory
#time-series-forecasting #survival-analysis #gradient-boosting #bayesian-inference #confidence-intervals #probability-distributions #evaluation-metrics #revenue-impact

**Problem statement:** A studio spends its entire runway before receiving any commercial signal, while wishlist trajectory, demo retention and review velocity are observable eighteen months earlier and uninterpretable without knowing what a healthy curve looks like for that genre — which requires seeing thousands of other games.

**ML task:** Predict the distribution of launch-window and first-year revenue from pre-release trajectory signals, benchmarked against a cross-studio corpus
**Input data:** Wishlist accumulation curves and their response to public beats; demo download and retention data; festival participation and its effect; trailer view and completion metrics; genre, price band, platform mix and launch window; realised sales outcomes contributed by participating studios.
**Target:** Revenue in the launch window and at twelve months, as a distribution.
**Evaluation metric:** Interval calibration on held-out titles, evaluated at several points in development — the forecast's value is that it updates, so accuracy at twelve months before launch matters as much as at one month. Report the interval width honestly; early in development it will be very wide, and a product that narrows it artificially is selling false confidence to people deciding whether to spend another year. Beware survivorship: the corpus must include games that sold almost nothing, which are the hardest to recruit and the most informative.
**Scope:** No individual studio can build this — one game is one observation, and a career yields two or three. The corpus requires studios to contribute their own outcomes into a pool, which has been done informally in developer communities and never systematically. The causal question — would a different trailer or price have helped — is not answerable from trajectory data and the product must not imply it is. 2 ML engineers plus a community-building effort, 9-12 months.
**Data availability:** Each studio holds its own data and nothing else. Third-party estimators reconstruct approximate sales from review counts with meaningful error, which is a usable seed and not a substitute for contributed truth.

---

## 2. Store Asset Attribute Effects Across a Cross-Title Corpus
#cnns #transformers #bert #contrastive-learning #gradient-boosting #hypothesis-testing #confidence-intervals #evaluation-metrics

**Problem statement:** Capsule art, trailer opening and store copy determine wishlist conversion, are chosen once on instinct, and cannot be tested within a small title because it lacks the traffic for a reliable comparison — which is exactly the population that most needs the answer.

**ML task:** Code store assets by content attributes and estimate their effect on conversion by genre and traffic source, pooling across many titles
**Input data:** Capsule art, screenshots, trailers and store copy across a large title corpus; attribute coding derived from the assets themselves — readability at thumbnail size, subject framing, text presence, colour and contrast, trailer opening content and pacing; impressions, click-through and wishlist conversion by traffic source; genre and price.
**Target:** Wishlist conversion rate given impression, attributable to asset attributes rather than to title identity.
**Evaluation metric:** Prospective validation is the only honest test — titles that change assets according to the model should show measurably higher conversion than a matched set that did not. Retrospective fit will be dominated by game quality and genre appeal, which confound every asset comparison and will make a correlational model look excellent while being useless. Report effects by genre separately; the craft rules practitioners circulate are probably genre-specific and have never been tested.
**Scope:** Attributes transfer across titles, assets do not, which is what makes a pooled model both useful and uncontroversial. The value is concentrated in low-traffic titles that can never run their own test, so the model must be evaluated on exactly that segment rather than on the large titles where it is easiest. 2 ML engineers with vision experience, 6-9 months.
**Data availability:** Assets are public. Conversion data is per-studio and requires the same contribution pool as item 1, which makes these one programme.

---

## 3. Completion Forecasting From Velocity and Discovery Rate
#time-series-forecasting #survival-analysis #bayesian-inference #confidence-intervals #gradient-boosting #evaluation-metrics #probability-distributions #worker-facing

**Problem statement:** Small teams plan eighteen months and take three years, funded from savings, and the overrun kills more studios than bad games do. The variable that actually drives it — the rate at which new work is discovered — is visible in every issue tracker and measured by nobody.

**ML task:** Forecast completion date as a distribution from observed task completion velocity and task discovery rate, distinguishing exploratory from known work
**Input data:** Issue tracker history — task creation, completion, reopening, estimate versus actual; task classification as exploratory or specified; team size and availability over time; project phase; comparable projects' trajectories where a corpus exists.
**Target:** Date of feature completion and of ship readiness, as a distribution.
**Evaluation metric:** Interval calibration against actual completion on finished projects. The critical property is that the interval be genuinely wide early and narrow late — a forecast that is precise in year one is wrong, and a model that reports precision it does not have would be worse than the plan it replaces, because it would be believed. Measure the discovery rate's contribution explicitly, since the claim is that it dominates and it should be demonstrated.
**Scope:** This works from data every team already generates in an ordinary tracker, which makes it unusually low-friction. Presenting the forecast against the runway is what converts it into a decision — the question is never when the game will be done, it is whether the money reaches it. 1-2 ML engineers, 4-6 months.
**Data availability:** Complete in any team using a tracker, though task classification as exploratory versus specified usually needs to be added.

---

## 4. Platform Requirement Checking and Certification Failure Prediction
#large-language-models #bert #gradient-boosting #change-point-detection #evaluation-metrics #compliance #automation #transfer-learning

**Problem statement:** Console certification failures are routine for teams submitting for the first time, each rejection costs a week, and the requirement documents describe testable behaviours that nobody checks automatically.

**ML task:** Map platform requirement documents to automated checks against a build, engine-aware, and predict which requirements a given project is most likely to fail before submission
**Input data:** Platform requirement documentation; build artefacts and runtime behaviour under test harnesses; engine and project structure; project characteristics — genre, save system design, multiplayer, platform mix; the team's prior submission history and outcomes.
**Target:** Certification failure on a specific requirement.
**Evaluation metric:** Recall on requirements that actually caused rejections, measured against submission history, since a missed requirement costs a week and a false alarm costs an hour — the asymmetry is severe and the threshold should reflect it. Precision still matters enough that the output must be a short prioritised list rather than every requirement flagged. Report by platform, since failure patterns differ substantially.
**Scope:** Requirement documentation is under NDA and each platform is a separate integration, which is the practical barrier and the reason no general tool exists. Engine-awareness is essential — the same requirement is checked differently in Unity, Unreal and a custom engine. Failure prediction is the piece that encodes what porting studios sell, which makes it valuable and also makes them the natural builder or the natural opponent. 2 engineers with console experience, 6-9 months per platform pair.
**Data availability:** Requirements are obtainable under developer agreements. Submission outcome history exists per studio and is small; pooling it across studios is what makes prediction possible.
