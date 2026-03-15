# CLAUDE.md — Agent Handoff Document

This is the primary instruction file for any Claude Code agent working on this project. Read this entire file before doing anything. It tells you exactly what the project is, what has been done, where to pick up, and how to generate output correctly.

---

## What This Project Builds

A structured Obsidian knowledge graph of industry problems worth solving, with a specific focus on **machine learning opportunities** embedded in each industry. The graph lives in `problem-index/` which is already configured as an Obsidian vault (`.obsidian/` folder present — do not modify it).

There are two spec files in the root:
- `CLAUDE_CODE_SPEC.md` — the primary reference for file formats, prompt templates, tag taxonomy, and the full industry list. Read this for details.
- `industry-problem-miner.md` — a more advanced pipeline spec (web scraping + debate engine). Not currently in use.

**All content is generated directly by Claude Code using the Write tool. No SDK, no API calls, no generate.ts, no TypeScript compilation.**

---

## Current State — WHERE TO PICK UP

Read `problem-index/_bookmark.md` first on every session. It is the authoritative state file.

**35 industries are complete** (as of 2026-03-15):
1–5: `behavioral-health-clinics`, `home-health-agencies`, `dental-practices`, `physical-therapy`, `medical-billing`
6–15: `urgent-care`, `veterinary-practices`, `pharmacy-independents`, `immigration-law`, `personal-injury-law`, `estate-planning`, `small-law-firms`, `compliance-consulting`, `general-contractors`, `electrical-contractors`
16–25: `plumbing-contractors`, `roofing-contractors`, `hvac-contractors`, `landscaping`, `painting-contractors`, `home-inspection`, `solar-installers`, `utility-contractors`, `property-management`, `commercial-real-estate`
26–35: `short-term-rentals`, `real-estate-appraisers`, `hoa-management`, `freight-brokerage`, `last-mile-delivery`, `warehouse-3pl`, `customs-brokers`, `cold-chain-logistics`, `contract-manufacturing`, `metal-fabrication`

