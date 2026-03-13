# Problem Index Generator — Claude Code Spec

## What This Builds

A static Obsidian knowledge graph. No scraping. No live data. Claude reasons from its own knowledge to generate a structured problem index across 155 industries. Every file is markdown with Obsidian internal links (`[[like this]]`).

---

## Output Structure

```
problem-index/
├── _index.md                          ← Master index, links to all industries
├── _bookmark.md                       ← Progress tracker, read this first on every run
├── industries/
│   ├── behavioral-health-clinics.md   ← Full industry profile + links to 5 problems
│   ├── home-health-agencies.md
│   └── ... (155 total)
└── problems/
    ├── behavioral-health-clinics/
    │   ├── high-impact.md
    │   ├── low-impact-1.md
    │   ├── low-impact-2.md
    │   ├── worker-life-1.md
    │   └── worker-life-2.md
    └── ... (155 × 5 = 775 problem files total)
```

---

## File Formats

### `_bookmark.md` — the state file

```markdown
# Bookmark

## Status
Last updated: {{ISO timestamp}}
Completed: {{N}} / 155 industries

## Completed
- [[behavioral-health-clinics]]
- [[home-health-agencies]]

## In Progress
- [[dental-practices]]

## Queue (next up)
- [[physical-therapy]]
- [[medical-billing]]
- ... (remaining in order)
```

**Rule:** Every run starts by reading `_bookmark.md`. Processing resumes from "In Progress" or the top of "Queue". After each industry is fully written, it moves to "Completed" and the next industry moves to "In Progress". This is the crash recovery and account-switch mechanism.

---

### `_index.md` — master index

```markdown
# Problem Index

A queryable knowledge graph of industry problems worth solving, structured for Obsidian.

## How to Use
- Browse by industry below
- Use Obsidian graph view to explore connections
- Search by problem type: `high-impact`, `low-impact`, `worker-life`

## Industries

### Healthcare & Clinical
- [[behavioral-health-clinics|Behavioral Health Clinics]]
- [[home-health-agencies|Home Health Agencies]]
- ...

### Legal
- [[immigration-law|Immigration Law Firms]]
- ...

(all 155 industries grouped by category)
```

---

### `industries/{industry-id}.md` — industry profile

```markdown
# {Industry Name}

## Profile
**Category:** {category}
**Market Size:** {estimated size, e.g. "$12B annually in the US"}
**Tech Maturity:** {Low | Medium | High} — {1-sentence explanation}
**Workforce:** {who actually does the work day-to-day}

## Key Pain Themes
{3-4 sentence paragraph describing the recurring operational frustrations in this industry. Be specific — name the actual workflows that cause pain, not vague generalities.}

## Current Tech Landscape
{2-3 sentences on what software/tools exist today, how well they work, and where the gaps are.}

## Problems
- [[problems/{industry-id}/high-impact|🔴 High Impact: {short title}]]
- [[problems/{industry-id}/low-impact-1|🟡 Low Impact: {short title}]]
- [[problems/{industry-id}/low-impact-2|🟡 Low Impact: {short title}]]
- [[problems/{industry-id}/worker-life-1|🟢 Worker Life: {short title}]]
- [[problems/{industry-id}/worker-life-2|🟢 Worker Life: {short title}]]
```

---

### `problems/{industry-id}/high-impact.md`

```markdown
# {Problem Title}

**Industry:** [[{industry-id}|{Industry Name}]]
**Type:** High Impact
**One-liner:** {One sentence. What changes the day after this is solved.}

## The Problem
{2-3 sentences. Describe the specific operational breakdown. Name the actual workflow, the people involved, and the consequence of it not being solved.}

## Why It's Unsolved
{2-3 sentences. What makes this hard — data messiness, regulatory friction, entrenched behavior, no clear buyer, or technical complexity?}

## What a Solution Looks Like
{2-3 sentences. Not a product pitch. What capability would need to exist? What inputs, what outputs, what decisions get automated or augmented?}

## Impact If Solved
{1-2 sentences. Quantify where possible — time saved, cost reduced, error rate dropped, revenue unlocked.}
```

