# IEP-Specific Student Progression & Retention Platform

**Niche:** [[niches/language-schools/intensive-english-programs/profile|Intensive English Programs (IEPs)]]
**Industry:** [[industries/language-schools|Language Schools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No platform today manages the full IEP student lifecycle — from placement testing through level progression, proficiency tracking, SEVIS compliance, and conditional university admission readiness — in a single system.
**Tags:** #gradient-boosting #binary-classification #tabular-ml #revenue-impact #data-integration

## The Problem
An IEP Program Director manages 200 students across 6 proficiency levels, each progressing at different rates through 8-week sessions. The director must track: which students are ready to advance to the next level, which are at risk of dropping out before reaching their university admission proficiency target, which are approaching the maximum time allowed on their I-20, and which need additional support to meet the TOEFL/IELTS score required by their conditional admission university. This information lives across 4-5 systems: the LMS (grades), the SIS (enrollment), the SEVIS portal (visa status), the university partner database (conditional admission requirements), and the placement test system (proficiency benchmarks).

## Why Nobody Has Built This
The IEP market is small (~500 programs nationally) and fragmented between university-affiliated programs (which must use the university's IT infrastructure) and standalone schools (which operate independently). No vendor has found a sustainable business model for a purpose-built IEP management platform at this market size. University-affiliated IEPs are constrained by university IT policies that mandate Canvas/Blackboard. Standalone schools lack the budgets to pay for enterprise solutions.

## What to Build
An IEP management platform that: (1) integrates placement test results with level assignment and class scheduling; (2) tracks student proficiency progression across sessions with CEFR/ACTFL-mapped benchmarks; (3) predicts student dropout risk based on attendance, grade trajectory, and engagement patterns; (4) monitors I-20 timelines and SEVIS compliance requirements; (5) maps student progress against conditional university admission proficiency thresholds; and (6) generates a unified dashboard showing the program director which students need intervention, which are on track, and which are ready for university transition.

## Target Customer
Program Directors at IEPs with 100+ students who currently maintain student progression data in spreadsheets and cannot answer "which of my students are at risk of dropping out this session?" without 2 hours of manual data compilation.

## Impact If Built
Improves student retention by an estimated 15-25% (through early dropout risk identification and intervention), reduces program director administrative time by 10-15 hours per session, and ensures SEVIS compliance gaps are caught before they trigger visa violations — protecting both students and the school's SEVP certification.
