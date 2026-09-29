# Every Case Outcome in the Country, and No Model of What a Case Is Worth

**Niche:** [[niches/personal-injury-law/litigation-analytics-court-data/profile|Court Data & Litigation Analytics Platforms]]
**Industry:** [[industries/personal-injury-law|Personal Injury Law Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The platform holds millions of resolved cases with judge, venue, counsel, insurer and timeline attached, and sells its customers a filtered list to read.
**Tags:** #gradient-boosting #survival-analysis #causal-inference #evaluation-metrics #confidence-intervals

## The Problem
Pass 1 states the problem in the operator layer precisely: experienced personal injury attorneys develop an intuition about what a case is worth, integrating injury severity, jurisdiction, judge and jury composition, opposing counsel, the specific insurer and their known negotiating patterns, liability clarity and client presentation — and that judgment is not systematised, varies between attorneys in the same firm, and does not transfer to associates. The consequence is inconsistent demands, cases settled too early or too late, and no firm-wide intelligence.

The litigation analytics platforms hold most of the inputs. Every case in their corpus carries its court, its judge, the parties, the law firms on both sides, the case type, the motions filed and how each was decided, the time from filing to each stage, and how it ended. Across millions of cases and many years, that is a rich panel about how litigation resolves, joined to nearly all of the structural variables an experienced attorney is actually weighing.

What they sell is retrieval. A customer filters to a judge and a motion type and reads a rate. They can see that a judge grants summary judgment forty per cent of the time — not what that means for their case, given its posture, its opposing counsel, its age, and the twelve other things that differ from the base rate.

The gap is that nothing predicts. The corpus supports models of how long a case will take, what the probability of surviving dispositive motions is, and — where amounts are recorded — what the resolution is likely to be. None of that is offered, because the product was built as a search engine over court records rather than as a model of litigation.

## Why Nobody Has Built This
The category grew out of docket retrieval. The original job was getting the filings, and the hard, expensive, defensible work was court coverage. Analytics arrived as counts over the records already collected — how many, how often, how long — which is honest and useful and required no modelling.

There is also real institutional caution about prediction in law. Some jurisdictions have restricted judge analytics outright, and vendors serving law firms are careful about a product that appears to tell a judge how they will rule. Base rates read as description; predictions read as claims.

And the outcome variable is genuinely messy. Most cases settle, most settlements are confidential, and the docket records a dismissal that discloses nothing about the amount. A model of case value has to work around the fact that the label is missing exactly where it matters most.

## What to Build
Prediction over the litigation corpus, with the missingness handled honestly rather than avoided.

**Model time to resolution as survival, not average.** Cases are ongoing, so the data is right-censored by construction; average time-to-disposition over closed cases is biased and is the number currently sold. A hazard model over case attributes gives an attorney the thing they actually need at intake — the distribution of how long this will take.

**Model motion outcomes conditionally.** The probability this motion succeeds before this judge, given the case type, posture, timing, and counsel — not the judge's marginal rate. The difference between a conditional estimate and a base rate is most of the value.

**Attack the settlement label directly.** Amounts are visible in verdicts, in reported settlements, in some court approvals, and in bankruptcy and lien records. That is a biased sample and can be treated as one — modelling selection into observability rather than pretending the observed cases are representative. Nobody in this market has tried.

**Build counsel and insurer effects properly.** Opposing counsel and the insurer behind them are two of the variables Pass 1 names, they appear in the docket, and they are pure entity-level random effects — the classic structure for partial pooling, which matters because most individual attorneys appear in few cases.

**Report intervals and publish calibration.** A predicted range with a stated confidence, and an accompanying record of how previous predictions performed. In a market rightly nervous about legal prediction, being the vendor that publishes its own error is the durable position.

## Target Customer
Chief Data Officer or VP of Analytics at a litigation data platform. The commercial context is that docket coverage is converging across vendors and search-and-count analytics are increasingly matched, which leaves prediction as the only unclaimed axis.

## Impact If Built
Case valuation is the central unsolved judgment of a $53B contingency fee industry, and it is currently made by intuition that varies attorney to attorney inside the same firm. A calibrated model over the litigation corpus would not replace that judgment, but it would give it a reference point that does not currently exist — and it would give the vendor a product its competitors cannot assemble without the same twenty years of court coverage.
