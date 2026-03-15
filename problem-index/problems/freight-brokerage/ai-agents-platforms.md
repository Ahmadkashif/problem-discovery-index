# AI Agents and Platforms — Freight Brokerage

**Industry:** [[freight-brokerage|Freight Brokerage]]
**Tags:** #ai-agent #ai-platform #automation #workflow-orchestration #revenue-impact

---

## Existing AI-Adjacent Platforms

### DAT / Truckstop
Load boards and spot rate data platforms. DAT's rate API provides lane-level rate data for pricing models. DAT has its own AI rate prediction features (RateView, Rate Intelligence). Integration target for market rate signal ingestion.

### Parade / Newtrul
Carrier capacity procurement automation platforms. Parade has built carrier matching and automated outreach capabilities. Parade is the closest existing product to the carrier outreach automation described in worker-life-1 — an acqui-hire or partnership target rather than a build.

### McLeod Software / Mercury Gate
TMS platforms for mid-to-large freight brokerages. Contain all transaction history. Integration targets for pricing models and analytics.

### FreightWaves SONAR
Freight market intelligence platform with granular capacity and demand data by lane and equipment type. SONAR API provides the external demand signal for lane rate prediction and capacity forecasting.

---

## AI Agent Opportunities

### 1. Load Pricing Agent
**Trigger:** New load entered in TMS.
**Action sequence:**
1. Identify lane, equipment, pickup date, weight from load record
2. Query DAT rate API for current lane spot rate and 7-day trend
3. Query FreightWaves SONAR for capacity-to-load ratio on this lane
4. Run pricing model: recommended shipper quote and target carrier buy rate with expected margin
5. Pre-populate the TMS quote field; broker reviews and sends to shipper
**Value:** Consistent margin-optimizing prices replace gut-feel pricing. Junior brokers price as well as senior brokers on routine lanes.

### 2. Carrier Outreach Agent
**Trigger:** Load accepted by shipper; coverage needed.
**Action sequence:**
1. Identify top-15 carrier candidates ranked by predicted acceptance probability
2. Send automated outreach (SMS + email) to candidates with load details and target rate
3. Collect responses and rates from carriers who reply
4. Surface accepted candidates to broker sorted by rate and reliability score
5. Track non-responding carriers for follow-up threshold (24 hours = next tier of candidates)
**Value:** Eliminates the manual outreach loop. Broker steps in for final negotiation and booking, not cold calling.

### 3. In-Transit Exception Agent
**Trigger:** Continuous monitoring of active shipments.
**Action sequence:**
1. Poll ELD position and HOS data for all in-transit loads
2. Compute ETA and compare to delivery appointment
3. Flag shipments with > 20% late probability given current position and HOS remaining
4. Send proactive shipper notification for flagged loads: "Your shipment is running approximately 2 hours behind schedule. The carrier estimates arrival at 3pm."
5. Alert broker only for severe late scenarios or driver-dark situations
**Value:** Proactive shipper communication converts service failures from surprises to managed situations. Shipper retention is significantly higher for brokers who communicate proactively vs. reactively.

---

## Build vs. Buy Assessment

| Capability | Build | Buy/Integrate | Notes |
|---|---|---|---|
| Lane rate prediction | Build | DAT API + SONAR API (data) | Pricing model is custom; market data is licensed |
| Carrier outreach automation | Buy/extend | Parade / Newtrul | Existing products; carrier-specific ranking is custom addition |
| Fraud detection | Build | FMCSA + carrier history | Anomaly detection model is custom |
| Demand forecasting | Build | TMS data + public signals | Time-series model is custom; external data is public |
| Late shipment prediction | Build | ELD APIs + weather API | ML model is custom; data feeds are commodity |
