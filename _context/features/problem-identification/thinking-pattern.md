# Problem Identification — How to Execute

## Step 1: Identify the Tacit Knowledge ML Opportunity

DO this FIRST for every industry. This is the highest-priority concept in the project.

ASK: "What does an experienced worker in this industry know that they cannot write a specification for?"

Tacit knowledge exists in EVERY industry — not just trades. Three categories:

1. **Physical/sensory** (trades, manufacturing, agriculture, clinical care) — pattern recognition through sight, sound, touch, smell
2. **Knowledge-work** (recruiting, consulting, sales, IT, finance) — pattern recognition through repeated exposure to cases, clients, deals, tickets, outcomes
3. **Transactional/retail** (dealers, buyers, merchandisers) — pricing intuition, demand sensing, customer read, inventory judgment

**The common thread: "I just know" or "you develop a feel for it" = ML target.**

DECIDE: Is this the most transformative opportunity in the industry?
- IF YES → make it the `high-impact.md` problem
- IF NO → list it first in `ml-opportunity.md`
- Industries marked `← HIGH tacit knowledge ML potential` → it MUST be strongly considered for `high-impact.md`

For tacit knowledge entries, WRITE an expanded "Why It's Hard" section covering:
- **Data collection challenge:** you have to capture the expert performing the task
- **Labeling challenge:** the expert may not agree with themselves
- **Deployment challenge:** it must be faster than the expert to be adopted

## Step 2: Walk Through a Worker's Day

DO this to identify the remaining 4 problems. Walk the timeline:

1. **Morning** — what administrative burden starts the day? → often a worker-life problem
2. **Core work** — what's the hardest judgment call? → often the high-impact or tacit knowledge opportunity
3. **Handoffs** — where do things fall through cracks between systems or people? → often a low-impact/customization gap
4. **End of day** — what reporting or compliance burden exists? → often a low-impact or worker-life problem
5. **Over time** — what expertise is lost when experienced workers leave? → the tacit knowledge angle

## Step 3: Verify Distinctness

CHECK every pair of problems before writing:

- Two low-impact problems: DO they target **different workflows**? "Scheduling" and "appointment management" is the SAME workflow. FAIL.
- Two worker-life problems: DO they target **different pain points**? "Documentation burden" twice with different framing is the SAME pain. FAIL.
- High-impact vs. low-impacts: IS the high-impact structurally different? It transforms; they customize. IF they're the same type of opportunity → reclassify.

## Step 4: Write ML Opportunity Entries

For each of the 4-5 entries, INCLUDE all of these fields — no exceptions:

1. **Problem statement** — what are we predicting and why does it matter?
2. **ML task** — classification, regression, detection, etc.
3. **Input data** — what goes in, what format, where does it come from?
4. **Target** — what exactly does the model output?
5. **Evaluation metric** — primary metric with justification (e.g., recall > precision for safety-critical)
6. **Scope** — honest assessment of build effort, team size, timeline
7. **Data availability** — the hardest part. Who has the data? What labeling is needed?

**IF you find yourself writing "patient data" instead of "Structured EHR fields (vitals, medications, diagnoses) + free-text nursing notes from past 6 visits" → STOP. Be specific.**

## Step 5: Write AI Agent/Platform Entries

For each of the 3-4 entries, ASK:

- What multi-step workflow could an LLM-powered agent handle autonomously?
- What vertical platform could aggregate data + workflow + intelligence?
- What recent capability (cheap inference, tool use, multimodal) makes this buildable NOW?

Each entry MUST be a distinct product concept — not a rephrasing of another entry.

## Failure Modes

- **IF you catch yourself writing vague problems** → STOP. Name the workflow, the person, the tool, and the consequence. "Improves efficiency" is always wrong.
- **IF two problems feel similar** → STOP. Ask "would the same product solve both?" If yes, they're the same problem.
- **IF your ML entries lack data specifics** → STOP. An ML engineer must be able to scope a project from the entry alone.
- **IF you forgot tacit knowledge** → STOP. Go back to Step 1. Every industry has it. No exceptions.