---

### `problems/{industry-id}/low-impact-1.md` and `low-impact-2.md`

```markdown
# {Problem Title}

**Industry:** [[{industry-id}|{Industry Name}]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** {One sentence. This is already solved generically — but not for this specific context.}

## The Problem
{2-3 sentences. What is the workflow gap? Why does the generic solution fall short for this industry?}

## What Already Exists
{2-3 sentences. Name the general-purpose tool or approach that partially solves this. What specifically doesn't fit?}

## The Customisation Gap
{2-3 sentences. What industry-specific logic, terminology, regulation, or workflow needs to be layered on top of the generic solution?}

## Impact If Solved
{1-2 sentences. This won't transform the industry — but it removes a persistent friction for a specific operator.}
```

---

### `problems/{industry-id}/worker-life-1.md` and `worker-life-2.md`

```markdown
# {Problem Title}

**Industry:** [[{industry-id}|{Industry Name}]]
**Type:** Worker Life Changing
**One-liner:** {One sentence. What does the worker get back — time, dignity, clarity, safety?}

## The Problem
{2-3 sentences. Describe the daily grind this worker faces. Be specific about the task, the frequency, and the human cost.}

## Why It Matters to the Worker
{2-3 sentences. Not the business impact — the individual impact. What does this worker lose to this problem every week? What would change for them personally if it were solved?}

## What a Solution Looks Like
{2-3 sentences. Keep it grounded. What would the worker actually interact with? What burden gets lifted?}

## Impact If Solved
{1-2 sentences. Frame it at the individual level — hours per week reclaimed, stress reduced, skill ceiling raised.}
```

---

## The Industry List (Processing Order)

Process in this exact order. Update `_bookmark.md` after each one.

```
HEALTHCARE & CLINICAL (8)
1.  behavioral-health-clinics
2.  home-health-agencies
3.  dental-practices
4.  physical-therapy
5.  medical-billing
6.  urgent-care
7.  veterinary-practices
8.  pharmacy-independents

LEGAL (5)
9.  immigration-law
10. personal-injury-law
11. estate-planning
12. small-law-firms
13. compliance-consulting

CONSTRUCTION & TRADES (10)
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

REAL ESTATE (5)
24. property-management
25. commercial-real-estate
26. short-term-rentals
27. real-estate-appraisers
28. hoa-management

LOGISTICS & SUPPLY CHAIN (5)
29. freight-brokerage
30. last-mile-delivery
31. warehouse-3pl
32. customs-brokers
33. cold-chain-logistics

MANUFACTURING & INDUSTRIAL (6)
34. contract-manufacturing
35. metal-fabrication
36. food-manufacturing
37. medical-device-mfg
38. electronics-contract-mfg
39. printing-shops

AGRICULTURE & FOOD (5)
40. crop-farming
41. livestock-operations
42. greenhouse-horticulture
43. food-distributors
44. restaurant-suppliers

PROFESSIONAL SERVICES (7)
45. accounting-firms-smb
46. staffing-agencies
47. it-managed-services
48. marketing-agencies-smb
49. engineering-consultants
50. environmental-consultants
51. hr-consultants

RETAIL & E-COMMERCE (5)
52. independent-retailers
53. ecommerce-sellers
54. auto-dealers-independent
55. specialty-food-retail
56. medical-supply-retail

FINANCIAL SERVICES (6)
57. independent-insurance-agents
58. mortgage-brokers
59. wealth-management-rias
60. credit-unions
61. tax-prep-firms
62. collections-agencies

EDUCATION (6)
63. k12-private-schools
64. tutoring-centers
65. vocational-schools
66. corporate-training
67. language-schools
68. childcare-centers

HOSPITALITY & FOOD SERVICE (5)
69. independent-restaurants
70. catering-companies
71. hotels-boutique
72. food-trucks
73. coffee-shops-independent

TRANSPORTATION (5)
74. owner-operator-trucking
75. towing-companies
76. moving-companies
77. charter-bus-operators
78. non-emergency-medical-transport

ENERGY (4)
79. energy-auditors
80. oil-gas-field-services
81. solar-installers (skip — covered in Construction)
82. utility-contractors (skip — covered in Construction)

TECHNOLOGY (5)
83. it-staffing-firms
84. software-dev-agencies
85. cybersecurity-mssp
86. data-analytics-consultants
87. cloud-infrastructure-consultants

NONPROFIT & GOVERNMENT (4)
88. nonprofits-social-services
89. faith-organizations
90. trade-associations
91. municipal-services

MEDIA & PUBLISHING (4)
92. independent-publishers
93. podcasting-networks
94. video-production-smb
95. news-media-local

SPORTS & FITNESS (3)
96. gyms-independent
97. personal-trainers
98. youth-sports-orgs

AUTOMOTIVE (4)
99.  auto-repair-shops
100. auto-body-shops
101. fleet-managers
102. rv-dealerships

SPECIALTY SERVICES (8)
103. cleaning-companies
104. pest-control
105. security-guard-firms
106. event-planning
107. tattoo-studios
108. funeral-homes
109. pet-services
110. alterations-tailoring

INSURANCE OPERATIONS (3)
111. insurance-tpa
112. public-adjusters
113. insurance-restoration

WELLNESS & PERSONAL CARE (4)
114. chiropractic-practices
115. acupuncture-practices
116. med-spas
117. hair-salons-independent

GOVERNMENT-ADJACENT (3)
118. grant-writers
119. public-defenders
120. land-surveyors
```

