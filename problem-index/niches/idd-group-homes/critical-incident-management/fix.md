# The ER Visit Nobody Reported

**Niche:** [[niches/idd-group-homes/critical-incident-management/profile|Critical Incident Reporting & Investigations]]
**Industry:** [[industries/idd-group-homes|IDD Group Homes]]
**Type:** Fix (Pain Point)
**One-liner:** A resident goes to the emergency room on a Saturday night, and by Monday nobody has asked whether it was a reportable incident.
**Tags:** #logistic-regression #feature-engineering #compliance #data-integration #quick-win
**Contested on:** Every serious competitor in this niche is fighting to get each critical incident reported, investigated and closed with corrective action inside the state's timeframes, and whoever keeps the share of incidents closed late lowest takes the account.

## The Problem
HHS OIG's series of state group-home audits found up to 99% of critical incidents unreported to the required agencies (OIG). Those audits worked from emergency-room claims for group-home residents; the Massachusetts follow-up reviewed 147 such claims for 128 residents (search summary). The visit is in the house log and later in the claims data; the incident report never gets written.

## Why It's Still Broken
The DSP who went to the ER assumed someone else would report it. The supervisor saw "ER visit, returned" and no injury narrative. Nobody compares the two lists.

## What a Fix Looks Like
A daily check that lists every ER visit, urgent-care visit, injury and PRN psychotropic dose for the past 24 hours that lacks a matching incident report, sent to the on-call supervisor with the state's deadline shown.

## Who Feels the Pain
Compliance directors facing state audits that apply the Access Rule's claims-matching requirement; residents whose injuries go uninvestigated.

## Impact If Fixed
Incidents are reported inside the deadline rather than discovered in an audit, for ~5–10 minutes a day per agency (estimate). If ~1 in 10 ER visits now goes unreported (estimate), a 40-home agency with ~200 ER visits a year (estimate) finds ~20 reportable incidents before the state does.
