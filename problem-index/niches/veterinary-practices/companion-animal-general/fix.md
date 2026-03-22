# Client No-Show and Lapsed Wellness Recall Recovery

**Niche:** [[niches/veterinary-practices/companion-animal-general/profile|Companion Animal General Practice]]
**Industry:** [[industries/veterinary-practices|Veterinary Practices]]
**Type:** Fix (Pain Point)
**One-liner:** 30-40% of annual wellness visits are missed because recall systems send the same generic reminder to every overdue client regardless of their likelihood to return, their preferred communication channel, or their pet's specific wellness needs.
**Tags:** #gradient-boosting #logistic-regression #feature-engineering #cross-validation #evaluation-metrics #revenue-impact #automation #tacit-knowledge-ml

## The Problem
Wellness recall drives 30-40% of a companion animal practice's annual revenue directly (exams, vaccinations, heartworm tests, dental cleanings) and generates 40-50% of diagnostic and surgical revenue indirectly (the wellness visit is when masses are discovered, bloodwork abnormalities are caught, and dental disease is graded). When a client doesn't return for their pet's annual visit, the practice loses $250-500 in immediate wellness revenue and $500-2,000 in downstream treatment revenue. Current recall systems — postcards, generic email blasts, automated phone reminders — treat every overdue client identically. A client who missed by 3 weeks gets the same message as one who hasn't been seen in 2 years. A client who always responds to text messages gets the same postcard as one who only responds to phone calls.

## Why It's Still Broken
Experienced receptionists and office managers develop tacit knowledge about which clients respond to which outreach: "The Hendersons always cancel but rebook if you call Tuesday morning," "Clients with puppies under 2 are more likely to return than senior dog owners," "Families with pet insurance almost always come back — the ones without it are price-sensitive and need a specific reason." This pattern recognition lives in the receptionist's head and disappears when they leave the practice. The PMS stores the raw data — appointment history, species and breed, insurance status, cancellation patterns, treatment history, communication preferences — but no recall system uses it to segment and personalize outreach. A gradient-boosted model trained on a practice's own recall history could predict reactivation probability and recommend the optimal channel, timing, and message urgency per client.

## What a Fix Looks Like
An intelligent recall layer that sits on top of the existing PMS and segments overdue clients into tiers: high-probability reactivation (auto-send personalized text with one-tap rebooking link and specific wellness items due), medium-probability (phone call from receptionist with specific talking points about their pet's overdue needs), and low-probability (re-engagement campaign with educational content about breed-specific health risks of skipping annual care). The system learns from each practice's own data — which outreach actions led to rebooked appointments — and continuously improves its segmentation. For the receptionist, it replaces the weekly "pull the overdue list and start calling" ritual with a prioritized action queue.

## Who Feels the Pain
The receptionist or office manager who spends 4-6 hours per week manually calling overdue clients from an undifferentiated list, and the practice owner who watches revenue dip when recall compliance drops below 65%.

## Impact If Fixed
Increasing recall reactivation from 55% to 75% for a typical independent practice with 2,500 active patients recovers $120K-250K in annual revenue (wellness + downstream diagnostics and treatment). The receptionist reclaims 4-6 hours per week of manual calling time, redirected to in-clinic client service.
