# AI Narrative Report Card Drafting Tool

**Niche:** [[niches/k12-private-schools/report-card-narrative-generation/profile|Report Card Narrative Generation]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool generates student-specific narrative report card drafts from academic data, attendance records, and teacher observation notes — every narrative is written from scratch.
**Tags:** #llm #text-generation #nlp #worker-facing #automation

## The Problem
A 4th grade teacher with 22 students writes 22 individualized narrative paragraphs covering math, reading, writing, science, and social-emotional development — a total of 88-110 paragraphs per reporting cycle. Each paragraph must reference the student's specific work ("Sarah's geometry project on tessellations demonstrated strong spatial reasoning"), note growth areas with constructive framing ("Marcus is building stamina in sustained writing tasks"), and align with the school's voice (warm, specific, strength-based). This process takes 8-12 hours per teacher per cycle, typically completed on weekends and evenings.

## Why Nobody Has Built This
Private schools are deeply concerned about AI-generated content feeling inauthentic — parents pay $30K+ for a personal educational experience and expect report card comments to reflect genuine teacher knowledge of their child. Early AI writing tools (generic LLMs) produce fluent but generic narratives that do not reference specific student work or classroom moments. Building a tool that parents cannot distinguish from teacher-written narratives requires integration with academic data (grades, assessments, assignment submissions) and teacher-provided observation notes as grounding inputs.

## What to Build
An LLM-based drafting tool that ingests a student's academic data (assignment grades, assessment results, attendance), teacher-entered observation notes (brief bullet points like "strong contributor in Socratic discussions" or "struggles with multi-step word problems"), and the school's narrative style guide. The tool generates a first draft that the teacher reviews, edits, and personalizes. The output should be 70-80% complete, requiring 2-3 minutes of teacher editing rather than 8-10 minutes of writing from scratch.

## Target Customer
Division heads and academic deans at schools with 200+ students where narrative report cards are a defining feature and teacher burnout during reporting periods is a retention risk.

## Impact If Built
Reduces per-teacher narrative writing time from 8-12 hours to 2-4 hours per reporting cycle. At a 400-student school with 25 teachers producing narratives, that is 100-200 hours saved per cycle — equivalent to 1-2 weeks of reclaimed instructional preparation time. Reduces teacher burnout during reporting periods, the #1 cited source of private school teacher dissatisfaction.
