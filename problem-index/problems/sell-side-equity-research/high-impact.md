# The Coverage Franchise That Lives in One Analyst's Head

**Industry:** [[sell-side-equity-research|Sell-Side Equity Research]]
**Type:** High Impact
**One-liner:** A senior analyst knows how each management team guides, which line item each stock will trade on, and where consensus is habitually wrong — and none of it is recorded anywhere a successor, an associate or the department can use.
**Tags:** #tacit-knowledge-ml #gradient-boosting #feature-engineering #causal-inference #evaluation-metrics #confidence-intervals #revenue-impact #worker-facing

## The Problem
Clients do not pay a broker for the reported numbers; they get those from the filing. They pay for the analyst who, ten minutes after the print, says "the beat is all below the line, the guide is the usual 3% sandbag, and what matters is that North America gross margin missed for the second quarter running." That read is built from years of exposure: this CFO always guides to the low end and beats by a similar amount; this company's stock ignores revenue and trades on net adds; this management team changes the KPI definition when the KPI gets worse; consensus on this name always lags the channel checks by a quarter.

None of that is written down in structured form. It lives in the analyst's head, in the cell comments of a twelve-year-old Excel model, in old notes nobody rereads, and in the morning-call scripts. When the analyst moves to a competitor or the buy side — which senior analysts do routinely — the department keeps the model file and loses the franchise. The successor reinitiates from scratch, the coverage drops in the broker vote for two or three cycles, and the clients follow the analyst.

Even while the analyst stays, the knowledge does not scale. The associate sees the conclusion and not the pattern behind it. The analyst's own calibration — how often their "consensus is too low" calls were right — is never measured, so neither the analyst nor the director of research knows which parts of the judgment are real.

## Why It's Unsolved
**Data collection.** The judgment is exercised in the moment — reading a press release, listening to a call, adjusting a cell — and the artifact that survives is the adjusted number, not the reason. Capturing it means instrumenting the analyst's actual workflow: every model revision, timestamped, with the evidence open at the time, joined to management guidance history and to the subsequent reported result. The pieces exist (model versions, published estimates in I/B/E/S, guidance in transcripts) but in different systems and formats, and model files are personal, idiosyncratically laid out and rarely versioned.

**Labelling.** The outcome of a forecast is observable — the company reports — but the label for the *judgment* is ambiguous. An analyst who raised estimates because of a channel check and was right for a different reason is indistinguishable in the outcome data from one who was right for the right reason. Analysts also disagree with their own past selves: asked to explain an old revision, they rationalise. Labels have to come from the contemporaneous record, not recollection.

**Deployment.** A senior analyst will not use a tool that is slower than their own read. On earnings morning the window is minutes. Anything that captures the judgment must sit inside the model and the authoring tool, run without being asked, and surface "this CFO's guide has been beaten by 2–4% in eleven of the last twelve quarters" before the analyst has to think it. And the analyst has a career incentive not to make themselves replaceable, which the design must respect rather than fight.

## What a Solution Looks Like
A per-coverage memory built from the department's own history. For each covered company: every published estimate and its realised value by line item, every management guide against the eventual result (the guidance-bias profile), the line items whose surprises historically moved the stock on the day (learned from the department's own forecasts and price reactions), and the analyst's revision history with the notes and transcript passages that accompanied each change.

Over it, models that learn the analyst's corrections: given the guide, the consensus and this management team's history, where would the analyst have moved the number, and how often has moving it that way been right? The output is advisory and shown in context — beside the cell, in the preview template — and every suggestion carries its track record.

And a forecast scorecard per analyst, per line item and per management team, reported privately to the analyst first. Knowing which parts of one's own read are calibrated is the single most useful feedback the job never provides.

## Impact If Solved
Analyst departure is the largest single source of franchise loss in a research department, and a coverage hand-over today restarts from a model file. A department that holds the guidance-bias profiles, the "what it trades on" history and the calibrated revision record of its analysts can hand a successor years of pattern recognition on day one, train associates on the pattern rather than the conclusion, and demonstrate to clients — with numbers — which of its calls carry information.
