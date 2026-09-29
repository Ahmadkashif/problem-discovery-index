# Analyst Interpretation Is the Product and Is Stored as a Field

**Niche:** [[niches/oil-gas-field-services/upstream-well-production-data/profile|Upstream Well & Production Data Providers]]
**Industry:** [[industries/oil-gas-field-services|Oil & Gas Field Services]]
**Type:** Fix (Pain Point)
**One-liner:** Geologists and analysts make thousands of interpretive calls a week about what a well actually is, and the database records the conclusion.
**Tags:** #tacit-knowledge-ml #graph-ml #anomaly-detection #worker-facing #data-integration

## The Problem
A great deal of what the company sells is interpretation, not transcription. Which landing zone a well is actually in when the filing is vague or wrong. Whether a production decline is reservoir behaviour, a shut-in, or a reporting gap. How to allocate commingled lease production to individual wells. Whether two filings describe the same wellbore. Which operator entity in a corporate chain the history belongs to.

Analysts and geologists make these calls constantly, drawing on knowledge of a basin, an operator's filing habits, and a state's conventions. The database records the resulting value.

The reasoning is not recorded. So the same ambiguity is re-adjudicated when new data arrives, different analysts resolve comparable cases differently, and a customer asking why a well is attributed to a particular zone gets an answer only if the person who decided is still there. In a business whose entire claim is that its normalized data is more trustworthy than the raw filings, the basis for that trust is undocumented.

## Why It's Still Broken
The schema holds values. It was designed as a normalized representation of the filings, and interpretation enters as a corrected value with no room for provenance beyond a source flag.

Throughput reinforces it. Analysts work through filing volumes on release schedules, and recording reasoning is time that does not clear the queue.

And there is a quiet product concern: a database that exposed how much of itself is interpretation rather than filing might seem less authoritative. The opposite is true for the sophisticated customers who already know, and who currently cannot tell which fields to trust.

## What a Fix Looks Like
Make interpretation a first-class, provenanced layer.

**Typed interpretation records.** The ambiguity encountered, the decision made, the evidence relied on, the analyst, the date, and a confidence level — attached to the field it produced. This is the difference between a database and a database you can audit.

**Basin and operator knowledge notes.** How a given operator files, which state conventions produce which artefacts, which formations are chronically misreported. This is what an analyst spends two years learning and it currently exists only in them.

**Revisit when evidence arrives.** An interpretation made under confidentiality should be reopened when the data is released, automatically. Today it persists unless someone notices.

**Surface confidence to customers.** Which fields are filed, which are derived, and which are interpreted with what confidence. Sophisticated customers build their own corrections precisely because they cannot tell, and telling them is a product improvement rather than an admission.

**Measure consistency.** Comparable ambiguities resolved differently by different analysts is a signal that exists in the data now and is never examined.

## Who Feels the Pain
Analysts, re-adjudicating the same ambiguities. New analysts, who take years to learn basin and operator conventions that are nowhere written. Customers, who build private correction layers over a product sold as authoritative. And every forecast downstream that rests on an interpreted field nobody can trace.

## Impact If Fixed
The normalization layer is the entire moat, and its most valuable component — expert interpretation of ambiguous filings — is stored as bare values. Provenancing it makes the database auditable, makes the interpretation consistent, and turns two years of analyst learning into an asset that survives their departure.
