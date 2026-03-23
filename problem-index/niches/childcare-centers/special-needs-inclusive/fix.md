# Teacher Accommodation Implementation Gap

**Niche:** [[niches/childcare-centers/special-needs-inclusive/profile|Special Needs Inclusive Programs]]
**Industry:** [[industries/childcare-centers|Childcare Centers]]
**Type:** Fix (Pain Point)
**One-liner:** IEPs specify classroom accommodations (visual schedules, sensory breaks, modified materials), but lead teachers who attend IEP meetings do not systematically transfer this knowledge to assistant teachers and substitutes — accommodations are implemented inconsistently.
**Tags:** #llm #text-generation #nlp #worker-facing #compliance

## The Problem
A child's IEP specifies: "visual schedule posted at eye level during transitions," "sensory break offered every 45 minutes," "simplified 2-step instructions for group activities," and "preferential seating near the teacher during circle time." The lead teacher who attended the IEP meeting implements these accommodations. But when the lead teacher is absent (sick day, break, professional development), the substitute or assistant teacher does not know about these accommodations. The IEP document is filed in the director's office, not accessible at the point of care. The child experiences an inconsistent environment, potentially triggering behavioral incidents that are then attributed to the child rather than the accommodation gap.

## Why It's Still Broken
IEP accommodation lists are written in educational jargon ("modify the sensory environment to reduce overstimulation triggers") that assistant teachers and substitutes may not understand. No system translates IEP accommodations into plain-language, classroom-specific action items posted where teachers can reference them. The director cannot monitor whether accommodations are being implemented — there is no accommodation compliance tracking equivalent to the ratio compliance tracking that licensing requires.

## What a Fix Looks Like
An accommodation management system that: (1) converts each child's IEP accommodations into plain-language action cards with specific instructions ("At 9:00, 9:45, 10:30 — offer Maya a sensory break at the calm corner. Show her the timer. 5 minutes."); (2) posts these action cards on the classroom's digital display or prints them for the wall, accessible to any staff member in the room; (3) prompts teachers to confirm accommodation implementation during the day (quick tap: "sensory break offered? Yes/No"); (4) tracks accommodation implementation rates per child over time; and (5) flags gaps to the director ("Maya's sensory breaks were missed 3 of 5 days this week").

## Who Feels the Pain
Children with disabilities who experience inconsistent support depending on which teacher is in the room — leading to preventable behavioral incidents, regression on IEP goals, and family frustration that the center "isn't following the IEP."

## Impact If Fixed
Accommodation implementation consistency improves from an estimated 60-70% (dependent on lead teacher presence) to 90%+ across all staff, reducing accommodation-gap-driven behavioral incidents by 40-50% and improving IEP goal progress rates — outcomes that directly affect the child's development and the family's trust in the program.
