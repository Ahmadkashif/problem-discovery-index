# The Pass Decision Nobody Grades

**Industry:** [[private-equity-firms|Private Equity Firms]]
**Type:** High Impact
**One-liner:** A partner kills nine in ten deals in the first hour of reading a CIM, the reason is logged as a dropdown, and the firm never checks how the companies it passed on actually turned out.
**Tags:** #tacit-knowledge-ml #large-language-models #gradient-boosting #survival-analysis #causal-inference #evaluation-metrics #confidence-intervals #revenue-impact

## The Problem
A mid-market sponsor sees several hundred to a couple of thousand opportunities a year and closes perhaps four to eight. The funnel is decided at the top, by the most senior people, fast: a partner reads a teaser or a CIM over a weekend and writes back "pass — this is a margin peak", "pass — top customer is 30% and they're hiding the renewal date", "pass — the founder isn't really selling", or "let's take a look". That judgement is the firm's most valuable research product. It is the distilled experience of hundreds of prior deals, it determines where every associate hour goes, and it is almost entirely tacit — partners cannot write down the rule, and two partners at the same firm will read the same CIM differently.

What gets recorded is a pass reason picked from a list in DealCloud or Salesforce — Valuation, Size, Sector, Quality, Process — plus, sometimes, an email. The CIM itself is often deleted under the NDA's return-or-destroy clause.

Then the world grades the decision. Within one to five years the passed company is bought by another sponsor, refinances, files, gets sold again at a higher multiple, or quietly disappears. Most of these outcomes are visible in PitchBook, Capital IQ, press releases and lender league tables. Nobody joins them back. The firm knows its realised returns on the deals it did and has no idea of its hit rate on the deals it declined — which is the larger and more informative half of its decision record.

## Why It's Unsolved
**Data collection is the expert performing the task.** The signal lives in the partner's first read: which pages they spent time on, which numbers they recomputed, which sentence made them stop. None of that is captured. Reconstructing it requires recording the screen-level work of the people least willing to be instrumented, or asking them to annotate their own reasoning at the moment they are moving fastest.

**Labels are noisy, delayed and selection-biased.** A passed deal's "outcome" is partly observable (did it trade, at what multiple, did a later sponsor make money) and partly not (the counterfactual return the firm would have earned with its own plan). Partners also disagree with themselves: the same CIM reread in a different market regime or with a full pipeline gets a different answer, and pass reasons are often post-hoc rationalisations of a gut call — "valuation" is the polite label for half of them. Any labelling scheme has to accept that inter-rater and intra-rater agreement will be moderate and measure it rather than hide it.

**Deployment must be faster than the partner.** A screening aid that takes longer to read than the CIM summary it replaces will be ignored by the one audience whose adoption matters. It must produce its view in the minutes between the CIM landing and the partner opening it, and it must show its reasoning in the partner's own vocabulary or it will not be trusted.

**The corpus is legally fragile.** CIMs arrive under NDA, often with explicit return-or-destroy obligations on deals not pursued. A firm can usually retain its own notes, its own analysis and the fact of the opportunity, but not necessarily the seller's document. The training set therefore has to be built from what the firm is entitled to keep, which shapes the whole design.

## What a Solution Looks Like
Start by making the decision record. For every opportunity: the source, the date, the deal team, the structured facts extracted at first read (revenue, EBITDA, growth, margin trend, concentration, end market, ownership), the screening decision, and a two-sentence reason in the partner's own words — captured by a reply-to-email or voice note, not a form. That record belongs to the firm regardless of what happens to the CIM.

Join outcomes continuously. Match every passed company to subsequent transactions, financings and news through PitchBook or Capital IQ identifiers and entity resolution, and record what happened at one, three and five years. This turns the pass log into a labelled dataset with censoring handled explicitly — most outcomes are still pending, and survival-style treatment is the honest frame.

Then learn the partner's read, not just the outcome. Train a model to predict the screening decision from first-read features and an LLM summary of the CIM, so that a new opportunity arrives with "your firm historically pursues 12% of deals like this; the closest ten prior opportunities and what happened to them". Separately, measure where the partners' passes disagree with eventual outcomes — sectors, sizes or deal sources where the firm systematically declines things that later work. That second output is uncomfortable and is the actual value.

## Impact If Solved
Screening is where a sponsor spends most of its senior time and makes most of its decisions, and the firm has never measured its accuracy. A graded pass record turns the partners' tacit judgement into something juniors can learn from and the firm can audit, routes associate hours to the opportunities the firm historically wins on, and surfaces the blind spots — the sector the firm keeps passing on that keeps producing three-times exits for someone else — that no amount of post-close portfolio reporting can reveal.
