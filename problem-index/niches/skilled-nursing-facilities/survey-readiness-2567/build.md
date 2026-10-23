# A State Survey-Team Citation Model From Public 2567 Narratives

**Niche:** [[niches/skilled-nursing-facilities/survey-readiness-2567/profile|State Survey Readiness & Plans of Correction]]
**Industry:** [[industries/skilled-nursing-facilities|Skilled Nursing Facilities]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Every finding every state survey team has written is public, and nobody has turned it into a forecast of what the next team will cite in a given building.
**Tags:** #bert #large-language-models #gradient-boosting #survival-analysis #evaluation-metrics #compliance #quick-win
**Contested on:** Every serious competitor in this niche is fighting to predict which F-tags this state's survey team will cite before the team walks in, and whoever's mock-survey findings best match the CMS-2567 that follows takes the account.

## The Problem
A DON preparing for survey uses a generic checklist covering every regulatory group. Her state's teams may have spent the last year citing medication storage, unnecessary psychotropics and infection control, while a neighbouring state's teams focus on falls supervision and care plans. That knowledge exists only with consultants who used to be surveyors.

## Why Nobody Has Built This
The 2567 narratives are long, inconsistent free text. Until recently, turning them into structured findings at scale needed a manual coding effort nobody would fund. Consultants sell judgement and have little reason to codify it.

## What to Build
A pipeline that parses every public 2567 into structured findings (F-tag, care area, evidence type, scope and severity, survey type, state agency, date). On top of it, a model scores each facility's probability of each tag group at its next survey, combining state agency citation trends, the facility's own history, PBJ staffing and turnover, MDS quality measures and complaint volume. A second model estimates days to the next standard survey from the state's backlog. Output a ranked readiness plan and a mock-survey script for the top risks, and grade it against the real 2567 when it arrives.

## Target Customer
Compliance leads at chains, survey-readiness consultancies wanting a data edge, and REITs or lenders watching survey risk in tenants.

## Impact If Built
Preparation targets the tags most likely to be cited instead of all of them. Avoiding even ~2 of the average 9.5 deficiencies per survey cycle (KFF; reduction is an estimate) protects the health inspection rating that anchors Five-Star, and facilities near the risk-based survey line know exactly what stands in their way.
