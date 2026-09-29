# Lineage: Data Labeling Services

**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Wave:** [[series/eras/wave-12-transformers|12 — Transformers]]
**The tool:** the Dawid–Skene model — a latent-class model that gives each labeller a confusion matrix of error rates and uses the EM algorithm to estimate those rates, and the most probable true label for each item, from redundant labels with no answer key
**Builder:** Dawid & Skene
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Checking a label costs as much as making it.

A labelling vendor sells a correct answer for each item, but to know whether an annotator is right you need someone more reliable to label the same item again — and that person is exactly the expensive resource the vendor was hired to avoid. The standard workaround is redundancy: send each item to several people and take a majority. Majority voting treats every labeller as equally reliable and every mistake as random. Neither is true. Some annotators are careless, some are systematically confused between two particular classes, and a majority of the careless outvotes the one who knew.

What the business needed was a way to estimate how good each labeller is *without* ground truth, from nothing but the pattern of their agreements and disagreements.

## What Got Built

A statistical model, published in March 1979 as *Maximum Likelihood Estimation of Observer Error-Rates Using the EM Algorithm*, Journal of the Royal Statistical Society Series C, volume 28, pages 20–28.

It assumes each item has one hidden true class, and each observer has a personal confusion matrix: the probability of recording class *j* when the truth is class *i*. Given several observers' labels on many items, the EM algorithm alternates two steps — estimate each item's likely true class from the current error rates, then re-estimate each observer's error rates from those likely classes — until they settle. The output is both a best-guess label per item and a report card per labeller. The abstract's own description is candid: EM is "a slow but sure way" to reach the maximum-likelihood estimates.

## Who Built It, And Why Them

A. P. Dawid and A. M. Skene, statisticians listed at University College London. There was no labelling industry and no firm: the problem they had was clinical. Their abstract frames it as measurement error in compiling medical records — several people eliciting the same patient's history and not agreeing, with no way to ask the patient's "true" answer.

Why statisticians and not the users of the records: the tool is an estimation method, and its load-bearing part — EM, named and set out by Dempster, Laird and Rubin only two years earlier in 1977 — was new statistical machinery rather than anything a clinic could build.

The labelling trade picked it up three decades later. In 2008 Rion Snow, Brendan O'Connor, Daniel Jurafsky and Andrew Ng tested Amazon Mechanical Turk workers against expert annotations on five language tasks; they wrote that "Dawid and Skene (1979) are the first to consider" the multiple-noisy-labeller case, modelled their bias correction "following Dawid and Skene", and reported that it improved annotation quality on two tasks. Toloka's open-source Crowd-Kit library today ships a `DawidSkene` class alongside majority vote, GLAD and MACE.

## What It Cost

The model's assumptions are the trade. It treats each labeller's error rates as fixed across all items, so it cannot see that an annotator is reliable on easy cases and lost on hard ones. It assumes labellers err independently given the truth, so a shared misreading of the guideline looks like confident agreement. And it needs redundancy — several paid labels per item — to work at all.

Those assumptions hold tolerably for many cheap, simple, redundant labels. They fail for scarce, expensive expert judgements where two specialists may reasonably disagree and there is no fixed truth for EM to converge on.

## What You Still Touch

When a labelling platform shows a "worker accuracy" score computed without a gold set, or aggregates five crowd votes into one delivered label, it is running this model or a descendant. That score also drives which annotators get paid, warned or removed.

- [[problems/data-labeling-services/high-impact|🔴 Measuring Annotation Quality Without Ground Truth]] — the exact problem Dawid and Skene named, now priced in expert-tier work
- [[problems/data-labeling-services/worker-life-1|🟢 Annotator Rejection Disputes]] — the per-labeller report card, felt from the other side
- [[niches/data-labeling-services/expert-tier-quality/profile|Expert-Tier Quality]]
- [[niches/data-labeling-services/the-annotator/profile|The Annotator]]

**Sources:** Oxford Academic record for Dawid & Skene (1979), *JRSS Series C* 28(1):20–28, DOI 10.2307/2346806 (title, authors, affiliation, abstract); Snow, O'Connor, Jurafsky & Ng, "Cheap and Fast — But is it Good?", EMNLP 2008 (ACL Anthology D08-1027; abstract and Dawid–Skene citations read from the PDF); Raykar et al., "Learning From Crowds", *JMLR* 11 (2010) (consulted; the abstract does not name Dawid–Skene); GitHub `Toloka/crowd-kit` (method list). Crowdsourcing's HIT is the subject of this vault's `lineage/crowdsourcing-platforms.md`, not repeated here. WebSearch was not used; research was by WebFetch on known URLs; JSTOR would not load. ⚠️ **Not established:** the specific clinical study behind the 1979 paper — only the abstract was accessible, so the medical framing above goes no further than it; the 1977 EM date is from Wikipedia, *Expectation–maximization algorithm*, not the original paper. How widely commercial labelling vendors use Dawid–Skene internally is not documented in anything I could read.
