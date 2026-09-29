# Fix: Nobody Knows Who the Programme Does Not Reach

**Niche:** Programme Operations & Compliance Reporting
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Fix (Pain Point)
**One-liner:** The completion rate is computed over the people who were enrolled, and nobody has ever counted the people who were not.
**Tags:** #evaluation-metrics #confidence-intervals #compliance #data-integration #descriptive-statistics
**Contested on:** Whether the administrative machinery runs itself, or consumes the awareness manager's week on enrolment, exceptions and evidence.

## The Problem

Ninety-eight per cent completion. The denominator is whoever the HR integration enrolled.

Outside it sit populations nobody has counted. The contractors working alongside employees with the same access. The agency staff in the call centre. The third-party support team with administrative credentials. The frontline workers who share a terminal. The subsidiary acquired eighteen months ago, still on its own systems. The consultants with mailboxes. The service accounts nobody owns.

Some of them have more access than most employees. The third-party administrator is a more valuable target than a marketing coordinator. And none of them appears in the denominator, so the completion figure says nothing about whether they were trained.

Nobody has looked, because the report shows a number over the population the integration covers, and no report shows the population it does not.

The check is straightforward. Take the identity provider's list of accounts with organisational access, compare it to the enrolled population, and look at the difference. Most organisations have never run it, and the result is usually larger and more interesting than anyone expects.

## Why It's Still Broken

**The denominator is invisible.** The report shows completion, not coverage, so the gap does not appear anywhere.

**The auditor asks about employees.** Compliance frameworks specify training for employees, so the employee population is what the evidence covers and the rest is outside the requirement.

**Contractors are somebody else's population.** They are managed through procurement, sit outside HR, and their training is frequently assumed to be their employer's responsibility.

**Running the reconciliation produces work.** Enumerating the uncovered population creates an obligation to do something about it, which is an unfunded programme.

**No single team owns the whole population.** HR owns employees, procurement owns contractors, identity owns accounts, and awareness enrols from HR.

**The number looks fine.** Ninety-eight per cent is a good number and there is no prompt to ask what it is ninety-eight per cent of.

## What a Fix Looks Like

**Run the reconciliation once.** Identity provider accounts against enrolled population. A query, an afternoon, and the resulting list is the fix's entire justification.

**Report coverage next to completion, permanently.** What proportion of the access-holding population is enrolled. A completion rate without this is the same uninterpretable figure that appears throughout this industry.

**Prioritise the gap by access, not by headcount.** A dozen third-party administrators matter more than two hundred enrolled marketing staff. Ranking the uncovered population by privilege turns a long list into a short actionable one.

**Make contractor training a contractual requirement.** Where the contractor's own employer should be training them, require evidence of it rather than assuming. Most organisations have never asked.

**Handle shared accounts explicitly.** Name the individuals who use them and train them, or record the account as untrained and treat it as a risk. Ignoring them is the only option with no defence.

**Include acquired entities in a plan.** An acquisition on separate systems will be outside the programme until somebody schedules the integration, and it is frequently outside for years.

**Ask the auditor about coverage.** An organisation that raises its own coverage gap with its auditor is in a better position than one that has it raised for them, and it usually results in a sensible remediation timeline rather than a finding.

## Who Feels the Pain

The organisation, which believes its workforce is trained and has trained the part of it that a particular integration happened to cover.

The security function, whose highest-exposure population — third-party administrators, privileged contractors — is frequently the least covered.

The awareness manager, reporting a number they have never been asked to qualify and may not have questioned themselves.

And the auditor and the insurer, treating a completion figure as a statement about an organisation when it is a statement about a subset of unstated size.

## Impact If Fixed

A single reconciliation between identity and enrolment is an afternoon's work and usually produces a list that surprises everyone who sees it.

Reporting coverage alongside completion converts an uninterpretable number into a meaningful one, and it is the same fix that applies to every metric in this industry.

And ranking the uncovered population by access rather than by headcount turns a large and daunting gap into a short list of genuinely high-exposure people who can be addressed in a week.
