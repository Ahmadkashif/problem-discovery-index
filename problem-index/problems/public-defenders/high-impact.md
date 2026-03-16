# Caseload Triage and Strategic Resource Allocation

**Industry:** [[public-defenders|Public Defenders]]
**Type:** High Impact
**One-liner:** Public defenders carrying 2-5x the ABA-recommended caseload have no systematic way to identify which of their 200+ open cases need immediate attention, investigation, or motion practice — a triage system that surfaces case-specific opportunity and risk signals could ensure that limited defender hours go where they change outcomes.
**Tags:** #bert #gradient-boosting #multiclass-classification #nlp #tabular-ml #revenue-impact

## The Problem

A public defender in a major urban office carries 150-400 active cases simultaneously. Each morning, they must decide which cases to work on — a decision that determines whether a suppression motion gets filed (potentially dismissing charges), whether a witness gets interviewed (potentially revealing exculpatory evidence), or whether a client gets a jail visit (potentially preventing a coerced plea). Currently, this triage happens through a combination of court calendar pressure (the cases with hearings tomorrow get attention) and gut feel (the attorney remembers which cases have been nagging at them).

The consequence of reactive, calendar-driven triage is that winnable cases get lost. A case where the stop was clearly unconstitutional sits in a stack of files because the attorney was consumed by trial prep on another case. A case where the complaining witness has recanted goes unnoticed because the paralegal's note is buried in a paper file. A client eligible for diversion programming serves six months waiting for a hearing because the attorney didn't flag the eligibility criteria during initial review.

The information to make better triage decisions exists but is scattered: police reports contain suppression signals (time of stop, basis for search, Miranda compliance), case files contain witness reliability indicators, court records contain judge-specific sentencing patterns, and client records contain mitigation factors. No system synthesizes these inputs into a prioritized action list.

## Why It's High Impact

At the individual case level, the difference between a triaged and untriaged approach can be months or years of a person's freedom. A suppression motion filed in week 2 vs. week 20 of a case can mean the difference between pretrial release and months in jail awaiting resolution. At the systemic level, better triage could redirect 15-25% of defender time from low-impact administrative tasks to high-impact case investigation and motion practice.

For a 200-case caseload, improving outcome on even 10% of cases (20 clients) by identifying actionable legal issues earlier translates to measurable reductions in incarceration days, conviction rates on suppressible cases, and plea bargains accepted under duress. Quantifying this in dollar terms: each avoided month of incarceration saves the state $3,000-$5,000 in direct costs and the individual far more in lost wages, family disruption, and downstream consequences.

## What a Solution Looks Like

The system ingests case data from the court management system (charges, hearing dates, judge assignment, prosecution unit), discovery documents (police reports, lab results, body camera logs), and client intake data (criminal history, employment, housing, mental health status). A BERT-based NLP model processes narrative discovery text to extract legal issue signals — Fourth Amendment suppression indicators, witness credibility flags, evidence chain-of-custody gaps, and procedural compliance issues.

These signals feed into a gradient-boosted multi-class classifier that categorizes each case into action tiers: (1) immediate investigation needed — high-probability legal issue identified, (2) motion practice opportunity — suppression, dismissal, or diversion eligible, (3) standard negotiation — facts favor plea resolution, (4) monitoring — awaiting lab results, witness location, or co-defendant resolution. The defender's daily dashboard shows their caseload sorted by action tier with specific recommended next steps: "Case #2024-CF-3847: Body camera footage shows Miranda violation at timestamp 14:22 — file suppression motion."

## Implementation Path

Training data comes from closed case records within the public defender's office — case files paired with outcomes (dismissed, acquitted, pled, convicted, sentence). Discovery text (police reports, lab results) paired with motion practice outcomes (suppression granted/denied) creates supervised training data for legal issue detection. The critical prerequisite is digitized case files — many offices still operate on paper, requiring an OCR and intake pipeline. MVP targets a single large urban office (200+ attorneys) with digitized records, training on 3-5 years of closed cases. Ethical review is essential — the system must be designed as a decision-support tool that highlights opportunities, never as a tool that recommends case abandonment. Integration with JustWare or the office's case management system for seamless workflow embedding. Timeline: 12-18 months with a dedicated team of 2 ML engineers, 1 NLP specialist, and 1 public defense attorney as domain expert.
