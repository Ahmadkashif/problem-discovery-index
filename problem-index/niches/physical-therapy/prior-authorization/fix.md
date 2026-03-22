# Auto-Generated Medical Necessity Narratives

**Niche:** [[niches/physical-therapy/prior-authorization/profile|Prior Authorization & Concurrent Review]]
**Industry:** [[industries/physical-therapy|Physical Therapy]]
**Type:** Fix (Pain Point)
**One-liner:** PTs stop writing the same medical necessity justification from scratch for every concurrent review — auto-generated narratives pull functional data and outcome scores from the EMR and format them to payer-specific criteria.
**Tags:** #large-language-models #transformers #bert #feature-engineering #automation #compliance #worker-facing

## The Problem
Every PT authorization extension requires a medical necessity narrative — a clinical justification explaining why the patient needs continued treatment. Payers want specific information: functional limitations with objective measurements, outcome score changes showing improvement, treatment goals with expected achievement timelines, and a discharge plan. PTs write these narratives from scratch for every extension request, pulling data from their daily notes, mentally calculating outcome score changes, and formatting the justification to match each payer's specific criteria. A PT managing a caseload of 30+ patients with staggered authorization cycles writes 3-5 medical necessity narratives per week, each taking 15-25 minutes. The content is largely templated — the same functional data from the EMR formatted into a narrative structure — but the manual assembly process is time-consuming and error-prone.

## Why It's Still Broken
Medical necessity narratives require synthesizing data scattered across multiple EMR sections — the initial evaluation's baseline measurements, the most recent daily note's current measurements, outcome measure scores from different assessment dates, and treatment plan goals. No PT EMR assembles this data into a narrative format automatically. The narratives also require payer-specific formatting: EviCore's concurrent review portal asks for functional data in a specific structure, Cohere Health wants different emphasis, and direct-to-payer submissions have yet another format. EMR vendors haven't built narrative generation because it requires natural language generation capability that traditional software doesn't provide, and the payer-specific formatting creates a moving target as UM vendors change their criteria. LLM-powered narrative generation is now technically feasible but no PT-specific implementation exists.

## What a Fix Looks Like
An automated narrative generator that: (1) pulls the patient's baseline functional data from the initial evaluation, (2) pulls current functional data from the most recent daily notes, (3) calculates change scores for all tracked outcome measures, (4) identifies treatment plan goals and current progress toward each, (5) generates a medical necessity narrative in prose format that presents this data as a clinical justification for continued treatment, and (6) formats the narrative to match the target payer's concurrent review criteria (EviCore format, Cohere Health format, generic payer format). The PT reviews the generated narrative, makes minor edits if needed, and submits — reducing a 15-25 minute task to 2-3 minutes. The narrative uses clinical language appropriate for utilization review and emphasizes the data points that payers weight most heavily in approval decisions (functional improvement trajectory, remaining goals, discharge timeline).

## Who Feels the Pain
PTs who spend 1-2 hours per week writing medical necessity narratives instead of treating patients or going home on time. Front desk staff who must chase PTs to complete narratives before authorization expires. Patients whose treatment continuity depends on timely, well-documented extension requests.

## Impact If Fixed
Recovers 1-2 hours per week per PT spent on narrative writing — across a 5-clinician practice, that's 5-10 clinical hours reclaimed weekly. Improves extension approval rates by ensuring narratives consistently include the specific data points payers require for approval. Reduces authorization-related treatment gaps by eliminating the delay caused by PTs postponing narrative writing due to time pressure.
