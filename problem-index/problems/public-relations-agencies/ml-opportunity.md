# Machine Learning Opportunities — Public Relations Agencies

**Industry:** [[public-relations-agencies|Public Relations Agencies]]
**Derived from:** [[problems/public-relations-agencies/high-impact|High Impact]], [[problems/public-relations-agencies/low-impact-1|Low Impact 1]], [[problems/public-relations-agencies/low-impact-2|Low Impact 2]], [[problems/public-relations-agencies/worker-life-1|Worker Life 1]], [[problems/public-relations-agencies/worker-life-2|Worker Life 2]]

---

## 1. Reporter–Story Fit Learned From Senior Publicists' Choices
#tacit-knowledge-ml #transformers #word-embeddings #gradient-boosting #evaluation-metrics #feature-engineering #worker-facing #revenue-impact

**Problem statement:** Senior publicists look at a client announcement and "just know" which few reporters will run it, with which angle and what kind of access, a judgement built from years of reading those reporters and watching what they took and ignored. The ML problem is to learn that judgement from the seniors' historical pitch choices and the coverage that followed, and to rank reporters and angles for a new story so an account executive can see the senior read before pitching.

**ML task:** Learning to rank reporters for a story, conditioned on angle and access type, plus a calibrated probability of coverage within 14 days for each recommended reporter–angle pair
**Input data:** Pitch records from outreach platforms and email (story, angle, reporter, access offered, send time, follow-ups, reply); the agency's monitoring archive of resulting coverage with outlet tier and message coding; each reporter's published articles over the past two years, embedded with a transformer encoder; beat and outlet changes; senior staff's explicit include and exclude decisions where they were recorded.
**Target:** Graded relevance per reporter–story pair (coverage carrying a key message in a priority outlet > coverage > substantive reply > open > ignored), and agreement with senior publicists' rankings on held-out stories.
**Evaluation metric:** NDCG@10 against held-out coverage outcomes, measured strictly out of time (train on earlier campaigns, test on later ones), because reporters' beats drift and random splits leak the future. Report agreement with senior rankings separately, with the seniors' own test-retest agreement on re-ranked stories as the ceiling. Precision at the top of the list matters more than recall: one wrongly pitched reporter can cost the relationship, while a missed long-shot costs little.
**Scope:** The data collection challenge is the hard part. The seniors' reasoning (the reporters they considered and rejected, and why) is rarely written down, so the system needs a near-zero-effort capture surface inside list building ("drop / keep / exclusive") and a back-fill pass that aligns historical pitches to coverage. The labelling challenge is that coverage is noisy and senior judgement drifts: labels must be weighted by outlet value and message carried, and a sample of stories should be re-ranked by the same seniors weeks apart to measure intra-rater reliability. The deployment challenge is speed: the ranked list must appear while the account executive is building it, faster than asking the senior down the corridor, and must show its evidence or seniors will dismiss it. Two ML engineers and one product engineer with a mid-size agency's media team, 6–9 months, with value first appearing as retrieval ("this reporter's last five pieces on this topic") before any ranker is trusted.
**Data availability:** Coverage archives sit in the agency's monitoring contract; pitch logs sit in outreach tools (Muck Rack, Cision, Prowly) or individual inboxes and must be exported with permission. Reporters' articles are public. Senior include and exclude decisions mostly do not exist and must be captured prospectively. Outreach vendors see pitch outcomes across many agencies and are the only parties with cross-agency labels.

---

## 2. Crisis Escalation Forecasting
#survival-analysis #change-point-detection #gradient-boosting #time-series-forecasting #evaluation-metrics #worker-facing

**Problem statement:** Given the first hours of an emerging issue (social posts, early articles, reporter inquiries), estimate whether and when it will reach national or tier-one media, so the crisis team escalates on evidence rather than on raw mention volume.

**ML task:** Time-to-event modelling of escalation to tier-one coverage, with change-point detection on mention-volume and amplifier-mix series as time-varying features
**Input data:** Historical issues from monitoring and social listening archives: hourly mention counts, the follower reach and type of amplifying accounts (journalists, activists, regulators, competitors), outlet sequence of pickup, reporter inquiries logged by the agency, the client's response time and response type.
**Target:** Hazard of first tier-one or national pickup over the next 6, 24 and 72 hours; the issue's peak volume as a secondary target.
**Evaluation metric:** Time-dependent concordance and Brier score at fixed horizons, plus recall at the alert threshold the senior counsellor sets. A missed escalation is far costlier than a false alarm, but false alarms that wake the senior counsellor nightly will get the system switched off, so report alerts per week alongside recall. The agency's own response changes the outcome; treat response as a covariate and do not read the model causally.
**Scope:** Positive cases (real escalations) are rare per client but common across an agency's or vendor's book over years. One data scientist and one engineer, 4–6 months, starting from a monitoring vendor's archive. The hard part is labelling issues consistently: deciding where one issue ends and another begins.
**Data availability:** Monitoring and listening vendors hold the series; agencies hold the inquiry logs and response timelines in spreadsheets and email. Platform terms limit retention of some social data.

