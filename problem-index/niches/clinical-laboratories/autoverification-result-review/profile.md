# Autoverification & Result Review

**Parent Industry:** [[industries/clinical-laboratories|Clinical Laboratories]]
**Category:** Highly Automatable
**Contested on:** Every serious competitor in this niche is fighting to take routine result review off technologists' hands, and whoever cuts technologist review minutes per thousand results with no rise in corrected reports takes the account.

## Profile
**Market Size:** ~$700M a year in middleware, rules configuration and technologist review time on held results (estimate)
**Share of Parent Industry:** ~1.5% of industry revenue (estimate)
**Digital Adoption:** Medium-High — middleware and rules engines are standard in mid-size and large labs; the review of held results is manual
**Target Buyer:** Laboratory director or core lab manager; lab automation lead at a reference lab
**Automation Potential:** Very High for routine release; the held minority needs judgement that can be learned

## What Makes This a Distinct Niche
Autoverification is the rules layer between analyser and patient record. Middleware checks each result against limits, delta checks, instrument flags and serum indices, and releases what passes. Everything else waits for a medical laboratory scientist. Rules are written once by a lab's own staff, rarely revalidated, and tuned conservatively, so they hold many real results and miss subtle spurious ones. The published IV-fluid contamination work shows both sides: a learned model caught contamination the current workflow missed, but its MCC fell from 0.747 to 0.387 at a second hospital (Clin Chem 2025). This niche is the industry's tacit-knowledge problem in operational form; see the hub's high-impact note.

## Current Tools & Gaps
Middleware from Data Innovations (Instrument Manager), Roche, Beckman Coulter, Siemens Healthineers and Abbott (AlinIQ); LIS rule engines in Epic Beaker, Oracle Health and Clinisys. Gaps: rules not learned from outcomes, no record of why held results were released or rejected, delta checks that fire on predictable patients, and no measure of how many released results were later corrected.

## Problems
- [[niches/clinical-laboratories/autoverification-result-review/build|🔨 Build: Spurious-Result Detection Learned From the Technologists' Own Holds]]
- [[niches/clinical-laboratories/autoverification-result-review/buy|🛒 Buy: Instrument Middleware Given a Learned Review Layer]]
- [[niches/clinical-laboratories/autoverification-result-review/fix|🔧 Fix: Delta Checks That Fire on Every Dialysis Patient]]
