# The Format Changed and Nothing Said So

**Niche:** [[niches/music-distribution-platforms/royalty-accounting-and-reconciliation/profile|Royalty Accounting & Reconciliation]]
**Industry:** [[industries/music-distribution-platforms|Music Distribution Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** A service added a column, the parser silently dropped a territory, and nobody noticed for four months.
**Tags:** #change-point-detection #quick-win #data-integration #automation #evaluation-metrics #descriptive-statistics #confidence-intervals #compliance
**Contested on:** Every serious competitor in this niche is fighting to turn dozens of incompatible statement formats into a payment an artist can trace back to a stream — and whoever makes a royalty statement explainable takes the trust the whole category runs on.

## The Problem
Statement ingestion depends on parsers written against each service's format. Services change formats — a new column, a renamed field, a different territory code, a changed deduction line — usually without notification. The parser does not fail loudly; it produces a plausible number that is wrong. Months later someone notices revenue from a territory looks low, and the correction affects thousands of artists who were underpaid and have already spent statements they were given.

## Why It's Still Broken
Parsers were written to succeed on the expected shape, so an unexpected shape produces a partial result rather than an error — a permissive parser is easier to ship and fails silently by design. Nobody validates the output against an expectation. Month-to-month variation is normal, which hides the break. And there is no obligation on services to announce changes.

## What a Fix Looks Like
Validate the output, not just the parse. Check ingested totals against expected revenue derived from reported streams, which is the fix and catches silent drops that a parser cannot. Compare every dimension month over month — territory, service, rate, deduction — since a missing territory is obvious in a comparison and invisible in a total. Fail loudly on unexpected columns or values rather than ignoring them, as a permissive parser is the root cause. Alert on distributional change rather than on absolute thresholds, because volume varies and structure should not. Keep the raw statement alongside the parsed output, so a later reconstruction is possible. Version parsers against observed formats and record when the format changed, which builds the history nobody has. Report ingestion health per service per period, which is a dashboard nobody maintains. Reconcile the payment received against the statement total, since those also diverge. Correct retrospectively and communicate clearly when it happens, as artists forgive an error and not a silent one. And share format change observations with other distributors where possible, since everyone is parsing the same files.

## Who Feels the Pain
Artists underpaid for months; royalty teams reconstructing four months of statements; support agents explaining corrections; and distributors whose accuracy claims rest on parsers nobody validates.

## Impact If Fixed
A permissive parser is easier to ship and fails silently by design, so a format change produces a plausible wrong number. Validating ingested totals against expected revenue from stream counts catches exactly the failure a parser cannot.
