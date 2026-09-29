# Guided Interview Tooling Adapted to Eligibility and Routing

**Niche:** [[niches/legal-practice-software/legal-aid-intake-triage/profile|Legal Aid & Access-to-Justice Intake]]
**Industry:** [[industries/legal-practice-software|Legal Practice Software]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** The legal aid sector built excellent open-source guided interview tooling for helping people complete court forms, and has not turned the same machinery toward the earlier decision of whether the organisation can help them at all.
**Tags:** #decision-trees #logistic-regression #evaluation-metrics #descriptive-statistics #workflow-orchestration #automation #compliance #worker-facing
**Contested on:** Every serious competitor serving legal aid is fighting to triage far more requests than the organisation can ever serve, defensibly and consistently, and to send the rest somewhere real — and whoever makes that triage defensible takes the contract.

## The Problem
Intake happens on the phone, in a queue, during hours a working person cannot always call. The screening questions are largely deterministic — household size, income, case type, county, opposing party for conflicts — and a substantial share of callers are screened out on facts they could have supplied themselves at any hour. Meanwhile the people who are eligible wait in the same queue. The organisation's scarcest resource, intake staff time, is spent substantially on collecting facts rather than on the judgment only a person can make.

## What Already Exists
Docassemble and the guided interview ecosystem built around it are mature, free, and genuinely well engineered, with a decade of use across statewide legal help sites and court self-help programmes. The sector has real technologists and a strong open-source culture. Eligibility rules are published. Conflict checking exists in every case management system. All the components are available and most are already deployed for a different purpose.

## The Customization Gap
The adaptation is to run the interview before the queue rather than after it, and to design it for a population under stress. It requires: (1) eligibility screening as a self-serve interview available at any hour, in plain language, with the income and household questions phrased the way applicants actually answer them; (2) accessibility as a first requirement rather than a later pass — mobile-first, low-literacy phrasing, screen-reader correctness, and genuine multilingual support, because this population is disproportionately affected by every one of those; (3) conflict checking at the earliest possible point, since a conflict discovered after a lengthy interview wastes the applicant's time and the organisation's; (4) never terminating an interview with a dead end — a screened-out applicant is routed to self-help resources, a referral, or a clinic, with the reason explained; and (5) warm handoff into staff intake with the facts already collected, so the human conversation starts at the judgment rather than at the household size.

## Target Customer
Legal aid organisations, statewide legal help site operators, court self-help centres, and the access-to-justice commissions that fund shared infrastructure across a state.

## Impact If Solved
Moving deterministic screening ahead of the queue typically frees a large share of intake capacity for the conversations that need a person, without reducing the number of people served — it changes what the staff time is spent on. For applicants, an answer at eleven at night instead of a busy signal at ten in the morning is the difference between engaging with the system and giving up, which is the sector's most-cited reason for unmet need.
