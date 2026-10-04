# What Gets Clicked, and What Gets Liked After the Click

**Data:** 1,712 AI-related YouTube videos collected with yt-dlp on 2026-10-03 (`research-facility/research/ai-youtube-video-titles/`). 1,666 have usable views and likes.
**Question:** what is the sweet spot between bait (clicked, then regretted) and worthy content nobody clicks?
**Replaces:** the approach behind `finance-research-workflows.md` and `top-5-video-scripts.md`, which were analytically sound and **unclickable**.

---

## 1. The core finding: clicks and value are separate dials

I used two signals:
- **Click pull:** views per day.
- **Value signal:** like rate, i.e. likes ÷ views. Likes are the closest thing in this data to "was it worth it and would I pass it on." Share counts aren't available.

The two are **essentially uncorrelated** (Spearman ρ = −0.06). A title can win one, both, or neither. Splitting at the medians (449 views/day, 1.9% like rate) gives four roughly equal groups:

| Group | Clicks | Value | What it is |
|---|---|---|---|
| **Sweet spot** | ≥ median | ≥ median | The target |
| **Bait** | ≥ median | < median | Clicked, then regretted |
| **Gem** | < median | ≥ median | Good content, bad packaging. **This is where my last scripts were heading.** |
| **Dead** | < median | < median | Neither |

## 2. What pushes a title into each group

| Title feature | Views/day (with vs without) | Like rate (with vs without) | % sweet | % bait | Verdict |
|---|---|---|---|---|---|
| **Contrarian verdict** (not / never / wrong / stop / won't / isn't) | 809 vs 425 | **2.23% vs 1.89%** | **34%** | 28% | ✅ Wins both dials |
| **Money or stakes** ($, billion, paid, money) | 2,008 vs 429 | 2.02% vs 1.90% | **45%** | 30% | ✅ Strongest sweet-spot rate |
| **Short title** (≤ 40 chars) | 466 | **2.48%** | **34%** | — | ✅ Over 80 chars: **6% sweet** |
| **"You / your"** | 619 vs 445 | 2.11% vs 1.89% | 28% | 25% | ✅ Mild help on both |
| **Named actor** (OpenAI, Google, Nvidia, Musk…) | **1,415 vs 319** | 1.67% vs 1.92% | 30% | **45%** | ⚠️ Big clicks, lower value. Bait risk |
| **Danger word** (kill, destroy, warns, collapse) | **2,175 vs 414** | 1.75% vs 1.90% | 31% | **41%** | ⚠️ Bait risk |
| **Question mark** | 228 vs 504 | ≈ same | 17% | 23% | ❌ Halves clicks unless the question breaks an expectation |
| **"How… / What is…"** opener | 256 vs 507 | ≈ same | 18% | 20% | ❌ |
| **Colon or pipe** (`Topic: Subtitle`, `… \| Show`) | 345 vs 510 | 1.75% vs 2.04% | 19% | 28% | ❌ Hurts both dials |

**The named-actor and danger-word penalty is real, not a quirk of channel size.** Like rate normally *rises* with channel size: 1.5% for channels whose median video gets under 10k views, 2.2% for channels whose median is over 1M. Named-actor titles mostly sit on big channels and still score below median, so their low like rate isn't explained by channel size.

### By title template

