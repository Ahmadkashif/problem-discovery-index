# Incident Reporting Built for Fifty State Rulebooks

**Industry:** [[assisted-living-communities|Assisted Living Communities]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Incident-reporting tools capture what happened; an assisted living community also needs to know, state by state, whether it must tell the state, the family, the physician or the ombudsman, by when, and on which form.
**Tags:** #large-language-models #transformers #bert #compliance #workflow-orchestration #automation #quick-win

## The Problem
A resident is found on the floor at 3 a.m. with a bruised hip. The caregiver writes an incident note and the on-call nurse decides whether to send her to hospital. Then the questions start. Is this reportable to the state licensing agency in this state? Within how many hours? Was it an unwitnessed fall, an injury of unknown origin or a possible neglect allegation, each of which may carry a different deadline? Who must be told: the family, the physician, the ombudsman? Must the service plan be updated? Executive directors answer from memory and a binder. A chain operating in a dozen states has a dozen answers, and 18 states changed their assisted living rules in 2025 (NCAL). Late or missing reports are a common citation, and they come up again when the next survey reads the incident log, or when a family's lawyer does.

## What Already Exists
EHR and eMAR suites (Yardi, PointClickCare, August Health) include incident modules with forms, notifications and trend reports. General risk-management and EHS incident tools do the same for hospitals and employers. Some states run online reporting portals. Each records the incident well. None turns it into the right state-specific obligations, with the clock running.

## The Customisation Gap
The adaptation is a maintained rules layer plus language understanding. It needs each state's reportable categories (falls with injury, elopement, abuse, neglect, exploitation, medication errors, deaths and communicable disease), deadlines, recipients and forms, versioned as rules change. It needs a classifier that reads the caregiver's free-text note and maps it to those categories, and flags notes that describe a reportable event without naming it ("found sitting by the door, coat on, 2 a.m."). It needs pre-filled state forms and family notifications drafted for the director to sign, with a timer per obligation. And memory care units carry extra rules in some states that apply only to residents with a dementia diagnosis.

## Impact If Solved
A community logging ~10–20 incidents a month (estimate) saves the director ~3–5 hours a month of looking up rules and filling forms (estimate), and a chain avoids late-report citations that each cost a plan of correction and, in some states, a fine. The bigger gain is a consistent record when a surveyor or a plaintiff asks what was known and when.
