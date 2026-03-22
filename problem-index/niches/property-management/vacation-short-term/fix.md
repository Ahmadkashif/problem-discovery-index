# Cleaning Crew Scheduling and Quality Verification

**Niche:** [[niches/property-management/vacation-short-term/profile|Vacation & Short-Term Rental]]
**Industry:** [[industries/property-management|Property Management]]
**Type:** Fix (Pain Point)
**One-liner:** STR turnover cleaning — the 3-5 hour window between checkout and check-in — is managed through text message groups with independent cleaners who miss messages, arrive late, or deliver inconsistent quality, and no verification system confirms the property is actually guest-ready before the next guest receives the check-in code.
**Tags:** #automation #worker-facing #quick-win #cnns #gradient-boosting

## The Problem
A 50-unit STR company processes 500-800 turnovers per month. Each turnover requires: stripping and remaking beds with fresh linens, cleaning all surfaces, restocking consumables (soap, toilet paper, coffee, paper towels), running dishwasher, checking for damage, and setting the property to guest-ready condition per the brand standard. Cleaning is performed by independent contractors or small cleaning companies, coordinated via text message: "Unit 12 checkout today 11 AM, check-in at 4 PM, please clean by 3 PM." The problems: cleaners miss messages (5-10% of the time), arrive late (15-20%), deliver inconsistent quality (10-15% of cleans require re-work), and don't report damage or missing items (unless egregious). The STR manager has no visibility into whether the clean happened, when it happened, and whether quality meets the standard — until the next guest complains. A single bad clean that results in a negative Airbnb review can reduce a listing's booking rate by 10-20% for months.

## Why It's Still Broken
TurnoverBnB and Properly connect cleaners with STR managers and provide scheduling, but quality verification is based on the cleaner self-reporting completion. No tool verifies that the property actually meets the guest-ready standard. Photo-based verification exists (the cleaner takes photos after cleaning) but requires the STR manager to review 10-20 photos per unit per turn — at 500 turns per month, that's 5,000-10,000 photos to review. Without visual AI to verify quality, photo-based verification creates more work than it saves.

## What a Fix Looks Like
A turnover management system with three components. First, automated scheduling: when a booking is confirmed, auto-schedule the turnover cleaning based on checkout time, check-in time, and cleaner availability — sent as a confirmed assignment, not a text request. Second, completion verification: the cleaner takes standardized photos (each room, bed, bathroom, kitchen) after completing the clean. A CNN-based quality assessment checks each photo against the property's guest-ready standard: beds properly made with correct linens, surfaces clear, bathroom clean, amenities restocked. The system flags issues ("bedroom 2: bed appears unmade" or "kitchen: dishes visible on counter") for the cleaner to correct before marking complete. Third, guest-ready confirmation: only when the quality check passes does the system send the check-in code to the guest and mark the property as ready — preventing guests from arriving to unclean properties.

## Who Feels the Pain
STR managers who discover a bad clean only when the guest complains — by which time the damage (negative review, refund request) is done. Cleaners who take pride in their work but get blamed for quality issues they weren't aware of (a previous guest's stain they didn't notice). Guests who check into properties that aren't guest-ready despite paying $200-500/night.

## Impact If Fixed
Eliminates guest-arrival-to-unclean-property incidents by verifying quality before issuing check-in access. Reduces cleaning quality callbacks by 60-80% through AI-assisted quality verification. Improves Airbnb/VRBO review scores by 0.1-0.3 stars on average through consistent cleanliness — worth $5K-15K per property per year in improved booking rates. Saves STR managers 10-15 hours per week in photo review and quality management.