| Template | Views/day | Like rate | % sweet | % bait | |
|---|---|---|---|---|---|
| **The [thing] nobody talks about** | 1,343 | **4.10%** | **75%** | 0% | ✅ Best template (n = 8; small sample) |
| **[Thing] is [dead/a bubble/here]**, a verdict | 1,520 | 1.97% | 36% | 33% | ✅ |
| **[Company] just [did X]** | 1,124 | 2.25% | 35% | 32% | ✅ Requires real news |
| **Why [thing] fails / why [claim]** | 447–546 | 2.15–2.49% | 31% | 15–26% | ✅ Lower clicks, high value |
| **How to [task]** | 440 | 2.36% | 31% | 17% | ✅ Value-heavy |
| **[Expert] WARNS [danger]** | **6,680** | **1.34%** | 24% | **59%** | ❌ The archetypal bait |
| **I tried / built [thing]** | 2,654 | 1.63% | 23% | **62%** | ⚠️ Bait unless the result is a real finding |
| **Inside [org]'s [effort]** | 3,748 | 1.28% | 25% | 50% | ⚠️ |
| **The future of [domain]** | 249 | 1.48% | 9% | 37% | ❌ |
| **Will AI [replace/save] [X]?** | 67 | 1.97% | 8% | 12% | ❌ Dead |
| **[AI] is transforming [domain]** | 76 | 1.64% | 16% | 12% | ❌ Dead |
| **AI in [domain]: [benefits/risks]** | **23** | 1.45% | **2%** | 12% | ❌ The deadest shape in the corpus |

## 3. What the sweet spot looks like in practice

These come from the finance, jobs, agents and software slices of the corpus. **Sweet:**

- *AI Was Supposed To Take Your Job. Why Hasn't It?* (11,957/day · 3.1%). **Broken expectation.** The viewer already holds the belief, and the title promises to resolve it.
- *AI Fails at 96% of Jobs (New Study)* (4,182/day · 4.4%). **Verdict plus a receipt.** The parenthesis promises evidence.
- *I Tracked Down the Hidden Workers Secretly Powering ChatGPT* (25,014/day · 2.2%). **Hidden people** behind a familiar thing.
- *We Let AI Run a Vending Machine. It Lost All the Money.* (WSJ · 2.8%). **Experiment with a punchline outcome.**
- *What 6 months of AI coding did to my dev team* (3.4%). **Lived evidence**, specific timeframe.
- *AI Replacing Developers Has Officially Failed* (2.5%). **Contrarian verdict** on a belief the audience feels anxious about.
- *it's boring, but it's what bursts the ai bubble* (3.6%). **Admits "boring"**, then promises it matters. Works because it signals substance.

**Bait:**

- *AI kill switch won't work in the long run: 'Godfather' of AI* (74,117/day · **0.6%**).
- *What if the AI Bubble Bursts (Day by Day)* (159,438/day · **0.6%**).
- *The Truth About the 700 OpenAI Agents That Attacked Hugging Face* (29,986/day · **0.5%**).

The pattern: **authority + fear + hypothetical, with nothing the viewer can take away.**

**Dead:**

- *A.I. and the Future for Humanity | FT Business*
- *Top AI Thinkers: Where Human-Machine Collaboration Works Best*
- *Building Agentic AI Systems with AWS Serverless • Speaker • Conf*

**Topic labels.** They describe a subject and promise nothing.

## 4. The rule set

A title needs **one click lever** and **one value promise**, in **≤ 50 characters where possible**:

| Click levers (pick one) | Value promises (pick one, and deliver it in the first 20 seconds) |
|---|---|
| A **broken expectation** ("was supposed to… why hasn't it?") | A **receipt**: a study, real data, "I tested it" |
| A **contrarian verdict** ("X has failed", "X isn't the problem") | A **mechanism**: the *why*, explained simply |
| **Hidden people / the thing nobody talks about** | A **repeatable line**: something the viewer can say in a meeting to look sharp. This is the share trigger |
| **Money or stakes** | A **thing to do differently on Monday** |
| A **named actor**, only when the video is genuinely about them | |

**Bait** is a click lever with no value promise, or a promise the video doesn't keep.
**Dead** is no click lever: topic labels, "the future of", "how X uses AI", "AI in X:", jargon, more than 60 characters, `Topic: Subtitle`.

## 5. My last work, scored honestly

