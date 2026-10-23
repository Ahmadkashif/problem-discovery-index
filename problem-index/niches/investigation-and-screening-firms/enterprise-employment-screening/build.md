# One Report Format for Two Different Buyers

**Niche:** [[niches/investigation-and-screening-firms/enterprise-employment-screening/profile|Enterprise Employment Background Screening]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The screening report is built as a single document for every employer, when a warehouse operator needs a same-day clear and a health system needs a continuously maintained record of who is still eligible to work.
**Tags:** #feature-engineering #evaluation-metrics #survival-analysis #workflow-orchestration #compliance #data-integration
**Contested on:** *Not terminal as stated.* The honest partial sentence is that every competitor is fighting to return a complete, defensible report inside the employer's hiring window — but the high-volume hourly employer and the regulated employer buy on different evidence: one renews on the share of applicants cleared the same day, the other on never missing a disqualifying record, licence lapse or exclusion after hire. Decomposed into contested sub-niches below.

## The Problem
Screening firms sell large employers a package and a report. The report is a point-in-time document: what the searches found on the day they ran. A high-volume employer reads it for one thing — clear or not, and when — and an hourly applicant who waits three days takes another job. A regulated employer reads it as the first entry in a record it must keep current: the nurse's licence, the driver's motor vehicle record, the federal and state exclusion lists, new arrests. The same product, sold under the same contract structure, serves both badly.

## Why Nobody Has Built This
The large screeners grew by acquisition and run one fulfilment platform under many brands; product lines are organised by package, not by the buyer's decision. Contracts and procurement scorecards measure turnaround and price per report, which pushes every customer toward the hourly employer's definition of success.

## What to Build
Two products on one fulfilment layer. For volume hiring, a decision service that returns component-level completion predictions at order time, clears what can be cleared immediately and isolates the one component holding the report. For regulated employers, a workforce eligibility record per employee — every source, its last check date, its next due date and every alert — with continuous monitoring and an audit view a surveyor or examiner can read.

## Target Customer
Heads of screening programmes at employers with more than 10,000 hires a year, and compliance leaders at hospital systems, banks and transportation companies.

## Impact If Built
Each buyer is measured on what it actually renews on, and screeners can price monitoring as a recurring service rather than an add-on to a document that is out of date the day after it is delivered.
