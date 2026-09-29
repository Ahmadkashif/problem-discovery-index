# Nobody Maintains the Acceptance Matrix

**Niche:** [[niches/esignature-document-workflow/mortgage-and-title-closing/profile|Mortgage & Title Closing]]
**Industry:** [[industries/esignature-document-workflow|E-Signature & Document Workflow]]
**Type:** Fix (Pain Point)
**One-liner:** Which counties accept electronic recording in what format, and which investors accept electronic notes, is knowledge every participant maintains privately in a spreadsheet that is out of date.
**Tags:** #descriptive-statistics #logistic-regression #evaluation-metrics #confidence-intervals #data-integration #compliance #quick-win #automation
**Contested on:** Every serious competitor in closing technology is fighting to get a loan to fund and an instrument to record without the parties being in a room — and whoever can do that across the widest set of counties, investors and lender overlays takes the volume.

## The Problem
Three thousand-odd recording jurisdictions, each with its own position on electronic recording, its own accepted formats, its own submitter requirements and its own fee schedule, changing without announcement. Every title agent, every lender and every closing platform keeps its own spreadsheet. The spreadsheets disagree, are stale, and are consulted by asking the person who maintains them. A closing fails, someone updates one cell in one spreadsheet, and the same failure happens next month at a different company.

## Why It's Still Broken
Nobody owns it. Each participant needs only its own footprint, so the incentive to maintain a complete picture is weak and the incentive to share it is weaker — some participants regard their coverage knowledge as a competitive advantage, which it is only because the industry has not commoditised it. Counties have no obligation to publish machine-readable capability data and mostly do not. And it is unglamorous maintenance work rather than a product, which means no vendor's roadmap has room for it.

## What a Fix Looks Like
Maintain it as shared reference data with contributed observations. A canonical record per jurisdiction covering electronic recording acceptance, accepted formats, submitter requirements, turnaround and fees, with an explicit last-verified date, because a stale record honestly labelled is usable and one silently stale is dangerous. Observations contributed from actual submissions — a rejection is a data point and every participant generates them — which makes the record self-maintaining at scale and is the mechanism that distinguishes this from another spreadsheet. Automated monitoring of county and submitter sources where they exist. The parallel matrix for investor and lender acceptance, which is smaller, changes less often and is entirely maintainable by hand. Expose it as a queryable service rather than a document, so it can be checked per file at application rather than remembered. And publish coverage statistics, which would show the industry where the actual gaps are — information no participant currently has and which is the argument for the counties that have not moved.

## Who Feels the Pain
Title agents and closing coordinators whose files fail late for a reason someone else already knew; lenders whose digital closing rates vary by geography for reasons they cannot see; and borrowers who take a morning off because a spreadsheet was six months old.

## Impact If Fixed
This is reference data, not technology, and its absence blocks the eligibility determination that would remove the largest brake on digital closing. The contributed-observation mechanism makes it viable to maintain, which is the part that has defeated every private attempt.
