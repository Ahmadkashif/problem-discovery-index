# Multi-Curriculum Student Progress Aggregation

**Niche:** [[niches/tutoring-centers/homeschool-enrichment-centers/profile|Homeschool Enrichment Centers]]
**Industry:** [[industries/tutoring-centers|Tutoring Centers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A progress tracking platform that aggregates learning data from multiple curriculum sources — the student's home math curriculum, the center's science labs, a co-op writing program — into a unified academic profile, regardless of which curricula the family uses.
**Tags:** #data-integration #nlp #text-classification #automation

## The Problem
A homeschool enrichment center serves 80 students, each using a different combination of home curricula. Student A uses Saxon Math at home and attends the center for science and writing. Student B uses Teaching Textbooks for math, BJU Press for science at home, and attends the center for writing only. The center director has no unified view of any student's overall academic progress — only the center's own assessments in the subjects they teach. Parents ask: "How is my child doing overall?" The center can only answer for the 2-3 subjects they cover, missing the 5-6 subjects taught at home. No tool aggregates progress across the fragmented homeschool education ecosystem.

## Why Nobody Has Built This
Homeschool curricula don't share data — each publisher has its own platform (or none), its own assessment framework, and its own progress metrics. There is no common data standard across homeschool curricula (unlike K-12 school SIS platforms that share SIS Interoperability standards). Building a multi-curriculum aggregation platform requires either integrating with dozens of curriculum providers (who have no API incentive) or accepting manual data entry from parents, which creates adoption friction. The homeschool market is also ideologically diverse — some families are deeply skeptical of centralized data collection about their children.

## What to Build
A parent-contributed progress portfolio where: (1) parents log home curriculum progress in a lightweight format (subject, curriculum name, current unit/chapter, assessment scores); (2) center instructors add center-based assessment data; (3) the platform maps all curriculum content to a common standards framework (Common Core or state standards, selectable by family) to provide a cross-curriculum skill inventory; (4) generates an academic transcript that aggregates home and center learning into a coherent record — critical for families whose children will eventually enter traditional school or apply to colleges. Privacy controls let parents choose exactly what data the center can see.

## Target Customer
Directors of homeschool enrichment centers and co-ops serving 30+ families who want to provide a unified academic picture across home and center instruction — and families who need transcripts for future school enrollment or college applications.

## Impact If Built
Creates the first cross-curriculum academic profile for homeschooled students — a need that intensifies as homeschool families seek college admissions or re-entry to traditional school. Positions the enrichment center as an academic coordination hub (not just a service provider), increasing parent engagement and retention. Enables state compliance documentation by mapping diverse curricula to required standards coverage.
