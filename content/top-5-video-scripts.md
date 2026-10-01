# Top 5 Topics — Briefs and Short Video Scripts

**Series:** workflow automation for finance research teams (personal brand)
**Format:** 60–90 second talking-head or explainer videos, roughly 150–220 spoken words each
**Source brief:** `content/finance-research-workflows.md` · vault branch `phase4/capital-markets-research`

> **Writing rule for all five:** describe *patterns*, never accuse a named firm. The vault says these gaps are common across the industry; it doesn't say any specific vendor or fund has them. Named products below appear only as examples of the category.

---

## 1. "Your fund marks every position daily. It has never graded a single thesis."

**What it's about.** Hedge funds measure P&L to the penny, but the *reasoning* behind each position (why it's mispriced, what the catalyst is, what would prove the analyst wrong) mostly lives in heads and in loose notes. So the fund can't tell whether an analyst was right for the right reasons, and when an analyst leaves, the judgement leaves too. The fix isn't more research. It's a lightweight **thesis ledger**: a three-field record drafted automatically from the analyst's own notes, confirmed in under a minute, and graded later against what actually happened.

**Vault source:** `problems/hedge-funds/high-impact.md`

**Script**

> **[Hook]** Your fund knows exactly how much every position made yesterday. It has no idea whether the *reason* you bought it was right.
>
> **[Setup]** Think about how a position actually gets sized. An analyst has a thesis: what the market's missing, the catalyst, what would make them wrong. Some of that gets written down. Most of it gets said out loud to the PM.
>
> **[Turn]** Then the outcome arrives. The stock moves, guidance beats or misses. All of it recorded in perfect detail. But it's attributed to factors and sectors, never to the thesis. A stock can go up for reasons that have nothing to do with your call.
>
> **[Payoff]** So here's the cheapest research upgrade most funds aren't making: a thesis ledger. Three fields (view, catalyst, falsifier) drafted automatically from notes you're already taking, confirmed in under a minute, and graded against what happened. Not to police analysts. To finally learn which kind of judgement actually carries information.
>
> **[Close]** P&L tells you what happened. Only the thesis tells you why. Start recording the why.

---

## 2. "Alt-data vendors get an answer key every earnings day, and nobody keeps score."

**What it's about.** Alternative-data research firms turn card, receipt and app panels into company KPI estimates sold to funds before earnings. Their product has a rare property: every estimate gets a **free, public answer key** on a known date, when the company reports. Yet a standing, honest accuracy record per ticker and metric is rarely kept on either side. Funds build private scorecards; vendors show their best calls. A graded **forecast ledger** turns an estimate into something a PM can actually size against. The same pattern runs through credit research, valuation marks and expert calls, which makes this a strong series opener.

**Vault source:** `niches/hedge-funds/alt-data-kpi-research-providers/` (top-scoring research pocket, 56/60)

**Script**

> **[Hook]** There's a corner of finance where every single forecast gets graded, for free, on a date you know in advance. And almost nobody keeps the scorecard.
>
> **[Setup]** Alt-data research firms take panels (card spend, email receipts, app usage) and turn them into estimates: this company's revenue, units, subscribers, before earnings.
>
> **[Turn]** Then the company reports. That's the answer key. Every estimate, right or wrong, by how much. Yet ask most teams: how accurate are you on *this* ticker, *this* metric, when the panel is thin? The honest answer usually lives in someone's personal spreadsheet.
>
> **[Payoff]** If you buy this data, build the ledger yourself: every estimate stored with its date and version, graded automatically on the print, summarised per ticker. If you sell it, a calibrated confidence on each number is the one feature a competitor without your archive can't copy.
>
> **[Close]** The market grades your research every quarter. The only question is whether you're keeping the marks.

---

## 3. "Thirty expert calls and no synthesis"

**What it's about.** In a diligence sprint or thesis build, an analyst runs 15–40 expert calls, then adds library transcripts on top. The answers overlap and contradict, and the experts aren't equally informed. The synthesis that goes to the investment committee is stitched together by hand the night before, and it loses three things: **how many** experts supported a claim, **who** they were, and **where they disagreed**. Per-call AI summaries don't fix this and can make it worse, because they sometimes state numbers the expert never gave. The workflow that's missing is claim-level synthesis with every statement linked to the transcript line behind it.

**Vault sources:** `problems/expert-networks/worker-life-2.md`, `niches/expert-networks/cross-call-synthesis/fix.md`

**Script**

