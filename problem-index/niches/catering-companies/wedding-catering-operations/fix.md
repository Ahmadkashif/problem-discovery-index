# Guest Count Volatility and Over-Prep Waste

**Niche:** [[niches/catering-companies/wedding-catering-operations/profile|Wedding Catering Specialists]]
**Industry:** [[industries/catering-companies|Catering Companies]]
**Type:** Fix (Pain Point)
**One-liner:** Wedding guest counts swing 5-15% between the final guarantee and actual attendance — and the caterer bears the cost of prepping for the guarantee while serving fewer guests.
**Tags:** #gradient-boosting #regression #tabular-ml #tacit-knowledge-ml #revenue-impact

## The Problem
Wedding couples provide a "final guest count" 7-14 days before the event, and the caterer preps and charges based on this number. But actual attendance is almost always lower: 5-15% of guaranteed guests no-show (travel complications, last-minute conflicts, plus-ones who do not come). The caterer preps for 200 and serves 175, wasting $1,500-$4,000 in food, labor, and rentals. The contract requires the couple to pay for the guaranteed count regardless — but enforcing payment for 25 uneaten plates strains the relationship and damages referral potential.

## Why It's Still Broken
The caterer faces an asymmetric risk: running short is catastrophic (running out of entrees at a wedding is a career-ending failure), so they always prep to guarantee plus 5-10%. There is no predictive model to calibrate the safety buffer — experienced caterers develop a feel for which weddings will have high no-show rates (destination weddings, young couples with out-of-town guests, weddings during holiday weekends), but this knowledge is tacit and imprecise.

## What a Fix Looks Like
A no-show prediction model trained on historical wedding attendance data: guest count guarantee vs. actual attendance, indexed by wedding type (local vs. destination), season, day of week, guest demographics, and RSVP response patterns. The model outputs a predicted actual attendance with confidence intervals, enabling the caterer to calibrate prep quantities and safety buffers per wedding rather than applying a blanket overage.

## Who Feels the Pain
The executive chef who watches $3,000 of prepped food go to waste after every wedding, and the owner who must choose between enforcing payment for uneaten plates (damaging relationships) or absorbing the cost (losing margin).

## Impact If Fixed
Reducing over-prep from 10-15% to 3-5% saves $800-$2,000 per wedding — $40K-$200K annually for a caterer doing 50-100 weddings/year.
