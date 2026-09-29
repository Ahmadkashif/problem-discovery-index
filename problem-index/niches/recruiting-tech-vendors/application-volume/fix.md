# Fix: Friction Filters for Persistence, Not Suitability

**Niche:** [[niches/recruiting-tech-vendors/application-volume/profile|Application Volume & Generative Noise]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** The twenty-minute application form with the re-typed resume is a volume control, and it selects the people with the most time rather than the people best suited.
**Tags:** #descriptive-statistics #evaluation-metrics #confidence-intervals #hypothesis-testing #workflow-orchestration #quick-win #worker-facing #automation
**Contested on:** Whether application friction will be recognised as the selection mechanism it is.

## The Problem

Application forms are long. Upload a resume, then re-type its contents into fields. Answer fifteen screening questions. Write three short essays. Create an account. Confirm an email. Twenty minutes, often more.

Some of this is genuine data collection. A large part of it is an implicit volume control — a widely-shared belief that a candidate unwilling to spend twenty minutes is not serious enough.

As a filter it selects for available time, tolerance for tedium and the absence of alternatives. Candidates with other options abandon. Candidates in employment applying in the evening abandon. Candidates with caring responsibilities abandon. Candidates using generative tooling do not abandon, because it costs them nothing.

So the friction removes precisely the population an employer most wants and leaves the automated volume untouched.

## Why It's Still Broken

Abandonment is measured as a conversion metric where it is measured at all, and interpreted as a funnel problem rather than as a selection effect. Nobody asks who abandoned.

The form's length also accretes: every function adds a question, nobody removes one, and the resume re-typing persists because a parser was unreliable once.

And the belief that friction filters for seriousness is deeply held and has never been tested, though it is directly testable.

## What a Fix Looks Like

Cut the form, and measure who the current one is removing.

Measure abandonment properly. Where in the form, and how the abandoning population differs from the completing one on anything observable. Most employers have never looked and the finding is consistently uncomfortable.

Delete the re-typing. Parse the resume and let the candidate correct it. The parsers are good now, this is the single largest friction point, and it serves no purpose whatsoever.

Cut to what is needed to decide. Contact details, the resume, the legal right to work, and the two or three genuine knockout questions. Everything else can be collected later from candidates who advance, which is a small fraction.

Move the effort to where it discriminates. If a signal is wanted, ask one specific question about the candidate's actual work — two minutes for someone suitable, and a far better signal than fifteen generic ones.

Test the belief. Run the short form on half the requisitions for a quarter and compare volume, hire quality, offer acceptance and the composition of who applied. This is a real experiment, it is cheap, and it will settle an assumption that currently drives the whole design.

And stop requiring account creation before application, which is a pure abandonment generator serving the employer's convenience.

## Who Feels the Pain

Candidates with the most options, who abandon first and are exactly who the employer wanted. Candidates with the least time — employed, caring, working multiple jobs — who abandon for reasons unrelated to suitability. And employers, who added friction to reduce volume and instead changed who applies, in a direction they did not intend and have not measured.

## Impact If Fixed

The form stops selecting on available time. Resume re-typing — the largest and most pointless friction in the process — disappears. And the belief that friction filters for seriousness gets tested rather than assumed, which is a quarter's experiment and would settle a design decision affecting every applicant in the market.
