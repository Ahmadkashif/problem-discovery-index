# NEC Code Compliance Checklist Generation by Job Type

**Industry:** [[electrical-contractors|Electrical Contractors]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** The NEC codebook and NFPA resources exist in digital form, but there's no tool that generates a project-specific compliance checklist — "for a new kitchen circuit in a 1987 house in Texas, these are the specific NEC 2020 requirements you must satisfy" — that accounts for local adoption, amendment, and the building's existing installation vintage.
**Tags:** #llm #text-classification #nlp #compliance #automation

## The Problem
Electrical code compliance is complex in three dimensions: the NEC is updated every 3 years; local jurisdictions adopt NEC editions on different schedules (a Texas jurisdiction may be on NEC 2017 while a California jurisdiction is on NEC 2023); and when working on existing installations, understanding which requirements apply to the new work (vs. which are grandfathered in the existing installation) requires experience with code adoption history and the "when work is done on existing systems" provisions. An experienced master electrician has internalized these rules — they know that adding a circuit in a kitchen requires AFCI protection under NEC 2020 but not necessarily under NEC 2017, and they know which code edition their local jurisdiction has adopted. Junior electricians and apprentices frequently make compliance errors on this dimension because the code is not systematically presented to them in the job-specific context.

## What Already Exists
The NEC codebook is available digitally (NFPA 70 on the NFPA website). Jurisdictions publish their adopted code editions. Mike Holt's Electrical Exam Preparation resources provide educational materials. Electrical code training courses exist. None of these generate a project-specific checklist: "you are adding a 20A bathroom circuit in a 2005 house in Jefferson County, Colorado — here are the 7 specific NEC 2020 requirements that apply to this work, and here are the 3 inspection items the Jefferson County inspector will specifically check."

## The Customisation Gap
A job-type compliance checklist generator needs: (1) a structured database of NEC requirements by article, mapped to specific job types (kitchen circuit, bathroom circuit, service upgrade, EV charger installation, generator interconnect); (2) a jurisdiction database mapping each municipality to its current adopted code edition and any local amendments; (3) the building vintage logic that determines what existing-installation grandfathering applies; (4) an LLM layer that synthesizes these into a plain-language compliance checklist for the specific job. The jurisdiction database is the key customization — it requires ongoing maintenance as jurisdictions update their adoptions and is not available in any current tool.

## Impact If Solved
Reduces code violations on permitted work that result in failed inspections — each failed inspection adds 1-5 days of delay and re-inspection cost. For an electrical contractor doing 10 permitted jobs per month, reducing the failed inspection rate from 15% to 5% saves 10-20 re-inspection days per month and the associated rework cost.
