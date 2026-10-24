# Award Terms Through a Federal Policy Shock

**Industry:** [[colleges-and-universities|Colleges & Universities]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Every research university re-reads thousands of federal award notices by hand each time an agency changes its terms, caps or termination rules, and research administration software stores the documents without saying what changed for each award.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #compliance #workflow-orchestration #data-integration

## The Problem
A research university with $500M a year in sponsored research (estimate) manages several thousand active awards from NIH, NSF, DOE, DOD, NASA and foundations. Each comes with a notice of award, agency general terms, programme-specific conditions and the negotiated facilities and administrative (F&A) rate agreement that sets how much overhead it can recover. In 2025 and 2026 these documents became moving targets. NIH announced a flat 15% cap on indirect costs, which was enjoined and then upheld on appeal in January 2026 (search summary). Agencies terminated or suspended awards on policy grounds, issued new certifications and changed terms mid-award. Each change sends post-award staff back through the portfolio to find which awards are affected, what spending is still allowable, what must be stopped and what can be billed before a stop date.

## What Already Exists
Research administration suites (Huron Research Suite, Kuali Research, Cayuse, InfoEd, Workday Grants Management) track proposals, awards, budgets and compliance approvals, and store award documents as attachments. ERP grants modules in Banner, Oracle and Workday hold the financial side. Agencies publish award data (NIH RePORTER, NSF's award search, USAspending), and the Council on Governmental Relations and NCURA circulate policy analysis to members.

## The Customisation Gap
The generic tools hold award records; they do not read them against a policy change. The research-specific logic is: parsing each notice of award into its operative terms (budget period, restrictions, prior-approval requirements, F&A base and rate, special conditions); mapping each agency announcement to the clauses it modifies; flagging affected awards with the cost categories now at risk; computing allowable closeout costs and the F&A recovery lost under a cap or termination; and keeping a per-award audit trail of what was known when, because Single Audit and agency audits test exactly that. Agency rules differ in vocabulary and structure, and the same award can be governed by agency, institutional and subaward terms at once.

## Impact If Solved
A post-award office that can answer "which awards does this change touch, and what does it cost us?" in a day instead of three weeks stops spending after stop dates, bills allowable closeout costs it would otherwise miss, and gives the vice president for research a defensible number for the board when federal policy moves again.
