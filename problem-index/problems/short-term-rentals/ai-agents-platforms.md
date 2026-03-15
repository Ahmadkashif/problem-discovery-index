# AI Agents and Platforms — Short-Term Rentals

**Industry:** [[short-term-rentals|Short-Term Rentals]]
**Tags:** #ai-agent #ai-platform #automation #workflow-orchestration #revenue-impact

---

## Existing AI-Adjacent Platforms

### PriceLabs / Beyond Pricing / Wheelhouse
Dynamic pricing platforms with demand modeling and rule-based rate adjustment. PriceLabs has a developer API. These are the integration targets for RL-based pricing enhancement and the primary competitors for any new pricing intelligence product.

### Guesty / Hostaway
Property management systems for professional STR operators. Log all booking data, guest communication, and operational tasks. The training data foundation and integration target for guest screening, messaging automation, and reporting.

### Breezeway / Properly
Operations platforms for STR turnover management. Properly has AI-powered cleaning verification (photo review). Breezeway focuses on task coordination and property condition tracking. Integration targets for turnover scheduling optimization.

---

## AI Agent Opportunities

### 1. Daily Operations Agent
**Trigger:** Each morning at 6am.
**Action sequence:**
1. Pull next 48 hours of check-outs and check-ins from booking calendar
2. Assign each turnover to an available cleaner using the scheduling optimization model
3. Send cleaners their task list (property, checkout window, check-in deadline)
4. Monitor cleaner check-ins and flag turnovers at risk of missing the check-in window
5. Notify manager only for exceptions — late cleaners, damage reports, special guest requests
**Value:** Eliminates daily manual turnover coordination. Reduces manager involvement to 5-10 minutes of exception review vs. 45-90 minutes of active coordination.

### 2. Guest Communication Agent
**Trigger:** Incoming guest message on any channel.
**Action sequence:**
1. Classify message intent from content
2. For routine intents (check-in info, amenity questions, early/late requests): generate response from property knowledge base and booking calendar; send automatically or with one-tap approval
3. For non-routine (damage reports, complaints, unusual requests): flag for manager with context summary
4. Log all communications to guest record in Guesty/Hostaway
**Value:** Reduces guest communication labor from 1-2 hours/day to 15 minutes of exception review. Improves Airbnb response rate score.

### 3. Revenue Optimization Agent
**Trigger:** Daily pricing review.
**Action sequence:**
1. Pull current rates for next 90 days from PriceLabs
2. Run RL pricing model to compute optimal rate recommendations per night
3. Identify nights where model recommendation deviates significantly from PriceLabs (≥ 10%)
4. Present deviation nights with rationale to manager for review
5. Apply approved adjustments back to PriceLabs via API
**Value:** Captures revenue improvements from per-property pricing personalization without replacing the existing pricing tool — works as an intelligent override layer.

### 4. Booking Review Agent
**Trigger:** New booking request received (Airbnb Instant Book off, or Vrbo booking).
**Action sequence:**
1. Score booking on problem probability from booking features and inquiry text
2. For low-risk: auto-approve and send check-in details
3. For medium-risk: flag for manager review with specific risk factors
4. For high-risk: send pre-decline message asking qualifying questions; await response before decision
**Value:** Reduces problem bookings without over-declining legitimate guests. Most STR managers either approve everything (too permissive) or decline anything unusual (too restrictive) — a probabilistic middle ground captures the best of both.

---

## Build vs. Buy Assessment

| Capability | Build | Buy/Integrate | Notes |
|---|---|---|---|
| RL pricing agent | Build | PriceLabs API | RL model is custom; PriceLabs is the integration layer |
| Guest screening | Build | Superhog API (identity check) | Behavioral classification is custom |
| Turnover scheduling | Build | Breezeway/Properly API | Scheduling optimization is custom |
| Guest messaging automation | Buy/extend | Hospitable / Guesty AI | LLM layer + property knowledge base integration is custom |
| Listing optimization | Build | Airbnb scrape + PMS | Regression model + LLM copy is custom |
