# Parent Communication Management Across Grades and Activities

**Industry:** [[k12-private-schools|K-12 Private Schools]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Parents receive 15+ messages per week from different school sources — email, app push, SMS, printed flyer — with no unified thread, no deduplication, and no way to filter by relevance to their specific child.
**Tags:** #llm #text-generation #nlp #automation

## The Problem
A parent with two children in different divisions (lower and upper school) receives separate communications from each division head, each homeroom teacher, the athletics department, the arts program, the business office, and the head of school. Messages arrive via email, a school app (Finalsite or ParentSquare), SMS alerts, and occasionally paper in a backpack. There is no single view of "everything relevant to the Smith family this week." Parents disengage from the noise and miss critical information (schedule changes, permission slips, payment deadlines), then blame the school for poor communication.

## What Already Exists
ParentSquare, Bloomz, and Finalsite's messaging module offer school-to-parent communication with some audience targeting. These tools can segment by grade or group, but they don't deduplicate across channels, don't summarize across sources, and don't let a parent say "just show me action items for my kids this week." The tools are sender-centric (optimized for the school to broadcast) rather than receiver-centric (optimized for the parent to consume).

## The Customisation Gap
The gap is a family-centric aggregation and summarization layer: ingest all outbound communications across channels, tag each by child, category (action required / informational / event), and urgency, then deliver a single weekly digest per family with a "requires your action" section at the top. The summarization must understand school-specific terminology (e.g., "MAP testing window" or "re-enrollment contract") and link back to the original message for detail. This requires NLP that is tuned to the K-12 private school communication style — not a generic email summarizer.

## Impact If Solved
Parent satisfaction scores on communication — consistently the #1 complaint category in NAIS school surveys — improve measurably. Permission slip and re-enrollment form completion rates increase because action items are no longer buried in noise. Teachers and administrators spend less time fielding "I didn't see that email" follow-ups.
