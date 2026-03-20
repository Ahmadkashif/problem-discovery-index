# Machine Learning Opportunities — Catering Companies

**Industry:** [[catering-companies|Catering Companies]]
**Derived from:** [[problems/catering-companies/high-impact|High Impact]], [[problems/catering-companies/low-impact-1|Low Impact 1]], [[problems/catering-companies/low-impact-2|Low Impact 2]], [[problems/catering-companies/worker-life-1|Worker Life 1]], [[problems/catering-companies/worker-life-2|Worker Life 2]]

---

## 1. Event Prep Quantity Prediction (Tacit Knowledge ML)
#gradient-boosting #linear-regression #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #gradient-descent #tacit-knowledge-ml #revenue-impact

**Problem statement:** Experienced catering chefs instinctively adjust prep quantities based on factors they cannot fully articulate — they "know" that a 200-person outdoor summer wedding with a cocktail hour and passed appetizers will consume 30% more protein per head than the standard recipe yield suggests, that corporate lunches with a 150-person guaranteed count will have 8-12% no-shows while social events overshoot by 5-8%, that a venue with a long cocktail hour drives appetizer consumption up and entree consumption down, and that certain menu combinations (heavy starch appetizers before a protein entree) reduce entree consumption by 10-15%. This knowledge develops over hundreds of events and lives entirely in the chef's head. When the chef is absent, the sous chef either over-preps (waste) or under-preps (running out mid-service, the cardinal sin of catering).

**ML task:** Regression — predict actual consumption quantities per menu item for a given event
**Input data:** Historical event records: guest count (guaranteed vs. actual attendance), venue type and characteristics (indoor/outdoor, cocktail hour duration, buffet vs. plated vs. stations vs. passed), service style, menu composition (full item list with course structure), date and season, day of week, event type (wedding/corporate/social/nonprofit gala), client demographics (corporate industry, age distribution if social), weather on event day, and actual consumption per item (leftover weights, pan counts, or item counts recorded post-event)
**Target:** Actual consumption quantity per menu item (in servings or weight), expressed as a ratio to the standard recipe-yield-per-guest-count baseline
**Evaluation metric:** MAE of predicted vs. actual consumption per item; weighted by item cost (a 10% miss on filet mignon costs 5x more than a 10% miss on rice pilaf); secondary metric: percentage of events where any item runs out (the asymmetric cost — running out is catastrophic, over-prepping 10% is acceptable)
**Scope:** Requires 2+ years of event history with post-event consumption tracking (pan counts, leftover weights). The primary data challenge is that most caterers do not systematically record actual consumption — they know what they prepped and they know what came back, but the "what came back" is recorded as "3 half-pans of chicken" in a text message, not a structured database field. Initial deployment requires 6-8 months of structured post-event data collection before the model has sufficient training data. Team: 1 ML engineer, 1 data engineer to build the ingestion pipeline from post-event records, 1 domain expert (executive chef) for feature engineering and sanity-checking predictions. 9-12 month build timeline.
**Data availability:** Historical data exists but is unstructured — in text messages, handwritten prep lists, and the chef's memory. Prospective data collection requires adding a 5-minute post-event logging step (photographing remaining food with quantity estimate). The labeling challenge is real: two chefs may disagree on whether 2.5 half-pans of leftover chicken means the prep was "right" or "too much," because their waste tolerance thresholds differ. The model must learn the house standard, not any individual chef's bias.

---

## 2. Event Profitability Prediction at Proposal Stage
#gradient-boosting #linear-regression #decision-trees #feature-engineering #cross-validation #evaluation-metrics #descriptive-statistics #revenue-impact

**Problem statement:** Catering companies commit to event pricing weeks before execution, but true profitability depends on variables that are estimated at proposal time and only known at completion — actual food costs (commodity prices shift, substitutions are made), actual labor hours (a 200-person plated dinner requires more service staff than a 200-person buffet, but how many more depends on venue layout, table count, and service style details that are finalized later), rental costs, and waste. Experienced sales managers carry mental models of event profitability by type, but these models are uncalibrated and biased toward memorable losses.

