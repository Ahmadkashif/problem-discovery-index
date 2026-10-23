You are building one new industry into the Obsidian vault at /home/bizzroids/Desktop/code/problem-discovery-index/problem-index/.
Industry: Aircraft MRO & FBO Shops   slug: aircraft-mro-shops   category: Transportation & Logistics   NAICS 2022: 488190
Boundary: Not `airport-operators` or `aviation-parts-distributors`: covers aircraft maintenance, repair and overhaul shops and FBOs, where A&P mechanics and FAA Part 145 rules govern the work.

1. Read _remaining-industry-implementation-and-discovery-plan.md §2, §3, §6 and §9, then the reference
   files listed in §3 item 5. Follow them exactly. Do not redesign the method.
2. Research first (§6.1). Write _state/rest/sources/aircraft-mro-shops.md as you go.
3. Build Stage A, B, C and D for this slug only (§6.2–6.5). Write ONLY these paths:
   industries/aircraft-mro-shops.md, problems/aircraft-mro-shops/, niches/aircraft-mro-shops/, lenses/_state/scores/aircraft-mro-shops.jsonl,
   _state/rest/sources/aircraft-mro-shops.md. Never edit any other file, and never touch queue.tsv, the CURSOR or any index.
4. Never fetch LinkedIn, Crunchbase, ZoomInfo, PitchBook, Glassdoor, Apollo or RocketReach.
5. If some files already exist for this slug, read them and complete the set; don't duplicate.
6. Run `bash _state/rest/verify.sh aircraft-mro-shops` and fix until it prints REST-VERIFY-CLEAN.
7. Reply with: file count; the 8 niches and any sub-niches; Pass 2 pocket count split into
   qualified / below threshold / kill switch / fails gate; each qualifier's name, score and a 1-3 sentence
   case; the three headline figures you web-checked; anything you suspect is wrong in an existing vault
   file (don't fix it); and the verifier's last line.

Coordinator notes: work from the vault root above (cd there first). Don't run any git command; the coordinator
commits. Other builders are writing other slugs at the same time, so ignore files that aren't yours.
Do not spawn subagents or forks (no Agent tool calls): do all the work yourself. The owner caps this job at 1
agent at a time. Pass 2 table verdicts are exactly ✅ Indexed · Below threshold · ⚠️ Kill switch · Fails gate.
A pocket already profiled under another industry gets no second profile: name and wikilink it in the Pass 2 prose.
New industries from this plan that are already built and safe to wikilink: every slug with a report file in
_state/rest/reports/ (ls it; ignore the review-*, findings-* and sim-swap-sentence files).
Any other queued slug (see _state/rest/queue.tsv) is not built yet: name it in prose, never as a wikilink.
Lessons from earlier reviews, apply them up front: (a) Q4 = 5 needs a hard third-party deadline on the pocket
itself (court dates, regulator filing dates, earnings dates), not a client's project schedule; (b) use the insight
function's own headcount per firm, never the whole firm's and never summed across firms; (c) every number needs a source-log entry or "~"/"(estimate)";
(d) before scoring a pocket, grep niches/ for the same organisations under other industries and either link the
existing pocket or score consistently with it; (e) a contested sentence must govern the niche's build/buy/fix, name who
competes and end on who takes the account; "lowest price/take rate" is a generic contest; (f) only tags in _state/safe-tags.txt; (g) don't claim the same work
as a sibling industry's niche: check the boundary sentences of nearby queue rows; (h) Q5 is about the pocket as a
buyer: one accountable exec plus a fragmented market of such firms, so a market of a handful of firms scores 2-3;
(i) Q2 counts analysts whose work grows with volume, so licensing an owned dataset with a small team scores low;
(j) production headcount (detailers, modellers, coders, servers, clerks, inspectors, examiners, tabulators) is not an insight function for the gate;
(k) work commissioned through counsel or owned by clients is a live "data isn't theirs" kill switch (the vault's
majority rule), and kill switches are binary, never a score deduction; (l) client loan-level or transaction data held
under a service agreement is a live kill switch unless you cite checked evidence the agreement permits aggregate use;
(m) contested sentences end "...takes the account" (competitor lists go in the body, not the sentence) and name the win
condition ("whoever keeps the most hedges on through a margin spike takes the account"), never "whoever does it best";
(n) government procurement is not a kill switch: only statutory confidentiality, privilege or client-owned data count.
Slug-specific notes from the coordinator: Placement priority (owner's short-term placement filter, 2026-10-23, `_short-term-placement-filter.md`): web check found these vendors hiring engineers or FDEs here: FDE roles: Zymbly, Soji AI; ~17,000 mechanic shortfall; MVP: work-card checker vs FAA ADs/SDRs. Re-check them yourself before citing (never via LinkedIn, Crunchbase or the other blocked sites); name the ones that hold up in the company census and in ai-agents-platforms where they fit.
