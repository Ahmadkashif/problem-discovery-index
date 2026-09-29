# Submission Intake From Documents Nobody Standardized

**Niche:** [[niches/independent-insurance-agents/mga-program-underwriters/profile|MGAs & Program Underwriters]]
**Industry:** [[industries/independent-insurance-agents|Independent Insurance Agents]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** A commercial submission arrives as an email with eight attachments, and rekeying it is the entire cost structure of the front end.
**Tags:** #ocr #large-language-models #named-entity-recognition #data-integration #workflow-orchestration

## The Problem
A commercial submission is an email from a retail agent with an ACORD application, a loss run, a schedule of values in a spreadsheet, a supplemental questionnaire, and often photographs or a driver list. The ACORD form is nominally standard and arrives as a PDF filled in by hand, by a rating system, or by a scan of a fax. The loss runs come from whichever carrier held the expiring policy, each in its own layout. The spreadsheets have no layout at all.

Someone has to turn that into structured data before an underwriter can look at it. Pass 1 describes the retail side of this — producers re-entering the same ACORD data into portal after portal — and the MGA is the receiving end of the same problem, doing it again on the way in.

It is the largest fixed cost in the front end, it is the reason submission turnaround is measured in days, and in a market where the first quote back often wins, days are business.

## What Already Exists
Intelligent document processing is a mature market with strong insurance-specific offerings — ACORD form extraction is a solved commercial problem, and loss run extraction is offered by several vendors and works reasonably on common formats.

## The Customization Gap
The pieces exist and the assembly does not.

**The submission is a package, not a document.** Value comes from reconciling across attachments — does the schedule of values total match the application, does the loss run cover the years the application claims, is the named insured the same entity throughout. Every vendor extracts documents; none reasons across the set, and the discrepancies between attachments are exactly what an underwriter checks first.

**Loss runs are the hard part and the important part.** Every carrier formats them differently, they arrive as scans, and the underwriting decision turns on them more than on anything else in the package. Extraction has to produce claims with dates, status, paid and reserved amounts, and cause — and has to distinguish an open claim with a large reserve from a closed one, because that difference is the risk.

**Classification and appetite screening at intake.** The first question is whether this risk is even in appetite, and answering it in minutes rather than a day changes the economics of the whole front end. That requires classifying the business from the description, which is a text problem no generic extraction product addresses.

**Confidence that routes rather than reports.** An underwriter needs to know which extracted figures are reliable and which need checking. A wrong loss total produces a wrong price on a bound risk, so calibrated per-field confidence gating human review is the difference between useful and dangerous.

**Extraction that also serves the declined.** Most submissions will not bind, and a system that only structures the ones that do recreates the data gap this niche's central problem describes.

## Target Customer
Chief Operating Officer or Head of Underwriting Operations at an MGA, where submission throughput per underwriter is the binding constraint on growth.

## Impact If Solved
Speed to quote is the competitive axis in delegated underwriting, and the front end is where the days go. Reducing intake from hours to minutes lets the same underwriting team handle far more submissions — and, because the structuring happens for every submission rather than only bound ones, it produces the full-funnel dataset that everything else worth building here depends on.
