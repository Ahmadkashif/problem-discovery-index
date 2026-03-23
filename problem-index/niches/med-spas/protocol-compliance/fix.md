# Pre-Treatment Screening & Contraindication Documentation Gaps

**Niche:** [[niches/med-spas/protocol-compliance/profile|Treatment Protocol & Compliance Management]]
**Industry:** [[industries/med-spas|Med Spas]]
**Type:** Fix (Pain Point)
**One-liner:** Pre-treatment screening for contraindications (pregnancy, active infections, medication conflicts, recent sun exposure) is done verbally and inconsistently — creating liability exposure when adverse events occur and no screening was documented.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #compliance #automation

## The Problem
Every med spa treatment has contraindications: laser treatments shouldn't be performed on tanned or sunburned skin, injectables are contraindicated during pregnancy, chemical peels interact with certain medications (Accutane, retinoids). Screening for these contraindications is supposed to happen before every treatment but often doesn't — especially for returning patients who "already filled out their intake form." When an adverse event occurs (a laser burn on a patient who was taking photosensitizing medication), the practice discovers there's no documentation of screening. The patient says "nobody asked me," and the practice has no evidence to the contrary.

## Why It's Still Broken
Pre-treatment screening adds 3-5 minutes to each appointment in a schedule already compressed for profitability. Staff skip screening for returning patients assuming "nothing has changed." Screening questions are treatment-specific (laser screening is different from injectable screening is different from peel screening), but most practices use a generic one-size-fits-all health history form. The screening process isn't enforced by any system — it's a human behavior problem disguised as a documentation problem.

## What a Fix Looks Like
Treatment-specific digital screening checklists that must be completed before the treatment room can be "checked in" in the practice management system. The system blocks treatment start until screening is documented. Checklists are adaptive: "Have you had sun exposure in the last 2 weeks?" only appears for laser treatments. "Are you currently pregnant or breastfeeding?" only appears for relevant procedures. For returning patients, the system pre-populates previous answers and asks "has anything changed?" — faster than full re-screening but still documented. Flag system for contraindication matches that require medical director review before proceeding.

## Who Feels the Pain
Providers who perform treatments without realizing a contraindication exists, practice owners who face malpractice claims with no screening documentation, and patients who experience preventable adverse events.

## Impact If Fixed
Eliminates the single largest source of preventable med spa adverse events, provides auditable documentation for every treatment, and reduces malpractice exposure by demonstrating consistent screening compliance.