| Old title | Verdict | Why |
|---|---|---|
| "Your fund marks every position daily. It has never graded a single thesis." | **Gem** (best case) | 75 chars. It has a broken expectation, but "thesis" and "marks" are insider words and nothing is at stake for the viewer |
| "Alt-data vendors get an answer key every earnings day — and nobody keeps score" | **Dead** | 78 chars. Jargon ("alt-data"). Nothing in it is about the viewer |
| "Thirty expert calls and no synthesis" | **Dead** | A topic label. "Synthesis" is a word nobody clicks |
| "MNPI clearance is the real speed limit on research" | **Dead** | Requires knowing the acronym before you'd care |
| "The associate on earnings night" | **Dead** | A label that reads like a chapter title |

The substance was right: the vault findings are real and specific. **The packaging was written for people who already agree.** I opened on the insider's vocabulary instead of the outsider's tension.

There's also a structural problem in the corpus: **finance is the weakest AI vertical for clicks** (median 178 views/day against 449 overall), and almost all of its sweet-spot videos are about the AI *bubble*. Finance-workflow videos barely exist. So the move is to **piggyback on the big narratives finance people already watch** (AI and jobs, AI hype vs reality, Wall Street) and **deliver the workflow insight as the receipt**.

---

## 6. The top 10, rebuilt

Each one: title (≤ 55 chars) → which lever and promise it uses → the first line of the video → what the video must deliver so it doesn't become bait → the vault receipt.

**1. AI Was Supposed to Replace Analysts. Why Hasn't It?**
- **Lever / promise:** broken expectation (the exact shape of a 3.1%-like-rate, 12k/day video) / mechanism.
- **Opening line:** "Every bank said AI would do the analyst's job by now. Walk into any research team at 6 a.m. and they're still copying numbers. Here's why."
- **Must deliver:** the answer. AI automated the parts that were never the bottleneck. The real time sinks are the last mile into *your* model, compliance sign-off, and synthesis across sources.
- **Receipt:** `problems/sell-side-equity-research/low-impact-2.md`, `problems/hedge-funds/low-impact-2.md`, `problems/expert-networks/worker-life-2.md`

**2. AI Is Making Every Analyst Think the Same Thing**
- **Lever / promise:** contrarian verdict / repeatable line.
- **Opening line:** "If you and 500 other funds read the same AI summary of the same earnings call in the same minute, what exactly is your edge?"
- **Must deliver:** the mechanism (identical summaries speed up consensus) and the fix (compare the call with *your own* prior expectations, not a generic summary).
- **Receipt:** `niches/asset-managers/fundamental-equity-research/fix.md`

**3. Your AI Research Summary Just Made Up a Number** *(experiment: you must actually run it)*
- **Lever / promise:** you + a danger that's true / receipt.
- **Opening line:** "I gave an AI 30 expert-call transcripts and asked for a summary. One market-share figure in it was never said by anyone."
- **Must deliver:** a real test on public or sample transcripts, the invented figure shown on screen, and the fix: every number linked back to its source line.
- **Receipt:** `niches/expert-networks/cross-call-synthesis/fix.md`. Only publish if your test actually reproduces it; otherwise retitle as *"How to Catch an AI Summary Making Up Numbers"*.

**4. The Hidden Workers Behind Every Number on Your Terminal**
- **Lever / promise:** hidden people (the 25k/day "hidden workers powering ChatGPT" shape) / mechanism.
- **Opening line:** "That revenue figure on your screen? At 2 a.m. in earnings season, a person decided what it means."
- **Must deliver:** how collection analysts standardise filings, why two vendors show different numbers for the same company, and what that means for anyone building a model.
- **Receipt:** `problems/financial-data-vendors/high-impact.md`, `worker-life-1.md`, `worker-life-2.md`

**5. The Research Bottleneck Nobody Talks About**
- **Lever / promise:** "nobody talks about" (the best template: 75% sweet) / a thing to do on Monday.
- **Opening line:** "It's not data. It's not models. At most funds, the slowest step in research is waiting for compliance to say yes."
- **Must deliver:** why the queue exists (MNPI risk on every call), why surveillance tools don't fix it (they're built for after the fact), and what risk-based triage looks like.
- **Receipt:** `problems/hedge-funds/low-impact-2.md`, `problems/expert-networks/low-impact-1.md`

