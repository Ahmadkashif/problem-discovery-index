# The Thesis Nobody Grades

**Industry:** [[hedge-funds|Hedge Funds]]
**Type:** High Impact
**One-liner:** A hedge fund marks every position to market daily and never records the reasoning behind it in a form that can be scored, so the analyst's judgement — the actual edge — is neither measured nor kept when the analyst leaves.
**Tags:** #tacit-knowledge-ml #large-language-models #gradient-boosting #causal-inference #evaluation-metrics #survival-analysis #feature-engineering #revenue-impact

## The Problem
An analyst at a long/short equity pod covers thirty to forty names. For each, they carry a thesis: why the stock is mispriced, what consensus is missing, what would prove them wrong, and how confident they are. Some of this is written — a pitch memo when the position is initiated, notes after earnings, a few lines in the research management system after an expert call. Most of it is held in the analyst's head and expressed in conversation with the PM, who sizes the position on the strength of it.

The things experienced analysts know best are the least written down. That this CFO always guides conservatively and then beats. That this management team's language on the call changes a quarter before a miss. That a distributor's tone in a channel check means inventory is building. That a short thesis is "right but early" and should be sized small until a catalyst. This is tacit knowledge in exactly the sense the term is used for a craftsman: pattern recognition developed across hundreds of quarters that the analyst cannot fully specify.

The outcome of every one of these judgements is recorded in perfect detail — the stock moved, the position made or lost money, the guidance was beaten or missed. P&L is attributed to factors, sectors and positions. It is not attributed to the thesis, the conviction level, the specific evidence, or the analyst's recurring read of a management team. When a pod is shut down after a drawdown, or an analyst moves to another platform, which happens every two or three years at multi-manager firms, the fund keeps the P&L history and loses the judgement that produced it.

## Why It's Unsolved
The data collection problem is that the expert's reasoning has to be captured at the moment of decision, by the expert, during the busiest part of their week. A thesis written after the fact is rationalised; a thesis written before is a tax on the analyst's time with no visible return to them. Research management systems exist and are used as filing cabinets: free text, inconsistent, missing exactly the fields that would make grading possible — conviction, horizon, the specific falsifier.

The labeling problem is that a position's P&L is a noisy label for the quality of the reasoning. A right thesis loses money when the market sells off; a wrong thesis makes money on a takeover nobody predicted. Factor-neutralised, catalyst-dated outcomes are the honest label, and even then experts disagree with themselves — the same analyst rates the same management team differently in March and September depending on recent experience. Positions are also selected: the theses that became large positions are not a random sample of the theses formed.

The deployment problem is cultural and temporal. Portfolio managers are paid on their judgement and are wary of a system that scores it; analysts fear that a recorded thesis is a recorded mistake. Any assistance has to arrive before the decision — before the call ends, before the open — and be faster than the analyst's own recall, or it will be ignored.

## What a Solution Looks Like
A thesis ledger first and a model second. Every position initiation, add, trim and exit is attached to a short structured record — thesis, key variables, expected catalyst and date, conviction, and what would change the view — drafted automatically from the analyst's own notes, model changes and call transcripts, and confirmed in seconds rather than written from scratch. Each record is graded later against factor-neutralised returns over the stated horizon and against whether the stated catalyst occurred as described.

On top of the ledger, learn the analyst's recurring reads. Pair earnings-call transcripts and management communications with the analyst's historical annotations ("sandbagging", "tone deteriorating", "promotional") and the subsequent outcome, and build models that surface those patterns to the next analyst who covers the name. The goal is not to replace the read but to make an experienced analyst's pattern recognition available, with its track record, to a junior or to their successor.

## Impact If Solved
A fund that can say which theses, analysts, evidence types and conviction levels carry information can reallocate capital and research effort on evidence rather than on recent P&L, which at a multi-manager platform with dozens of pods is worth a material share of risk budget. Retaining an analyst's documented judgement through a departure turns the most expensive recurring loss in the industry — the edge walking out of the door — into something the firm keeps.
