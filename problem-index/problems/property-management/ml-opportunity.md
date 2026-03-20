# Machine Learning Opportunities — Property Management

**Industry:** [[property-management|Property Management]]
**Derived from:** [[problems/property-management/high-impact|High Impact]], [[problems/property-management/low-impact-1|Low Impact 1]], [[problems/property-management/low-impact-2|Low Impact 2]], [[problems/property-management/worker-life-1|Worker Life 1]], [[problems/property-management/worker-life-2|Worker Life 2]]

---

## 1. Tenant Churn Prediction and Renewal Scoring
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #conditional-probability-and-bayes-theorem #revenue-impact

**Problem statement:** Predict which tenants are unlikely to renew at their upcoming lease expiration, 90-120 days in advance, to enable proactive retention outreach before the non-renewal decision is finalized.

**ML task:** Binary classification (will not renew at next lease expiration: yes/no) from tenant behavior features
**Input data:** Tenant features from AppFolio/Buildium: payment history (on-time rate, late fee frequency, trend), maintenance request frequency and recency, length of tenancy, communication volume trend, lease renewal history, unit type and rent level vs. market
**Target:** Renewal probability per tenant at 90-day horizon; risk segment (payment issues, engagement decline, likely relocation); recommended outreach action
**Evaluation metric:** AUC-ROC on held-out lease expirations; recall on non-renewing tenants; revenue retained through proactive outreach to flagged tenants vs. control group
**Scope:** Any property management firm with 200+ units and 3+ years of AppFolio/Buildium data has training data. Gradient boosting on ~12 tenant features: 3-4 week project. AppFolio or Buildium as the integration platform. High business value, low modeling complexity.
**Data availability:** AppFolio and Buildium log all payment events, maintenance requests, and communication history. Renewal outcome (renewed vs. vacated) is the supervision label — available from the next lease record for the unit.

---

## 2. Maintenance Request Urgency Classification
#gradient-boosting #large-language-models #decision-trees #feature-engineering #cross-validation #evaluation-metrics #entropy-cross-entropy-kl-divergence #quick-win

**Problem statement:** Classify incoming tenant maintenance requests by urgency tier (emergency/24hr, urgent/72hr, routine/scheduled) and category (HVAC, plumbing, electrical, appliance, cosmetic) to enable automated triage and dispatch routing.

**ML task:** Multiclass classification — urgency tier + maintenance category from request text; structured features (unit type, season, prior request history for this unit)
**Input data:** Historical maintenance requests with urgency classification and category labels from resolved work orders. Supervision signal: actual dispatch urgency and time-to-resolution from the work order system.
**Target:** Urgency classification per incoming request; maintenance category; recommended contractor type; draft work order with vendor routing
**Evaluation metric:** Agreement rate with experienced property manager urgency assessment on held-out requests; recall on emergency-classified requests (minimize misclassification of emergencies as routine); precision on emergency classification (minimize false emergencies)
**Scope:** Quick win — maintenance request text classification is well within current LLM capability. Fine-tuning a classification model on labeled work orders from AppFolio or Buildium: 2-3 week project. The habitability law urgency mapping is the domain-specific component.
**Data availability:** AppFolio and Buildium log maintenance requests with resolution outcomes and dispatch records. Any firm with 1,000+ historical work orders has sufficient training data. The urgency label can be derived from actual response time (emergency = dispatched within 4 hours; routine = scheduled within 7 days).

---

## 3. Tenant Quality Scoring from Application Data
#gradient-boosting #decision-trees #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #conditional-probability-and-bayes-theorem #revenue-impact

**Problem statement:** Score rental applicants on tenancy outcome probability (pays on time, renews lease, leaves unit in good condition) from application data to supplement formal credit and background screening.

