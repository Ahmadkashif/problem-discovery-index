# Undocumented JCL Job Dependencies

**Niche:** [[niches/cloud-infrastructure-consultants/legacy-mainframe-migrators/profile|Legacy Mainframe Migrators]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Mainframe batch schedules contain thousands of JCL jobs with undocumented dependencies, causing migrated batch workflows to fail silently when jobs execute out of order on the new platform.
**Tags:** #graph-ml #anomaly-detection #data-integration #tacit-knowledge-ml

## The Problem
A typical mainframe runs 5,000-50,000 batch jobs nightly, orchestrated by CA-7, Control-M, or TWS. These jobs have implicit dependencies — Job B reads a file that Job A creates, but this dependency is encoded only in the JCL (dataset names in DD statements) and the operator's head, not in the scheduler's dependency graph. When these jobs are migrated to cloud-based schedulers (Airflow, Control-M for cloud), missing dependencies cause data-before-ready errors, empty file processing, and silent data corruption.

## Why It's Still Broken
Mainframe operators who understood job dependencies retired years ago. The JCL is the only remaining documentation, and parsing JCL to extract implicit file-based dependencies requires understanding GDG (Generation Data Group) naming, DISP parameters, and dataset concatenation — none of which modern DevOps engineers are trained on. Scheduler migration tools export explicit dependencies but miss the 30-40% that are implicit.

## What a Fix Looks Like
A JCL analysis tool that parses all job streams, extracts every dataset reference (input and output), builds a complete dependency graph including implicit file-based dependencies, and flags circular dependencies and race conditions. The output is an Airflow-compatible DAG definition with all dependencies — explicit and implicit — properly modeled. Consultants run this before migration to ensure batch schedules will execute correctly on the new platform.

## Who Feels the Pain
Migration engineers who spend weeks in production-support mode after batch migration go-live, debugging job failures caused by missing dependencies at 3 AM.

## Impact If Fixed
Eliminates 80% of post-migration batch job failures, reduces stabilization period from 3 months to 3 weeks, and prevents data corruption incidents that average $100K-$500K per occurrence in financial services.
