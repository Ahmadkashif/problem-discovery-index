# FDA Detention Risk Pre-Screening Tool

**Niche:** [[niches/customs-brokers/fda-regulated-food-cosmetics/profile|FDA-Regulated Food & Cosmetics Importers]]
**Industry:** [[industries/customs-brokers|Customs Brokers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool pre-screens food import entries for FDA detention risk before the shipment arrives — checking whether the product type, country of origin, or manufacturer appears on FDA's Import Alert list or has a detention history — so the importer can prepare for detention rather than being surprised at the port.
**Tags:** #gradient-boosting #bert #compliance #revenue-impact

## The Problem
FDA maintains Import Alerts — standing instructions to detention officers to detain specific products from specific countries or specific manufacturers "without physical examination" (DWPE). A shipment of canned vegetables from a Vietnamese manufacturer on Import Alert 99-19 (filthy foods) will be detained automatically. The customs broker filing the entry often doesn't check the Import Alert list before filing — they discover the detention after the shipment is held, the importer is charged demurrage, and a private lab analysis ($2,000-$5,000) is required to overcome the detention. Had the broker known the product was on an Import Alert before filing, they could have advised the importer to obtain preemptive lab results or source from a different manufacturer.

## Why Nobody Has Built This
FDA's Import Alert database is publicly available but not easily cross-referenced against entry data. Import Alerts reference products by product code, country, and sometimes manufacturer — but not by HTS code. The broker must translate the HTS classification into FDA product code, then search the Import Alert database by product code and country — a manual cross-reference that no system performs automatically during entry preparation.

## What to Build
An FDA detention risk screening tool that: (1) accepts the entry line items (HTS code, country of origin, manufacturer); (2) maps HTS codes to FDA product codes; (3) checks the Import Alert database for matching alerts by product, country, and manufacturer; (4) returns a detention risk assessment per line item ("high risk — product on Import Alert 99-19 from Vietnam; recommend preemptive lab analysis"); (5) provides the specific Import Alert citation and the evidence required to overcome the detention.

## Target Customer
Customs brokers and FDA compliance officers at importers filing food, supplement, or cosmetic entries. Approximately 1,000 brokerages handle significant FDA-regulated food import volume.

## Impact If Built
Pre-screening for detention risk saves $5,000-$20,000 per detention event (demurrage, lab costs, refusal processing) by enabling preemptive action. For a broker filing 50 FDA-regulated entries per month, identifying 5-10 high-risk entries before they arrive prevents 2-3 detentions monthly — saving $10K-$60K per month.
