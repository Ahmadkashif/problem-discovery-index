# Record Matching Judged on Speed and Never on Whether It Was Right

**Niche:** [[niches/hr-consultants/background-screening-providers/profile|Background Screening Providers]]
**Industry:** [[industries/hr-consultants|HR Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Deciding whether a court record belongs to this candidate is the whole product, and the firm measures turnaround instead of accuracy.
**Tags:** #named-entity-recognition #binary-classification #gradient-boosting #evaluation-metrics #compliance

## The Problem
A background check is an identity resolution problem wearing a compliance costume. Court records are indexed by name and partial date of birth, sometimes an address, rarely anything better. There are thousands of people with a given common name, and the question the screener must answer is whether *this* felony conviction belongs to *this* candidate.

Get it wrong in one direction and an innocent person loses a job over someone else's record. Get it wrong in the other and the employer hires against a record that was real. Both are the company's liability, and the first is the one that generates FCRA litigation.

The matching is done by rules — name variants, date of birth tolerance, address overlap — tuned by hand, plus human review on anything ambiguous. Those rules were set years ago by people who have often left, and the thresholds inside them are numbers nobody can now justify. Whether the current configuration is over- or under-matching, and where, is not measured.

Meanwhile the operation is measured obsessively on turnaround, because turnaround is what employers evaluate at renewal. Speed has a dashboard. Accuracy has a legal department.

## Why Nobody Has Built This
Ground truth looked unavailable, so nobody looked for it. In fact there is a steady, high-quality supply of it: every consumer dispute is a labelled example, adjudicated by the firm's own process, with a definite outcome. Disputes are handled by a compliance function whose job is resolving each one within the statutory window and closing the file. They are treated as incidents to be cleared, not as a dataset.

The second reason is that measuring accuracy creates a record. A firm that quantifies its own false match rate has produced a document, and legal instinct in a heavily litigated sector is not to. That instinct is defensible in the short run and expensive in the long run — the disputes arrive whether or not anyone counts them.

And the incentives are asymmetric on the wrong side. Under-matching — missing a record that was there — produces no dispute, because the candidate who benefits does not complain and the employer never finds out.

## What to Build
A measured, calibrated matching layer, trained on the firm's own dispute history.

**Assemble the label set.** Every dispute filed, its adjudication, and the record and candidate involved. Years of these exist. Reconstructing them into training data is a data engineering project, not a research one.

**Replace thresholds with a scored model.** Name rarity — a common surname and a common given name carry far less matching weight than an unusual pair, and no fixed rule captures this — plus date components, address and employment overlap, jurisdiction and record age. Output a calibrated probability, so that "route to human review" becomes a decision about cost and risk rather than a rule nobody can explain.

**Estimate the invisible error.** Under-matching leaves no trace, so it needs deliberate measurement: sample completed screens and re-run them under an expanded search, and quantify what the production configuration missed. Every firm in this market claims completeness and none of them has measured it.

**Route review by expected consequence.** A borderline match on a decades-old misdemeanour and a borderline match on a recent felony carry different costs. Review capacity is the constraint, and it is currently allocated by rule-trigger rather than by what is at stake.

## Target Customer
Chief Data Officer or VP of Operations at a national screening provider. The argument is about liability, and it is one the general counsel will make for you: FCRA class actions over mismatched records are a persistent cost in this sector, and a calibrated, documented matching process is a materially better defensive position than a rule set nobody can explain the provenance of.

## Impact If Built
People lose jobs over other people's criminal records, routinely, and the firms that cause it cannot say how often. Fixing the match rate is a genuine consumer outcome. Commercially it lets a provider hold accuracy constant while pushing more volume through automated adjudication — which is the only way turnaround improves without hiring, and turnaround is what the contract is won on.
