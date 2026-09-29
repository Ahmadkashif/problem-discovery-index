# Thirty Years of Agency Decisions and No Model of What Gets Accepted

**Niche:** [[niches/pest-control/pesticide-registration-regulatory-affairs/profile|Pesticide Registration & Regulatory Affairs Consulting]]
**Industry:** [[industries/pest-control|Pest Control]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The firm has argued thousands of positions to the agency and knows which ones landed, and every new strategy call starts from a senior scientist's memory.
**Tags:** #gradient-boosting #transformers #word-embeddings #evaluation-metrics #causal-inference

## The Problem
A registration strategy is a set of bets. Which studies will the agency require and which can be waived or bridged from an existing dataset. Which exposure model and which input assumptions will survive review. What the label can claim without triggering additional data requirements. Whether to argue a point now or concede it and preserve credibility for a harder one later.

Each bet is worth a great deal. A waived chronic toxicology study saves millions of dollars and two years. An exposure assumption the agency rejects late in review can restart a submission cycle. A label position that gets pushed back narrows a market.

These bets are placed on judgment. A senior regulatory scientist who has run submissions for twenty years knows how a particular division has treated a particular argument, which reviewers are exacting about which endpoints, and what the agency has been signalling in recent decisions. That knowledge is the firm's actual product and it exists as recollection.

The record that would replace recollection is right there. The firm has its own submission archive: what was proposed, what was requested, what was argued, what was granted, and how long each took. The agency's own public output — registration review dockets, risk assessments, decision documents, response-to-comment files — runs to an enormous, searchable corpus of reasoning, and it is where the agency explains why it accepted or rejected exactly these kinds of arguments. Nobody has assembled either.

## Why Nobody Has Built This
Regulatory consulting is a senior-labour business. The economics reward billing experienced scientists' time, not building an asset that would make less experienced scientists nearly as effective. The value of the archive accrues to the firm; the cost of building it comes out of utilisation.

The corpus is also genuinely hard. Agency decision documents are long, technical, inconsistently structured PDFs, and the thing worth extracting from them — the reasoning connecting a specific data gap to a specific conclusion — is buried in prose. The submissions on the firm's side are matter-organised, so reconstructing what happened requires reading a correspondence trail.

And there is a persistent belief in the profession that the outcome depends too much on the specific reviewer to be modelled. That belief has never been tested, which is itself the point.

## What to Build
An outcome-labelled model of agency decision-making, built on the firm's archive plus the public docket record.

**Structure the submission history.** For each submission: product class, active ingredient chemistry, use pattern, studies proposed and waived, exposure approach, label claims sought, agency requests received, positions conceded, final outcome, and elapsed time at each stage. This is the training set and it is a genuine moat — a competitor has its own archive, but no one has anybody else's.

**Extract reasoning from the public docket.** Registration review decisions, risk assessments and response-to-comment documents state, in the agency's own words, why a data requirement applied or was waived. Modern language models extract structured claim-and-rationale pairs from exactly this kind of technical prose, and the result is a precedent base searchable by argument rather than by product name.

**Predict the data requirement set.** Given a product's chemistry and use pattern, the probability each study is required. This is the highest-value question at the start of an engagement, it is answered today by analogy to remembered products, and it is a well-shaped multi-label problem over a structured input.

**Predict review duration and the request pattern.** Programmes are planned against agency timelines that vary widely by product class and workload. A model of elapsed time and of the likelihood of a mid-review information request is directly useful to a registrant planning a launch.

**Test the reviewer hypothesis.** The profession believes outcomes hinge on individual reviewers. The docket record identifies divisions and often reviewers. Measuring how much variance is actually attributable there settles a load-bearing belief either way, and both answers are commercially useful.

## Target Customer
Managing Director or VP of Regulatory Sciences at a specialist registration consultancy. The argument is direct: the firm's competitive advantage is currently four people's memories, and those people are retiring.

## Impact If Built
Registration programmes cost tens of millions of dollars and years of market exclusion when the strategy is wrong. A model that predicts data requirements and review outcomes from thirty years of decisions turns the firm's most valuable and least durable asset into one that compounds — and lets a mid-level scientist give advice currently only available from a principal.