**ML task:** Binary classification (good tenancy outcome: yes/no) from rental application features; separate models for payment risk and property damage risk
**Input data:** Historical rental application data with tenancy outcome labels. Features: income-to-rent ratio, employment type (W-2 vs. self-employed vs. unstable), length of prior tenancies, number of prior rental addresses (high move frequency is a signal), reference quality indicators, credit tier. Labels: paid on time throughout tenancy, renewed lease, left unit in good condition (security deposit returned in full vs. damage deductions).
**Target:** Tenancy quality score per applicant; specific risk flags (payment risk, damage risk, early departure risk)
**Evaluation metric:** AUC on tenancy outcome for approved applicants; recall on high-damage tenants; property manager agreement rate on flagged applications
**Scope:** Requires multi-year tenancy outcome data. A property management firm with 500+ historical tenancies and consistent application intake records has training data. Gradient boosting on ~12 application features: 4-6 week project. CRITICAL: must comply with fair housing law — features cannot include protected class proxies; model must be audited for disparate impact. This model requires legal review before deployment.
**Data availability:** Application data is in AppFolio/Buildium. Tenancy outcomes (payment history, deposit disposition) are in the same system. The join is straightforward. Fair housing compliance audit is the primary deployment gate.

---

## 4. Rental Pricing Optimization
#gradient-boosting #decision-trees #linear-regression #survival-analysis #feature-engineering #cross-validation #evaluation-metrics #bias-variance-tradeoff #revenue-impact

**Problem statement:** Estimate optimal asking rent for a vacant unit given current comparable listings, unit characteristics, and seasonal demand patterns to maximize rent yield while minimizing days-to-fill.

**ML task:** Regression — optimal asking rent from unit features and market conditions; survival analysis — expected days-to-fill at different asking price points
**Input data:** Zillow/Apartments.com rental listing data (asking rent + days to fill) for comparable units by sub-market, bedroom count, and amenity set. Property-specific features: unit size, condition, included utilities, parking, appliances, building age.
**Target:** Recommended asking rent for a specific unit; expected days-to-fill curve at ±5% price points; seasonal demand adjustment (March-May is peak demand in most markets)
**Evaluation metric:** Actual vs. modeled days-to-fill at recommended price; rent per occupied day for units priced by model vs. manually; comparison to market median rent for similar units
**Scope:** Rental listing data is commercially available (Zillow API, CoStar). Sub-market feature values require local training data. Gradient boosting regression: 4-6 week project. A property management platform (AppFolio) could provide this as a native feature using their aggregated portfolio data.
**Data availability:** Zillow's Rental Manager API and Apartments.com provide listing data. CoStar provides commercial rental data. The property manager's own historical listing-to-lease time data is the platform-specific training signal.

---

## 5. Move-Out Damage Assessment from Inspection Photos
#cnns #transfer-learning #loss-functions #backpropagation #evaluation-metrics #gradient-descent #feature-engineering

**Problem statement:** Classify move-out inspection photos by damage type and severity to automate itemized damage descriptions and cost estimates for security deposit accounting letters.

**ML task:** Multi-label object detection per photo — damage type (wall scuff, paint damage, carpet stain, broken fixture, cleaning deficiency) and severity (normal wear vs. chargeable damage per standard security deposit guidelines)
**Input data:** Move-out inspection photos labeled with damage type and normal-wear vs. chargeable-damage classification. AppFolio inspection records with security deposit charge outcomes as supervision signal.
**Target:** Damage classification per photo with chargeability determination; itemized damage description for the security deposit letter; cost estimate range from repair cost database
**Evaluation metric:** Agreement rate with experienced property manager chargeability assessment; security deposit dispute rate for letters generated with model vs. without; coverage (what fraction of common damage types does the model classify correctly?)
**Scope:** Labeled move-out inspection photos require property manager annotation (is this chargeable or normal wear?). A consortium of property management firms providing annotated inspection photos: 6-9 month data collection program. Fine-tuning a CNN on 10,000-20,000 labeled inspection photos: 8-12 week training project. AppFolio or Buildium partnership provides both training data and distribution.
**Data availability:** Move-out inspection photos are taken by property managers and stored in AppFolio or their photo apps. Charge outcome (charged vs. normal wear) is in the security deposit accounting record. The join is available in firms with consistent digital inspection workflows.
