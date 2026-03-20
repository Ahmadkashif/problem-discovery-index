# AI Agents and Platforms — Customs Brokers

**Industry:** [[customs-brokers|Customs Brokers]]
**Tags:** #ai-agent #ai-platform #transformers #bert #large-language-models #gradient-boosting #compliance #automation #revenue-impact

---

## Existing AI-Adjacent Platforms

### CBP ACE (Automated Commercial Environment)
CBP's entry filing portal. All formal entries are filed through ACE. ACE data includes examination status, liquidation outcomes, and entry rejection notices. The data source for examination risk modeling.

### CBP CROSS Database
Public database of binding tariff classification rulings. 60,000+ rulings with product descriptions and HTS assignments. The primary training data source for HTS classification models. Publicly accessible.

### Descartes CustomsInfo / Amber Road
Enterprise trade compliance platforms with HTS content and tariff program databases. These are the distribution channels for a classification model — broker adoption occurs through the tools they already use.

---

## AI Agent Opportunities

### 1. Entry Preparation Agent
**Trigger:** New shipment documents received (invoice, packing list, BOL uploaded to entry management system).
**Action sequence:**
1. Extract customs-required data fields from all uploaded documents
2. Reconcile extracted data across documents (invoice quantity vs. packing list, value consistency)
3. Run HTS classification model on product descriptions; present top-3 candidates to broker
4. Run pre-submission completeness check for the identified HTS codes and country of origin
5. Populate entry fields in ACE workflow; flag low-confidence items for broker review
**Value:** Reduces entry preparation time from 20-30 minutes to 5-8 minutes of review. Reduces keying errors and HTS misclassifications.

### 2. Exclusion Opportunity Alert Agent
**Trigger:** Weekly batch run against USTR exclusion feed + client import portfolio.
**Action sequence:**
1. Pull new Section 301/232 exclusion publications from USTR Federal Register feed
2. Match each new exclusion against client import records using semantic similarity
3. Calculate duty savings for matches above confidence threshold
4. Draft exclusion application or refund claim for high-value matches
5. Alert broker with matched exclusions, savings estimate, and draft application
**Value:** Ensures no client exclusion opportunities are missed. Converts a reactive (client-asks-broker) process into proactive advisory.

### 3. Quarterly Client Value Report Agent
**Trigger:** Quarterly scheduled run per client.
**Action sequence:**
1. Pull all entries filed for the client in the past 12 months from entry management system
2. Generate duty spend by HTS chapter and country of origin
3. Run trade program eligibility analysis against each entry line
4. Identify unclaimed eligible programs with duty savings calculation
5. Generate formatted client report with duty optimization opportunities and action items
**Value:** Delivers systematic value analysis that converts transactional clients to advisory engagements. Every client gets a professional duty review without dedicated analyst time.

---

## Build vs. Buy Assessment

| Capability | Build | Buy/Integrate | Notes |
|---|---|---|---|
| HTS classification model | Build | CROSS database (training data) | Transformer fine-tune is custom; data is public |
| Invoice data extraction | Build | AWS Textract / Google DocAI (base) | Customs-specific extraction layer is custom |
| Exclusion matching | Build | USTR feed (data) | Semantic similarity model is custom |
| Entry completeness check | Build | ACE + entry management system | Rules + LLM for commodity-specific requirements is custom |
| Trade program eligibility | Build | Public tariff schedules | Rules-based classification + LLM for edge cases is custom |
| Examination risk scoring | Build | ACE entry history | Gradient boosting; entry history is proprietary |
