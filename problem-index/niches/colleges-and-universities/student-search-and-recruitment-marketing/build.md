# Attribution From Purchased Name to Enrolled Student

**Niche:** [[niches/colleges-and-universities/student-search-and-recruitment-marketing/profile|Student Search & Recruitment Marketing]]
**Industry:** [[industries/colleges-and-universities|Colleges & Universities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Colleges buy names by the hundred thousand and cannot say which list, campaign or visit produced the students who actually enrolled.
**Tags:** #causal-inference #gradient-boosting #survival-analysis #feature-engineering #evaluation-metrics #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to turn purchased and owned prospect names into enrolled first-year students, and whoever delivers the most enrolled students per recruitment dollar takes the account.

## The Problem
A mid-sized private college buys names from several sources each year, runs search campaigns through an agency, sends counsellors to high school fairs and runs digital ads. Its CRM records touches, and the agency reports inquiry and application rates by list. Whether a name bought in sophomore year produced an enrolled student two years later, net of students who would have applied anyway, is not measured. Budgets roll forward.

## Why Nobody Has Built This
The data joins span two years, several vendors and the SIS. Agencies report on what they control, and the outcome that matters (enrolled, retained, paying) sits outside their systems. Holdout testing on name lists is rare because nobody wants to risk the class.

## What to Build
A time-to-enrollment model over every prospect record with touches as time-varying covariates, deliberately randomised holdouts on a slice of purchased names, and incremental enrolled students per dollar by source, campaign and territory. It runs inside the college's CRM and SIS data and ends in a reallocation plan for next year's search buy.

## Target Customer
Admissions directors and enrollment analytics leads at colleges spending $500K–$5M a year on recruitment.

## Impact If Built
Search budgets move to the sources that produce enrolled students, not inquiries. Cutting the bottom quarter of name purchases at a college buying 200,000 names a year saves ~$100K–$200K with no loss of enrolled students (estimate).
