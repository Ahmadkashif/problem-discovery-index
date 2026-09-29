# Millions of Clearances, Renewed on a Cycle, and No One Has Measured Whether the Rules Work

**Niche:** [[niches/childcare-centers/childcare-background-check-vendors/profile|Childcare Background Check & Screening Vendors]]
**Industry:** [[industries/childcare-centers|Childcare Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** These processors adjudicate millions of childcare workers against fifty different disqualification schemes and re-screen the same people years later — the only body of evidence on whether any of it is calibrated, and it has never been analysed.
**Tags:** #bayesian-inference #survival-analysis #evaluation-metrics #confidence-intervals #causal-inference

## The Problem
Federal law requires a comprehensive background check on every childcare worker before unsupervised contact with children: fingerprint-based criminal history, sex offender registries in every state the person has lived, and child abuse and neglect registries. It must be repeated on a fixed cycle. State-contracted processors and screening vendors run the submissions, apply that state's disqualification list to whatever comes back, and issue the determination that lets a person work.

The adjudication is the work. A criminal history record arrives as a disposition code from a court system that may or may not be legible; the state statute lists offences that permanently or temporarily bar employment; someone has to decide whether this record matches that list, and whether this record even belongs to this person. Multiply by millions of workers a year across fifty jurisdictions that define the list differently.

Doing this for years produces two datasets nobody else has.

The first is a map of how disqualification rules are actually applied. Not the statute — the statute is public — but the realised decision: which record types, which dispositions, which offence codes from which state's court system, produce which outcome, and where adjudicators disagree with each other. Every state wrote its own list, and the effect of those drafting choices on who can work in childcare has never been compared across states, because no one holds all fifty in one place except the processors.

The second is longitudinal. The same worker is screened again at renewal. Across millions of workers and multiple cycles, the vendor observes what appeared on the record of an already-cleared population between one screening and the next. That is the only empirical basis anyone has for the questions the whole system rests on: is the renewal interval right, is the offence list catching what it should, and are the barriers doing the work they were written to do.

Neither has been examined. The output is a clearance.

## Why Nobody Has Built This
The invoice is a determination, priced per screening. Analysis of the determinations is not a deliverable to anyone, and the customer — a state agency or a childcare operator — is buying compliance, not evidence.

The vendor also has no standing to question the rules. The disqualification list is statute. A processor that published findings on which barriers were and were not doing anything would be arguing with its own regulator and its own contracting authority, and would risk the contract.

The renewal-cycle data is the most sensitive dataset in the operation and the least likely to be touched. It concerns individuals, in a child-protection context, under FCRA and state law, and the instinct — a correct one — is to use it for the determination it was collected for and nothing else.

That instinct has a real limit, though, and it is worth naming: the useful question is whether the *rules* are calibrated, not which individual is dangerous. The second question should not be asked of this data at all — an individual-level risk score for childcare workers would be indefensible on evidence and on principle, and the value here does not require it. The rules can be evaluated in aggregate without scoring a single person.

## What to Build
**Treat record matching as the probabilistic problem it is.** An applicant is matched to criminal history, registry entries and abuse records by name, date of birth and identifiers of varying quality. Common names, transliterations, married names and shared birthdates make this genuinely uncertain, and it is largely handled by rules and human review. Modelled properly, with a posterior on whether this record belongs to this person, false matches become measurable rather than anecdotal — and a false match is a person wrongly denied work.

**Compare the fifty schemes against each other.** The same criminal record produces different outcomes in different states, and the vendor can quantify the divergence across its whole footprint. What fraction of applicants disqualified in one state would clear in another, and on which offence categories, is answerable today and unanswered.

**Analyse the renewal cycle as survival data, in aggregate.** Time from clearance to a disqualifying event appearing on a cleared population's record is time-to-event data with heavy censoring. It speaks directly to whether the statutory renewal interval is too long, too short, or wrong for particular record categories — a question every state legislature has guessed at.

**Quantify adjudicator variance.** The same file reviewed by different adjudicators does not always yield the same determination. Measuring that disagreement rate, and where it concentrates, is straightforward with a controlled re-review sample and is the cheapest available quality improvement.

**Report on the barrier, not the person.** The whole output should be about rules, intervals and process — which offence categories are load-bearing, where the statutes diverge without justification, how long clearance actually takes and what drives it. This is exactly the evidence the agencies commissioning the screening lack.

## Target Customer
Chief Compliance Officer at a national screening vendor, or the programme director at a state agency running the background check unit. The argument to the vendor is that evidence about its own process is the only defensible ground in a contract renewal fought on price. The argument to the agency is that it is legislating the disqualification list with no measurement of its effect.

## Impact If Built
Every state wrote a barrier list for childcare employment, none has measured it, and the consequences fall in both directions — workers wrongly excluded from the only job available to them, and gaps nobody has looked for. The one organisation holding the evidence issues determinations and files them.
