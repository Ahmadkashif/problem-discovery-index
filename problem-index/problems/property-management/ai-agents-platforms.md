# AI Agents and Platforms — Property Management

**Industry:** [[property-management|Property Management]]
**Tags:** #ai-agent #ai-platform #automation #workflow-orchestration #revenue-impact

---

## Existing AI-Adjacent Platforms

### AppFolio
The leading property management platform for small-to-mid-sized residential portfolios. AppFolio has been actively adding AI features (AI leasing assistant, maintenance request routing). All tenant behavior data, payment history, and maintenance records live here — the primary training data source and integration target.

### Buildium (RealPage)
AppFolio's primary competitor in the small-to-mid-sized residential segment. Acquired by RealPage (which also owns AI-based revenue management for large multifamily). Buildium's portfolio data and RealPage's AI capabilities create the natural platform for ML-enhanced property management at smaller portfolio sizes.

### RealPage Revenue Management
Dynamic pricing and revenue optimization platform for large multifamily operators. Uses portfolio-level pricing intelligence to optimize rents across thousands of units. The smaller portfolio equivalent of this capability is the gap for independent property managers.

---

## AI Agent Opportunities

### 1. Renewal Risk Management Agent
**Trigger:** Monthly run, 120 days before each tenant's lease expiration.
**Action sequence:**
1. Score all tenants with lease expirations in the next 120 days using churn prediction model
2. Segment by risk level and primary churn signal
3. Generate personalized renewal outreach strategy per segment: high-risk payment history → payment plan offer; engagement decline → proactive maintenance check; likely relocation → early renewal incentive
4. Draft renewal offers for manager review and approval
5. Track outreach outcomes and update renewal probability
**Value:** Proactive renewal outreach 120 days before expiration recovers 20-30% of would-be non-renewers. Each recovered renewal is worth $1,500-$4,000 in avoided turnover cost.

### 2. Maintenance Triage and Dispatch Agent
**Trigger:** New maintenance request submitted by tenant (AppFolio/Buildium tenant portal).
**Action sequence:**
1. Classify request urgency (emergency/24hr, urgent/72hr, routine/scheduled) and maintenance category
2. For emergency: immediately notify on-call property manager with classification rationale and preferred emergency vendor contacts
3. For routine: generate work order with preferred vendor routing, draft message to tenant confirming receipt and estimated timeline
4. For routine during business hours: auto-dispatch to preferred vendor with work order
5. Log all dispatch actions to work order record
**Value:** Reduces after-hours emergency misclassification. Reduces routine maintenance dispatch time from 5-10 minutes to auto-dispatch. Tenant response time improves, which is the top driver of tenant satisfaction and renewal probability.

### 3. Tenant Communication Response Agent
**Trigger:** New inbound message from tenant (email, text, or portal message).
**Action sequence:**
1. Classify message intent (maintenance status, payment inquiry, renewal question, complaint, general)
2. Look up relevant account data (open work orders, payment status, lease terms, renewal date)
3. Draft response with specific account information populated
4. Present draft to manager for review (one-click send for routine cases, manual edit for complex cases)
5. Log sent communication to tenant record
**Value:** Reduces response time from same-day to same-hour. Reduces communication labor from 2-3 hours/day to 45 minutes/day. Enables portfolio scaling without headcount increase.

### 4. Move-Out Documentation Agent
**Trigger:** Property manager marks move-out inspection complete.
**Action sequence:**
1. Process inspection photos through damage classification model
2. Match to move-in condition photos for the same unit to identify new damage
3. Pull vendor invoice amounts for completed repairs, or lookup cost range from database
4. Generate itemized security deposit accounting letter in the state-required format
5. Calculate deposit return amount (deposit minus itemized charges)
6. Flag for manager review with deadline countdown (state-specific statutory deadline)
**Value:** Reduces move-out documentation time from 45-60 minutes to 10-15 minutes. Ensures statutory compliance with security deposit deadlines. Creates a well-documented basis for withholding that reduces tenant dispute success rate.

---

## Build vs. Buy Assessment

| Capability | Build | Buy/Integrate | Notes |
|---|---|---|---|
| Tenant churn prediction | Build | AppFolio/Buildium data export | Gradient boosting; feature engineering is PM-specific |
| Maintenance request triage | Build | AppFolio API | LLM classification + habitability law mapping is custom |
| Communication drafting | Build | AppFolio/Buildium API + LLM | Account data integration is custom; LLM drafting is commodity |
| Rental pricing intelligence | Buy/extend | Zillow API + RealPage (partial) | Sub-market feature adjustment is custom |
| Move-out damage classification | Build | AppFolio inspection photos | Vision model is custom; requires labeled dataset assembly |
| Tenant quality scoring | Build | AppFolio/Buildium data | Requires fair housing legal review before deployment |