---

## Claude Code Implementation

### Entry point: `generate.ts`

```typescript
import Anthropic from "@anthropic-ai/sdk";
import fs from "fs/promises";
import path from "path";

const client = new Anthropic();
const OUTPUT_DIR = "./problem-index";
const BOOKMARK_FILE = path.join(OUTPUT_DIR, "_bookmark.md");

// --- Types ---
interface BookmarkState {
  completed: string[];
  inProgress: string | null;
  queue: string[];
  lastUpdated: string;
}

// --- Bookmark ---
async function readBookmark(): Promise<BookmarkState> {
  try {
    const raw = await fs.readFile(BOOKMARK_FILE, "utf-8");
    const completed = [...raw.matchAll(/^- \[\[(.+?)\]\]/gm)].map(m => m[1]);
    const inProgressMatch = raw.match(/## In Progress\n- \[\[(.+?)\]\]/);
    const inProgress = inProgressMatch ? inProgressMatch[1] : null;
    const queueSection = raw.split("## Queue")[1] ?? "";
    const queue = [...queueSection.matchAll(/^- \[\[(.+?)\]\]/gm)].map(m => m[1]);
    return { completed, inProgress, queue, lastUpdated: new Date().toISOString() };
  } catch {
    // First run — build from full industry list
    const { INDUSTRIES } = await import("./industries.js");
    return {
      completed: [],
      inProgress: null,
      queue: INDUSTRIES.map(i => i.id),
      lastUpdated: new Date().toISOString(),
    };
  }
}

async function writeBookmark(state: BookmarkState): Promise<void> {
  const completedLines = state.completed.map(id => `- [[${id}]]`).join("\n");
  const inProgressLine = state.inProgress ? `- [[${state.inProgress}]]` : "_none_";
  const queueLines = state.queue.map(id => `- [[${id}]]`).join("\n");

  const content = `# Bookmark

## Status
Last updated: ${state.lastUpdated}
Completed: ${state.completed.length} / 120 industries

## Completed
${completedLines || "_none yet_"}

## In Progress
${inProgressLine}

## Queue (next up)
${queueLines || "_all done_"}
`;
  await fs.writeFile(BOOKMARK_FILE, content, "utf-8");
}

// --- LLM call ---
async function generate(prompt: string): Promise<string> {
  const response = await client.messages.create({
    model: "claude-opus-4-5",
    max_tokens: 2000,
    messages: [{ role: "user", content: prompt }],
  });
  const block = response.content[0];
  if (block.type !== "text") throw new Error("Unexpected block type");
  return block.text;
}

// --- Prompts ---
function industryPrompt(industry: { id: string; name: string; category: string }): string {
  return `Write the industry profile markdown file for "${industry.name}" in the "${industry.category}" category.

