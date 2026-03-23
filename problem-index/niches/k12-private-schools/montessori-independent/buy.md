# Montessori-Aware SIS Integration

**Niche:** [[niches/k12-private-schools/montessori-independent/profile|Montessori Independent Schools]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** General SIS tools (FACTS, Gradelink) handle billing and enrollment, and Transparent Classroom handles Montessori observations, but they do not integrate — forcing teachers and admins into a dual-system workflow.
**Tags:** #data-integration #workflow-orchestration #automation #quick-win

## The Problem
A Montessori school typically runs Transparent Classroom for academic observation and FACTS or Gradelink for enrollment, billing, and family communication. Student and family data must be manually synchronized between systems. When a new student enrolls in FACTS, they must be manually created in Transparent Classroom. When a family's contact information changes, it must be updated in both systems. Progress observations in Transparent Classroom cannot be surfaced through the parent portal in FACTS.

## What Already Exists
Transparent Classroom provides Montessori-specific observation tracking, lesson planning, and progress documentation. FACTS SIS and Gradelink provide enrollment management, billing, parent portal, and standard school administration. Both offer APIs, but no pre-built integration exists.

## The Customization Gap
The integration must map between two fundamentally different academic data models: FACTS uses grade-subject-grade (a student gets a "B" in "3rd Grade Math"), while Transparent Classroom uses competency-material-mastery-level (a student is "practicing" the "stamp game" in the "mathematics" area). A bi-directional sync must handle student enrollment (FACTS to TC), academic progress surfacing (TC to FACTS parent portal), and family contact data (bi-directional). The integration must preserve the integrity of both data models without forcing one into the other's structure.

## Target Customer
Montessori school administrators managing dual-system data entry, currently spending 3-5 hours per week on manual data synchronization between observation and administrative systems.

## Impact If Solved
Eliminates 3-5 hours per week of manual data sync. Enables parents to see Montessori progress observations through the school's primary parent portal instead of requiring a separate Transparent Classroom login. Reduces data entry errors that cause billing and communication problems.
