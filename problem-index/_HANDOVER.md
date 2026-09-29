# Handover — Vault Evaluation for a Web Series

**For:** a fresh agent picking this up cold.
**From:** the previous session (Phase 3 author).
**Date:** 2026-09-21.
**Read this whole file before touching anything.**

---

## 1. What the owner actually wants

A **web series** about **how businesses shaped the technology we now take for granted.**

**The direction of travel matters and is easy to get wrong.** Each episode starts from **a specific piece of technology or a specific mechanic** — something the audience already uses or has heard of — and works backwards to the **business case that dictated its shape.**

It achieves two things, in the owner's own words:

1. Builds the case that **business is the ultimate entity tech works towards.**
2. Builds an understanding of **tech evolution as a consequence of business evolution.**

**Audience:** fresh graduates and aspiring forward deployed engineers. People who already use the technology and have never once asked why it behaves the way it does.

**Start small.** The owner's phrase is *"niche tech creations"* — specific mechanics, not eras. Not "the cloud." More like: why a checkout scans a barcode; why your card payment settles days after it is approved; why an airfare changes while you refresh the page.

### The distinction that the previous session got wrong

| | |
|---|---|
| **What the owner wants** (tech-first) | *"Why does every booking system withhold inventory and move the price while you watch? Because one airline needed to beat a cheaper rival in 1985."* |
| **What was built** (industry-first) | *"Airlines had a perishable-inventory problem, so they built yield management."* |

Same facts, reversed. In the owner's version **the artefact is the subject and the business case is the explanation.** Hold that line.

---

## 2. What the owner asked for originally, and what happened instead

**The original question was small:** *look at this vault and tell me honestly whether its starting point is rich enough to build this series from.*

**That question was never directly answered.** Instead the previous session proposed and ran a five-stage expansion ("Phase 3"), adding 213 files and ~228,000 words across `series/`, `origins/` and `history/`. The owner approved each stage as it was proposed, but the premise behind all of them was the previous session's, not the owner's.

**The honest assessment now, stated plainly:** the vault's pre-existing `industries/`, `problems/` and `niches/` layers were **already sufficient** to begin. The expansion answered a question the owner had not asked.

**The lesson is not "don't expand."** Expansion is welcome and the owner expects it **where a gap is proven**. The lesson is about **order**: the previous session proposed a five-stage build *before* diagnosing whether anything was missing, and on its own premise rather than the owner's.

**Diagnose first. Then, if the diagnostic finds real gaps, propose a staged build scoped to exactly those gaps** — and expect it to be approved. A multi-stage expansion backed by evidence is the right answer; one backed by an assumption is not.

---

## 3. What is on disk

### The original vault — this is the primary material

| Layer | Size | What it is |
|---|---|---|
| `industries/<slug>.md` | **250** | Hub note per industry: profile, pain themes, current tech landscape, analysis |
| `problems/<slug>/` | **250 dirs × 7** | Five problem notes + `ml-opportunity.md` + `ai-agents-platforms.md` |
| `niches/<slug>/` | **250 dirs** | `_overview.md` + niche subdirs, each with `profile/build/buy/fix` |
| `metadata/` | 3 | Canonical tag registry + math/ML taxonomies |

`industries/`, `problems/` and `niches/` are keyed by the **same slug** in exact 1:1:1 parity. **~13,346 files. This layer is append-only — never edit it.** Full conventions in `CLAUDE.md`.

**This is real, specific, checked material**: named customers, unit economics, named incumbent tools, and genuinely unsolved problems. It is the series' raw material.

### Phase 3 — treat as optional reference, not as the frame

| Layer | Size | What it is | Use it? |
|---|---|---|---|
| `series/eras/` | 12 | Computing eras 1955→now, dated triggers, mechanisms, what broke | **Useful** — dated spine |
| `origins/<x>/the-mechanism.md` | 18 | How a business question became a modelling problem, and what it cost | **Most useful thing here** |
| `origins/<x>/the-fight.md` | 18 | The competitive contest the technology was built to win | **Useful** |
| `history/<slug>.md` | 66 | Per-industry history: Before → Origin Event → What Became Cheap → How It Was Solved → Trade-Off | Useful, industry-first framing |
| `series/failures/` | 40 | Post-mortems of famous failures | **Tangential.** Built on a premise the owner did not ask for |

