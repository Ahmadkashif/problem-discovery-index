# Machine Learning Opportunities — Faith Organizations

**Industry:** [[faith-organizations|Faith Organizations]]
**Derived from:** [[problems/faith-organizations/high-impact|High Impact]], [[problems/faith-organizations/low-impact-1|Low Impact 1]], [[problems/faith-organizations/low-impact-2|Low Impact 2]], [[problems/faith-organizations/worker-life-1|Worker Life 1]], [[problems/faith-organizations/worker-life-2|Worker Life 2]]

---

## 1. Congregant Engagement Trajectory Prediction (Tacit Knowledge ML)
#gradient-boosting #survival-analysis #decision-trees #feature-engineering #evaluation-metrics #maximum-likelihood-estimation #probability-distributions #expectation-variance-covariance #cross-validation #tacit-knowledge-ml #revenue-impact

**Problem statement:** Experienced pastors detect family disengagement from subtle multi-signal patterns — attendance frequency shifts, giving cadence changes, small-group withdrawal, reduced volunteerism — weeks before anyone else notices. This tacit pattern recognition breaks down as congregations grow past 150-200 members and cannot scale through hiring alone.

**ML task:** Survival analysis (time-to-disengagement) with Cox proportional hazards or gradient-boosted survival trees, producing per-household hazard scores updated weekly.
**Input data:** Weekly attendance check-in records (service time, consistency), giving transaction logs (amount, frequency, method), small-group roster status (active/dormant/left), volunteer shift completion rates, event RSVP and attendance records, membership milestone dates (first visit, membership class, baptism). All sourced from Planning Center, Tithely/Pushpay exports, and manual attendance logs. Critically, pastor engagement assessments — periodic ratings of household engagement health — serve as the tacit-knowledge ground truth.
**Target:** Binary disengagement event (defined as 8+ consecutive weeks of zero attendance with no communicated absence) with time-to-event modeling. Secondary target: pastor-agreement score (does the model's risk ranking match the pastor's intuitive ranking?).
**Evaluation metric:** Concordance index (C-index) for survival predictions; precision@k for the top-20 at-risk list compared against pastoral assessments. Recall matters more than precision — missing a drifting family is costlier than a false alert that prompts an unnecessary check-in call.
**Scope:** 3-person team (ML engineer, data engineer, domain advisor who is a pastor), 4-6 month build. Requires partnership with 10-15 congregations for training data diversity. The hardest part is the labeling phase: pastors must regularly rate household engagement to create the tacit-knowledge training signal, and they will disagree with each other and with themselves over time.
**Data availability:** Attendance and giving data exist in church management platforms but require ETL pipelines to normalize across Planning Center, Breeze, Church Community Builder, and CSV exports. The tacit-knowledge labels require a structured collection process — a weekly 10-minute exercise where the pastor flags 5-10 households they're concerned about, with brief reasoning notes. This is the bottleneck.

---

## 2. Giving Pattern Anomaly Detection
#gradient-boosting #change-point-detection #feature-engineering #evaluation-metrics #time-series-forecasting #descriptive-statistics #probability-distributions #revenue-impact

**Problem statement:** Churches depend on consistent giving but have no early warning when giving patterns shift at the aggregate or household level — a major donor quietly reduces contributions, seasonal giving dips arrive earlier than expected, or a campaign underperforms relative to historical norms. Staff discover shortfalls only when the monthly financial report reveals a gap.

**ML task:** Unsupervised anomaly detection on giving time series at both household and aggregate levels.
**Input data:** Transaction-level giving records (date, amount, fund designation, method) for each household, aggregated into weekly and monthly time series. Supplementary features: attendance correlation, campaign calendar, seasonal indicators (Christmas, Easter, fiscal year-end), local economic indicators (unemployment rate, median home price changes).
**Target:** Anomaly scores for (a) individual households showing unexpected giving trajectory changes and (b) aggregate fund-level giving relative to seasonal baselines. Flagged anomalies feed a dashboard, not automated actions.
**Evaluation metric:** Precision at the alert level — the finance team should investigate 80%+ of flagged anomalies and confirm them as real pattern shifts, not noise. False-positive rate must stay below 15% to maintain trust.
**Scope:** 2-person team, 3-month build. The model is straightforward (Isolation Forest or Prophet-based decomposition); the challenge is data normalization across giving platforms and handling the high variance inherent in faith-based giving (large one-time gifts skew baselines).
**Data availability:** Giving data is well-structured in platforms like Tithely and Pushpay. Churches are protective of financial data, so the system must run on-premises or in a single-tenant cloud environment. Anonymized aggregate models can be pre-trained, with per-church fine-tuning on local data.

