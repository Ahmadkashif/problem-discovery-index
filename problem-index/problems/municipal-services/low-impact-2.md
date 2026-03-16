# Permitting Workflow Automation

**Industry:** [[municipal-services|Municipal Services]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Permitting software exists but cannot read a plan set and check it against the local amendment to the International Building Code — so plan reviewers spend weeks on tasks a well-configured LLM could pre-screen in minutes.
**Tags:** #llm #text-generation #nlp #compliance #automation

## The Problem
Building permit applications arrive as a stack of documents: site plans, structural drawings, energy calculations, contractor licenses, and narrative descriptions. A plan reviewer must verify each submission against the municipality's adopted building code (typically IBC/IRC with local amendments), zoning ordinance, fire code, ADA requirements, and stormwater management rules. A single residential permit may require checking 30-50 code provisions. Commercial permits can involve 200+. Reviewers are chronically backlogged — median permit review time in US municipalities is 4-8 weeks, and some jurisdictions exceed 6 months, directly stalling construction and economic development.

## What Already Exists
Accela, Tyler EnerGov, and OpenGov provide permit tracking and workflow management — they route applications through review stages and generate status notifications. But they are workflow tools, not compliance analysis tools. The actual code-checking step is entirely manual: a human reviewer opens the plan PDF, opens the code book, and cross-references line by line. Some jurisdictions use e-plan review tools (Bluebeam, ProjectDox) for markup collaboration, but these do not perform automated compliance checks.

## The Customisation Gap
Each municipality adopts building codes with local amendments — setback requirements, snow load tables, seismic zones, stormwater detention ratios, and fire sprinkler thresholds all vary. A general-purpose document analysis tool cannot know that this specific city requires a 25-foot rear setback in R-1 zones instead of the IBC default 20-foot, or that the local fire marshal requires NFPA 13D sprinklers in all new construction over 3,000 square feet. An LLM-based pre-screening system fine-tuned on a municipality's specific adopted code (including all local amendments, variance history, and plan reviewer correction patterns) could flag the 15-20 most common rejection reasons before a human reviewer ever opens the file, reducing review cycles from weeks to days.

## Impact If Solved
Cuts first-review rejection rates by 40-50% (currently 60-70% of permits are returned for corrections on first submission), reduces average review time from 6 weeks to under 2 weeks, and frees senior plan reviewers to focus on complex commercial projects instead of catching missing setback dimensions on residential additions.