The next industry in the processing queue is `food-manufacturing` (industry #36 in MANUFACTURING & INDUSTRIAL).

**Every session starts by reading `_bookmark.md` to verify current state before writing any files.**

---

## File Structure Per Industry — 8 Files

Each industry produces exactly 8 files. Use this exact path structure:

```
problem-index/
├── industries/{industry-id}.md              ← industry profile
└── problems/{industry-id}/
    ├── high-impact.md                       ← industry-transforming problem
    ├── low-impact-1.md                      ← customization opportunity #1
    ├── low-impact-2.md                      ← customization opportunity #2
    ├── worker-life-1.md                     ← worker quality-of-life problem #1
    ├── worker-life-2.md                     ← worker quality-of-life problem #2
    ├── ml-opportunity.md                    ← 4-5 scoped ML problem statements
    └── ai-agents-platforms.md              ← AI agent/platform opportunities
```

After completing all 8 files for an industry, update `_bookmark.md`: move it from "In Progress" to "Completed" and advance the next industry to "In Progress".

---

## Tag Taxonomy — USE THESE EXACT TAGS

All problem cards (`high-impact.md`, `low-impact-*.md`, `worker-life-*.md`) and analysis docs (`ml-opportunity.md`, `ai-agents-platforms.md`) carry tags on a `**Tags:**` line immediately after `**One-liner:**`. Apply 2-5 tags per file. Mix all three tiers.

### Tier 1 — ML Algorithm / Model (what technique)
```
#logistic-regression   #linear-regression    #random-forest
#gradient-boosting     #svm                  #cnn
#rnn                   #lstm                 #transformer
#bert                  #llm                  #autoencoder
#isolation-forest      #k-means              #dbscan
#gaussian-process      #bayesian-network     #reinforcement-learning
#diffusion-model       #gan
```

### Tier 2 — ML Task Type (what the model does)
```
#binary-classification   #multiclass-classification   #regression
#object-detection        #semantic-segmentation        #named-entity-recognition
#text-classification     #seq2seq                      #time-series-forecasting
#anomaly-detection       #recommendation               #ranking
#text-generation         #speech-recognition           #ocr
#change-point-detection  #survival-analysis            #causal-inference
#pose-estimation
```

### Tier 3 — ML Application Domain (which field)
```
#computer-vision   #nlp   #speech-processing   #tabular-ml
#graph-ml          #multimodal   #signal-processing
```

### Priority & Context Tags (always check these)
```
#tacit-knowledge-ml   #quick-win   #automation   #data-integration
#workflow-orchestration   #compliance   #worker-facing
#revenue-impact   #ai-agent   #ai-platform
```

---

## PRIORITY RULE: Tacit Knowledge ML (`#tacit-knowledge-ml`)

**This is the highest-priority opportunity type in the entire project.**

In any industry where workers develop mastery through repeated sensory, perceptual, or judgment-based tasks — trades, clinical care, manufacturing, agriculture, transportation, food service — there are problems where an experienced worker has internalized pattern recognition that they cannot fully articulate but act on constantly. These are prime ML targets.

**Examples of what to look for:**
- An electrician who can visually scan a panel and sense a wiring problem before testing → `#cnn` + `#object-detection` + `#computer-vision` + `#tacit-knowledge-ml`
- A mechanic who hears an engine knock and identifies the failing bearing → `#cnn` + `#multiclass-classification` + `#speech-processing` + `#tacit-knowledge-ml`
- A nurse sensing patient deterioration before vitals confirm it → `#gradient-boosting` + `#anomaly-detection` + `#tabular-ml` + `#tacit-knowledge-ml`
- A welder visually grading weld quality → `#cnn` + `#semantic-segmentation` + `#computer-vision` + `#tacit-knowledge-ml`
- A plumber reading pipe vibration patterns as symptoms → `#lstm` + `#anomaly-detection` + `#signal-processing` + `#tacit-knowledge-ml`
- A crop farmer assessing soil health by touch and color → `#cnn` + `#multiclass-classification` + `#computer-vision` + `#tacit-knowledge-ml`

**Rules:**
1. For every industry with human-contact, field work, or craft skill: the `ml-opportunity.md` MUST include at least one tacit knowledge ML entry listed FIRST.
2. For industries where tacit knowledge ML is the most transformative opportunity: it MUST be the `high-impact.md` problem — not a supporting item in `ml-opportunity.md`.
3. Tacit knowledge problems require a more detailed "Why It's Hard" section: explain the data collection challenge (you have to capture the expert performing the task), the labeling challenge (the expert may not agree with themselves), and the deployment challenge (it must be faster than the expert to be adopted).

---

## File Content Formats

### `industries/{id}.md` — Industry Profile

```markdown
# {Industry Name}

## Profile
**Category:** {category}
**Market Size:** {estimated size}
**Tech Maturity:** {Low | Medium | High} — {1-sentence explanation}
**Workforce:** {who does the work day-to-day}

## Key Pain Themes
{3-4 sentence paragraph. Specific workflows, not vague generalities.}

## Current Tech Landscape
{2-3 sentences on existing tools, how well they work, where the gaps are.}

## Problems
- [[problems/{id}/high-impact|🔴 High Impact: {short title}]]
- [[problems/{id}/low-impact-1|🟡 Low Impact: {short title}]]
- [[problems/{id}/low-impact-2|🟡 Low Impact: {short title}]]
- [[problems/{id}/worker-life-1|🟢 Worker Life: {short title}]]
- [[problems/{id}/worker-life-2|🟢 Worker Life: {short title}]]
- [[problems/{id}/ml-opportunity|🔵 ML Opportunities]]
- [[problems/{id}/ai-agents-platforms|🤖 AI Agents & Platforms]]
```

### `problems/{id}/high-impact.md`

PRIORITY: If this industry has human-contact or craft work, check for tacit knowledge ML opportunities first. If one exists and is the most transformative, make it the high-impact problem.

```markdown
# {Problem Title}

**Industry:** [[{id}|{Industry Name}]]
**Type:** High Impact
**One-liner:** {One sentence. What changes the day after this is solved.}
**Tags:** {algorithm tag} {task type tag} {domain tag} {#tacit-knowledge-ml if applicable} {context tags}

## The Problem
{2-3 sentences. Specific workflow, specific people, specific consequence.}

## Why It's Unsolved
{2-3 sentences. What makes this genuinely hard — data, labeling, deployment, regulatory, behavioral?}

## What a Solution Looks Like
{2-3 sentences. Inputs, outputs, what gets automated or augmented.}

## Impact If Solved
{1-2 sentences. Quantify where possible.}
```

### `problems/{id}/low-impact-1.md` and `low-impact-2.md`

```markdown
# {Problem Title}

**Industry:** [[{id}|{Industry Name}]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** {Already solved generically — not for this specific context.}
**Tags:** {relevant tags}

## The Problem
{2-3 sentences. What is the workflow gap? Why does the generic solution fall short?}

## What Already Exists
{2-3 sentences. Name the general-purpose tool. What specifically doesn't fit?}

## The Customisation Gap
{2-3 sentences. What industry-specific logic, terminology, regulation, or workflow needs to be layered on?}

## Impact If Solved
{1-2 sentences. Friction removed for a specific operator.}
```

### `problems/{id}/worker-life-1.md` and `worker-life-2.md`

```markdown
# {Problem Title}

**Industry:** [[{id}|{Industry Name}]]
**Type:** Worker Life Changing
**One-liner:** {What does the worker get back — time, dignity, clarity, safety?}
**Tags:** {relevant tags, include #worker-facing}

## The Problem
{2-3 sentences. Daily grind. Specific task, frequency, human cost.}

## Why It Matters to the Worker
{2-3 sentences. Individual impact, not business impact.}

## What a Solution Looks Like
{2-3 sentences. What would the worker interact with? What burden is lifted?}

## Impact If Solved
{1-2 sentences. Hours reclaimed, stress reduced, skill ceiling raised.}
```

### `problems/{id}/ml-opportunity.md`

Generate 4-5 scoped ML problem statements. **List the tacit knowledge ML entry first if one exists.** Each entry includes a precise ML task definition with data, target, and evaluation metric — specific enough that an ML engineer could scope the project in a meeting.

```markdown
# Machine Learning Opportunities — {Industry Name}

**Industry:** [[{id}|{Industry Name}]]
**Derived from:** [[problems/{id}/high-impact|High Impact]], [[problems/{id}/low-impact-1|Low Impact 1]], [[problems/{id}/low-impact-2|Low Impact 2]], [[problems/{id}/worker-life-1|Worker Life 1]], [[problems/{id}/worker-life-2|Worker Life 2]]

---

## 1. {Opportunity Title}
{tags including algorithm + task type + domain + #tacit-knowledge-ml if applicable}

**Problem statement:** {1-2 sentences describing the ML problem precisely.}

**ML task:** {e.g., "Named Entity Recognition + Binary Classification"}
**Input data:** {what goes in — modality, format, example sources}
**Target:** {what the model predicts — labels, structure, output format}
**Evaluation metric:** {primary metric and why; note any asymmetric costs e.g. recall > precision for safety-critical cases}
**Scope:** {3-4 sentences on build effort, data requirements, team size, timeline. Be honest about difficulty.}
**Data availability:** {how easy is it to get training data? Who has it? What labeling is needed?}

---

## 2. {Next opportunity}
...
```

### `problems/{id}/ai-agents-platforms.md`

Generate 3-4 AI agent or vertical platform opportunities. Each is a distinct product concept, not a rephrasing.

```markdown
# AI Agents & Platform Opportunities — {Industry Name}

**Industry:** [[{id}|{Industry Name}]]

---

## 1. {Agent/Platform Name}
{tags — use #ai-agent or #ai-platform}

**Concept:** {2-3 sentences. What does this agent or platform do autonomously?}
**Inputs:** {what it receives — data, triggers, user commands}
**Outputs / Actions:** {what it produces or does — decisions, documents, API calls, alerts}
**Why now:** {1-2 sentences. What recent capability (LLMs, cheap inference, new APIs) makes this buildable today?}
**Market:** {who pays, rough size, whether there's an existing buyer category}

---
```

---

## Processing Order

Process industries in this exact order (from `industries.ts`). Current position: industry #36, `food-manufacturing`.

```
COMPLETED (35):
1.  behavioral-health-clinics
2.  home-health-agencies
3.  dental-practices
4.  physical-therapy
5.  medical-billing
6.  urgent-care
7.  veterinary-practices
8.  pharmacy-independents
9.  immigration-law
10. personal-injury-law
11. estate-planning
12. small-law-firms
13. compliance-consulting
14. general-contractors
15. electrical-contractors
16. plumbing-contractors
17. roofing-contractors
18. hvac-contractors
19. landscaping
20. painting-contractors
21. home-inspection
22. solar-installers
23. utility-contractors
24. property-management
25. commercial-real-estate
26. short-term-rentals
27. real-estate-appraisers
28. hoa-management
29. freight-brokerage
30. last-mile-delivery
31. warehouse-3pl
32. customs-brokers
33. cold-chain-logistics
34. contract-manufacturing
35. metal-fabrication

QUEUE:
36. food-manufacturing          ← START HERE
7.  veterinary-practices
8.  pharmacy-independents
9.  immigration-law
10. personal-injury-law
11. estate-planning
12. small-law-firms
13. compliance-consulting
14. general-contractors
15. electrical-contractors      ← HIGH tacit knowledge ML potential
16. plumbing-contractors        ← HIGH tacit knowledge ML potential
17. roofing-contractors
18. hvac-contractors            ← HIGH tacit knowledge ML potential
19. landscaping
20. painting-contractors
21. home-inspection
22. solar-installers
23. utility-contractors
24. property-management
25. commercial-real-estate
26. short-term-rentals
27. real-estate-appraisers
28. hoa-management
29. freight-brokerage
30. last-mile-delivery
31. warehouse-3pl
32. customs-brokers
33. cold-chain-logistics
34. contract-manufacturing
35. metal-fabrication           ← HIGH tacit knowledge ML potential
36. food-manufacturing          ← HIGH tacit knowledge ML potential
37. medical-device-mfg
38. electronics-contract-mfg
39. printing-shops
40. crop-farming                ← HIGH tacit knowledge ML potential
41. livestock-operations        ← HIGH tacit knowledge ML potential
42. greenhouse-horticulture
43. food-distributors
44. restaurant-suppliers
45. accounting-firms-smb
46. staffing-agencies
47. it-managed-services
48. marketing-agencies-smb
49. engineering-consultants
50. environmental-consultants
51. hr-consultants
52. independent-retailers
53. ecommerce-sellers
54. auto-dealers-independent
55. specialty-food-retail
56. medical-supply-retail
57. independent-insurance-agents
58. mortgage-brokers
59. wealth-management-rias
60. credit-unions
61. tax-prep-firms
62. collections-agencies
63. k12-private-schools
64. tutoring-centers
65. vocational-schools
66. corporate-training
67. language-schools
68. childcare-centers
69. independent-restaurants      ← HIGH tacit knowledge ML potential
70. catering-companies
71. hotels-boutique
72. food-trucks
73. coffee-shops-independent
74. owner-operator-trucking      ← HIGH tacit knowledge ML potential
75. towing-companies
76. moving-companies
77. charter-bus-operators
78. non-emergency-medical-transport
79. energy-auditors
80. oil-gas-field-services
81. it-staffing-firms
82. software-dev-agencies
83. cybersecurity-mssp
84. data-analytics-consultants
85. cloud-infrastructure-consultants
86. nonprofits-social-services
87. faith-organizations
88. trade-associations
89. municipal-services
90. independent-publishers
91. podcasting-networks
92. video-production-smb
93. news-media-local
94. gyms-independent
95. personal-trainers
96. youth-sports-orgs
97. auto-repair-shops            ← HIGH tacit knowledge ML potential
98. auto-body-shops              ← HIGH tacit knowledge ML potential
99. fleet-managers
100. rv-dealerships
101. cleaning-companies
102. pest-control                ← HIGH tacit knowledge ML potential
103. security-guard-firms
104. event-planning
105. tattoo-studios
106. funeral-homes
107. pet-services
108. alterations-tailoring       ← HIGH tacit knowledge ML potential
109. insurance-tpa
110. public-adjusters
111. insurance-restoration
112. chiropractic-practices      ← HIGH tacit knowledge ML potential
113. acupuncture-practices
114. med-spas
115. hair-salons-independent
116. grant-writers
117. public-defenders
118. land-surveyors              ← HIGH tacit knowledge ML potential
```

Industries marked `← HIGH tacit knowledge ML potential` must have a tacit knowledge ML entry in `ml-opportunity.md` and should strongly consider it for `high-impact.md`.

---

## Workflow Per Session

1. **Read `problem-index/_bookmark.md`** — verify current state and which industry is "In Progress"
2. **Pick up from In Progress** (or the top of Queue if none)
3. **Generate all 8 files** for the industry using the formats above
4. **Update `_bookmark.md`** — move the industry to Completed, set the next one to In Progress
5. **Continue for BATCH_SIZE industries** (default: 3-5 per session)
6. **Stop cleanly** — leave `_bookmark.md` in a consistent state

---

## Quality Standards

- **Specificity over generality** — name the actual workflow, the actual tool, the actual consequence. No vague statements like "improves efficiency."
- **Tacit knowledge ML first** — for craft and human-contact industries, this is the highest priority problem to identify.
- **ML problem statements are engineer-ready** — someone should be able to scope a project from the `ml-opportunity.md` entry alone.
- **Tags are precise** — use algorithm + task + domain tiers together. `#gradient-boosting #binary-classification #tabular-ml` not just `#ml-classification`.
- **Obsidian links are correct** — all `[[wiki-links]]` must match the actual file paths in the vault. Industry profile links to 7 documents. Problem cards link back to their industry.
- **No repetition across the 5 problem cards** — each of the 5 problems in an industry must be distinct. The 2 low-impacts must target different workflows. The 2 worker-lifes must target different pain points.

---

## Environment Notes

- No package.json, no node_modules, no TypeScript compilation needed.
- `industries.ts` in the root is a reference list only — use it to confirm industry IDs and names.
- `problem-index/.obsidian/` is pre-configured — do not modify it.
- No `ANTHROPIC_API_KEY` needed — you are the generator.
