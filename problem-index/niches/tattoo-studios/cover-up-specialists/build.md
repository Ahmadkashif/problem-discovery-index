# Cover-up Feasibility Assessment Tool

**Niche:** [[niches/tattoo-studios/cover-up-specialists/profile|Cover-up Specialists]]
**Industry:** [[industries/tattoo-studios|Tattoo Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool exists to analyze an existing tattoo's characteristics (ink density, color saturation, line weight, scarring) and generate cover-up design constraints automatically.
**Tags:** #cnn #semantic-segmentation #computer-vision #tacit-knowledge-ml

## The Problem
Cover-up feasibility assessment is entirely dependent on an experienced artist's visual judgment. They look at an existing tattoo and mentally process ink density, color depth, line thickness, skin scarring, and placement to determine what's coverable, what needs laser lightening first, and what design constraints apply (minimum size, required darkness, shapes that work with existing lines). Clients send photos via DM asking "can this be covered?" and artists either schedule an in-person consult or make rough guesses from photos — neither scales.

## Why Nobody Has Built This
The assessment requires computer vision that understands tattoo-specific visual features (ink saturation aging, scar tissue texture, color layer depth) — a domain with no labeled training dataset. Building this requires partnering with experienced cover-up artists to annotate hundreds of existing tattoos with feasibility assessments, design constraints, and difficulty ratings. The visual-to-constraint mapping is a form of tacit knowledge that artists develop over thousands of consultations.

## What to Build
A mobile app where a client or artist photographs the existing tattoo under standardized lighting guidance, and the system generates a feasibility report: ink density map (hot spots that need extra coverage), color analysis (which existing colors will bleed through), scar tissue detection, and minimum cover-up size estimate. The output is a constraint brief the artist can use to start designing, plus a client-facing summary explaining what's achievable without an in-person visit.

## Target Customer
Cover-up specialists handling 10+ consultations per month, where 30-40% of inquiries are non-viable — the tool saves 1-2 hours per week in wasted consultations and enables remote pre-screening.

## Impact If Built
Reduces in-person consultation volume by 30-40% by pre-screening non-viable cover-ups remotely, enables artists to take on 2-3 additional viable projects per month, and sets client expectations before the first meeting.
