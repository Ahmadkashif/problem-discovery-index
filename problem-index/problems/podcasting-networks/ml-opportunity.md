# Machine Learning Opportunities — Podcasting Networks

**Industry:** [[podcasting-networks|Podcasting Networks]]
**Derived from:** [[problems/podcasting-networks/high-impact|High Impact]], [[problems/podcasting-networks/low-impact-1|Low Impact 1]], [[problems/podcasting-networks/low-impact-2|Low Impact 2]], [[problems/podcasting-networks/worker-life-1|Worker Life 1]], [[problems/podcasting-networks/worker-life-2|Worker Life 2]]

---

## 1. Show Retention Prediction from Pilot Audio Signals
#lstm #gradient-boosting #regression #nlp #speech-processing #tacit-knowledge-ml

**Problem statement:** Experienced producers listen to a pilot episode and predict whether listeners will return for episode 3 — reading host chemistry, pacing, topic coherence, and production quality cues that they cannot fully articulate but act on consistently. This tacit judgment needs to be captured in a model that can evaluate pre-release audio at scale.

**ML task:** Regression (predicted episode 3 retention rate as a continuous value between 0 and 1)
**Input data:** Raw pilot episode audio (WAV/MP3, typically 30-90 minutes) processed into: (a) speech-processing features — vocal energy variance per speaker, turn-taking cadence, crosstalk frequency, silence gap distribution, laughter/reaction event density, speaking rate variance; (b) NLP features from auto-transcript — topic coherence score across segments, question density, narrative arc structure (setup/tension/resolution patterns), vocabulary richness, guest vs. host talk ratio; (c) tabular metadata — show category, host prior podcast experience, episode duration, planned release cadence, number of competing shows in category.
**Target:** Episode 3 retention rate (listeners who download episode 3 / listeners who download episode 1), measured 30 days post-launch. Sourced from network analytics dashboards (Megaphone, Chartable).
**Evaluation metric:** RMSE on held-out shows, with secondary emphasis on Spearman rank correlation (the model must correctly rank shows from highest to lowest retention, even if point estimates are off). Asymmetric loss weighting: under-predicting retention for a good show is less costly than over-predicting retention for a bad show (the latter wastes production budget).
**Scope:** This is a 6-9 month build requiring a team of 2-3 (ML engineer, audio/NLP specialist, data engineer). The audio feature extraction pipeline is the hardest component — extracting meaningful prosodic features from conversational podcast audio is significantly harder than from clean speech. The model likely starts as a gradient-boosted ensemble on hand-engineered features, with LSTM components added for temporal audio patterns once the feature pipeline is validated.
**Data availability:** Medium difficulty. Networks have download data and episode audio but typically lack per-listener retention curves (Spotify holds this data). A practical proxy is cohort-level download decay (ep1 vs ep3 downloads). Labeling requires aligning audio features with 30-day-lagged retention outcomes. A network with 200+ show launches over 3 years has a workable training set; smaller networks would need to pool data.

---

## 2. Episode Performance Prediction
#gradient-boosting #regression #tabular-ml #nlp #revenue-impact

**Problem statement:** After a show is established, networks need to predict which upcoming episodes will over- or under-perform the show's baseline, so they can allocate marketing spend, schedule cross-promos, and price ad inventory dynamically.

