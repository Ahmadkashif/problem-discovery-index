# AI Agents and Platforms — Commercial Real Estate

**Industry:** [[commercial-real-estate|Commercial Real Estate]]
**Tags:** #ai-agent #ai-platform #automation #workflow-orchestration #revenue-impact

---

## Existing AI-Adjacent Platforms

### CoStar / LoopNet
The dominant CRE data platform. CoStar's AI features (property recommendations, lease comp analysis) are available only to subscribers at $8,000-$25,000 per year. This price point excludes thousands of independent brokers and small firms — the market opportunity for CoStar-alternative analytics.

### Buildout
CRE-specific marketing and CRM platform used by thousands of commercial brokers. Produces offering memoranda, property flyers, and email campaigns. Has a large OM archive and is the natural distribution platform for OM generation AI.

### ClientLook
CRE-specific CRM with deal tracking, contact management, and pipeline analytics. Contains the deal history data needed for pipeline velocity prediction and relationship intelligence.

### TREPP
Commercial real estate data platform focused on CMBS loan and property transaction data. Provides the public transaction data that is the foundation for cap rate modeling without CoStar.

---

## AI Agent Opportunities

### 1. Offering Memorandum Generation Agent
**Trigger:** Broker creates a new listing in Buildout with property data and financials.
**Action sequence:**
1. Receive property data (address, type, rent roll, operating statement, asking price)
2. Pull market data: submarket comparable transactions, cap rate trend, submarket vacancy and absorption statistics
3. Generate OM narrative sections: executive summary, investment highlights, property description, market overview
4. Format financial tables: rent roll summary, NOI calculation, returns analysis at multiple cap rate scenarios
5. Assemble PDF OM in the broker's brand template
6. Deliver to broker for review, with tracked-changes editing interface for revisions
**Value:** Returns 12-20 hours of analyst time per listing to the broker. Enables boutique investment sales firms to market with institutional-quality materials.

### 2. Deal Stall Detection and Re-Engagement Agent
**Trigger:** Daily monitoring of all active deals in ClientLook or Buildout.
**Action sequence:**
1. Compute deal stage duration vs. median for that deal type and stage
2. Flag deals in the top-quartile of stage duration (likely stalling)
3. Generate recommended re-engagement action per stalled deal (schedule tour, send new market data, schedule call with principal)
4. Draft a specific client message for the broker's review (references the specific deal and current market conditions)
5. Surface in broker's weekly priority list
**Value:** Recovers deals that would go cold from broker inattention during busy periods. Long-cycle deal businesses lose more revenue to dormant relationships than to competition.

### 3. Lease Abstraction Agent
**Trigger:** Document uploaded to deal file in Buildout or DocuSign.
**Action sequence:**
1. Identify document type (lease vs. PSA vs. other)
2. Run clause extraction model on lease document
3. Generate structured abstract with all standard fields populated
4. Flag unusual clauses (non-standard termination rights, co-tenancy provisions, unusual CAM caps)
5. Deliver to deal file as a structured abstract + risk flag summary
**Value:** Reduces per-lease abstraction from 2-4 hours to 20-30 minutes of review. Enables thorough due diligence without outside counsel on straightforward leases. Catches risk provisions that manual review under time pressure might miss.

### 4. Tenant Prospecting Agent
**Trigger:** Broker creates a new leasing assignment for a vacant space.
**Action sequence:**
1. Receive space parameters: location, property type, square footage, asking rent
2. Pull companies in the relevant size tier and industry type within the submarket
3. Score each company on prospect probability (employment growth + lease expiration timing + industry co-location patterns)
4. Return ranked prospect list with contact information and outreach rationale
5. Export to broker's CRM for outreach campaign
**Value:** Replaces cold business directory canvasing with targeted prospect outreach. Precision prospecting reduces the time-to-signed-LOI by improving tenant targeting from the first contact.

---

## Build vs. Buy Assessment

| Capability | Build | Buy/Integrate | Notes |
|---|---|---|---|
| Cap rate / valuation model | Build | TREPP + deed records (data) | Model is custom; public data is the input |
| Lease abstraction | Build | DocuSign / Buildout API | LLM fine-tune on CRE leases; extraction layer is custom |
| OM generation | Build | Buildout API | LLM fine-tune on OM corpus; template/layout is custom |
| Tenant prospect scoring | Build | LinkedIn API + public records | Multi-source feature pipeline + custom model |
| Deal pipeline intelligence | Build | ClientLook / Buildout API | CRE-specific survival analysis; stage data is in CRM |
| Market data / comparables | Build | TREPP + county records | Long-term data accumulation; CoStar-alternative positioning |
