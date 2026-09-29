# Adverse Action and Appeal Practice

**Niche:** [[niches/identity-verification-vendors/failed-applicant-remediation/profile|Failed-Applicant Remediation]]
**Industry:** [[industries/identity-verification-vendors|Identity Verification Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Credit decisions come with a stated reason and a right to dispute the underlying data, and a verification failure comes with neither.
**Tags:** #compliance #workflow-orchestration #evaluation-metrics #automation #worker-facing #data-integration #descriptive-statistics #confidence-intervals
**Contested on:** Every serious competitor in this niche is fighting to give a person who could not be verified a documented route to prove who they are — and whoever builds that route stops the category's silent failure from being permanent.

## The Problem
Consumer credit developed a whole apparatus around adverse decisions: a stated reason, disclosure of the data source, a right to obtain the file, a dispute process with a required response time, and correction obligations on the furnisher. It exists because decisions made about people from data they cannot see require recourse. Identity verification makes decisions of comparable consequence from data the person cannot see, and the equivalent apparatus is largely absent.

## What Already Exists
Adverse action notice requirements and reason codes; consumer file disclosure rights; dispute and reinvestigation processes with deadlines; furnisher correction obligations; and the supervisory framework enforcing all of it.

## The Customization Gap
The adaptation is to a real-time decision about identity rather than creditworthiness. It requires: (1) reason codes for verification failure that do not exist and must be defined, which is the substantive work and would be useful across the category; (2) a dispute path that resolves in minutes or days rather than weeks, since the person is trying to open an account now; (3) an explanation that does not reveal enough to help an impostor, which is a genuine design constraint and is solvable; (4) responsibility split between the vendor, the institution and the underlying data source, so the recourse path must be routed rather than assumed; and (5) obligations that apply unevenly depending on use case, which makes voluntary adoption the practical route.

## Target Customer
Product, compliance and support leadership, institutions carrying the obligation, consumer advocates, and regulators examining automated identity decisions.

## Impact If Solved
Credit built recourse because decisions from invisible data require it, and identity verification makes comparable decisions with none. Defining verification reason codes is the first step and the whole category lacks them.
