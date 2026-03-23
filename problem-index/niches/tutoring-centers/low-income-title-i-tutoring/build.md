# High-Dosage Tutoring Impact Measurement Platform

**Niche:** [[niches/tutoring-centers/low-income-title-i-tutoring/profile|Low-Income / Title I Tutoring Providers]]
**Industry:** [[industries/tutoring-centers|Tutoring Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A platform that measures whether high-dosage tutoring is actually producing academic gains — with enough granularity to show impact within a semester, not just after annual state test results arrive 6 months later.
**Tags:** #gradient-boosting #regression #tabular-ml #causal-inference #compliance

## The Problem
A tutoring provider has a $2M contract to serve 1,500 Title I students with 3x/week tutoring sessions. After one semester, the district asks: "Is this working?" The provider can show attendance (how many sessions each student attended) but not impact (how much each student learned). State test scores won't arrive for 6 months. District benchmark assessments happen quarterly but aren't designed to measure tutoring-specific skill gains. The provider has no way to demonstrate causally that their tutoring produced academic improvement beyond what the student would have achieved through regular classroom instruction alone — the fundamental question that determines contract renewal.

## Why Nobody Has Built This
Measuring tutoring impact requires: (1) frequent, standardized skill assessments aligned to the specific skills being tutored (not annual state tests covering the full curriculum); (2) a comparison framework that isolates tutoring effects from classroom instruction effects; (3) dosage-response analysis (more sessions = more gain?) that requires joining attendance data with assessment data at the student level. Building this requires ed-measurement expertise combined with implementation at scale across multiple schools — a capability that neither ed-tech companies (who sell tools, not measurement) nor research institutions (who study impact retrospectively) currently offer as a product.

## What to Build
An impact measurement platform that: (1) provides brief (5-minute), skill-targeted diagnostic probes administered at tutoring sessions every 2-3 weeks; (2) tracks skill mastery trajectory per student with statistical growth modeling; (3) uses dosage-response analysis to estimate the causal effect of tutoring sessions on skill gains (comparing students with high vs. low attendance, controlling for baseline ability); (4) generates district-ready impact reports showing aggregate and subgroup gains with statistical confidence intervals; (5) identifies students who are not responding to the intervention — triggering diagnostic reassessment and approach changes before the contract period ends.

## Target Customer
Program directors at tutoring providers holding $500K-$50M high-dosage tutoring contracts with school districts who need to demonstrate measurable academic impact for contract renewal and ESSER/Title I compliance.

## Impact If Built
Provides the first within-year impact evidence for high-dosage tutoring contracts — critical as ESSER funding sunsets and districts become more discriminating about which tutoring providers to retain. Identifies non-responding students 8-12 weeks earlier than annual assessments, enabling mid-course corrections. Positions the provider as an evidence-driven partner rather than a staffing agency — the key differentiator for contract renewal.
