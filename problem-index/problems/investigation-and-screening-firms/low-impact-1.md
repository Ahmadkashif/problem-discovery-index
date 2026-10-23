# Adverse Action Across Fair-Chance Jurisdictions

**Industry:** [[investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Applicant tracking systems and screening platforms send the federal pre-adverse and adverse action letters well; the state and local fair-chance sequences layered on top are run from a compliance memo and a calendar.
**Tags:** #large-language-models #transformers #decision-trees #compliance #workflow-orchestration #automation #data-integration

## The Problem
When a background report contains something an employer may act on, the FCRA requires a pre-adverse action notice with a copy of the report and a summary of rights, a pause (customarily five business days, though the statute names no number), and then a final adverse action notice. That much is standard. But a California employer must first have made a conditional offer before looking at conviction history, then make an individualized assessment of the offence's nature and gravity, the time elapsed and the job, then give the candidate at least five business days to respond, five more if the candidate says the record is wrong. An employer hiring in unincorporated Los Angeles County has a further ordinance since September 2024, including limits on rescinding an offer because the screening vendor was slow. New York City, Philadelphia, Illinois and others each have their own sequence, forms and waiting periods. NELP counts 15 states and 22 cities and counties whose fair-chance laws reach private employers.

A national employer hiring hourly workers in forty states, some of them remote, has to run the right sequence for each candidate based on where the job is performed, sometimes where the candidate lives, the salary, the record type and the record's age. Screening firms field the questions, and many offer adjudication and adverse action services, so the burden lands on their compliance teams as much as the employer's.

## What Already Exists
Workday, iCIMS, Greenhouse and other applicant tracking systems integrate with screening platforms and send templated pre-adverse and adverse action letters with configurable waiting periods. Screening firms (First Advantage, HireRight, Checkr and others) offer adverse action modules and adjudication matrices. Employment law firms publish fair-chance trackers, and compliance content vendors supply state-by-state summaries.

## The Customisation Gap
The generic workflow knows one sequence with a timer. What fair-chance compliance needs is a versioned rule engine keyed to the worksite and the candidate's work arrangement, the salary band (FCRA's seven-year limit lifts at $75,000), the record type and age, and the date of the decision, so a firm can show which rule it applied two years later. It needs the individualized assessment captured as a structured record — the factors weighed, the candidate's mitigating evidence, the decision-maker — drafted from the report and the candidate's response rather than typed, and jurisdiction-specific notices generated with the right content and timing. And it needs the candidate's dispute of the record routed back to the screening firm's reinvestigation clock so the two processes do not run blind of each other.

## Impact If Solved
Employers and the screening firms that run adjudication for them would stop handling fair-chance cases by exception, cutting an estimated ~3–5 business days from every flagged candidate's decision and ~30–60 minutes of compliance staff time per case (estimate), and removing the most common procedural ground for class actions under state fair-chance laws.
