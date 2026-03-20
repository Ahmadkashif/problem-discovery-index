# AI Agents and Platforms — Real Estate Appraisers

**Industry:** [[real-estate-appraisers|Real Estate Appraisers]]
**Tags:** #ai-agent #ai-platform #large-language-models #gradient-boosting #feature-engineering #evaluation-metrics #automation #compliance #revenue-impact

---

## Existing AI-Adjacent Platforms

### TOTAL by a la mode
The dominant residential appraisal report writing software. All report data lives here. a la mode has AI features in development (form field automation, comparable data import). Integration target for market commentary generation, adjustment support, and CU pre-review. a la mode's report library is the best potential training data source for appraisal-specific NLP.

### CoreLogic / Black Knight
National real estate data aggregators with MLS data, property characteristics, and appraisal history. CoreLogic's Trestle platform provides MLS data APIs. These are the data foundation for market-calibrated adjustment development.

### Fannie Mae Collateral Underwriter (CU)
Post-submission AI review system that scores every submitted appraisal on multiple risk dimensions. CU is the external quality signal that appraisers optimize against. Understanding CU scoring patterns is the basis for pre-submission risk prediction.

---

## AI Agent Opportunities

### 1. Pre-Submission Report Review Agent
**Trigger:** Appraiser marks report complete in TOTAL and initiates submission.
**Action sequence:**
1. Parse the completed report fields and narrative sections
2. Check internal consistency: market commentary direction vs. comp price trend; adjustment grid vs. market-calibrated adjustment norms; USPAP required field completeness
3. Flag specific inconsistencies with brief explanation and suggested correction
4. Score predicted CU risk (low/medium/high) with specific predicted flag reasons
5. Appraiser reviews flags, makes corrections, resubmits clean report
**Value:** Catches common revision triggers before submission. Reduces revision request rate from lenders. Protects the appraiser's quality metrics with AMC clients.

### 2. Market Conditions Auto-Update Agent
**Trigger:** New appraisal assignment received.
**Action sequence:**
1. Identify subject property's submarket (zip code or neighborhood boundary)
2. Pull current MLS statistics from CoreLogic/MLS API: sold count, DOM, median price, list-to-sale ratio, active inventory
3. Compute month-over-month and year-over-year trends
4. Generate FNMA-formatted market conditions commentary
5. Pre-populate the market conditions section in TOTAL for appraiser review
**Value:** Eliminates 15-20 minutes of MLS data gathering and writing per assignment. Ensures market commentary reflects current conditions rather than copied-forward text from a prior report.

### 3. Comparable Search and Ranking Agent
**Trigger:** Appraiser enters subject property characteristics in the comp search workflow.
**Action sequence:**
1. Query MLS/CoreLogic for candidate comparables within proximity and recency filters
2. Score each candidate by multi-attribute similarity to the subject (using market-calibrated adjustment weights)
3. Rank and present top-10 candidates with estimated total adjustment magnitude per candidate
4. Flag candidates with large single adjustments (GLA difference > 200 sq ft at current market rate) as lower quality
5. Appraiser selects final 3-6 comps from the ranked list
**Value:** Reduces comp search time from 20-30 minutes to 5-minute review. Produces defensible comp selections with lower total adjustments and lower CU risk.

---

## Build vs. Buy Assessment

| Capability | Build | Buy/Integrate | Notes |
|---|---|---|---|
| Market-calibrated adjustment model | Build | CoreLogic/MLS data (input) | Hedonic regression is custom; market data is licensed |
| CU pre-submission risk scoring | Build | TOTAL API | Feature engineering from report fields is custom |
| Market commentary generation | Build | TOTAL + CoreLogic API | LLM fine-tune on appraisal corpus; data integration is custom |
| Comparable ranking | Build | CoreLogic Trestle API | Ranking model is custom; property data is licensed |
| Floor plan sketch generation | Build | LiDAR / camera APIs | Computer vision / measurement model is custom |
| Condition/quality classification | Build | — | Vision model; requires UCDP data partnership |
