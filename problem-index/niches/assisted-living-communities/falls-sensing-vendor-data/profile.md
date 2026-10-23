# Fall Detection & Resident Sensing Vendor Data Teams

**Parent Industry:** [[industries/assisted-living-communities|Assisted Living Communities]]
**Category:** Insight Layer
**Value-Chain Position:** Suppliers selling into the industry

## What They Do
SafelyYou (AI video fall detection with post-fall review), Inspiren (AUGi room sensors, e-call and care analytics; $70M raised in September 2026) and Teton.ai (computer vision, Copenhagen) install cameras or sensors in residents' rooms, detect falls and bed exits, and report response times and fall trends to operators. Their data science teams train detection models and build analytics from the events their own hardware captures. Operators pay a subscription per unit.

## Insight Function
**Size:** ~10–40 data scientists and analytics engineers per vendor (estimate); clinical staff who review individual falls are production
**Output:** Detection models, fall and response dashboards, post-fall reports and occasional outcome studies
**Proprietary data:** Video and sensor event streams from thousands of resident rooms, labelled with falls and outcomes, captured by the vendor's own devices
**Clock:** None set by a third party; operators renew subscriptions on their own calendars
**Buyer:** Chief Technology or Chief Product Officer at the vendor

## Scorecard
| Criterion | Weight | Score |
|---|---|---|
| Q1 Insight is the invoice | ×3 | 2 |
| Q2 Labor mass + repeatable | ×2 | 3 |
| Q3 Proprietary data moat | ×3 | 5 |
| Q4 External clock | ×2 | 2 |
| Q5 Buyer + market | ×2 | 3 |
| **Weighted total** | | **37/60** |

**Kill switches:** undetermined (subscription and consent terms unread) for the sensor and video corpus, which the vendor captures with its own hardware; the score is for this half. The half of the work that pulls resident records from operators' EHRs runs under business associate and service agreements and would carry a "data isn't theirs" switch.
**Verdict:** Logged — below threshold. The industry's richest unlabelled-to-labelled dataset on falls in dementia care, but the analysis is bundled into a subscription, no external deadline governs it, and a handful of vendors make a small buyer market. Named here mainly as engineering employers: SafelyYou and Inspiren were both hiring engineers on their own boards on 2026-10-24 (see the source log). The nearest scored twin is the sepsis prediction vendors under general hospitals ([[niches/general-hospitals/sepsis-deterioration-prediction-vendors/profile|🔍 Sepsis & Deterioration Prediction Vendors]], 32, kill switch), which work on hospitals' EHR data rather than their own sensors.