Use EXACTLY this format — no deviations:

# ${industry.name}

## Profile
**Category:** ${industry.category}
**Market Size:** {estimated size}
**Tech Maturity:** {Low | Medium | High} — {1-sentence explanation}
**Workforce:** {who does the work day-to-day}

## Key Pain Themes
{3-4 sentence paragraph. Specific workflows, not vague generalities.}

## Current Tech Landscape
{2-3 sentences on existing tools, how well they work, where the gaps are.}

## Problems
- [[problems/${industry.id}/high-impact|🔴 High Impact: {short title}]]
- [[problems/${industry.id}/low-impact-1|🟡 Low Impact: {short title}]]
- [[problems/${industry.id}/low-impact-2|🟡 Low Impact: {short title}]]
- [[problems/${industry.id}/worker-life-1|🟢 Worker Life: {short title}]]
- [[problems/${industry.id}/worker-life-2|🟢 Worker Life: {short title}]]

Output only the markdown. No preamble.`;
}

function problemPrompt(
  industry: { id: string; name: string },
  type: "high-impact" | "low-impact-1" | "low-impact-2" | "worker-life-1" | "worker-life-2"
): string {
  const templates: Record<string, string> = {
    "high-impact": `Write a HIGH IMPACT problem card for the ${industry.name} industry.
This problem transforms the industry the next day if solved.

PRIORITY CHECK: If this industry involves human contact, field work, or craft skill, look first for tacit knowledge problems — situations where an experienced worker has internalized pattern recognition (visual, auditory, tactile, olfactory) that a machine learning model could capture and scale. If you find one, make it the high-impact problem and tag it #tacit-knowledge-ml. Examples: fault detection by sound, quality assessment by sight, early warning by subtle sensory cues.

Format:
# {Problem Title}

**Industry:** [[${industry.id}|${industry.name}]]
**Type:** High Impact
**One-liner:** {one sentence — what changes the day after this is solved}
**Tags:** {2-5 tags from the taxonomy: algorithm tag + task type tag + domain tag + priority tags}

## The Problem
{2-3 sentences. Specific workflow, specific people, specific consequence.}

## Why It's Unsolved
{2-3 sentences. What makes this genuinely hard?}

## What a Solution Looks Like
{2-3 sentences. Inputs, outputs, what gets automated or augmented.}

## Impact If Solved
{1-2 sentences. Quantify where possible.}`,

    "low-impact-1": `Write a LOW IMPACT problem card (first of two) for the ${industry.name} industry.
This problem is already solved generically but not customised for this industry's specific context.

Format:
# {Problem Title}