---

## 3. Small Group Health Scoring
#gradient-boosting #decision-trees #feature-engineering #evaluation-metrics #logistic-regression #cross-validation #probability-distributions #bias-variance-tradeoff #data-integration

**Problem statement:** Small groups (Bible studies, life groups, discipleship cohorts) are the primary relational engine of most churches, but leaders and staff have no visibility into which groups are thriving and which are quietly dying. A group that started with 12 members may have 4 active participants and a burned-out facilitator, but this only surfaces when the group formally disbands.

**ML task:** Binary classification (healthy vs. at-risk) with probability calibration, scored monthly per group.
**Input data:** Group roster size over time, meeting attendance rates, leader tenure and training completion, member overlap with other church activities (worship attendance, volunteering, giving), leader self-reported health surveys (quarterly), member join/leave events with tenure-at-departure. Sourced from Planning Center Groups, Church Community Builder, or manual tracking sheets.
**Target:** Binary label: group survives the next quarter vs. dissolves or falls below minimum viable size (3 active members). Secondary target: facilitator burnout risk (binary).
**Evaluation metric:** F1-score with emphasis on recall — catching at-risk groups early allows intervention (co-leader assignment, curriculum change, pastoral visit). Acceptable precision threshold: 0.7+.
**Scope:** 2-person team, 3-month build. Requires partnership with churches that track small-group attendance systematically — probably 20-30% of mid-size congregations. The biggest challenge is defining "healthy" — some groups are intentionally small and intimate, which looks like decline in raw numbers.
**Data availability:** Small-group tracking is the least digitized part of church operations. Many groups self-report via text message or don't report at all. Data collection infrastructure (a simple weekly check-in form for group leaders) must be built alongside the model.

---

## 4. Event Attendance and Resource Demand Forecasting
#gradient-boosting #decision-trees #linear-regression #feature-engineering #evaluation-metrics #cross-validation #probability-distributions #confidence-intervals #workflow-orchestration

**Problem statement:** Churches plan events — holiday services, vacation Bible school, community outreach meals, special concerts — with wildly inaccurate attendance estimates. Easter might draw 2x normal attendance, but whether it's 1.8x or 2.4x determines whether you need overflow seating, additional parking volunteers, and extra children's ministry rooms. Under-preparation creates chaotic visitor experiences; over-preparation wastes volunteer hours and budget.

**ML task:** Regression predicting event attendance count, with prediction intervals for resource planning.
**Input data:** Historical event attendance by type (holiday service, special event, recurring program), weather forecasts, local school and community calendars, social media engagement metrics (event page views, RSVPs, shares), email open/click rates for event promotions, year-over-year congregation growth rate, day-of-week and time-of-day features. Sourced from Planning Center Events, Facebook/Eventbrite RSVPs, and email marketing platforms.
**Target:** Predicted attendance count with 80% prediction interval. Secondary outputs: predicted children's ministry headcount (for staffing ratios), predicted parking lot utilization.
**Evaluation metric:** Mean Absolute Percentage Error (MAPE) on held-out events, targeting < 15% for recurring events and < 25% for novel events. Interval coverage should hit 80% calibration.
**Scope:** 2-person team, 2-3 month build. The model itself is simple regression; the value is in the integration — translating an attendance prediction into concrete resource requirements (X greeters, Y nursery workers, Z parking attendants, W chairs in overflow configuration) using church-specific staffing ratios.
**Data availability:** Event attendance data exists in most church management platforms but is often incomplete for non-Sunday events. Churches with 3+ years of consistent tracking across event types provide sufficient training data. Newer or smaller churches can use a cold-start model based on congregation size and event type benchmarks.
