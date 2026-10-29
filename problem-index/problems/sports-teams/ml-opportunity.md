# Machine Learning Opportunities — Sports Teams & Clubs

**Industry:** [[sports-teams|Sports Teams & Clubs]]
**Derived from:** [[problems/sports-teams/high-impact|High Impact]], [[problems/sports-teams/low-impact-1|Low Impact 1]], [[problems/sports-teams/low-impact-2|Low Impact 2]], [[problems/sports-teams/worker-life-1|Worker Life 1]], [[problems/sports-teams/worker-life-2|Worker Life 2]]

---

## 1. Learning the Area Scout's Projection
#tacit-knowledge-ml #gradient-boosting #survival-analysis #large-language-models #transformers #evaluation-metrics #feature-engineering #revenue-impact

**Problem statement:** Veteran scouts read an amateur player's delivery, body and makeup and "know" what he will become, a judgement built from thousands of looks that they cannot specify and that leaves with them. The ML problem is to learn, from each scout's historical reports and the later careers of the players they saw, which parts of their read carry information beyond measured traits, and to surface it with a track record.

**ML task:** Time-to-event modelling of professional outcomes (time to Double-A, time to MLB debut, career value over six years) from structured grades, embedded free-text report passages and tracking features; plus scout-level calibration of stated future value.
**Input data:** Scouting reports (20–80 grades, future value, free-text notes, dates, scout ID) from the club's scouting system; amateur tracking (pitch velocity, spin, release, bat speed from TrackMan, Hawk-Eye or portable units) and video timestamps; amateur stat lines; the draft (every club's picks and bonuses, public); minor- and major-league outcomes from public game logs.
**Target:** Hazard of reaching each level by year; six-year career value; and the residual of outcome over what tracking and draft slot already predict, attributed to report content and scout.
**Evaluation metric:** Concordance index and integrated Brier score for the survival model, measured strictly by draft year (train on 2012–2018 classes, test on 2019–2020), because random splits leak a scout's later knowledge. The headline is incremental value: does adding report text and scout identity improve calibration over a tracking-plus-slot baseline? For scout calibration, report each scout's future-value grade against realised value with confidence intervals sized to his small number of signed players. Missing a later-blooming player costs more than a false positive at the cross-checker stage, so report recall in the top tier of realised outcomes.
**Scope:** The data-collection challenge is the hardest part. The expert's read has to be captured as he scouts, so the product starts as a voice-to-report tool at the park that saves him time, with clip and pitch timestamps attached. History must be reconstructed from old reports whose scales drifted. The labelling challenge is that scouts disagree with themselves: the same scout grades the same player differently after a good or bad look, so repeated reports on one player must be used to estimate each scout's own consistency, which caps the achievable agreement. Outcomes are also selected (only signed players have pro careers) and confounded by development. The deployment challenge is speed: the signal must reach a cross-checker before he travels and the draft room within minutes, faster than the director's own recall, or it is ignored. 2 ML engineers and 1 baseball analyst, 6–9 months, with value appearing first as retrieval ("this scout's last six 'projectable frame' pitchers and how they turned out").
**Data availability:** Reports and scout IDs sit only inside each club; outcomes, draft picks and most minor-league stats are public; amateur tracking coverage is growing but patchy below college level. No pooled dataset exists across clubs, and none should be assumed.

---

## 2. Minor-League Per-Game Demand and Price-Tier Model
#gradient-boosting #bayesian-inference #time-series-forecasting #feature-engineering #quick-win #revenue-impact

**Problem statement:** Predict paid attendance by seat tier for every upcoming home date at a minor-league club and recommend a price for each tier, so prime dates are priced up and weeknights filled, using signals available weeks ahead and a demand prior pooled across clubs.

