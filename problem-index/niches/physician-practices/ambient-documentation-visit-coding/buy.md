# EHR-Bundled Ambient Extended With Specialty Coding

**Niche:** [[niches/physician-practices/ambient-documentation-visit-coding/profile|Ambient Documentation & Office Visit Coding]]
**Industry:** [[industries/physician-practices|Physician Practices]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The free ambient scribe inside the EHR writes a good primary care note; specialty practices need it extended with procedure documentation, specialty templates and the coding rules their audits test.
**Tags:** #large-language-models #transformers #data-integration #compliance #revenue-impact #quick-win
**Contested on:** Every serious competitor in this niche is fighting to turn the office visit into a signed note that supports the billed E/M level and risk-adjustment codes before the physician leaves for the day, and whoever closes the most notes the same day with no downcoding on payer or RADV audit takes the account.

## The Problem
athenahealth includes athenaAmbient at no extra subscription cost (HIT Consultant), and other EHRs bundle Microsoft's or their own scribes. For a primary care group the bundled tool may be enough. A dermatology, orthopaedic or gastroenterology practice bills procedures alongside E/M visits, and the free scribe does not know when a visit plus procedure needs modifier -25, or what a procedure note must contain.

## What Already Exists
EHR-native ambient (athenaAmbient, Epic's AI Charting for Community Connect groups), third-party scribes with specialty templates (Abridge, Ambience, Suki, Commure), and coding modules in the EHR.

## The Customization Gap
The specialty layer needs:

- procedure note templates that capture site, size, technique and counts in the form the CPT code requires;
- separately identifiable E/M detection for modifier -25;
- the specialty's audit history, since dermatology and orthopaedics draw different payer edits;
- the practice's own templates and phrasing, so physicians do not rewrite every note.

## Target Customer
Specialty groups and MSOs of 10–200 physicians already on an EHR that bundles a scribe.

## Impact If Solved
Practices keep the free scribe and add only the specialty layer, saving ~$100–$300 per clinician per month against a second scribe licence (estimate), while cutting modifier and procedure-documentation denials by ~20%–30% (estimate).