`series/_plan.md` and `series/_bookmark.md` document Phase 3's reasoning and its 90 corrected myths. **The myth list is worth reading** — it records facts this vault itself previously got wrong.

### Known defects — inherit these, do not rediscover them

- **Unverified claim:** a "Greg Stuart / IAB" quote about last-click attribution appears in several Phase 3 files. It was searched for and **not corroborated**. Files carry inline warnings. Do not put it in a script.
- **Deprecated tags:** 31 deprecated tag types are in use across the protected layers. Known, flagged, **unapproved for fixing**. Audit against `_state/safe-tags.txt` (138), **not** `metadata/tags.md` (190) — the latter includes the deprecated section and will silently pass them.
- **Research coverage is uneven.** WebSearch hit its session cap during Phase 3; later files ran on WebFetch and say so in-file. A top-up pass is owed before anything becomes a script.
- **Verification:** `bash series/_state/verify-phase3.sh` checks structure, links, tags and that protected layers are untouched.

---

## 4. YOUR TASK

> **Evaluate the vault again. Identify if adding more industries and niches will help build a more cohesive understanding and a smoother story.**
>
> **Again, the idea is to identify if the story has unexplained gaps. If you see that, ideate the gap and name an industry that would service it.**

### How to read that task

This is a **diagnostic** question first: *does the narrative have holes, and if so what would fill them?* The owner is **open to another expansion programme** — they want one where it is justified. What they do not want is a build proposed ahead of the evidence for it.

Your **first** deliverable is an **assessment with named recommendations**, not files.

**If the assessment finds real gaps, follow it with a staged expansion plan scoped to those gaps** — industries and niches to add, in what order, and which episode each unlocks. The owner wants that build where it is justified; it simply has to be earned by the diagnostic rather than assumed.

If the honest answer is "the vault is sufficient, add nothing," **that is also a perfectly good answer and you should give it.** The point is that the conclusion follows the evidence, in that order.

### What counts as a gap

A gap is a place where **the tech-evolution story cannot be told end to end** because a link is missing. Test it by trying to tell the chain out loud:

> *A mechanic exists → because a business needed it → that business existed because of an earlier mechanic → …*

Where does that chain break? Where do you have to say *"and then somehow…"*? That is a gap.

Concrete examples of the shape:
- **A mechanic with no owner in the vault.** If you want to explain why interchange fees exist, is there an industry here that owns that story?
- **A missing ancestor.** The vault is largely US SMB and digital-platform businesses. The technologies those industries *inherited* were mostly invented at large enterprises that may not be represented.
- **A missing consequence.** A mechanic gets invented, and the industry that exists purely because of it is absent.

### Constraints

- **Additive only.** Never edit `industries/`, `problems/`, `niches/`, `metadata/` or `plans/`.
- **Name specific industries**, with the gap each one closes and the episode it unlocks. Not categories.
- **Prefer fewer, better.** A short list you can defend beats a long list you cannot — but do not undercount either. If twenty industries are genuinely missing, say twenty.
- **Say if nothing is needed.** Do not manufacture gaps to look thorough, and do not suppress real ones to look disciplined.
- **Scope the build to the gaps you proved.** If you recommend an expansion, say how many industries, in what stages, and what each stage unlocks.
- **Verify before asserting.** If you cannot confirm a date or figure, say so. The vault's own standard is that a negative finding is a real finding.

### Before you start

Read a small sample rather than the whole vault:
```
industries/freight-brokerage.md
industries/payment-processors.md
problems/payment-processors/high-impact.md
niches/telehealth-platforms/_overview.md
origins/airlines/the-mechanism.md      # closest existing thing to the owner's episode spec
```

`origins/airlines/the-mechanism.md` is worth reading carefully — it takes one commercial question, turns it into a modelling problem, gives the actual decision rule, and states what was traded away. It is framed industry-first, but it is the nearest thing on disk to the owner's ask.

---

## 5. One thing to ask the owner early

**The delivery format is still unknown** — written, spoken, video, length, tone. The previous session never asked, and it materially changes what "a gap" even means. Ask before producing anything script-shaped.