**Industry:** [[${industry.id}|${industry.name}]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** {one sentence — already solved generically, not for this context}

## The Problem
{2-3 sentences. The workflow gap and why the generic solution falls short.}

## What Already Exists
{2-3 sentences. Name the general tool. What specifically doesn't fit?}

## The Customisation Gap
{2-3 sentences. What industry-specific logic needs to be layered on?}

## Impact If Solved
{1-2 sentences. Friction removed for a specific operator.}`,

    "low-impact-2": `Write a LOW IMPACT problem card (second of two, different from the first) for the ${industry.name} industry.
This problem is already solved generically but not customised for this industry's specific context.

Format:
# {Problem Title}

**Industry:** [[${industry.id}|${industry.name}]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** {one sentence — already solved generically, not for this context}

## The Problem
{2-3 sentences.}

## What Already Exists
{2-3 sentences.}

## The Customisation Gap
{2-3 sentences.}

## Impact If Solved
{1-2 sentences.}`,

    "worker-life-1": `Write a WORKER LIFE CHANGING problem card (first of two) for the ${industry.name} industry.
If solved, this is a huge unlock for a worker in this industry — not the business, the individual worker.

Format:
# {Problem Title}

**Industry:** [[${industry.id}|${industry.name}]]
**Type:** Worker Life Changing
**One-liner:** {one sentence — what does the worker get back: time, dignity, clarity, safety?}

## The Problem
{2-3 sentences. Daily grind. Specific task, frequency, human cost.}

## Why It Matters to the Worker
{2-3 sentences. Individual impact, not business impact. What do they lose every week?}

## What a Solution Looks Like
{2-3 sentences. What would the worker interact with? What burden is lifted?}

## Impact If Solved
{1-2 sentences. Hours reclaimed, stress reduced, skill ceiling raised.}`,

    "worker-life-2": `Write a WORKER LIFE CHANGING problem card (second of two, different from the first) for the ${industry.name} industry.
If solved, this is a huge unlock for a worker in this industry — not the business, the individual worker.

Format:
# {Problem Title}

**Industry:** [[${industry.id}|${industry.name}]]
**Type:** Worker Life Changing
**One-liner:** {one sentence — what does the worker get back?}

## The Problem
{2-3 sentences.}

## Why It Matters to the Worker
{2-3 sentences.}

## What a Solution Looks Like
{2-3 sentences.}

## Impact If Solved
{1-2 sentences.}`,
  };

  return `${templates[type]}\n\nOutput only the markdown. No preamble.`;
}

// --- File writers ---
async function writeIndustry(
  industry: { id: string; name: string; category: string },
  content: string
): Promise<void> {
  const filePath = path.join(OUTPUT_DIR, "industries", `${industry.id}.md`);
  await fs.mkdir(path.dirname(filePath), { recursive: true });
  await fs.writeFile(filePath, content, "utf-8");
}

async function writeProblem(
  industryId: string,
  problemType: string,
  content: string
): Promise<void> {
  const filePath = path.join(OUTPUT_DIR, "problems", industryId, `${problemType}.md`);
  await fs.mkdir(path.dirname(filePath), { recursive: true });
  await fs.writeFile(filePath, content, "utf-8");
}

// --- Main loop ---
async function main() {
  await fs.mkdir(OUTPUT_DIR, { recursive: true });

  const state = await readBookmark();
  console.log(`Resuming. Completed: ${state.completed.length}, Queue: ${state.queue.length}`);

  const { INDUSTRIES } = await import("./industries.js");

  // Determine what to process next
  const toProcess = state.inProgress
    ? [state.inProgress, ...state.queue]
    : state.queue;

  if (toProcess.length === 0) {
    console.log("All industries complete.");
    return;
  }

  // Process one industry per run to stay well within rate limits
  // Increase BATCH_SIZE cautiously if running on a fresh account
  const BATCH_SIZE = 3;
  const batch = toProcess.slice(0, BATCH_SIZE);

  for (const industryId of batch) {
    const industry = INDUSTRIES.find(i => i.id === industryId);
    if (!industry) {
      console.warn(`Unknown industry: ${industryId}, skipping`);
      continue;
    }

    console.log(`\nProcessing: ${industry.name}`);
    state.inProgress = industryId;
    await writeBookmark(state);

    try {
      // 1. Industry profile
      console.log("  → industry profile");
      const industryContent = await generate(industryPrompt(industry));
      await writeIndustry(industry, industryContent);

      // 2. Five problems sequentially — no parallel to avoid rate limits
      const problemTypes = [
        "high-impact",
        "low-impact-1",
        "low-impact-2",
        "worker-life-1",
        "worker-life-2",
      ] as const;

      for (const pType of problemTypes) {
        console.log(`  → ${pType}`);
        const content = await generate(problemPrompt(industry, pType));
        await writeProblem(industryId, pType, content);
        await sleep(1500); // 1.5s between calls
      }

      // Mark complete
      state.completed.push(industryId);
      state.inProgress = null;
      state.queue = state.queue.filter(id => id !== industryId);
      state.lastUpdated = new Date().toISOString();
      await writeBookmark(state);
      console.log(`  ✓ ${industry.name} complete`);

    } catch (err) {
      console.error(`  ✗ Failed on ${industry.name}:`, err);
      // Leave inProgress as-is so next run retries this industry
      await writeBookmark(state);
      process.exit(1); // Stop cleanly, don't corrupt state
    }
  }

  console.log(`\nBatch complete. Run again to continue.`);
  console.log(`Progress: ${state.completed.length} / 120`);
}

function sleep(ms: number) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

main().catch(err => {
  console.error("Fatal:", err);
  process.exit(1);
});
```

---

## Rate Limit Strategy

| Account state | BATCH_SIZE | Calls per run |
|---|---|---|
| Fresh / just switched | 3 industries | 18 API calls |
| Warmed up | 5 industries | 30 API calls |
| Confident | 10 industries | 60 API calls |

Each industry = 6 API calls (1 profile + 5 problems). With 1.5s gaps between calls, a batch of 3 takes ~3 minutes. The bookmark saves state after every completed industry — if you hit a rate limit mid-industry, the next run retries that industry from scratch (6 calls, not a big loss).

---

## Running It

```bash
# Install
npm install @anthropic-ai/sdk tsx typescript

# First run — creates _bookmark.md automatically
npx tsx generate.ts

# Subsequent runs — reads bookmark, resumes where it left off
npx tsx generate.ts

# Check progress at any time
cat problem-index/_bookmark.md
```

---

## Tag Taxonomy

All problem cards and ML/AI docs carry tags from these three tiers. Apply 2-5 tags per file. Tags go on the `**Tags:**` line immediately after `**One-liner:**`.

### Tier 1 — ML Algorithm / Model
What technique does the solution primarily use?

| Tag | When to use |
|---|---|
| `#logistic-regression` | Binary or multiclass classification on tabular data |
| `#linear-regression` | Continuous output prediction, tabular data |
| `#random-forest` | Ensemble classification/regression, tabular data |
| `#gradient-boosting` | XGBoost / LightGBM / CatBoost — tabular, high accuracy |
| `#svm` | Support Vector Machine — small-to-medium datasets |
| `#cnn` | Convolutional Neural Network — images, signals, audio spectrograms |
| `#rnn` | Recurrent Neural Network — sequential data |
| `#lstm` | Long Short-Term Memory — sequences with long dependencies |
| `#transformer` | Attention-based — text, vision, multimodal |
| `#bert` | Pre-trained language model fine-tuning |
| `#llm` | Large language model — generation, reasoning, extraction |
| `#autoencoder` | Representation learning, anomaly detection |
| `#isolation-forest` | Unsupervised anomaly detection, tabular data |
| `#k-means` | Unsupervised clustering |
| `#dbscan` | Density-based clustering, irregular shapes |
| `#gaussian-process` | Probabilistic regression with uncertainty estimates |
| `#bayesian-network` | Probabilistic graphical models |
| `#reinforcement-learning` | Agent/environment, sequential decision-making |
| `#diffusion-model` | Generative — image, audio, signal synthesis |
| `#gan` | Generative Adversarial Network |

### Tier 2 — ML Task Type
What does the model predict or produce?

| Tag | When to use |
|---|---|
| `#binary-classification` | Two-class output (yes/no, pass/fail, at-risk/safe) |
| `#multiclass-classification` | 3+ discrete output classes |
| `#regression` | Continuous numeric output |
| `#object-detection` | Locate and classify objects in images/video |
| `#semantic-segmentation` | Pixel-level image classification |
| `#named-entity-recognition` | Extract typed entities from text |
| `#text-classification` | Assign categories to documents or sentences |
| `#seq2seq` | Sequence-in, sequence-out (translation, summarization) |
| `#time-series-forecasting` | Predict future values from historical sequences |
| `#anomaly-detection` | Flag outliers in data streams or records |
| `#recommendation` | Rank items for a user or context |
| `#ranking` | Order a set of candidates by relevance or quality |
| `#text-generation` | Produce natural language output |
| `#speech-recognition` | Convert audio to text (ASR) |
| `#ocr` | Optical character recognition — documents, forms, signs |
| `#change-point-detection` | Detect shifts in time-series distributions |
| `#survival-analysis` | Time-to-event prediction (churn, failure, death) |
| `#causal-inference` | Estimate treatment effects from observational data |
| `#pose-estimation` | Detect body / object pose from images or video |

### Tier 3 — ML Application Domain
Which field does this belong to?

| Tag | When to use |
|---|---|
| `#computer-vision` | Image, video, thermal, depth data |
| `#nlp` | Text understanding and generation |
| `#speech-processing` | Audio, voice, sound analysis |
| `#tabular-ml` | Structured rows/columns — the most common real-world case |
| `#graph-ml` | Graph neural networks, network analysis |
| `#multimodal` | Combines 2+ modalities (e.g. image + text) |
| `#signal-processing` | Vibration, EMG, EEG, sensor streams |

### Priority & Context Tags
Apply alongside the above tiers.

| Tag | When to use |
|---|---|
| `#tacit-knowledge-ml` | **Top-priority.** Worker has internalized pattern recognition through experience. ML can capture, codify, and scale this. See below. |
| `#quick-win` | Buildable in <4 weeks with available data |
| `#automation` | Replaces a fully manual, repetitive step |
| `#data-integration` | Core challenge is joining / reconciling disparate data sources |
| `#workflow-orchestration` | Core challenge is sequencing and routing work between systems |
| `#compliance` | Solution directly addresses a regulatory or legal constraint |
| `#worker-facing` | Primary beneficiary is the individual worker, not the business |
| `#revenue-impact` | Solution directly unlocks or protects revenue |
| `#ai-agent` | Opportunity for an autonomous AI agent (multi-step, tool use) |
| `#ai-platform` | Opportunity to build a vertical AI platform or workflow layer |

---

## Tacit Knowledge ML — Priority Rule

**Definition:** Tacit knowledge is expertise that workers have internalized through years of practice that they cannot fully articulate but express through intuition, judgment, and pattern recognition. This is the *most important* ML opportunity in any profession with human contact or craft work.

**Examples:**
- An electrician who can look at a panel and immediately sense something is wrong in the wire routing before testing anything → computer vision + classification
- A mechanic who hears a knock and knows which bearing is failing → acoustic ML, `#cnn` + `#multiclass-classification` + `#speech-processing`
- A nurse who senses a patient is about to deteriorate hours before vitals confirm it → multivariate anomaly detection, `#tabular-ml` + `#anomaly-detection`
- A welder who judges weld quality by visual inspection → `#computer-vision` + `#semantic-segmentation`
- A soil scientist who feels soil texture and estimates composition → `#multimodal` + `#regression`
- A plumber who reads water pressure fluctuation patterns as a symptom → `#time-series-forecasting` + `#anomaly-detection`

**When to apply:** For any industry where workers develop mastery through repeated, high-stakes sensory or perceptual tasks — trades, clinical care, manufacturing QC, agriculture, transportation, food service — the `ml-opportunity.md` file MUST include at least one entry targeting tacit knowledge. This entry carries `#tacit-knowledge-ml` and is listed first in the document.

**Why this matters:** These problems are structurally hard to solve because the knowledge holder often cannot write a spec. The value of the ML solution is not incremental efficiency — it is the preservation and scalability of rare expertise that took decades to develop.

---

## Obsidian Setup

The vault is already configured. `problem-index/` contains `.obsidian/` with `app.json`, `graph.json`, `workspace.json`. Open Obsidian → `Open folder as vault` → select `problem-index/`.

Graph view color coding:
- **Red** → `#tacit-knowledge-ml` (highest priority opportunities)
- **Blue** → `#computer-vision`
- **Dark blue** → `#nlp`
- **Purple** → `#deep-learning`
- **Yellow** → `#quick-win`
- **Green** → `#tabular-ml`
- **Orange** → `#speech-processing`

Navigate: start at `_index.md` → industry profile → problem cards → `ml-opportunity.md`.

---

## What Comes After This

Once the index is populated, the queryable layer is a simple script that:
1. Takes a natural language question: *"What's the best problem to solve using linear regression?"*
2. Reads all problem files from `problem-index/problems/`
3. Passes them as context to Claude with the question
4. Returns a ranked, reasoned answer

The index *is* the RAG corpus. You built it with Claude, you query it with Claude.