> **[Hook]** You've done thirty expert calls this week. Quick question: how many of them actually agreed with your thesis?
>
> **[Setup]** Former employees, customers, competitors, distributors. Fifteen to forty calls in a sprint, plus a stack of library transcripts on top.
>
> **[Turn]** And the synthesis, the part closest to the decision, is done by rereading everything at midnight. The memo says "customers like the product." It doesn't say that was four of eleven customers, that the dissenters were all mid-market, or that the strongest quote came from someone who left four years ago.
>
> **[Twist]** And no, a summary per call doesn't solve it. Summaries occasionally invent a number the expert never said, and it slides straight into the model.
>
> **[Payoff]** What you want is claim-level synthesis: every claim pulled out, grouped by question, with who said it, how recent and how informed they are, and a link to the exact transcript line. Plus a flag while there's still time: "you haven't spoken to a single mid-market customer."
>
> **[Close]** More calls won't get you more conviction. A synthesis you can check will.

---

## 4. "MNPI clearance is the real speed limit on research"

**What it's about.** Every expert call, channel check, dataset and management meeting at a fundamental fund has to be cleared for material non-public information. In practice that means compliance officers reading requests and transcripts one at a time, so the **compliance queue is the bottleneck on research speed**, and reviews vary depending on who reads what. Existing surveillance tools hunt for misconduct *after* the fact. Research needs *forward-looking* clearance: triage by risk, an approval in minutes for the routine majority, real attention for the few that warrant it, and an audit trail an examiner can follow. The argument is that this is faster **and** safer.

**Vault source:** `problems/hedge-funds/low-impact-2.md`

**Script**

> **[Hook]** The slowest step in your research process probably isn't research. It's waiting for compliance to say yes.
>
> **[Setup]** Every expert call, every dataset, every management meeting carries MNPI risk. So someone in compliance checks the request against the restricted list, sometimes listens in, reviews the notes after.
>
> **[Turn]** A busy analyst requests dozens of calls a month. Each one waits in the same queue, reviewed by whichever officer picks it up. That's slow, and it's inconsistent, which is the part examiners actually care about.
>
> **[Insight]** Here's the trap: the tools most firms own are surveillance tools. They're built to catch problems after the conversation. Research needs the opposite: clearance before it.
>
> **[Payoff]** Triage by risk. Match the expert's history and the topics against holdings and recent corporate events. Approve the routine majority in minutes, with the reason recorded. Send the genuinely risky few to a human who now has time to look properly.
>
> **[Close]** Done right, this is the rare automation that makes you faster *and* more defensible. Same controls, better spent.

---

## 5. "The associate on earnings night"

**What it's about.** In reporting season a sell-side research associate starts before the 6:30 a.m. release. They put the print into the analyst's model, build the variance table, draft the first-take note and charts, then do it again for the next company, sometimes three in a day. Clean structured data already exists (Daloopa, Canalyst, Capital IQ, FactSet and others). The **last mile** is the analyst's *own* model: its layout, segment splits and adjustments, which live in the associate's head and break silently when a company re-segments. The human angle is the strongest part. This job is supposed to be an apprenticeship in judgement, and it's being spent copying numbers.

**Vault sources:** `problems/sell-side-equity-research/worker-life-1.md`, `problems/sell-side-equity-research/low-impact-2.md`

**Script**

> **[Hook]** It's 5:40 a.m. The press release drops at 6:30. You have until the morning meeting.
>
> **[Setup]** If you've been a research associate, you know the drill. Download the release, put it into the model, variance table, first-take note, charts, to the analyst before 7:30. Then the call, the revised model, the price target. Then the next company.
>
> **[Turn]** Here's the strange part: the data is already available clean. You can buy it structured, linked to source. But it's not *your analyst's* model: their rows, their segment split, their version of "adjusted." That mapping lives in your head, and it breaks the quarter a company re-segments.
>
> **[Payoff]** So the automation that matters isn't another dataset. It's a layer that learns your model from last quarter's fills, proposes this quarter's with a source link on every cell, and flags exactly where the company changed its presentation. You check exceptions instead of typing.
>
> **[Close]** This job is meant to teach you judgement. Every hour spent copying numbers is an hour not spent learning why your analyst changed the one that mattered.

---

## Production notes

- **Order to publish:** 2 → 1 → 5 → 3 → 4. Open with the boldest argument, follow with the big idea, then the most relatable pain, then the two workflow fixes.
- **No hard pitch in any script.** The close is the takeaway. If you want a soft call to action, use "what does this look like on your team?" and keep the company in your profile, not in the video.
- **Before recording:** every claim above is a pattern described in the vault, not a sourced statistic. Don't add numbers (hit rates, hours, market sizes) without checking them first. See the must-check list in `content/finance-research-workflows.md`.
