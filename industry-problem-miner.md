# Industry Problem Miner — TypeScript Codebase Setup

A pipeline that ingests signals from 150+ industries, extracts recurring pain patterns, scores them against an engineering filter, and generates debate-style problem statements.

---

## Table of Contents

1. [Project Structure](#project-structure)
2. [Prerequisites](#prerequisites)
3. [Initial Setup](#initial-setup)
4. [Environment Configuration](#environment-configuration)
5. [Stage 1 — Industry Seed List](#stage-1--industry-seed-list)
6. [Stage 2 — Signal Collection](#stage-2--signal-collection)
7. [Stage 3 — Pain Extraction](#stage-3--pain-extraction)
8. [Stage 4 — Engineering Filter Scoring](#stage-4--engineering-filter-scoring)
9. [Stage 5 — Debate Engine](#stage-5--debate-engine)
10. [Orchestrator](#orchestrator)
11. [Running the Pipeline](#running-the-pipeline)
12. [Industry Seed List](#industry-seed-list)

---

## Project Structure

```
industry-problem-miner/
├── src/
│   ├── stages/
│   │   ├── stage1-industries.ts       # Industry seed list loader
│   │   ├── stage2-signals.ts          # Signal collection (Reddit, G2, job posts)
│   │   ├── stage3-extraction.ts       # LLM pain extraction
│   │   ├── stage4-scoring.ts          # Engineering filter scoring
│   │   └── stage5-debate.ts           # Two-agent debate engine
│   ├── data/
│   │   └── industries.ts              # The curated industry list
│   ├── types/
│   │   └── index.ts                   # Shared TypeScript interfaces
│   ├── utils/
│   │   ├── llm.ts                     # Anthropic API wrapper
│   │   ├── scraper.ts                 # HTTP + rate limiting utilities
│   │   └── storage.ts                 # JSON persistence layer
│   └── orchestrator.ts                # Main pipeline runner
├── output/
│   ├── signals/                       # Raw collected signals per industry
│   ├── pain-statements/               # Extracted pain patterns
│   ├── scores/                        # Engineering filter scores
│   └── debates/                       # Final debate outputs
├── .env
├── package.json
└── tsconfig.json
```

---

## Prerequisites

- Node.js >= 20
- npm >= 9
- An Anthropic API key
- A Reddit API key (free — create an app at reddit.com/prefs/apps)
- Optional: ScraperAPI or Bright Data key for G2/Capterra

---

## Initial Setup

```bash
# Create project
mkdir industry-problem-miner && cd industry-problem-miner
npm init -y

# TypeScript + runtime
npm install -D typescript ts-node @types/node
npm install -D tsx                         # Fast TS runner, no compile step needed

# Core dependencies
npm install @anthropic-ai/sdk               # LLM calls
npm install axios                           # HTTP requests
npm install cheerio                         # HTML parsing
npm install p-limit                         # Concurrency control
npm install dotenv                          # Env vars
npm install zod                             # Runtime type validation

# Dev utilities
npm install -D @types/cheerio prettier eslint
```

---

## tsconfig.json

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "resolveJsonModule": true,
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

---

## package.json scripts

```json
{
  "scripts": {
    "start": "tsx src/orchestrator.ts",
    "stage1": "tsx src/stages/stage1-industries.ts",
    "stage2": "tsx src/stages/stage2-signals.ts",
    "stage3": "tsx src/stages/stage3-extraction.ts",
    "stage4": "tsx src/stages/stage4-scoring.ts",
    "stage5": "tsx src/stages/stage5-debate.ts",
    "typecheck": "tsc --noEmit"
  }
}
```

---

## Environment Configuration

```bash
# .env
ANTHROPIC_API_KEY=your_key_here
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=IndustryMiner/1.0
SCRAPER_API_KEY=optional_for_g2_capterra

# Pipeline controls
MAX_INDUSTRIES_PER_RUN=10              # Process in batches
SIGNALS_PER_INDUSTRY=50               # Cap signals per source
CONCURRENCY_LIMIT=3                   # Parallel requests
```

---

## Shared Types

```typescript
// src/types/index.ts

export interface Industry {
  id: string;
  name: string;
  category: string;
  subreddits: string[];
  g2Categories: string[];
  jobKeywords: string[];
}

export interface Signal {
  industryId: string;
  source: "reddit" | "g2" | "capterra" | "jobs";
  content: string;
  url?: string;
  score?: number;               // Reddit upvotes or review stars
  collectedAt: string;
}

export interface PainStatement {
  industryId: string;
  statement: string;
  frequency: "common" | "occasional" | "rare";
  currentSolution: string;      // What people do today (spreadsheet, VA, etc.)
  signals: string[];            // Source excerpts that led to this
}

export interface EngineeringScore {
  industryId: string;
  painStatement: string;
  isRepetitiveAndStructured: number;   // 0-10
  hasDataComponent: number;            // 0-10 (transform, classify, predict, generate)
  currentSolutionIsBad: number;        // 0-10
  totalScore: number;
  reasoning: string;
}

export interface DebateResult {
  industryId: string;
  painStatement: string;
  engineeringScore: number;
  bullCase: string;
  bearCase: string;
  verdict: string;
  worthPursuing: boolean;
}
```

---

## LLM Utility Wrapper

```typescript
// src/utils/llm.ts
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY });

export async function callLLM(
  systemPrompt: string,
  userMessage: string,
  maxTokens = 2000
): Promise<string> {
  const response = await client.messages.create({
    model: "claude-opus-4-5",
    max_tokens: maxTokens,
    system: systemPrompt,
    messages: [{ role: "user", content: userMessage }],
  });

  const block = response.content[0];
  if (block.type !== "text") throw new Error("Unexpected response type");
  return block.text;
}

export async function callLLMJson<T>(
  systemPrompt: string,
  userMessage: string,
  maxTokens = 2000
): Promise<T> {
  const raw = await callLLM(systemPrompt, userMessage, maxTokens);
  const cleaned = raw.replace(/```json\n?|```/g, "").trim();
  return JSON.parse(cleaned) as T;
}
```

---

## Storage Utility

```typescript
// src/utils/storage.ts
import fs from "fs/promises";
import path from "path";

export async function saveJson(filePath: string, data: unknown): Promise<void> {
  await fs.mkdir(path.dirname(filePath), { recursive: true });
  await fs.writeFile(filePath, JSON.stringify(data, null, 2), "utf-8");
}

export async function loadJson<T>(filePath: string): Promise<T | null> {
  try {
    const raw = await fs.readFile(filePath, "utf-8");
    return JSON.parse(raw) as T;
  } catch {
    return null;
  }
}

export async function appendJson<T>(filePath: string, item: T): Promise<void> {
  const existing = (await loadJson<T[]>(filePath)) ?? [];
  existing.push(item);
  await saveJson(filePath, existing);
}
```

---

## Stage 1 — Industry Seed List

```typescript
// src/stages/stage1-industries.ts
import "dotenv/config";
import { industries } from "../data/industries.js";
import { saveJson } from "../utils/storage.js";

export async function runStage1(): Promise<void> {
  console.log(`Loaded ${industries.length} industries`);

  // Filter out excluded categories
  const excluded = ["adult", "gambling", "alcohol", "music", "brewery"];
  const filtered = industries.filter(
    (ind) => !excluded.some((ex) => ind.category.toLowerCase().includes(ex))
  );

  console.log(`After exclusions: ${filtered.length} industries`);
  await saveJson("output/stage1-industries.json", filtered);
  console.log("Stage 1 complete → output/stage1-industries.json");
}

runStage1();
```

---

## Stage 2 — Signal Collection

```typescript
// src/stages/stage2-signals.ts
import "dotenv/config";
import axios from "axios";
import pLimit from "p-limit";
import { loadJson, saveJson } from "../utils/storage.js";
import type { Industry, Signal } from "../types/index.js";

const limit = pLimit(Number(process.env.CONCURRENCY_LIMIT ?? 3));

// --- Reddit OAuth ---
async function getRedditToken(): Promise<string> {
  const res = await axios.post(
    "https://www.reddit.com/api/v1/access_token",
    "grant_type=client_credentials",
    {
      auth: {
        username: process.env.REDDIT_CLIENT_ID!,
        password: process.env.REDDIT_CLIENT_SECRET!,
      },
      headers: { "User-Agent": process.env.REDDIT_USER_AGENT },
    }
  );
  return res.data.access_token;
}

async function fetchRedditSignals(
  industry: Industry,
  token: string
): Promise<Signal[]> {
  const signals: Signal[] = [];
  const searchTerms = ["hate", "annoying", "broken", "wish", "pain", "manual"];

  for (const subreddit of industry.subreddits.slice(0, 2)) {
    for (const term of searchTerms.slice(0, 3)) {
      try {
        const res = await axios.get(
          `https://oauth.reddit.com/r/${subreddit}/search`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
              "User-Agent": process.env.REDDIT_USER_AGENT,
            },
            params: { q: term, limit: 10, sort: "relevance", t: "year" },
          }
        );

        const posts = res.data?.data?.children ?? [];
        for (const post of posts) {
          const { selftext, title, score, permalink } = post.data;
          if (selftext && selftext.length > 100) {
            signals.push({
              industryId: industry.id,
              source: "reddit",
              content: `${title}\n\n${selftext}`.slice(0, 1000),
              url: `https://reddit.com${permalink}`,
              score,
              collectedAt: new Date().toISOString(),
            });
          }
        }

        await sleep(500); // Be polite to Reddit
      } catch (err) {
        console.warn(`Reddit error for ${subreddit}/${term}:`, err);
      }
    }
  }

  return signals;
}

function sleep(ms: number) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

export async function runStage2(): Promise<void> {
  const industries = await loadJson<Industry[]>("output/stage1-industries.json");
  if (!industries) throw new Error("Run stage 1 first");

  const token = await getRedditToken();
  const maxIndustries = Number(process.env.MAX_INDUSTRIES_PER_RUN ?? 10);
  const batch = industries.slice(0, maxIndustries);

  const tasks = batch.map((industry) =>
    limit(async () => {
      console.log(`Collecting signals: ${industry.name}`);
      const signals = await fetchRedditSignals(industry, token);
      await saveJson(`output/signals/${industry.id}.json`, signals);
      console.log(`  → ${signals.length} signals collected`);
    })
  );

  await Promise.all(tasks);
  console.log("Stage 2 complete → output/signals/");
}

runStage2();
```

---

## Stage 3 — Pain Extraction

```typescript
// src/stages/stage3-extraction.ts
import "dotenv/config";
import fs from "fs/promises";
import { loadJson, saveJson } from "../utils/storage.js";
import { callLLMJson } from "../utils/llm.js";
import type { Industry, Signal, PainStatement } from "../types/index.js";

const SYSTEM_PROMPT = `You are a pain pattern analyst. Given a set of raw signals from an industry (Reddit posts, reviews, job listings), extract recurring friction points.

Return a JSON array of pain statements. Each object must have:
- statement: a clear, specific description of the pain (1-2 sentences)
- frequency: "common" | "occasional" | "rare"  
- currentSolution: what people currently do to deal with this (e.g. "manual spreadsheet", "no solution", "expensive consultant")
- signals: array of 2-3 short excerpts from the input that support this

Only extract SPECIFIC, REPEATABLE process pains. Ignore vague complaints. Focus on things that sound like work someone does over and over again.`;

export async function runStage3(): Promise<void> {
  const industries = await loadJson<Industry[]>("output/stage1-industries.json");
  if (!industries) throw new Error("Run stage 1 first");

  const signalFiles = await fs.readdir("output/signals").catch(() => []);

  for (const file of signalFiles) {
    const industryId = file.replace(".json", "");
    const industry = industries.find((i) => i.id === industryId);
    if (!industry) continue;

    const signals = await loadJson<Signal[]>(`output/signals/${file}`);
    if (!signals || signals.length === 0) continue;

    console.log(`Extracting pain: ${industry.name} (${signals.length} signals)`);

    const signalText = signals
      .slice(0, 30)
      .map((s, i) => `[${i + 1}] ${s.content}`)
      .join("\n\n---\n\n");

    try {
      const painStatements = await callLLMJson<PainStatement[]>(
        SYSTEM_PROMPT,
        `Industry: ${industry.name}\n\nSignals:\n${signalText}`
      );

      const withId = painStatements.map((p) => ({ ...p, industryId }));
      await saveJson(`output/pain-statements/${industryId}.json`, withId);
      console.log(`  → ${painStatements.length} pain statements extracted`);
    } catch (err) {
      console.error(`  Extraction failed for ${industry.name}:`, err);
    }
  }

  console.log("Stage 3 complete → output/pain-statements/");
}

runStage3();
```

---

## Stage 4 — Engineering Filter Scoring

```typescript
// src/stages/stage4-scoring.ts
import "dotenv/config";
import fs from "fs/promises";
import { loadJson, saveJson } from "../utils/storage.js";
import { callLLMJson } from "../utils/llm.js";
import type { PainStatement, EngineeringScore } from "../types/index.js";

const SYSTEM_PROMPT = `You are a machine learning engineer evaluating whether a business pain point is worth automating.

Score the following pain statement across three dimensions (0-10 each):

1. isRepetitiveAndStructured — Does the task happen frequently and follow a predictable pattern? Can it be described as an algorithm?
2. hasDataComponent — Does solving it require data transformation, classification, prediction, or generation? (ML sweet spot)
3. currentSolutionIsBad — How painful/expensive/slow is the current solution? (spreadsheet = 6, human VA = 7, nothing = 9, bad legacy software = 8)

Return JSON with: isRepetitiveAndStructured, hasDataComponent, currentSolutionIsBad, totalScore (sum), reasoning (2-3 sentences explaining your scores).`;

export async function runStage4(): Promise<void> {
  const files = await fs.readdir("output/pain-statements").catch(() => []);
  const allScores: EngineeringScore[] = [];

  for (const file of files) {
    const statements = await loadJson<PainStatement[]>(
      `output/pain-statements/${file}`
    );
    if (!statements) continue;

    console.log(`Scoring: ${file} (${statements.length} statements)`);

    for (const statement of statements) {
      try {
        const score = await callLLMJson<Omit<EngineeringScore, "industryId" | "painStatement">>(
          SYSTEM_PROMPT,
          `Pain statement: ${statement.statement}\nCurrent solution: ${statement.currentSolution}`
        );

        allScores.push({
          industryId: statement.industryId,
          painStatement: statement.statement,
          ...score,
        });
      } catch (err) {
        console.error("Scoring failed:", err);
      }
    }
  }

  // Sort by total score descending
  allScores.sort((a, b) => b.totalScore - a.totalScore);
  await saveJson("output/scores/all-scores.json", allScores);

  // Top 20
  const top20 = allScores.slice(0, 20);
  await saveJson("output/scores/top20.json", top20);

  console.log(`Stage 4 complete → Top score: ${allScores[0]?.totalScore}/30`);
  console.log("→ output/scores/");
}

runStage4();
```

---

## Stage 5 — Debate Engine

```typescript
// src/stages/stage5-debate.ts
import "dotenv/config";
import { loadJson, saveJson } from "../utils/storage.js";
import { callLLM } from "../utils/llm.js";
import type { EngineeringScore, DebateResult } from "../types/index.js";

const BULL_PROMPT = `You are an engineer who believes in building things. Your job is to make the strongest possible case for WHY this problem is worth solving. Focus on: technical feasibility, automation potential, scalability of a solution, and size of the problem. Be specific. 3-5 sentences.`;

const BEAR_PROMPT = `You are a pragmatic engineer who has been burned by bad bets. Your job is to argue why this problem is a TRAP — why it seems solvable but isn't, why the market won't pay, why the data is too messy, or why incumbents already solved it. Be specific. 3-5 sentences.`;

const VERDICT_PROMPT = `You are a senior engineer making a final call. You've heard both sides. Give a 2-3 sentence verdict: is this worth spending 2-4 weeks prototyping? Answer YES or NO and say why.`;

export async function runStage5(): Promise<void> {
  const top20 = await loadJson<EngineeringScore[]>("output/scores/top20.json");
  if (!top20) throw new Error("Run stage 4 first");

  const results: DebateResult[] = [];

  for (const item of top20) {
    console.log(`Debating: ${item.painStatement.slice(0, 60)}...`);

    const context = `Industry: ${item.industryId}\nProblem: ${item.painStatement}\nCurrent solution: mentioned in score\nEngineering score: ${item.totalScore}/30\nReasoning: ${item.reasoning}`;

    const [bullCase, bearCase] = await Promise.all([
      callLLM(BULL_PROMPT, context),
      callLLM(BEAR_PROMPT, context),
    ]);

    const verdict = await callLLM(
      VERDICT_PROMPT,
      `Bull case:\n${bullCase}\n\nBear case:\n${bearCase}\n\nProblem: ${item.painStatement}`
    );

    const worthPursuing =
      verdict.toLowerCase().includes("yes") &&
      !verdict.toLowerCase().startsWith("no");

    results.push({
      industryId: item.industryId,
      painStatement: item.painStatement,
      engineeringScore: item.totalScore,
      bullCase,
      bearCase,
      verdict,
      worthPursuing,
    });
  }

  const winners = results.filter((r) => r.worthPursuing);
  await saveJson("output/debates/all-debates.json", results);
  await saveJson("output/debates/winners.json", winners);

  console.log(
    `Stage 5 complete → ${winners.length}/${results.length} problems worth pursuing`
  );
  console.log("→ output/debates/");
}

runStage5();
```

---

## Orchestrator

```typescript
// src/orchestrator.ts
import "dotenv/config";
import { runStage1 } from "./stages/stage1-industries.js";
import { runStage2 } from "./stages/stage2-signals.js";
import { runStage3 } from "./stages/stage3-extraction.js";
import { runStage4 } from "./stages/stage4-scoring.js";
import { runStage5 } from "./stages/stage5-debate.js";

async function main() {
  console.log("=== INDUSTRY PROBLEM MINER ===\n");

  console.log("--- Stage 1: Loading industries ---");
  await runStage1();

  console.log("\n--- Stage 2: Collecting signals ---");
  await runStage2();

  console.log("\n--- Stage 3: Extracting pain statements ---");
  await runStage3();

  console.log("\n--- Stage 4: Engineering filter scoring ---");
  await runStage4();

  console.log("\n--- Stage 5: Debate engine ---");
  await runStage5();

  console.log("\n=== PIPELINE COMPLETE ===");
  console.log("Check output/debates/winners.json for actionable problems.");
}

main().catch(console.error);
```

> **Note on imports:** Stage files export their `run` functions. Remove the bare `runStageX()` call at the bottom of each file when using the orchestrator — or guard them with `if (process.argv[1] === fileURLToPath(import.meta.url))`.

---

## Running the Pipeline

```bash
# Full pipeline
npm start

# Run individual stages
npm run stage1
npm run stage2
npm run stage3
npm run stage4
npm run stage5

# Type check only
npm run typecheck
```

Output flows like this:

```
output/
├── stage1-industries.json        ← Filtered industry list
├── signals/
│   ├── healthcare-staffing.json  ← Raw signals per industry
│   └── ...
├── pain-statements/
│   ├── healthcare-staffing.json  ← Extracted pain patterns
│   └── ...
├── scores/
│   ├── all-scores.json           ← All scored problems
│   └── top20.json                ← Top 20 by engineering score
└── debates/
    ├── all-debates.json          ← Full debate transcripts
    └── winners.json              ← Problems worth pursuing
```

---

## Industry Seed List

> Curated list of 155 industries across 18 categories. Adult, gambling, alcohol/brewery, and music industries excluded. Each entry maps to real subreddits and signal sources.

```typescript
// src/data/industries.ts
import type { Industry } from "../types/index.js";

export const industries: Industry[] = [

  // ── HEALTHCARE & CLINICAL ───────────────────────────────────────────────
  { id: "behavioral-health-clinics", name: "Behavioral Health Clinics", category: "Healthcare", subreddits: ["therapists", "mentalhealth", "counselors"], g2Categories: ["mental-health"], jobKeywords: ["clinical documentation", "insurance billing"] },
  { id: "home-health-agencies", name: "Home Health Agencies", category: "Healthcare", subreddits: ["homehealth", "nursing", "cna"], g2Categories: ["home-health"], jobKeywords: ["visit scheduling", "care plan compliance"] },
  { id: "dental-practices", name: "Dental Practices", category: "Healthcare", subreddits: ["dentistry", "dentalassistant", "dentalhygiene"], g2Categories: ["dental"], jobKeywords: ["insurance claims", "patient scheduling"] },
  { id: "physical-therapy", name: "Physical Therapy Clinics", category: "Healthcare", subreddits: ["physicaltherapy", "DPT"], g2Categories: ["physical-therapy"], jobKeywords: ["prior authorization", "outcome tracking"] },
  { id: "medical-billing", name: "Medical Billing Companies", category: "Healthcare", subreddits: ["medicalbilling", "healthcareit"], g2Categories: ["medical-billing"], jobKeywords: ["claim denial", "ERA posting", "EOB processing"] },
  { id: "urgent-care", name: "Urgent Care Centers", category: "Healthcare", subreddits: ["urgentcare", "emergencymedicine"], g2Categories: ["urgent-care"], jobKeywords: ["patient flow", "triage documentation"] },
  { id: "veterinary-practices", name: "Veterinary Practices", category: "Healthcare", subreddits: ["veterinary", "vet", "vettech"], g2Categories: ["veterinary"], jobKeywords: ["appointment scheduling", "inventory management"] },
  { id: "pharmacy-independents", name: "Independent Pharmacies", category: "Healthcare", subreddits: ["pharmacy", "pharmacist"], g2Categories: ["pharmacy"], jobKeywords: ["prior auth", "drug interaction checking"] },

  // ── LEGAL ───────────────────────────────────────────────────────────────
  { id: "immigration-law", name: "Immigration Law Firms", category: "Legal", subreddits: ["immigration", "legaladvice", "immigrationlaw"], g2Categories: ["legal"], jobKeywords: ["form preparation", "case tracking", "deadline management"] },
  { id: "personal-injury-law", name: "Personal Injury Law Firms", category: "Legal", subreddits: ["personalinjury", "legaladvice"], g2Categories: ["legal"], jobKeywords: ["demand letter", "medical record review", "settlement tracking"] },
  { id: "estate-planning", name: "Estate Planning Attorneys", category: "Legal", subreddits: ["estateplanning", "personalfinance"], g2Categories: ["legal"], jobKeywords: ["document drafting", "trust administration"] },
  { id: "small-law-firms", name: "Small Law Firms (General)", category: "Legal", subreddits: ["lawfirm", "legaladvice", "paralegal"], g2Categories: ["legal-practice-management"], jobKeywords: ["time tracking", "billing", "document management"] },
  { id: "compliance-consulting", name: "Regulatory Compliance Consulting", category: "Legal", subreddits: ["compliance", "riskmanagement"], g2Categories: ["compliance"], jobKeywords: ["audit trail", "policy management", "reporting"] },

  // ── CONSTRUCTION & TRADES ───────────────────────────────────────────────
  { id: "general-contractors", name: "General Contractors", category: "Construction", subreddits: ["generalcontractor", "construction", "Homebuilding"], g2Categories: ["construction-management"], jobKeywords: ["subcontractor coordination", "change order", "lien waiver"] },
  { id: "electrical-contractors", name: "Electrical Contractors", category: "Construction", subreddits: ["electricians", "electrician"], g2Categories: ["field-service"], jobKeywords: ["permit tracking", "job costing", "scheduling"] },
  { id: "plumbing-contractors", name: "Plumbing Contractors", category: "Construction", subreddits: ["Plumbing", "plumbers"], g2Categories: ["field-service"], jobKeywords: ["service dispatch", "parts inventory", "invoicing"] },
  { id: "roofing-contractors", name: "Roofing Contractors", category: "Construction", subreddits: ["roofing", "Roofing"], g2Categories: ["field-service"], jobKeywords: ["estimate generation", "insurance supplement", "crew scheduling"] },
  { id: "hvac-contractors", name: "HVAC Contractors", category: "Construction", subreddits: ["HVAC", "hvacadvice"], g2Categories: ["field-service"], jobKeywords: ["preventive maintenance", "equipment tracking", "dispatch"] },
  { id: "landscaping", name: "Landscaping Companies", category: "Construction", subreddits: ["landscaping", "lawncare"], g2Categories: ["field-service"], jobKeywords: ["route optimization", "seasonal scheduling", "client billing"] },
  { id: "painting-contractors", name: "Painting Contractors", category: "Construction", subreddits: ["paint", "contractorUK"], g2Categories: ["field-service"], jobKeywords: ["estimate accuracy", "material ordering", "crew tracking"] },
  { id: "home-inspection", name: "Home Inspection Services", category: "Construction", subreddits: ["homeinspection", "FirstTimeHomeBuyer"], g2Categories: ["home-inspection"], jobKeywords: ["report generation", "photo documentation", "scheduling"] },

  // ── REAL ESTATE ─────────────────────────────────────────────────────────
  { id: "property-management", name: "Property Management Companies", category: "Real Estate", subreddits: ["PropertyManagement", "landlord", "realestateinvesting"], g2Categories: ["property-management"], jobKeywords: ["maintenance requests", "lease renewals", "rent collection"] },
  { id: "commercial-real-estate", name: "Commercial Real Estate Brokers", category: "Real Estate", subreddits: ["CommercialRealEstate", "realestate"], g2Categories: ["commercial-real-estate"], jobKeywords: ["lease abstraction", "deal tracking", "comp analysis"] },
  { id: "short-term-rentals", name: "Short-Term Rental Operators", category: "Real Estate", subreddits: ["airbnb", "vrbo", "ShortTermRentals"], g2Categories: ["vacation-rental"], jobKeywords: ["dynamic pricing", "channel management", "guest communication"] },
  { id: "real-estate-appraisers", name: "Real Estate Appraisers", category: "Real Estate", subreddits: ["appraisal", "realestate"], g2Categories: ["appraisal"], jobKeywords: ["comparable selection", "report writing", "AMC communication"] },
  { id: "hoa-management", name: "HOA Management Companies", category: "Real Estate", subreddits: ["HOA", "PropertyManagement"], g2Categories: ["hoa-management"], jobKeywords: ["violation tracking", "meeting minutes", "dues collection"] },

  // ── LOGISTICS & SUPPLY CHAIN ─────────────────────────────────────────────
  { id: "freight-brokerage", name: "Freight Brokerages", category: "Logistics", subreddits: ["FreightBrokers", "trucking", "logistics"], g2Categories: ["freight"], jobKeywords: ["carrier vetting", "load tracking", "rate negotiation"] },
  { id: "last-mile-delivery", name: "Last-Mile Delivery Companies", category: "Logistics", subreddits: ["logistics", "delivery", "supplychain"], g2Categories: ["fleet-management"], jobKeywords: ["route optimization", "proof of delivery", "exception handling"] },
  { id: "warehouse-3pl", name: "Third-Party Logistics (3PL)", category: "Logistics", subreddits: ["logistics", "supplychain", "warehouse"], g2Categories: ["warehouse-management"], jobKeywords: ["inventory accuracy", "pick-pack", "WMS integration"] },
  { id: "customs-brokers", name: "Customs Brokers", category: "Logistics", subreddits: ["importers", "logistics", "supplychain"], g2Categories: ["customs"], jobKeywords: ["HTS classification", "duty calculation", "CBP filing"] },
  { id: "cold-chain-logistics", name: "Cold Chain Logistics", category: "Logistics", subreddits: ["foodsafety", "logistics"], g2Categories: ["cold-chain"], jobKeywords: ["temperature monitoring", "compliance documentation", "carrier qualification"] },

  // ── MANUFACTURING & INDUSTRIAL ───────────────────────────────────────────
  { id: "contract-manufacturing", name: "Contract Manufacturers", category: "Manufacturing", subreddits: ["manufacturing", "machinists", "CNC"], g2Categories: ["manufacturing"], jobKeywords: ["quote generation", "capacity planning", "quality inspection"] },
  { id: "metal-fabrication", name: "Metal Fabrication Shops", category: "Manufacturing", subreddits: ["metalworking", "machinists", "welding"], g2Categories: ["manufacturing"], jobKeywords: ["material tracking", "job scheduling", "inspection records"] },
  { id: "food-manufacturing", name: "Food & Beverage Manufacturing", category: "Manufacturing", subreddits: ["foodscience", "foodmanufacturing"], g2Categories: ["food-manufacturing"], jobKeywords: ["batch records", "HACCP compliance", "supplier COA"] },
  { id: "medical-device-mfg", name: "Medical Device Manufacturing", category: "Manufacturing", subreddits: ["medicaldevices", "FDA"], g2Categories: ["quality-management"], jobKeywords: ["DHF documentation", "CAPA", "21 CFR Part 820"] },
  { id: "electronics-contract-mfg", name: "Electronics Contract Manufacturing", category: "Manufacturing", subreddits: ["electronics", "PCB", "manufacturing"], g2Categories: ["manufacturing"], jobKeywords: ["BOM management", "component sourcing", "test documentation"] },
  { id: "printing-shops", name: "Commercial Printing Shops", category: "Manufacturing", subreddits: ["printing", "graphicdesign"], g2Categories: ["print-management"], jobKeywords: ["job ticketing", "prepress proofing", "bindery scheduling"] },

  // ── AGRICULTURE & FOOD ──────────────────────────────────────────────────
  { id: "crop-farming", name: "Crop Farming Operations", category: "Agriculture", subreddits: ["farming", "agriculture", "crops"], g2Categories: ["agriculture"], jobKeywords: ["field scouting", "spray records", "yield tracking"] },
  { id: "livestock-operations", name: "Livestock Operations", category: "Agriculture", subreddits: ["farming", "livestock", "ranching"], g2Categories: ["agriculture"], jobKeywords: ["herd health records", "feed management", "breeding tracking"] },
  { id: "greenhouse-horticulture", name: "Greenhouse & Horticulture", category: "Agriculture", subreddits: ["horticulture", "greenhouse", "gardening"], g2Categories: ["agriculture"], jobKeywords: ["crop scheduling", "IPM records", "nutrient management"] },
  { id: "food-distributors", name: "Food Distributors", category: "Agriculture", subreddits: ["foodindustry", "supplychain"], g2Categories: ["distribution"], jobKeywords: ["order management", "expiry tracking", "route planning"] },
  { id: "restaurant-suppliers", name: "Restaurant Supply Companies", category: "Agriculture", subreddits: ["restaurantowners", "foodservice"], g2Categories: ["distribution"], jobKeywords: ["catalog management", "order processing", "delivery coordination"] },

  // ── PROFESSIONAL SERVICES ────────────────────────────────────────────────
  { id: "accounting-firms-smb", name: "SMB Accounting Firms", category: "Professional Services", subreddits: ["Accounting", "taxpros", "smallbusiness"], g2Categories: ["accounting"], jobKeywords: ["bookkeeping workflow", "tax prep", "client portal"] },
  { id: "staffing-agencies", name: "Staffing & Temp Agencies", category: "Professional Services", subreddits: ["recruiting", "humanresources", "staffing"], g2Categories: ["staffing"], jobKeywords: ["candidate matching", "timesheet management", "client billing"] },
  { id: "it-managed-services", name: "IT Managed Service Providers (MSPs)", category: "Professional Services", subreddits: ["msp", "sysadmin", "ITManagers"], g2Categories: ["it-management"], jobKeywords: ["ticket triage", "patch management", "client reporting"] },
  { id: "marketing-agencies-smb", name: "SMB Marketing Agencies", category: "Professional Services", subreddits: ["agency", "marketing", "PPC"], g2Categories: ["marketing"], jobKeywords: ["reporting automation", "client onboarding", "campaign tracking"] },
  { id: "engineering-consultants", name: "Engineering Consultants", category: "Professional Services", subreddits: ["civilengineering", "engineering", "consulting"], g2Categories: ["project-management"], jobKeywords: ["project tracking", "deliverable management", "timesheet"] },
  { id: "environmental-consultants", name: "Environmental Consultants", category: "Professional Services", subreddits: ["environmental", "sustainability", "geology"], g2Categories: ["environmental"], jobKeywords: ["field data collection", "regulatory reporting", "sample tracking"] },
  { id: "hr-consultants", name: "HR Consulting Firms", category: "Professional Services", subreddits: ["humanresources", "HRpros"], g2Categories: ["human-resources"], jobKeywords: ["policy documentation", "employee handbook", "compliance tracking"] },

  // ── RETAIL & E-COMMERCE ──────────────────────────────────────────────────
  { id: "independent-retailers", name: "Independent Retail Stores", category: "Retail", subreddits: ["retailhell", "smallbusiness", "entrepreneur"], g2Categories: ["retail"], jobKeywords: ["inventory management", "shrinkage tracking", "reorder points"] },
  { id: "ecommerce-sellers", name: "E-Commerce Sellers (Multi-channel)", category: "Retail", subreddits: ["ecommerce", "FulfillmentByAmazon", "Etsy"], g2Categories: ["ecommerce"], jobKeywords: ["listing management", "return processing", "repricing"] },
  { id: "auto-dealers-independent", name: "Independent Auto Dealers", category: "Retail", subreddits: ["askcarsales", "UsedCars", "cardealer"], g2Categories: ["automotive"], jobKeywords: ["inventory photos", "title processing", "floor plan tracking"] },
  { id: "specialty-food-retail", name: "Specialty Food Retail", category: "Retail", subreddits: ["cheesemaking", "butcher", "foodie"], g2Categories: ["retail"], jobKeywords: ["perishable inventory", "traceability", "label compliance"] },
  { id: "medical-supply-retail", name: "Medical Supply Distributors", category: "Retail", subreddits: ["medicalsupplies", "homehealth"], g2Categories: ["healthcare-distribution"], jobKeywords: ["insurance billing", "product expiration", "order tracking"] },

  // ── FINANCIAL SERVICES ───────────────────────────────────────────────────
  { id: "independent-insurance-agents", name: "Independent Insurance Agents", category: "Financial Services", subreddits: ["Insurance", "InsuranceAgent", "LifeInsurance"], g2Categories: ["insurance"], jobKeywords: ["quote comparison", "policy renewal", "claims follow-up"] },
  { id: "mortgage-brokers", name: "Mortgage Brokers", category: "Financial Services", subreddits: ["Mortgages", "RealEstate", "FirstTimeHomeBuyer"], g2Categories: ["mortgage"], jobKeywords: ["document collection", "pipeline tracking", "rate lock management"] },
  { id: "wealth-management-rias", name: "Registered Investment Advisors (RIAs)", category: "Financial Services", subreddits: ["financialplanning", "CFP", "investing"], g2Categories: ["wealth-management"], jobKeywords: ["rebalancing", "client reporting", "compliance documentation"] },
  { id: "credit-unions", name: "Credit Unions", category: "Financial Services", subreddits: ["CreditUnions", "personalfinance"], g2Categories: ["banking"], jobKeywords: ["loan origination", "member onboarding", "regulatory reporting"] },
  { id: "tax-prep-firms", name: "Tax Preparation Firms", category: "Financial Services", subreddits: ["taxpros", "tax", "Accounting"], g2Categories: ["tax"], jobKeywords: ["document gathering", "return assembly", "e-filing workflow"] },
  { id: "collections-agencies", name: "Debt Collection Agencies", category: "Financial Services", subreddits: ["collections", "debtcollection"], g2Categories: ["collections"], jobKeywords: ["skip tracing", "payment plan tracking", "compliance logging (FDCPA)"] },

  // ── EDUCATION ───────────────────────────────────────────────────────────
  { id: "k12-private-schools", name: "Private K-12 Schools", category: "Education", subreddits: ["Teachers", "education", "k12"], g2Categories: ["education"], jobKeywords: ["admissions tracking", "tuition billing", "academic reporting"] },
  { id: "tutoring-centers", name: "Tutoring Centers & Learning Studios", category: "Education", subreddits: ["tutoring", "Teachers", "learnmath"], g2Categories: ["tutoring"], jobKeywords: ["session scheduling", "progress tracking", "billing"] },
  { id: "vocational-schools", name: "Vocational & Trade Schools", category: "Education", subreddits: ["vocational", "tradeSchool"], g2Categories: ["education"], jobKeywords: ["enrollment management", "accreditation compliance", "placement tracking"] },
  { id: "corporate-training", name: "Corporate Training Providers", category: "Education", subreddits: ["instructionaldesign", "elearning", "training"], g2Categories: ["learning-management"], jobKeywords: ["course completion tracking", "certification management", "content updates"] },
  { id: "language-schools", name: "Language Schools & ESL Programs", category: "Education", subreddits: ["languagelearning", "TEFL", "ESL"], g2Categories: ["education"], jobKeywords: ["level assessment", "attendance tracking", "curriculum scheduling"] },
  { id: "childcare-centers", name: "Childcare & Daycare Centers", category: "Education", subreddits: ["ECEProfessionals", "childcare", "Daycare"], g2Categories: ["childcare"], jobKeywords: ["attendance tracking", "licensing compliance", "parent communication"] },

  // ── HOSPITALITY & FOOD SERVICE ───────────────────────────────────────────
  { id: "independent-restaurants", name: "Independent Restaurants", category: "Hospitality", subreddits: ["restaurantowners", "KitchenConfidential", "Serverlife"], g2Categories: ["restaurant-management"], jobKeywords: ["food cost tracking", "labor scheduling", "waste logging"] },
  { id: "catering-companies", name: "Catering Companies", category: "Hospitality", subreddits: ["catering", "weddingplanning", "chef"], g2Categories: ["catering"], jobKeywords: ["event BEO management", "staffing", "menu costing"] },
  { id: "hotels-boutique", name: "Boutique Hotels & Inns", category: "Hospitality", subreddits: ["hotel", "hotelpros", "HotelManagement"], g2Categories: ["hotel-management"], jobKeywords: ["revenue management", "housekeeping coordination", "OTA channel management"] },
  { id: "food-trucks", name: "Food Truck Operators", category: "Hospitality", subreddits: ["foodtrucks", "restaurantowners"], g2Categories: ["restaurant-management"], jobKeywords: ["event booking", "permitting", "inventory restocking"] },
  { id: "coffee-shops-independent", name: "Independent Coffee Shops", category: "Hospitality", subreddits: ["barista", "Coffee", "smallbusiness"], g2Categories: ["pos"], jobKeywords: ["inventory tracking", "staff scheduling", "wholesale ordering"] },

  // ── TRANSPORTATION ───────────────────────────────────────────────────────
  { id: "owner-operator-trucking", name: "Owner-Operator Trucking", category: "Transportation", subreddits: ["Truckers", "trucking", "FreightBrokers"], g2Categories: ["fleet-management"], jobKeywords: ["IFTA reporting", "load board", "ELD compliance"] },
  { id: "towing-companies", name: "Towing Companies", category: "Transportation", subreddits: ["towing", "Tow_Trucks"], g2Categories: ["field-service"], jobKeywords: ["dispatch", "impound tracking", "insurance billing"] },
  { id: "moving-companies", name: "Moving & Storage Companies", category: "Transportation", subreddits: ["moving", "moveradvice"], g2Categories: ["moving"], jobKeywords: ["quote estimation", "crew scheduling", "claims management"] },
  { id: "charter-bus-operators", name: "Charter Bus Operators", category: "Transportation", subreddits: ["motorcoach", "transportation"], g2Categories: ["fleet-management"], jobKeywords: ["trip scheduling", "driver compliance (CDL/DOT)", "passenger manifest"] },
  { id: "non-emergency-medical-transport", name: "Non-Emergency Medical Transport (NEMT)", category: "Transportation", subreddits: ["healthcare", "medicaltransport"], g2Categories: ["medical-transport"], jobKeywords: ["Medicaid billing", "trip assignment", "driver compliance"] },

  // ── ENERGY & UTILITIES ───────────────────────────────────────────────────
  { id: "solar-installers", name: "Residential Solar Installers", category: "Energy", subreddits: ["solar", "solarenergy", "solarpanels"], g2Categories: ["solar"], jobKeywords: ["permit coordination", "utility interconnection", "install scheduling"] },
  { id: "energy-auditors", name: "Energy Auditing Firms", category: "Energy", subreddits: ["EnergyAuditing", "sustainability", "HVAC"], g2Categories: ["energy-management"], jobKeywords: ["audit report generation", "incentive identification", "blower door data"] },
  { id: "utility-contractors", name: "Utility Contractors (Gas/Water/Telecom)", category: "Energy", subreddits: ["construction", "utilities"], g2Categories: ["field-service"], jobKeywords: ["as-built documentation", "permit tracking", "field inspection logs"] },
  { id: "oil-gas-field-services", name: "Oil & Gas Field Services", category: "Energy", subreddits: ["oilfield", "PetroleumEngineers"], g2Categories: ["oil-gas"], jobKeywords: ["well log data", "daily reporting", "compliance (OSHA/EPA)"] },

  // ── TECHNOLOGY / SAAS ────────────────────────────────────────────────────
  { id: "it-staffing-firms", name: "IT Staffing Firms", category: "Technology", subreddits: ["recruiting", "cscareerquestions", "sysadmin"], g2Categories: ["staffing"], jobKeywords: ["candidate pipeline", "SOW tracking", "timesheet approval"] },
  { id: "software-dev-agencies", name: "Software Development Agencies", category: "Technology", subreddits: ["webdev", "freelance", "agency"], g2Categories: ["project-management"], jobKeywords: ["project scoping", "client reporting", "resource allocation"] },
  { id: "cybersecurity-mssp", name: "Cybersecurity MSSPs", category: "Technology", subreddits: ["netsec", "cybersecurity", "msp"], g2Categories: ["cybersecurity"], jobKeywords: ["alert triage", "client reporting", "vulnerability tracking"] },
  { id: "data-analytics-consultants", name: "Data & Analytics Consultants", category: "Technology", subreddits: ["datascience", "analytics", "BusinessIntelligence"], g2Categories: ["analytics"], jobKeywords: ["data pipeline documentation", "client dashboarding", "data quality QA"] },
  { id: "cloud-infrastructure-consultants", name: "Cloud Infrastructure Consultants", category: "Technology", subreddits: ["aws", "devops", "cloudcomputing"], g2Categories: ["cloud"], jobKeywords: ["cost optimization", "architecture review", "runbook documentation"] },

  // ── NONPROFIT & GOVERNMENT ───────────────────────────────────────────────
  { id: "nonprofits-social-services", name: "Social Services Nonprofits", category: "Nonprofit", subreddits: ["nonprofit", "socialwork", "socialjustice"], g2Categories: ["nonprofit"], jobKeywords: ["grant reporting", "case management", "volunteer coordination"] },
  { id: "faith-organizations", name: "Religious Organizations & Churches", category: "Nonprofit", subreddits: ["churchplanting", "ministry", "pastors"], g2Categories: ["church-management"], jobKeywords: ["member database", "donation tracking", "volunteer scheduling"] },
  { id: "trade-associations", name: "Trade Associations & Chambers", category: "Nonprofit", subreddits: ["associations", "nonprofit"], g2Categories: ["association-management"], jobKeywords: ["membership renewal", "event management", "certification tracking"] },
  { id: "municipal-services", name: "Municipal Government Services", category: "Government", subreddits: ["localgovernment", "municipalfinance"], g2Categories: ["government"], jobKeywords: ["permit issuance", "inspection scheduling", "public records management"] },

  // ── MEDIA & PUBLISHING ───────────────────────────────────────────────────
  { id: "independent-publishers", name: "Independent Book Publishers", category: "Media", subreddits: ["selfpublish", "publishing", "writing"], g2Categories: ["publishing"], jobKeywords: ["rights management", "royalty tracking", "metadata distribution"] },
  { id: "podcasting-networks", name: "Podcast Networks & Producers", category: "Media", subreddits: ["podcasting", "podcasts", "audioengineering"], g2Categories: ["podcast"], jobKeywords: ["episode production workflow", "guest booking", "ad insertion tracking"] },
  { id: "video-production-smb", name: "SMB Video Production Companies", category: "Media", subreddits: ["videography", "filmmakers", "weddingvideography"], g2Categories: ["video-production"], jobKeywords: ["project milestone tracking", "asset delivery", "client feedback collection"] },
  { id: "news-media-local", name: "Local News & Digital Media Outlets", category: "Media", subreddits: ["journalism", "localnews"], g2Categories: ["content-management"], jobKeywords: ["editorial calendar", "freelancer management", "content distribution"] },

  // ── SPORTS & FITNESS ────────────────────────────────────────────────────
  { id: "gyms-independent", name: "Independent Gyms & Fitness Studios", category: "Fitness", subreddits: ["gymowner", "personaltraining", "fitness"], g2Categories: ["fitness"], jobKeywords: ["member management", "class scheduling", "retention campaigns"] },
  { id: "personal-trainers", name: "Personal Trainers & Coaches", category: "Fitness", subreddits: ["personaltraining", "fitness", "ptuk"], g2Categories: ["fitness"], jobKeywords: ["client progress tracking", "program design", "scheduling & billing"] },
  { id: "youth-sports-orgs", name: "Youth Sports Organizations", category: "Fitness", subreddits: ["youth_sports", "coaching", "soccer"], g2Categories: ["sports-management"], jobKeywords: ["registration management", "scheduling", "volunteer coordination"] },

  // ── AUTOMOTIVE ──────────────────────────────────────────────────────────
  { id: "auto-repair-shops", name: "Independent Auto Repair Shops", category: "Automotive", subreddits: ["AskMechanics", "MechanicAdvice", "AutoRepair"], g2Categories: ["auto-repair"], jobKeywords: ["labor time tracking", "parts ordering", "warranty claims"] },
  { id: "auto-body-shops", name: "Auto Body & Collision Shops", category: "Automotive", subreddits: ["autobody", "Autobody_Refinishing"], g2Categories: ["auto-repair"], jobKeywords: ["insurance supplement writing", "parts procurement", "photo documentation"] },
  { id: "fleet-managers", name: "Corporate Fleet Management", category: "Automotive", subreddits: ["fleetmanagement", "fleet"], g2Categories: ["fleet-management"], jobKeywords: ["preventive maintenance scheduling", "fuel tracking", "driver compliance"] },
  { id: "rv-dealerships", name: "RV & Powersports Dealerships", category: "Automotive", subreddits: ["RVs", "RVliving", "powersports"], g2Categories: ["automotive"], jobKeywords: ["floor plan tracking", "PDI checklist", "warranty registration"] },

  // ── SPECIALTY SERVICES ───────────────────────────────────────────────────
  { id: "cleaning-companies", name: "Commercial & Residential Cleaning Companies", category: "Specialty Services", subreddits: ["cleaning", "CommercialCleaning", "housekeeping"], g2Categories: ["field-service"], jobKeywords: ["route optimization", "inspection checklists", "client retention"] },
  { id: "pest-control", name: "Pest Control Companies", category: "Specialty Services", subreddits: ["pestcontrol", "PestControl"], g2Categories: ["field-service"], jobKeywords: ["treatment records", "chemical usage logs", "scheduling routes"] },
  { id: "security-guard-firms", name: "Private Security Guard Companies", category: "Specialty Services", subreddits: ["SecurityGuards", "physicalsecurity"], g2Categories: ["security"], jobKeywords: ["guard tour verification", "incident reporting", "shift scheduling"] },
  { id: "event-planning", name: "Event Planning Companies", category: "Specialty Services", subreddits: ["eventplanning", "weddingplanning", "eventprofs"], g2Categories: ["event-management"], jobKeywords: ["vendor coordination", "timeline management", "budget tracking"] },
  { id: "tattoo-studios", name: "Tattoo Studios", category: "Specialty Services", subreddits: ["tattoo", "TattooArtists"], g2Categories: ["appointment-scheduling"], jobKeywords: ["deposit tracking", "consent form management", "artist portfolio management"] },
  { id: "funeral-homes", name: "Funeral Homes & Crematories", category: "Specialty Services", subreddits: ["funeralhomes", "DeathCare"], g2Categories: ["funeral"], jobKeywords: ["case file management", "death certificate filing", "preneed contract tracking"] },
  { id: "pet-services", name: "Pet Boarding & Grooming Services", category: "Specialty Services", subreddits: ["doggrooming", "petsitting", "Dogtraining"], g2Categories: ["pet-care"], jobKeywords: ["vaccination record tracking", "appointment scheduling", "client communication"] },
  { id: "alterations-tailoring", name: "Alterations & Tailoring Shops", category: "Specialty Services", subreddits: ["tailors", "sewing", "alterations"], g2Categories: ["appointment-scheduling"], jobKeywords: ["order tracking", "pickup reminders", "measurement records"] },

  // ── INSURANCE (OPERATIONS) ───────────────────────────────────────────────
  { id: "insurance-tpa", name: "Third-Party Administrators (TPAs)", category: "Insurance", subreddits: ["Insurance", "workcomp", "benefitsadmin"], g2Categories: ["insurance"], jobKeywords: ["claims adjudication", "eligibility verification", "provider credentialing"] },
  { id: "public-adjusters", name: "Public Adjusters", category: "Insurance", subreddits: ["Insurance", "homeowners"], g2Categories: ["insurance"], jobKeywords: ["damage documentation", "estimate preparation", "claim supplement tracking"] },
  { id: "insurance-restoration", name: "Insurance Restoration Contractors", category: "Insurance", subreddits: ["roofing", "waterdamage", "restorationcontractors"], g2Categories: ["construction-management"], jobKeywords: ["xactimate writing", "photo documentation", "supplement negotiation"] },

  // ── WELLNESS & PERSONAL CARE ─────────────────────────────────────────────
  { id: "chiropractic-practices", name: "Chiropractic Practices", category: "Wellness", subreddits: ["chiropractic", "ChiropracticAdvice"], g2Categories: ["chiropractic"], jobKeywords: ["SOAP note documentation", "insurance billing", "patient recall"] },
  { id: "acupuncture-practices", name: "Acupuncture & Integrative Health", category: "Wellness", subreddits: ["acupuncture", "ChineseHerbalMedicine"], g2Categories: ["healthcare"], jobKeywords: ["intake forms", "insurance verification", "treatment planning"] },
  { id: "med-spas", name: "Medical Spas", category: "Wellness", subreddits: ["aesthetics", "medispa", "skincare"], g2Categories: ["spa-management"], jobKeywords: ["consent form management", "appointment booking", "before-after photo tracking"] },
  { id: "hair-salons-independent", name: "Independent Hair Salons & Barbershops", category: "Wellness", subreddits: ["hairstylist", "barber", "Barber"], g2Categories: ["salon-management"], jobKeywords: ["appointment no-show", "retail inventory", "client history tracking"] },

  // ── GOVERNMENT-ADJACENT ──────────────────────────────────────────────────
  { id: "grant-writers", name: "Grant Writing Consultants", category: "Government-Adjacent", subreddits: ["grantwriting", "nonprofit"], g2Categories: ["project-management"], jobKeywords: ["deadline tracking", "narrative templates", "reporting compliance"] },
  { id: "public-defenders", name: "Public Defender Offices", category: "Government-Adjacent", subreddits: ["PublicDefenders", "legaladvice", "law"], g2Categories: ["legal"], jobKeywords: ["case load management", "court date tracking", "discovery management"] },
  { id: "land-surveyors", name: "Land Surveying Companies", category: "Government-Adjacent", subreddits: ["Surveying", "landsurveyors"], g2Categories: ["survey"], jobKeywords: ["CAD deliverable management", "permit coordination", "field note digitization"] },

];
```

---

## What to Build Next

Once Stage 1 runs cleanly, Stage 2 is where the ML learning begins in earnest. You'll start hitting real engineering problems:

- **Rate limiting** — Reddit, G2, and job boards all throttle. This forces you to design a robust retry/queue system.
- **Data cleaning** — raw signals are noisy. You'll write text preprocessing pipelines.
- **Embeddings** — once Stage 3 runs, converting pain statements to vectors and clustering them across industries is where ML becomes hands-on.
- **Prompt engineering** — getting the LLM to extract structured JSON reliably from messy Reddit threads is a real problem that teaches you how models work under pressure.

The debate engine in Stage 5 is also your first real multi-agent system. From there, you have a natural path into **retrieval-augmented generation (RAG)**, **fine-tuning on domain-specific data**, and eventually **autonomous research agents**.

This codebase is the foundation for all of that.
