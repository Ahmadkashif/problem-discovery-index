# Machine Learning Opportunities — Event Planning

**Industry:** [[event-planning|Event Planning]]
**Derived from:** [[problems/event-planning/high-impact|High Impact]], [[problems/event-planning/low-impact-1|Low Impact 1]], [[problems/event-planning/low-impact-2|Low Impact 2]], [[problems/event-planning/worker-life-1|Worker Life 1]], [[problems/event-planning/worker-life-2|Worker Life 2]]

---

## 1. Event Scope and Budget Prediction from Client Brief
#gradient-boosting #bert #regression #nlp #tabular-ml #tacit-knowledge-ml

**Problem statement:** Experienced event planners read a client brief — a mix of vision descriptions, mood board references, guest count, and stated budget — and instantly know the real budget needed. They've calibrated this intuition through hundreds of final invoices. A "rustic elegant" wedding for 200 in Austin triggers a mental model: $75K-$95K. This tacit knowledge is the difference between planners who set expectations correctly and those who plan to an unrealistic budget for three months before discovering the mismatch.

**ML task:** Regression (predict total event cost by category from event description and parameters)
**Input data:** Event type (wedding, corporate, social), guest count, style descriptors (natural language from client communication), venue type and market/city, season, specific requirements mentioned (live music, custom floral, specialty catering), client demographic signals (if available)
**Target:** Total event cost, broken down by category (venue, catering, floral, entertainment, photography/video, rentals, stationery, transportation, planning fee), with confidence intervals
**Evaluation metric:** MAPE on total cost targeting <15%; category-level MAE. Model must handle the wide variance in event costs (same "type" can cost $10K or $100K depending on market and style).
**Scope:** Requires 2,000-10,000 completed events with final cost breakdowns and original client briefs/descriptions. NLP for style descriptor extraction + gradient boosting for cost prediction. 2-person team, 6-9 months. Challenge: event costs vary dramatically by market — model may need market-specific calibration.
**Data availability:** Event management platforms (HoneyBook, Planning Pod) contain proposals and invoices but rarely in standardized format. Vendor invoices scattered across email. Multi-planner dataset needed for market coverage. Planners may be reluctant to share financial data.

---

## 2. Vendor-Event Matching and Recommendation
#gradient-boosting #recommendation #tabular-ml

**Problem statement:** Matching vendors to events based on style compatibility, budget tier, reliability, and team chemistry is a planner's most valuable skill. Systematizing this could enable new planners to leverage institutional knowledge.

**ML task:** Ranking / recommendation (given event parameters, rank vendors by predicted fit)
**Input data:** Event characteristics (type, style, budget tier, guest count, venue), vendor profiles (style portfolio, pricing tier, capacity, reviews), planner's past vendor selections for similar events, vendor-vendor compatibility scores from past events, vendor performance history
**Target:** Vendor fit score for each event; post-event satisfaction rating as ground truth
**Evaluation metric:** NDCG@3 (top 3 recommended vendors include eventual selection); post-event satisfaction correlation with predicted fit
**Scope:** Requires 1,000-5,000 event-vendor pairings with satisfaction data. 1-2 person team, 4-6 months. Challenge: vendor databases are planner-specific and not shared across the industry.
**Data availability:** Planner CRMs contain vendor usage history. Review platforms (The Knot, WeddingWire) provide quality signals. Post-event surveys provide satisfaction data when collected. Data is fragmented across individual planners.

---

## 3. Day-Of Timeline Prediction and Risk Identification
#gradient-boosting #regression #tabular-ml

**Problem statement:** Day-of execution timelines are built from templates but actual timing varies significantly. Identifying which timeline items are at risk of running over — and by how much — enables better buffer planning.

**ML task:** Regression (predict actual duration for each timeline item based on event characteristics)
**Input data:** Timeline item type (setup, ceremony, dinner, speeches, dances), guest count, venue characteristics (space constraints, transition distances), vendor profiles, weather conditions, time of year
**Target:** Actual duration per timeline item; probability of exceeding planned duration by >15 minutes
**Evaluation metric:** MAE on duration predictions; recall on "over-time" predictions targeting 80%+
**Scope:** Requires 500-2,000 events with actual timeline data (timestamps for major milestones). 1-person team, 3-4 months. Data collection challenge: most planners don't systematically record actual timeline vs. planned.
**Data availability:** Planned timelines exist in planning tools. Actual timing must be collected through day-of apps or retrospective planner notes. Photo timestamps provide proxy data for actual timeline.

---

## 4. Client Communication Pattern and Churn Risk
#gradient-boosting #binary-classification #tabular-ml

**Problem statement:** Client relationships that go sideways often show warning signs in communication patterns weeks before an explicit complaint: response delays, tone shifts, decreasing engagement with shared documents.

**ML task:** Binary classification (will this client express significant dissatisfaction or terminate contract within 30 days?)
**Input data:** Communication frequency and response times, message sentiment trends, document engagement (proposal views, mood board interactions), budget vs. spend trajectory, number of change requests, meeting cancellation rate
**Target:** Binary: client relationship at risk / on track
**Evaluation metric:** AUC-ROC; recall for at-risk identification targeting 80% at reasonable precision
**Scope:** Trainable on 500-2,000 client relationships with satisfaction outcomes. 1-person team, 2-3 months. Challenge: small dataset and subjective outcome definition.
**Data availability:** Communication logs in email and CRM systems. Document engagement from planning platforms. Satisfaction data from post-event surveys and contract completions.

---

## 5. Dynamic Pricing and Capacity Optimization
#gradient-boosting #regression #tabular-ml

**Problem statement:** Planners price based on intuition rather than demand data. During peak season (October, June), they're overbooked; during off-season, they discount desperately. Market-aware pricing could smooth demand and maximize revenue.

**ML task:** Regression (predict market demand and optimal pricing for a given date and event type)
**Input data:** Historical booking patterns by date and event type, market pricing data, venue availability indicators, economic conditions, wedding trend data (popular dates shift year to year)
**Target:** Predicted demand for planning services by date; recommended pricing by event type and date
**Evaluation metric:** Revenue improvement vs. flat-pricing baseline; booking rate at recommended prices
**Scope:** Requires 3+ years of booking history from multiple planners in a market. 1-person team, 2-3 months. Challenge: small sample sizes for individual planners; market-level data needed.
**Data availability:** Individual planner booking history from CRM systems. Market-level data requires aggregation across planners. Venue availability as a demand proxy.