**6. Wall Street Gets Its Homework Graded. Nobody Looks.**
- **Lever / promise:** named actor plus broken expectation / repeatable line.
- **Opening line:** "Every forecast an analyst makes gets a public answer key on earnings day. Almost nobody keeps the score."
- **Must deliver:** two or three concrete examples (KPI estimates vs reported numbers, valuation marks vs exit prices) and the simplest version of a scorecard a team could start this week.
- **Receipt:** `_scorecard-index-phase4.md` § The pattern, `niches/hedge-funds/alt-data-kpi-research-providers/build.md`

**7. AI Was Supposed to Save Junior Bankers. It Didn't (Yet)**
- **Lever / promise:** broken expectation plus jobs angle / mechanism.
- **Opening line:** "It's midnight. A first-year is checking every number in a 60-page deck against the model, with a pen."
- **Must deliver:** why tie-out and model-filling survived the AI wave (the work is in the firm's own layouts, not the public data) and what actually removes it. Stay fair: "hasn't yet", not "never will".
- **Receipt:** `problems/investment-banking-boutiques/worker-life-2.md`, `problems/private-equity-firms/worker-life-1.md`

**8. I Let AI Do an Analyst's Earnings Night** *(experiment: you must actually run it)*
- **Lever / promise:** an experiment with an outcome (the WSJ vending-machine shape) / receipt.
- **Opening line:** "6:30 a.m., the results drop. I gave the whole job to AI: update the model, write the note, before the 7:30 meeting. Here's where it broke."
- **Must deliver:** a real run on a public company's release. Show what worked (pulling the numbers) and what broke (mapping into an existing model, segment changes, first-take judgement).
- **Receipt:** `problems/sell-side-equity-research/worker-life-1.md`, `low-impact-2.md`

**9. Private Equity's Most Valuable Data Is a Dropdown**
- **Lever / promise:** contrarian twist / repeatable line.
- **Opening line:** "A PE firm looks at a thousand companies to buy ten. The other 990 decisions get recorded as one word: 'Passed.'"
- **Must deliver:** why declined deals are the richest research a firm owns, and the lightweight habit (a voice note per pass) that turns them into an advantage.
- **Receipt:** `problems/private-equity-firms/high-impact.md`

**10. Stop Doing Expert Calls Until You Fix This**
- **Lever / promise:** imperative "stop" (a strong template on smaller channels) / a thing to do on Monday.
- **Opening line:** "Thirty calls, three hundred pages of transcripts, and your memo says 'customers like the product.' How many customers? Which ones?"
- **Must deliver:** a claim-by-claim synthesis template (claim, how many sources, who, where they disagree) that viewers can copy.
- **Receipt:** `problems/expert-networks/worker-life-2.md`

### Publishing order

**1 → 6 → 4 → 5 → 9 → 2 → 7 → 10**, with the two experiments (**3, 8**) slotted in once they're actually recorded.

Start with the two broad, broken-expectation titles to build reach. Use the "hidden" and "nobody talks about" ones to build trust. Then the contrarian and "stop" ones, which tend to earn comments and shares from people who already follow you.

---

## 7. Caveats

- **This is general AI YouTube, not finance LinkedIn.** The levers should transfer, but the click thresholds won't. Test with 3–4 posts before committing to a series.
- **Likes are a proxy for value, not shares.** Comment rate tells a similar story. "Nobody talks about" has the highest comment rate in the corpus at 0.51%, against a median of 0.17%.
- **Views per day favour recent uploads, and big channels choose particular title shapes.** Small templates (n < 10) are directional only.
- **Never fabricate the receipt.** Titles 3 and 8 only work if the experiment is real. The fastest way to become bait is a value promise the video doesn't keep.
