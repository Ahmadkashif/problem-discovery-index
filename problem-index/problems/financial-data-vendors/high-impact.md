# The Standardisation Judgement Inside Every Number

**Industry:** [[financial-data-vendors|Financial Data Vendors]]
**Type:** High Impact
**One-liner:** Every standardised financial in a terminal passes through a collection analyst's tacit judgement about where an issuer's idiosyncratic line item belongs, and that judgement is never recorded, never measured and lost every time the analyst leaves.
**Tags:** #tacit-knowledge-ml #transformers #large-language-models #gradient-boosting #k-nearest-neighbors #evaluation-metrics #confidence-intervals #revenue-impact

## The Problem
A 10-Q lands on EDGAR at 4:05 p.m. The XBRL pre-populates most of the vendor's template within minutes, and then a collection analyst reads the parts that matter. "Other operating (income) expense, net" contains a gain on the sale of a business line disclosed only in note 14. A segment has been renamed and its definition quietly widened. Stock-based compensation is presented inside three different expense lines. Revenue includes a pass-through cost the company excludes from its own "net revenue" KPI. Each of these is a mapping decision onto the vendor's standardised template — the one that feeds Capital IQ's standardised EBITDA, FactSet Fundamentals' normalised figures, LSEG's Worldscope-lineage fields — and every screen, comp table, factor model and backtest a client runs inherits it.

The analysts who make these decisions well are recognisably better than those who do not, and they cannot say exactly why. A senior collector who has covered industrial issuers for six years reads a footnote and "just knows" the item is recurring in substance despite the label, or that this company always restates the prior quarter in the next 10-K, or that a negative value in this field is a sign convention error rather than a real loss. That knowledge was built from thousands of filings and hundreds of client error tickets, and it lives in their head and in an internal wiki nobody reads.

What the vendor stores is the resulting number. The reasoning, the alternative mapping that was considered, the confidence, and the analyst's identity are overwritten or kept in an audit log no one analyses. Quality control is a sample: a reviewer re-keys a percentage of filings and counts discrepancies against policy. Errors surface when a client's model disagrees with a competitor's terminal, which is weeks later and arrives as a support ticket.

## Why It's Unsolved
**The data collection problem.** The expert's judgement is only visible as its output. To learn it, the vendor has to capture the expert performing the task — which footnote they read, which XBRL tag they overrode, which mapping they chose and against which alternative — and current keying tools record the final value, not the path. Retrofitting that capture into a production tool used under earnings-season deadlines is resisted precisely because it slows the analyst down at the moment throughput matters most.

**The labelling problem.** The experts disagree with each other and with themselves. Two senior analysts given the same ambiguous footnote will map it differently a meaningful fraction of the time, and the same analyst may map comparable items differently in Q1 and Q3 because the house policy changed in between or because nothing forced consistency. Historical mappings therefore encode a mixture of judgement, policy drift and error, and training naively on them reproduces all three. Any label set needs policy-version stamping, adjudication on disagreement and an explicit "ambiguous" class.

**The deployment problem.** A model must be faster than the expert and must know when it is not. If it proposes a mapping the analyst then has to verify from scratch, it adds time rather than removing it, and it will be switched off in the first earnings season. It has to be right with high confidence on the routine eighty per cent, abstain clearly on the rest, and show the footnote evidence for every proposal so the check takes seconds.

**The incentive problem.** Content operations are measured on timeliness and sample error rate, not on whether the standardisation decisions were consistent across issuers. A model trained to imitate today's analysts optimises the wrong thing unless consistency becomes a measured outcome.

## What a Solution Looks Like
Capture first. Instrument the collection tool so that every override of a pre-populated XBRL value, every mapping choice, the source passage the analyst was viewing, and the policy version in force are stored as a decision record. That record is the training set, and within one earnings season it is the largest structured corpus of expert accounting judgement in existence.

Learn the mapping as retrieval plus classification. For a new line item, retrieve the most similar prior decisions — same issuer's history, same industry, same footnote language — with what the expert chose, then score candidate template positions with a model conditioned on the label, the amount's behaviour, the XBRL tag, the footnote text and the issuer's own history. Calibrated confidence decides the route: auto-accept, propose-with-evidence, or send to a senior analyst with the disagreement history attached.

Use the error tickets as the gold labels they are. Every client-reported discrepancy that was investigated and resolved is an adjudicated example of a decision that was wrong, with the corrected mapping and the reason, and that corpus exists in every vendor's support system.

Measure consistency directly: the same item type across issuers, the same issuer across quarters, and the same footnote across analysts. Inconsistency becomes a number content leadership manages.

## Impact If Solved
Collection is the largest cost line in a fundamentals business and is staffed to the peak of earnings season; moving the routine majority of mapping decisions to assisted acceptance compresses time-to-standardised-data from hours to minutes and redeploys senior analysts to the ambiguous cases where they are worth their salary. More importantly, it turns the vendor's real moat — decades of expert mapping judgement — from something that walks out of the building with attrition into a versioned, measurable asset that explains every number it produces.