**ML task:** Hierarchical regression of per-game attendance (club, level and league effects with partial pooling) with gradient-boosted residuals; a tier-level price-response curve fit on price changes; and constrained revenue optimisation per date.
**Input data:** Game schedules, start times and announced attendance from the MLB Stats API across affiliated levels; club promotions calendars (fireworks, giveaways, theme nights) scraped from club sites; NOAA weather history and forecasts; school and holiday calendars; local competing events; SeatGeek public-API lowest and highest listed prices and listing counts per game as a resale-demand signal; and, for the MVP, a synthetic primary-sales generator per tier calibrated to announced attendance.
**Target:** Paid attendance per tier per game; the price elasticity per tier and date type; a recommended price per tier.
**Evaluation metric:** Mean absolute percentage error of game-level attendance on a held-out final month and on a held-out club (a new pilot club has little history), against a naive "same promo, last season" baseline. For pricing, simulated revenue per available seat against the club's flat-price season, reported with uncertainty, because the elasticity is fit on few price changes. Under-forecasting a sell-out costs more than over-forecasting a Tuesday, so report error separately on the top-decile demand dates.
**Scope:** This is the two-week MVP: one engineer builds the scraper and feature set in the first week, the pooled model and a price-tier recommender in the second, and shows backtests on a dozen clubs. Production needs a pilot club's real tier-level sales (to replace the synthetic generator), a licence or the club's own feed for MLB data (MLB's data notice limits commercial and bulk use, not checked here), and a season to measure lift in a controlled way (alternate dates or comparable clubs).
**Data availability:** Schedules and announced attendance are public; announced attendance counts tickets sold, including no-shows and comps, so it is an upper bound on paid demand. Resale listing prices are public through SeatGeek's free API (search summary), but listing-level detail needs partner access. Tier-level primary sales belong to each club and its ticketer.

---

## 3. Sponsor Exposure Detection and Outcome Lift
#cnns #object-detection #causal-inference #hypothesis-testing #confidence-intervals #revenue-impact

**Problem statement:** Measure what each partner actually received, logo exposure by placement, size, clarity and duration across broadcast, stream and social, reconcile it to contract entitlements, and, where a partner shares outcome data, estimate the sponsorship's incremental effect on the partner's business.

**ML task:** Logo detection and tracking in video frames with clarity and occlusion scoring; entitlement extraction from contracts with an LLM into a schedule of countable obligations; geo-holdout or synthetic-control lift estimation on partner outcomes.
**Input data:** Licensed broadcast and stream video and the club's own social posts; LED and video-board play logs; partner contracts; partner outcome data (store sales by market, app installs, site visits, redemption codes) shared under a data agreement.
**Target:** Exposure seconds and quality-weighted impressions per entitlement; delivered versus owed per contract line; incremental outcome per partner with an interval.
**Evaluation metric:** Mean average precision and per-logo recall of detection against hand-labelled frames (recall matters more: an uncounted exposure under-states delivery and weakens the renewal case). For lift, interval width and pre-period fit of the synthetic control. A lift claim without a credible counterfactual is worse than none, because partners' finance teams will check it.
**Scope:** Detection is a solved pattern with per-logo fine-tuning (2–4 weeks per new logo set). The work is in entitlement reconciliation and in getting partners to share outcome data. 2 engineers and 1 measurement analyst, 4–6 months. Detection runs on logos and signage; any demo with crowd or player imagery uses consented or synthetic footage.
**Data availability:** Video rights sit with the league and broadcaster; the club's own posts and board logs are its own. Partner outcome data is the partner's and must be contracted for, which is the binding constraint.

---

## 4. Automatic Play Tagging From Game Video and Tracking
#transformers #cnns #seq2seq #transfer-learning #evaluation-metrics #worker-facing #automation

**Problem statement:** Tag every possession, shift or play with the staff's own vocabulary (play type, coverage, set name, result) so the video coordinator reviews only uncertain tags and coaches' clip requests assemble automatically.

**ML task:** Temporal action segmentation and multi-label classification over synchronised video and player-tracking sequences, fine-tuned on the staff's historical tags; natural-language clip retrieval over the tagged library.
**Input data:** The club's game and opponent video (league video exchange), synchronised tracking where the club has access, the league event feed, and the coordinator's historical tags and corrections.
**Target:** Start and end of each play and a set of staff-defined labels per play; ranked clips for a query.
**Evaluation metric:** Per-label F1 against coordinator tags on held-out games, and the share of plays needing correction, the outcome the coordinator feels. Report it per label, because coaches care most about the rare, specific sets that models get wrong.
**Scope:** Start from a model pretrained on public broadcast footage, fine-tune per club with a few hundred tagged games, and keep humans on low-confidence tags. 2 ML engineers, 4–6 months to a useful per-club model; vocabulary drift each season needs continuous learning from corrections.
**Data availability:** Clubs hold their own film and tags; tracking access depends on league terms, which differ by league and were not checked here. Public footage with consented or synthetic players can carry the demo.

---

## 5. Ranking Ticket Leads for Inside Sales
#gradient-boosting #logistic-regression #survival-analysis #feature-engineering #worker-facing #revenue-impact

**Problem statement:** Score every contact in a club's CRM on the probability of buying a ticket plan or group outing in the next 30 days, and explain the score, so inside reps call the warmest names first.

**ML task:** Binary classification with calibrated probabilities, plus a time-to-purchase hazard model for timing the call after a trigger (a recent attended game, a resale listing, an email click).
**Input data:** Ticketing purchase, scan and transfer history; CRM activity; email and web engagement; resale behaviour where the ticketer shares it; the schedule and results.
**Target:** Purchase of a plan or group outing within 30 days of the score date.
**Evaluation metric:** Lift in the top decile against the club's recency-ordered list, and conversions per hundred dials in a randomised A/B across reps, which controls for rep skill. Calibration matters because managers set quotas from it.
**Scope:** A standard propensity model; the work is joining identities across ticketing, CRM and email. 1 data scientist and 1 engineer, 3 months. Renewal-risk scoring for existing members is a separate product sold by ticketers and CRM vendors.
**Data availability:** Each club holds its own CRM and receives ticketing data from its ticketer under its ticketing agreement; consent and email-tracking rules apply to marketing use.
