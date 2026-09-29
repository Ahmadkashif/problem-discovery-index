# Reports Land on Teachers Who Were Never Asked What They Need

**Niche:** [[niches/k12-private-schools/adaptive-assessment-publishers/profile|Adaptive Assessment Publishers]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Fix (Pain Point)
**One-liner:** The organization knows precisely which reports are opened and for how long, and designs them from committee judgment anyway.
**Tags:** #tacit-knowledge-ml #text-classification #evaluation-metrics #worker-facing #data-integration

## The Problem
The score is only half the product. What schools actually consume is a set of reports — class summaries, individual growth profiles, instructional groupings, learning statements tied to score bands — and Pass 1 puts teachers at 8-12 hours a week on non-instructional work, which is the budget these reports compete against.

Reports are designed by product and research teams working from expertise, advisory panels, and periodic usability sessions. That is a reasonable process and it is blind in a specific way: the organization can see exactly which reports are opened, by whom, for how long, and which are generated and never viewed. That telemetry exists and is used for product analytics rather than for understanding what teachers are trying to do with the data.

The deeper loss is on the interpretation side. Support staff and professional learning consultants spend their days explaining what a score means and what to do about it, and answering the same questions in every district and school. Those questions are the most precise available description of where the reports fail, and they are answered and closed.

## Why It's Still Broken
Assessment organizations are structured around measurement quality, and reporting sits downstream of it. The research function owns the score; the product function owns the report; and the professional learning function owns explaining it — three groups with three metrics and no shared record of what teachers actually do.

The support and training questions are also treated as service. They are logged for response time, not classified for content, so no one has ever counted them.

And there is an assumption, rarely examined, that the difficulty is teacher data literacy rather than report design. That framing puts the fix in training rather than in the product and has held for a long time.

## What a Fix Looks Like
Treat teacher interaction as the primary evidence about the product.

**Classify the support and training question stream.** Every question a consultant answers about interpreting a score or a report, coded by report, by concept, and by grade. A cluster of questions about one report is a specific instruction about what to redesign, and it replaces a design process that currently runs on panel judgment.

**Join report usage to what teachers then did.** Which reports are opened, which are abandoned, and — where the publisher's platform reaches into instructional decisions — what followed. This is the only measurement of whether a report changed anything.

**Capture consultant knowledge as structured material.** Professional learning staff develop precise, effective explanations of difficult concepts through hundreds of repetitions. Those explanations are the best interpretive content the organization has and exist as slides and personal habit.

**Test report changes properly.** Reports are shipped to millions of users, and comparing versions is straightforward and rarely done — so design questions are settled by opinion when they could be settled by evidence.

**Report on the reports.** Which are used, by whom, and how much, fed back to the research and product teams as a standing measure rather than an occasional study.

## Who Feels the Pain
Teachers, receiving reports built on assumptions about what they need. Professional learning consultants, answering the same questions for years with nothing accumulating. Product teams, designing without the usage evidence sitting in their own telemetry. And schools, paying for assessment whose instructional value depends on reports nobody has verified are usable.

## Impact If Fixed
Assessment's justification is that it improves instruction, and that claim rests entirely on whether teachers can act on what comes back. Closing the loop between the support question stream, report usage, and report design is cheap, uses evidence the organization already generates, and attacks the one part of the product that measurement rigour has never been applied to.
