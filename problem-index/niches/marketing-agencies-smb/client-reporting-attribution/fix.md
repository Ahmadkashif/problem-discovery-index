# Inconsistent Reporting Across Account Managers

**Niche:** [[niches/marketing-agencies-smb/client-reporting-attribution/profile|Client Reporting and ROI Attribution]]
**Industry:** [[industries/marketing-agencies-smb|SMB Marketing Agencies]]
**Type:** Fix (Pain Point)
**One-liner:** Each account manager creates reports differently — different metrics, different formats, different levels of narrative detail — making it impossible for the agency owner to assess performance quality across the client portfolio.
**Tags:** #automation #workflow-orchestration #worker-facing #quick-win

## The Problem
In a 15-person agency with 4 account managers, each AM creates client reports using their personal templates, their preferred metrics, and their own interpretation of what "a good report" looks like. One AM writes 3 pages of narrative with strategic recommendations; another sends a dashboard link with no commentary. One includes cost-per-lead; another reports cost-per-click. The agency owner reviews a sampling of reports each month and finds inconsistency that undermines the agency's brand quality: a client who switches from AM-1 to AM-2 receives a completely different reporting experience. Worse, the agency cannot aggregate performance data across clients (for benchmarking or case studies) because each AM reports different metrics.

## Why It's Still Broken
Most agencies create a "reporting template" in their first year and assume it will be followed. But without enforcement, AMs deviate: they add custom sections for one client, remove sections they consider irrelevant for another, and gradually evolve their personal approach away from the standard. The template is a Google Doc or Looker Studio report that anyone can copy and modify. There is no system that enforces a minimum standard (these metrics, this narrative structure, this format) while allowing AM-level customization within guardrails.

## What a Fix Looks Like
A report generation system with enforced templates: the agency defines the mandatory report structure (required sections, required metrics per section, minimum narrative length per section), and each AM generates reports within this framework. Customization is allowed within sections (each AM can add client-specific notes) but the structure, metrics, and format are consistent. The agency owner gets a portfolio view: all clients' key metrics in a single dashboard, comparable across AMs. Quality scoring flags reports that are below the narrative minimum or missing required sections before they are sent to clients.

## Who Feels the Pain
Agency owners who cannot assess report quality or compare performance across their portfolio, clients who experience inconsistent service when their AM changes, and AMs who waste time building reports from scratch rather than following a streamlined process.

## Impact If Fixed
Standardizes report quality across the team, reduces per-report creation time by 30-40% through templatization, and enables portfolio-level performance analysis that was previously impossible due to inconsistent metric selection.