---

## 3. Message Pull-Through Coding Against the Client's Message House
#bert #large-language-models #transformers #evaluation-metrics #hypothesis-testing #automation #data-integration

**Problem statement:** Code every article and broadcast transcript about a client for which of the client's key messages it carried, whether a spokesperson was quoted, the tonality toward the client, and the outlet's tier, consistently from month to month and between coders.

**ML task:** Passage-level multi-label classification of message presence against a client-specific message set, with few-shot adaptation from examples, plus document-level tonality classification
**Input data:** Coverage text and broadcast transcripts from monitoring; the client's message house with example sentences per message; historical human coding from the agency or a measurement vendor; the client's priority outlet list.
**Target:** Per message: carried fully, partially or not at all, with the supporting passage; tonality toward the client; spokesperson quoted yes or no.
**Evaluation metric:** Agreement with a double-coded gold set, reported as Cohen's kappa against the human coders' own inter-coder kappa, which is the realistic ceiling. Report per-message F1, because rare messages are the ones clients ask about. Partial pull-through is the hardest category and should be evaluated separately.
**Scope:** One ML engineer and one measurement lead, 3–4 months for a reusable pipeline; each new client needs a message house with 10–30 examples per message. The model drafts and a human checks a sample each month.
**Data availability:** Coverage is licensed through the monitoring contract; human coding exists at measurement firms and the better agencies but varies in quality. A double-coded gold set must be built for evaluation.

---

## 4. Coverage-to-Outcome Attribution
#causal-inference #bayesian-inference #time-series-forecasting #linear-regression #evaluation-metrics #revenue-impact

**Problem statement:** Estimate the incremental effect of a coverage burst on outcomes the client holds (site visits, branded search, demo requests, AI-answer citations of the brand) so the agency can replace AVEs with an evidenced effect size.

**ML task:** Interrupted time-series and synthetic-control estimation of coverage effects, with hierarchical pooling across campaigns
**Input data:** Dated coverage events with tier and message coding; the client's daily web analytics, search-console and CRM series; paid media spend over the same period as a confounder; competitor coverage; tracked AI-answer citations.
**Target:** Incremental visits, searches or leads attributable to each coverage event or campaign window, with an uncertainty interval.
**Evaluation metric:** Placebo tests on pre-period dates and on control series that coverage should not move; calibration of intervals on simulated injected effects. A confident wrong attribution is worse than a wide interval, because it will be repeated in a budget meeting.
**Scope:** One data scientist, 3 months for a template; per client, a week of data plumbing. Effects from single articles are usually too small to detect; campaign-level windows are realistic.
**Data availability:** Outcome data belongs to the client and needs access; agencies rarely get it, which is the main barrier rather than the method.

---

## 5. Journalist Beat Drift and Move Detection
#word-embeddings #k-means-clustering #logistic-regression #evaluation-metrics #feature-engineering #automation

**Problem statement:** Detect from published bylines when a reporter has changed beat, outlet or status (freelance, laid off, left journalism) before the media database updates, so pitch lists stop going to the wrong people.

**ML task:** Byline entity resolution across outlets, topic clustering of each reporter's recent articles to measure beat drift, and binary classification of "moved or changed beat in the last 60 days"
**Input data:** Article bylines and text from monitoring feeds; outlet staff pages; bounce and auto-reply messages from outreach; media database records with their last-verified dates.
**Target:** Current beat cluster per reporter; probability of a change since last verification; matched identity across outlets.
**Evaluation metric:** Precision of change alerts against researcher-verified updates (a false alert costs a researcher a check; a miss costs a burned pitch), and recall on known moves within 30 days.
**Scope:** One engineer and one data scientist, 3 months, feeding a database research team's verification queue rather than updating records automatically.
**Data availability:** Media database vendors hold verification histories and have the strongest data; agencies hold bounce logs. Bylines are public.