**ML task:** Regression (predicted download count within 7 days of release, normalized as a multiplier of the show's trailing 8-episode average)
**Input data:** Tabular features per episode — release day/time, episode duration, days since last episode, guest presence (yes/no), guest social media following, episode title keyword embeddings, topic similarity to recent high-performing episodes in the category, concurrent release density (how many competing shows publish that day). NLP features from episode description and transcript preview — topic novelty score, clickbait indicators, question hooks.
**Target:** 7-day download count as a ratio to the show's trailing average. Sourced from hosting platform analytics.
**Evaluation metric:** MAE on the multiplier (a prediction of 1.2x vs actual 1.3x is a 0.1 error). Secondary: binary accuracy on "will this episode exceed the show's average?" (threshold at 1.0x).
**Scope:** 3-4 month build for one ML engineer. Feature engineering is straightforward since all inputs are tabular or short-text. The main challenge is that episode performance has high variance driven by external events (a true-crime show spikes when its subject appears in the news), and the model must gracefully handle these exogenous shocks rather than overfitting to them.
**Data availability:** High. Networks have complete episode-level download histories going back years. Guest metadata can be scraped from show notes and social platforms. No manual labeling needed — the target variable is directly observable.

---

## 3. Sponsor-Show Matching
#gradient-boosting #recommendation #tabular-ml #nlp

**Problem statement:** Mid-tier shows are under-monetized because programmatic ad tools match on category and CPM rather than content-brand psychographic alignment. A recommendation model that surfaces non-obvious sponsor-show pairings with explainable fit scores would unlock revenue currently left on the table.

**ML task:** Recommendation with ranking (given a show, rank candidate sponsors by predicted campaign performance; given a sponsor, rank candidate shows)
**Input data:** Show features — transcript-derived topic clusters (via LDA or embedding clustering), audience demographic estimates, listener review sentiment, episode-level engagement metrics, historical sponsor performance on the show. Sponsor features — product category, brand voice descriptors, target demographic, historical podcast ad spend and performance across shows, creative style (host-read vs. pre-produced).
**Target:** Campaign performance metric: either cost-per-acquisition (CPA) for direct-response sponsors or brand lift survey delta for awareness sponsors. Where CPA is unavailable, proxy with sponsor renewal rate (did the sponsor re-book after the initial campaign?).
**Evaluation metric:** NDCG@10 for the ranked list of sponsor-show pairings. Secondary: precision@5 (are the top 5 recommendations all viable pairings that a sales rep would agree to pitch?).
**Scope:** 4-6 month build, 2 engineers (ML + data). The cold-start problem is significant: new shows and new-to-podcast sponsors have no historical performance data, so the model must fall back to content-based features. Building the sponsor feature set requires ingesting data from multiple sources (Magellan AI for competitive brand tracking, LinkedIn for brand contacts, the network's own CRM).
**Data availability:** Medium. Networks have their own campaign performance data, but it is siloed per network. Magellan AI and Podscribe provide cross-network brand activity data at a cost. Sponsor features require enrichment from external sources. A single mid-size network may have 200-500 historical campaigns — enough to train a gradient-boosted model but not a deep learning approach.

---

## 4. Audience Growth Forecasting
#gradient-boosting #time-series-forecasting #tabular-ml

**Problem statement:** Network executives make catalog investment decisions (which shows to renew, which to sunset, where to allocate marketing budget) using trailing download trends and gut feel. A forecasting model that projects audience trajectory 3-6 months out would enable data-driven portfolio management.

**ML task:** Time-series forecasting (predict monthly average downloads per episode for each show, 3 and 6 months forward)
**Input data:** Time-series features — weekly download history per show (minimum 12 weeks), download trend slope, variance, seasonality pattern. Contextual features — show category growth rate, number of new competing shows launched in the category per month, cross-promo activity (number and placement of promos for this show), social media mention velocity, Apple Podcasts chart position history, review volume and sentiment trend.
**Target:** Monthly average downloads per episode at T+3 and T+6 months. Sourced from hosting platform analytics.
**Evaluation metric:** MAPE (mean absolute percentage error) on held-out future periods. Secondary: directional accuracy (did the model correctly predict growth vs. decline?). Directional accuracy matters more than point accuracy for portfolio decisions.
**Scope:** 3-4 month build, 1-2 engineers. Gradient-boosted models (LightGBM) on engineered time-series features will likely outperform deep learning given the small number of shows per network (50-200). The key challenge is incorporating exogenous signals (category trends, competitor launches) that drive inflection points the time-series alone cannot predict.
**Data availability:** High for download data; medium for external signals. Apple Podcasts chart data can be scraped or purchased. Social media mention data requires API access. Category-level growth rates can be estimated from Podtrac industry reports. No manual labeling needed.
