# The Determination Corpus Nobody Has Ever Queried

**Niche:** [[niches/hoa-management/condo-project-review-services/profile|Condominium Project Review Services]]
**Industry:** [[industries/hoa-management|HOA Management]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm has rendered eligibility determinations on tens of thousands of condominium projects and has never asked which ones later went wrong.
**Tags:** #gradient-boosting #binary-classification #survival-analysis #anomaly-detection #evaluation-metrics #compliance

## The Problem
Every conventional mortgage on a condominium requires the project to be found eligible before the loan can be made. The reviewer collects the association's budget, reserve study, insurance, litigation disclosure, and questionnaire responses, and renders a determination against agency criteria. After Surfside those criteria tightened substantially — deferred maintenance, special assessments, and structural condition became disqualifying in ways they were not before — and a review that used to be a checklist became a judgment.

The firm has been making those judgments at volume for years. Each one is stored as a case: the project, the evidence, the finding, the date. Together they are the only assembled record of the financial and physical condition of the US condominium stock, refreshed every time a unit in a project comes up for financing.

Nobody has ever looked at it as a body. The reviewer decides eligible or ineligible today, and the system's memory of the project is that one word plus an expiry date. It does not know that this project's reserve contribution has fallen in each of the last four reviews, that its insurance deductible tripled, that its special assessment history has become chronic, or that projects that looked like this eighteen months ago are the ones now failing.

## Why Nobody Has Built This
The product is a binary answer delivered by a deadline, and the deadline is a closing. Everything about the operation is optimized for turnaround: intake, chase the missing document, decide, deliver. A determination is complete when it is issued, and no part of the workflow has any reason to revisit it.

The other reason is that "wrong" has no definition in this business. A project found eligible that later requires a $60,000-per-unit special assessment was not necessarily an error under the criteria as they stood. So nobody counts, and without counting there is nothing to learn from.

That is a choice, not a constraint. The outcomes are observable in the firm's own subsequent reviews of the same projects — which is to say the firm already collects the answer, one project at a time, and throws away the connection.

## What to Build
A longitudinal project layer over the determination corpus.

**Link determinations into project histories.** The unit of analysis has always been the review; it should be the project across reviews. Reserve contributions, delinquency rates, insurance terms, and assessment events over four or five successive reviews are a trajectory, and the trajectory is far more informative than any single snapshot.

**Model deterioration, not eligibility.** Eligibility is a rules question the criteria already answer. The valuable prediction is which currently-eligible projects are heading toward failure — a large special assessment, a structural finding, an insurance non-renewal — within the next one to three years. Every input is in the corpus and the outcomes label themselves as later reviews arrive.

**Flag inconsistency between reviewers.** In any high-volume judgment operation, similar cases decided by different people diverge. Comparing determinations across matched projects surfaces where the criteria are being applied unevenly, which matters commercially — an inconsistent reviewer is a repurchase risk — and matters more if an agency ever audits.

**Score the questionnaire itself.** Association responses are self-reported, and some are wrong. Cross-checking stated reserves against the budget, stated litigation against public records, and stated maintenance against the reserve study is a set of consistency rules that can flag the responses worth challenging before a reviewer spends an hour on them.

## Target Customer
VP of Operations or Chief Credit Officer at a project review firm, or the equivalent function inside a large mortgage originator's condo review department. The pitch is a risk one and lands directly: lenders are exposed on projects they approved, and a firm that can say which of its live approvals are deteriorating is offering something no competitor has.

## Impact If Built
Lenders currently learn a condominium project has failed when a borrower defaults or a loan cannot be sold. The review firm can see it coming from the documents it already reads. Turning a per-file determination business into a monitored portfolio is both a much better product and a far more defensible one — the corpus takes years to accumulate and cannot be bought.
