# Autonomous Diabetic Eye Screening AI Vendors

**Parent Industry:** [[industries/optometry-practices|Optometry Practices]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
Companies whose FDA-cleared software reads retinal photographs and returns a diabetic retinopathy result without an eye doctor, billed under CPT 92229 (a national average of about $50, per AEYE Health). Digital Diagnostics (LumineticsCore, formerly IDx-DR), Eyenuk (EyeArt) and AEYE Health are the US vendors (recalled). AEYE's clearance for a handheld camera was announced in April 2024, with 92%–93% sensitivity and 89%–94% specificity (search summary). They sell mostly to primary care, health systems and plans, which places them beside the optometry practice: they take diabetic screening volume that once came to optometrists and send referable cases on. Their clinical science and ML teams build and validate the models and monitor deployed performance.

## Insight Function
**Size:** ~10-40 ML engineers, clinical scientists and regulatory staff per vendor (estimate); image graders are production
**Output:** Cleared algorithms, validation studies, deployment performance monitoring
**Proprietary data:** Training and validation image sets assembled from partner sites and trials, and deployed-model logs
**Clock:** FDA submissions on the vendor's own schedule; customers' quality-measure seasons are the client's dates
**Buyer:** Chief medical or chief science officer at the vendor

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 2 |
| Q2 Labor mass + repeatable | ×2 | 2 |
| Q3 Proprietary data moat | ×3 | 4 |
| Q4 External clock | ×2 | 2 |
| Q5 Buyer + market | ×2 | 3 |
| **Weighted total** | | **32/60** |

**Kill switches:** **HIPAA**. Monitoring and retraining run on customers' retinal images and results under business-associate agreements. Scored consistently with [[niches/diagnostic-imaging-centers/radiology-ai-vendor-data-science/profile|🔍 Radiology AI & Reporting Vendors' Clinical Data Science Teams]] (32, kill switch). [[niches/dental-practices/dental-imaging-ai-vendors/profile|🔍 Dental Imaging Analysis Vendors]] (49) was scored before the current rulings.
**Verdict:** Logged — kill switch. A product business whose data is its customers' PHI. On 25 October 2026 only AEYE Health was hiring engineers, in Tel Aviv.