**ML task:** Regression — predict actual event margin (revenue minus all costs) from proposal-stage features
**Input data:** Historical event records with proposal details (guest count, menu selections, service style, venue, date) linked to actual post-event P&L (food cost, labor cost, rental cost, travel/logistics cost, waste cost, revenue)
**Target:** Event margin as percentage of revenue; secondary target: itemized cost category predictions (food, labor, rental, logistics) for line-item visibility
**Evaluation metric:** MAE on margin prediction; percentage of events where predicted margin is within 3 points of actual; bias analysis by event type to detect systematic under- or over-estimation
**Scope:** Requires integration with accounting system (QuickBooks, Xero) for actual cost data and CRM/proposal system (CaterTrax, Better Cater) for proposal features. Minimum 200 events with full P&L data for initial model training. Team: 1 ML engineer, 1 data engineer for ETL from accounting and CRM systems. 6-9 month build timeline.
**Data availability:** Proposal data exists in CRM systems; actual cost data exists in accounting systems; the gap is the linkage between the two — most caterers cannot automatically match a QuickBooks invoice to a CaterTrax event record. The data engineering to build this linkage is 40% of the project effort.

---

## 3. Seasonal Demand Forecasting and Capacity Planning
#gradient-boosting #time-series-forecasting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #expectation-variance-covariance #automation

**Problem statement:** Catering demand is highly seasonal and lumpy — wedding season (May-October), corporate holiday season (November-December), and gala/fundraiser clusters create peaks that require staffing, procurement, and equipment rental decisions weeks in advance. Most caterers staff and purchase reactively, leading to over-staffing in slow weeks and frantic hiring of day-of temp staff during peak weeks.

**ML task:** Time-series forecasting — predict weekly event volume, revenue, and production load 4-8 weeks ahead
**Input data:** Historical booking patterns (inquiry date, booking date, event date, event size, event type), pipeline data (current inquiries not yet booked with estimated close probability), seasonal indices (wedding season timing varies by region), local event calendar (major venue bookings, convention calendar, holiday schedule), macroeconomic indicators (corporate event budgets correlate with business confidence indices)
**Target:** Weekly event count, total guest count, and aggregate production hours for 4-8 week forecast horizon
**Evaluation metric:** MAPE on weekly event count and total guest count; forecast bias (systematic over- or under-prediction by season); decision-quality metric: did the forecast correctly identify weeks requiring overtime or temp staff hiring?
**Scope:** Requires 3+ years of booking history for seasonal pattern detection. Minimum viable model uses booking patterns and pipeline data only; enhanced model adds external signals. Team: 1 ML engineer. 4-6 month build timeline.
**Data availability:** Booking history exists in CRM or event management systems; pipeline data (current inquiries) is often tracked informally in email or spreadsheets rather than a structured CRM pipeline. The primary data gap is pipeline conversion probability — most caterers do not track inquiry-to-booking conversion rates by event type or lead source.

---

## 4. Client Lifetime Value and Rebooking Prediction
#gradient-boosting #logistic-regression #linear-regression #decision-trees #feature-engineering #cross-validation #evaluation-metrics #probability-distributions #revenue-impact

**Problem statement:** Catering client rebooking rates vary dramatically by segment — corporate clients who book quarterly town halls are worth 10-20x a one-time wedding client, but the signals that predict rebooking (satisfaction, relationship quality, event type recurrence) are not systematically captured or analyzed. Sales managers invest equal follow-up effort across all past clients rather than prioritizing high-LTV accounts.

**ML task:** Binary classification (will this client rebook within 12 months?) + regression (predicted lifetime revenue over 3 years)
**Input data:** Client event history (event count, frequency, average spend, event types), post-event feedback (formal surveys if collected, informal notes from coordinators), payment behavior (promptness, disputes), referral activity (did they refer other clients?), client industry and event type (corporate with recurring events vs. social one-time), communication frequency and recency
**Target:** Binary rebook indicator (12-month window); continuous LTV estimate (3-year revenue)
**Evaluation metric:** AUC-ROC on rebook classification; calibration of rebook probability (are clients predicted at 70% actually rebooking 70% of the time?); MAE on LTV regression
**Scope:** Requires CRM data with client history and event records. Minimum 500 clients with 2+ years of history for rebook pattern detection. Feature engineering for communication signals may require email/text log access. Team: 1 ML engineer. 3-5 month build timeline.
**Data availability:** Client event history is available in CRM/event management systems. Post-event satisfaction data is the primary gap — most caterers do not systematically collect or structure post-event feedback. Referral tracking is typically informal ("how did you hear about us?" on the inquiry form, if asked at all).
