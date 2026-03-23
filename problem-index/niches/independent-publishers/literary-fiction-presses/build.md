# Manuscript-to-Market Fit Scoring for Acquisition Decisions

**Niche:** [[niches/independent-publishers/literary-fiction-presses/profile|Literary Fiction Presses]]
**Industry:** [[industries/independent-publishers|Independent Publishers]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool helps an acquisitions editor assess whether a manuscript fits their press's identity, audience, and financial targets — a judgment call currently based on taste, gut feeling, and a comp title search in a browser tab.
**Tags:** #transformer #text-classification #nlp #tacit-knowledge-ml #revenue-impact

## The Problem
An acquisitions editor at a literary press reads 200–500 submissions per year seriously enough to evaluate market fit. For each, they consider: Does this voice match our press identity? Are there comparable titles that performed well? Is the audience reachable with our distribution and marketing channels? Will bookstores shelve this in a category that sells? This evaluation is pure tacit knowledge — experienced editors develop an instinct for "this is a Graywolf book" versus "this is a Catapult book" that they cannot articulate as rules. When the founding editor retires, the press's identity often drifts because the successor lacks the same pattern library.

## Why Nobody Has Built This
Publishing is culturally resistant to algorithmic acquisition — editors view their taste as an art form, not a data problem. The training data is sparse: a press with 15 years of history has published 200–400 titles, which is a small dataset. The features that matter (prose style, thematic resonance, voice) are hard to quantify. And the outcome variable is noisy — a book's sales depend on timing, reviews, cover design, and marketing execution, not just manuscript quality. Building a model that an editor would trust requires demonstrating that it captures editorial identity, not just predicting bestsellers.

## What to Build
A recommendation tool trained on the press's backlist: full text of published titles, their sales data, review coverage, and the editor's own notes on why they acquired each book. The model learns the stylistic and thematic DNA of the press — not "good" versus "bad" writing, but "this press" versus "not this press." For each new submission, it produces a fit score and surfaces the 3–5 most similar backlist titles with their performance data. It also identifies comparable titles from the broader market (BookScan data) with sales trajectories. The editor still decides — the tool gives them data to support the intuition they already have.

## Target Customer
Acquisitions editors and editorial directors at literary presses publishing 10–50 titles per year who evaluate 500+ submissions annually.

## Impact If Built
Reduces initial manuscript evaluation time by 40%, freeing 200+ hours per year for deeper editorial work. Helps identify 2–3 additional acquisitions per year that the editor might have missed in the submission pile. Reduces acquisition risk by surfacing comp title performance data — potentially preventing 1–2 underperforming titles per year ($20K–$50K in avoided losses).
