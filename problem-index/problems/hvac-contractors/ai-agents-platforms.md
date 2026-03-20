# AI Agents and Platforms — HVAC Contractors

**Industry:** [[hvac-contractors|HVAC Contractors]]
**Tags:** #ai-agent #ai-platform #gradient-boosting #lstms-and-grus #decision-trees #feature-engineering #time-series-forecasting #evaluation-metrics #automation #workflow-orchestration #revenue-impact

---

## Existing AI-Adjacent Platforms

### ServiceTitan
Same dominance as in plumbing. Logs all service call history, equipment records, customer data, maintenance agreements, and technician dispatch. The data foundation for all HVAC ML applications.

### ecobee / Sensi (Emerson) / Carrier Côr
Smart thermostat platforms with continuous runtime and temperature data. ecobee has a developer API. Carrier Côr integrates with Carrier dealer portals for equipment status. These platforms have the sensor data that enables predictive failure detection — but the data isn't currently surfaced to contractors in actionable form.

### Testo / Fieldpiece
Bluetooth-enabled manifold gauge sets that digitally capture refrigerant circuit readings. Testo's Smart Probes and Fieldpiece's Job Link platform already capture gauge readings digitally — the data exists, it's just not integrated into diagnostic decision support. These are the data capture endpoints for a refrigerant diagnosis model.

### Carrier / Trane Dealer Portals
OEM equipment data — model, serial number, original installation date, factory specification sheets. Integration source for equipment age and specification data used in efficiency recommendation tools.

---

## AI Agent Opportunities

### 1. Refrigerant Diagnostic Assistant Agent
**Trigger:** Technician connects Bluetooth manifold gauge to the service call in the mobile app.
**Action sequence:**
1. Receive live gauge readings (suction, discharge, suction line temp, liquid line temp) from Testo/Fieldpiece Bluetooth adapter
2. Pull ambient and indoor return temperatures from the tech's temperature probes
3. Compute superheat, subcooling, pressure ratio
4. Run differential diagnosis model — return top-3 fault conditions with probabilities
5. Display step-by-step narrowing diagnostic sequence for the top diagnosis (e.g., "measure capacitor microfarad before condemning compressor")
6. On confirmation of root cause, auto-populate the service call repair code in ServiceTitan
**Value:** Brings 5-year technician diagnostic reasoning to the fingertips of a 1-year tech. Reduces misdiagnosis callbacks. Reduces time to confirmed diagnosis from 30-45 minutes to 15-20 minutes.

### 2. Maintenance Agreement Retention Agent
**Trigger:** Weekly batch run, 90 days before each customer's renewal date.
**Action sequence:**
1. Score all customers with renewals in the next 90 days using the churn prediction model
2. Segment flagged high-risk customers by predicted churn reason
3. Generate personalized retention messages per segment (equipment age → replacement consultation offer; engagement lapse → complimentary filter check; price sensitivity → loyalty discount offer)
4. Queue outreach in ServiceTitan or connected CRM for service advisor review
5. Track outreach outcomes and update customer retention probability
**Value:** Converts reactive renewal management into proactive retention. Targets the right message to the right customer based on why they're likely to cancel.

### 3. Proactive Replacement Outreach Agent
**Trigger:** Weekly run against customer database.
**Action sequence:**
1. Query all customers with equipment age ≥ 10 years who haven't been quoted a replacement in 24 months
2. Pull local utility rates and current manufacturer rebates for the equipment tier appropriate to each customer's system
3. Generate a 10-year cost-of-ownership comparison (continue repairing vs. replace with current high-efficiency equipment)
4. Generate personalized outreach email/SMS with the savings estimate and seasonal call-to-action
5. Book an efficiency consultation call or service visit directly from the outreach message
**Value:** Proactive equipment replacement outreach from data has 2-3× higher close rate than cold calling. Converts the firm's existing customer database into a pipeline of replacement opportunities.

### 4. Smart Thermostat Alert Agent
**Trigger:** Anomaly detected in connected thermostat runtime data.
**Action sequence:**
1. Monitor runtime time series for all connected customers via thermostat API (ecobee, Sensi)
2. Flag when runtime deviation from seasonal baseline exceeds threshold (anomaly detection model)
3. Generate customer-facing alert: "Your HVAC system is running longer than usual — this may indicate a service issue. We recommend scheduling a check before your utility bill increases."
4. Trigger proactive service call booking offer with priority scheduling
5. Brief the assigned technician with the runtime anomaly pattern before the service call
**Value:** Converts smart thermostat data into a proactive service revenue stream. Customers who receive a proactive alert before a comfort failure are more loyal and more likely to approve preventive work.

---

## Build vs. Buy Assessment

| Capability | Build | Buy/Integrate | Notes |
|---|---|---|---|
| Refrigerant diagnosis model | Build | Bluetooth gauge integration (Testo/Fieldpiece) | Gauge reading capture is buy; diagnosis model is build |
| Maintenance churn prediction | Build | ServiceTitan data export | Model is custom; feature engineering is HVAC-specific |
| Smart thermostat anomaly detection | Build | ecobee/Sensi API for data | Anomaly model is custom; data capture is buy |
| Load calculation tool | Buy/extend | Wrightsoft (simplified) | Existing software; mobile UX is the gap |
| Efficiency recommendation engine | Build | Utility rate API + manufacturer rebate feeds | Integration is custom; model is simple regression |
| Refrigerant compliance logging | Integrate | ServiceTitan API | Automation layer over existing data |
