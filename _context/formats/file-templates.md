# File Templates

**Every file you create MUST use the exact template below. Do not improvise structure. Do not add, remove, rename, or reorder sections. If your output deviates from these templates, it is wrong — fix it.**

---

## 1. Industry Profile — `industries/{id}.md`

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

---

## 2. High Impact Problem — `problems/{id}/high-impact.md`

```markdown
# {Problem Title}

**Industry:** [[{id}|{Industry Name}]]
**Type:** High Impact
**One-liner:** {One sentence. What changes the day after this is solved.}
**Tags:** {2-5 tags from taxonomy}

## The Problem
{2-3 sentences. Specific workflow, specific people, specific consequence.}

## Why It's Unsolved
{2-3 sentences. What makes this genuinely hard?}

## What a Solution Looks Like
{2-3 sentences. Inputs, outputs, what gets automated or augmented.}

## Impact If Solved
{1-2 sentences. Quantify where possible.}
```

If `#tacit-knowledge-ml` applies, ADD an expanded "Why It's Hard" covering: data collection challenge, labeling challenge, deployment challenge.

---

## 3. Low Impact Problem — `problems/{id}/low-impact-{1|2}.md`

```markdown
# {Problem Title}

**Industry:** [[{id}|{Industry Name}]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** {Already solved generically — not for this specific context.}
**Tags:** {relevant tags}

## The Problem
{2-3 sentences. What is the workflow gap?}

## What Already Exists
{2-3 sentences. Name the general-purpose tool. What doesn't fit?}

## The Customisation Gap
{2-3 sentences. What industry-specific logic needs layering on?}

## Impact If Solved
{1-2 sentences. Friction removed for a specific operator.}
```

---

## 4. Worker Life Problem — `problems/{id}/worker-life-{1|2}.md`

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

---

## 5. ML Opportunity — `problems/{id}/ml-opportunity.md`

```markdown
# Machine Learning Opportunities — {Industry Name}

**Industry:** [[{id}|{Industry Name}]]
**Derived from:** [[problems/{id}/high-impact|High Impact]], [[problems/{id}/low-impact-1|Low Impact 1]], [[problems/{id}/low-impact-2|Low Impact 2]], [[problems/{id}/worker-life-1|Worker Life 1]], [[problems/{id}/worker-life-2|Worker Life 2]]

---

## 1. {Opportunity Title}
{tags including #tacit-knowledge-ml if applicable — ALWAYS list tacit knowledge entry first}

**Problem statement:** {1-2 sentences describing the ML problem precisely.}
**ML task:** {e.g., "Named Entity Recognition + Binary Classification"}
**Input data:** {modality, format, example sources}
**Target:** {what the model predicts}
**Evaluation metric:** {primary metric and why}
**Scope:** {3-4 sentences on build effort, data requirements, team size, timeline.}
**Data availability:** {how easy to get training data? Who has it?}

---

## 2. {Next opportunity}
...
```

4-5 entries per industry. Tacit knowledge ML entry MUST be listed FIRST.

---

## 6. AI Agents & Platforms — `problems/{id}/ai-agents-platforms.md`

```markdown
# AI Agents & Platform Opportunities — {Industry Name}

**Industry:** [[{id}|{Industry Name}]]

---

## 1. {Agent/Platform Name}
{tags — use #ai-agent or #ai-platform}

**Concept:** {2-3 sentences. What does this do autonomously?}
**Inputs:** {data, triggers, user commands}
**Outputs / Actions:** {decisions, documents, API calls, alerts}
**Why now:** {1-2 sentences. What recent capability makes this buildable?}
**Market:** {who pays, rough size, existing buyer category}

---
```

3-4 entries per industry.

---

## 7. Niche Overview — `niches/{industry-id}/_overview.md`

```markdown
# Niche Analysis — {Industry Name}

**Parent Industry:** [[industries/{industry-id}|{Industry Name}]]

## Niche Selection

Applied four-axis niche discovery: Market Share, Digital Adoption, Underserved Audience, Automation Potential.

| # | Niche | Category | Est. Market Size | Digital Adoption | Target Buyer |
|---|---|---|---|---|---|
| 1 | {Niche Name} | {Category} | {size} | {level} | {buyer} |
| ... |

## Why These Niches
{3-4 sentences explaining coverage and excluded segments.}

## Niches
- [[niches/{industry-id}/{niche-id}/profile|{emoji} {Niche Name}]]
- ...
```

8 niches per industry. Emoji: 🔵 High Market Share, 🟠 Low Digitized, 🟣 Underserved Audience, ⚡ Highly Automatable.

---

## 8. Niche Profile — `niches/{industry-id}/{niche-id}/profile.md`

```markdown
# {Niche Name}

**Parent Industry:** [[industries/{industry-id}|{Industry Name}]]
**Category:** {High Market Share | Low Digitized | Underserved Audience | Highly Automatable}

## Profile
**Market Size:** {size}
**Share of Parent Industry:** {percentage}
**Digital Adoption:** {Low | Low-Medium | Medium | Medium-High | High} — {1 sentence}
**Target Buyer:** {specific role/persona}
**Automation Potential:** {Low | Medium | High} — {1 sentence}

## What Makes This a Distinct Niche
{3-4 sentences.}

## Current Tools & Gaps
{2-3 sentences.}

## Problems
- [[niches/{industry-id}/{niche-id}/build|🔨 Build: {title}]]
- [[niches/{industry-id}/{niche-id}/buy|🛒 Buy: {title}]]
- [[niches/{industry-id}/{niche-id}/fix|🔧 Fix: {title}]]
```

---

## 9. Niche Build — `niches/{industry-id}/{niche-id}/build.md`

```markdown
# {Problem Title}

**Niche:** [[niches/{industry-id}/{niche-id}/profile|{Niche Name}]]
**Industry:** [[industries/{industry-id}|{Industry Name}]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** {What product capability doesn't exist today?}
**Tags:** {2-5 tags}

## The Problem
{2-3 sentences.}

## Why Nobody Has Built This
{2-3 sentences.}

## What to Build
{2-3 sentences.}

## Target Customer
{1-2 sentences.}

## Impact If Built
{1-2 sentences.}
```

---

## 10. Niche Buy — `niches/{industry-id}/{niche-id}/buy.md`

```markdown
# {Problem Title}

**Niche:** [[niches/{industry-id}/{niche-id}/profile|{Niche Name}]]
**Industry:** [[industries/{industry-id}|{Industry Name}]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** {Generic solution exists but doesn't fit this niche.}
**Tags:** {2-5 tags}

## The Problem
{2-3 sentences.}

## What Already Exists
{2-3 sentences.}

## The Customization Gap
{2-3 sentences.}

## Target Customer
{1-2 sentences.}

## Impact If Solved
{1-2 sentences.}
```

---

## 11. Niche Fix — `niches/{industry-id}/{niche-id}/fix.md`

```markdown
# {Problem Title}

**Niche:** [[niches/{industry-id}/{niche-id}/profile|{Niche Name}]]
**Industry:** [[industries/{industry-id}|{Industry Name}]]
**Type:** Fix (Pain Point)
**One-liner:** {What manual/broken process needs fixing?}
**Tags:** {2-5 tags}

## The Problem
{2-3 sentences.}

## Why It's Still Broken
{2-3 sentences.}

## What a Fix Looks Like
{2-3 sentences.}

## Who Feels the Pain
{1-2 sentences.}

## Impact If Fixed
{1-2 sentences.}
```

---

## 12. Learning Plan Files

See `CLAUDE.md` section "Learning Plans" for the 7-file plan structure under `problem-index/plans/{tag-id}/`.
