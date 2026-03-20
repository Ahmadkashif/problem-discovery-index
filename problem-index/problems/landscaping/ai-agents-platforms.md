# AI Agents and Platforms — Landscaping

**Industry:** [[landscaping|Landscaping]]
**Tags:** #ai-agent #ai-platform #cnns #gradient-boosting #decision-trees #transfer-learning #feature-engineering #evaluation-metrics #automation #workflow-orchestration #revenue-impact

---

## Existing AI-Adjacent Platforms

### Jobber
Leading field service management platform for small landscaping firms. Logs service history, client records, scheduling, and billing. Integration point for churn prediction and route optimization models. Jobber's own AI features are limited to scheduling suggestions and invoice automation.

### LMN (Landscape Management Network)
Landscaping-specific CRM with job costing and estimating features. Popular with larger, growth-focused firms. Contains the cost and revenue data needed for job profitability analysis.

### Service Autopilot / Real Green Systems
Lawn care-specific platforms with fertilization program tracking, route management, and customer communication. Real Green has territory management that could integrate with a coverage scoring model.

### iNaturalist / PlantNet
Open-source plant identification platforms with large labeled photo datasets. These are training data sources, not deployment platforms — but the PlantNet API could be integrated as a base model for weed identification fine-tuning.

---

## AI Agent Opportunities

### 1. Pre-Season Renewal and Outreach Agent
**Trigger:** February 1st (90 days before typical lawn care season start) annual run.
**Action sequence:**
1. Score all prior-year customers on renewal probability using churn prediction model
2. Segment by churn reason (disengaged, service quality, price sensitivity)
3. Generate personalized outreach messages per segment with early-season offer
4. Queue outreach in Jobber or Service Autopilot for account manager review
5. Track response rates and update customer status as renewals are confirmed
**Value:** Converts reactive spring renewal scramble into a structured 90-day proactive campaign. Recovers 10-15% of at-risk customers who would otherwise cancel by default.

### 2. Disease and Deficiency Alert Agent
**Trigger:** Technician submits a turf observation photo during a service stop.
**Action sequence:**
1. Run disease/deficiency classification on submitted photo
2. Return differential diagnosis with recommended treatment and timing
3. If treatment requires a product not on the truck, flag for supply pickup or next-visit scheduling
4. Log diagnosis and treatment applied to the customer record
5. Schedule a follow-up observation at the next service visit to confirm treatment outcome
**Value:** Reduces incorrect or deferred disease treatment. Creates a diagnostic record that tracks turf health trends across seasons for each customer.

### 3. Route Optimization Agent
**Trigger:** Daily at 6am before crew dispatch.
**Action sequence:**
1. Pull today's scheduled stops from Jobber
2. Apply property-specific duration estimates from the trained job duration model
3. Solve optimal stop sequence with access constraint and service-day window filters
4. Assign stops to available crews based on equipment configuration matching
5. Push routes to crew mobile apps
**Value:** Reduces daily drive time by 15-25%. Eliminates routing failures from access constraint violations. Improves end-of-day completion rate.

### 4. Upsell Opportunity Agent
**Trigger:** Weekly run, triggered by seasonal calendar flags.
**Action sequence:**
1. Identify lawn care customers without fertilization programs (April trigger) or fertilization customers without irrigation service (May trigger)
2. Score each customer on upsell acceptance probability (tenure, spending trend, service engagement)
3. Generate personalized upsell message with the incremental service value proposition
4. Queue for account manager outreach in priority order
**Value:** Systematic upsell outreach to the existing customer base generates 20-35% higher average revenue per customer compared to reactive upsell only.

---

## Build vs. Buy Assessment

| Capability | Build | Buy/Integrate | Notes |
|---|---|---|---|
| Turf disease classification | Build | iNaturalist/PlantNet API (base model) | Fine-tuning on residential lawn data is custom |
| Customer churn prediction | Build | Jobber data export | Standard gradient boosting; feature engineering is custom |
| Route optimization | Buy/extend | DPR, Jobber routing | Duration model is custom; routing solver is commodity |
| Weed identification | Build | PlantNet API (fine-tune) | Fine-tuning for lawn context is custom |
| Irrigation walkthrough app | Build | — | No existing structured observation capture tool |
| Upsell opportunity scoring | Build | Jobber/LMN data export | Simple rule-based + ML hybrid |
