# History: Data Labeling Services

**Industry:** [[industries/data-labeling-services|Data Labeling Services]]
**Primary Wave:** [[series/eras/wave-12-transformers|12 — Transformers]]
**Secondary Wave:** [[series/eras/wave-07-big-data|7 — Big Data]]
**Origin Parent:** omitted — see below
**Episode Tier:** 1
**Transferable Pattern:** An industry that sells ground truth cannot check its own output against ground truth, and the mechanism it uses instead — consensus among annotators — is a proxy that degrades exactly where the money has moved. That is a real, unsolved measurement gap. It sits inside a second, older gap that no measurement fixes: the pay and rejection terms are set unilaterally, and a better model does not change who gets to set them.

> **Origin Parent — omitted, with a flagged near-miss.** None of the eighteen `origins/` industries has a real claim on this one. `origins/pharma-rd-cros/legacy.md` draws a line to this industry — "not the clinical content — the outsourcing shape. The CRO solved episodic, specialist, quality-critical work by building a standing third-party industry around it" — and that is a genuine structural echo, worth naming, but it is exactly the kind of adjacency `series/_plan.md` already flags for electric-utilities→agtech-platforms and process-manufacturing→metal-fabrication: a shape in common, not a transplant. No CRO discipline, headcount or company flows into this industry. Its real parent is a **sibling history file, not an origin**: [[history/crowdsourcing-platforms|Crowdsourcing Platforms]], which itself carries an omitted Origin Parent. Data labeling is therefore a native birth once removed — a child of a child, with no origins-tier ancestor anywhere in the chain.

## Before the Vendor — a general marketplace, not yet a category

Everything in [[history/crowdsourcing-platforms|Crowdsourcing Platforms]] applies here first: **Amazon Mechanical Turk launched 2 November 2005**, built to solve Amazon's own duplicate-catalogue problem, and "crowdsourcing" was not even coined as a word until Jeff Howe's *Wired* piece seven months later, June 2006. What existed by the late 2000s was a general-purpose market for short, priced, on-demand human tasks — market research, transcription, catalogue cleanup. Nothing about it was specific to machine learning yet.

## The Origin Event — ImageNet, not a company

The moment a general crowdsourcing platform became infrastructure for a specific industry is dated more precisely than the industry's own founding stories suggest. **Fei-Fei Li conceived ImageNet in 2006** and began building the project with Princeton's Christiane Fellbaum in 2007. **Labelling ran on Amazon Mechanical Turk from July 2008 to April 2010**, ultimately drawing roughly 49,000 workers across 167 countries to filter and label over 160 million candidate images down to the released set — by 2012, ImageNet was reportedly the largest academic user of Mechanical Turk anywhere. The dataset was first presented at CVPR in 2009; the ImageNet Large Scale Visual Recognition Challenge launched in 2010; **AlexNet's 2012 win** is the moment this vault and most others treat as deep learning's practical arrival.

That is the actual origin event: a research team discovering that a general labour marketplace could be pointed at one specific, repeatable task — image annotation — at a scale no lab could staff internally. The commercial vendors followed the pattern within a year or two. **CrowdFlower, founded 2007**, built a business around exactly this shape before ImageNet's labelling had even finished. **Appen**, by contrast, is a decade older than any of this — **founded in 1996 in Sydney by linguist Dr Julie Vonwiller** as a linguistics data company — and only became a "data labeling" business by pivoting an existing workforce-and-linguistics operation toward ML training data as the market appeared around it.

## What Became Cheap

Producing a labelled training set — a purchasable, delivered dataset, priced per unit, sourced from a workforce with no employment relationship to the buyer — at a scale that would have required a research grant and a graduate cohort a decade earlier.

## How It Was Actually Solved, and Where the Method Stops Working

Quality control runs on **consensus arithmetic**: majority vote across multiple annotators, gold-standard questions seeded into the task stream, inter-annotator agreement scores, and reviewer sampling on top. All of this is a genuinely good answer to *"is this bounding box in roughly the right place"* — three independent annotators agreeing on a box location is meaningful evidence.

It is a much weaker answer to *"is this chain of legal reasoning sound"* or *"is this code review correct"* or *"which of these two model responses is actually better,"* which is precisely the tier of work the market has moved toward as frontier labs shifted spend from bounding boxes to RLHF preference data and reasoning traces. Consensus among annotators who each have a defensible but different view of a genuinely hard question does not converge on truth; it converges on whichever answer is easiest to agree on, which is not the same thing. **This vault's own hub note calls this the industry's defining fact: it sells its most expensive product with its weakest quality signal**, and nothing in the ten years since ImageNet has produced a real substitute for consensus at the expert tier.

## The Contest — the crowdsourcing-era winner did not stay on top

Unlike dental practices or crowdsourcing platforms generally, this industry does have a legible contest, and a legible loser. **CrowdFlower rebranded as Figure Eight in 2017 and was acquired by Appen in 2019** — Appen's absorption of the crowdsourcing-native challenger looked, at the time, like consolidation into the incumbent. It was not the end state. **Scale AI, founded 2016 by Alexandr Wang and Lucy Guo through Y Combinator**, built specifically for machine-learning data from the start rather than pivoting into it, rode autonomous-vehicle annotation into the RLHF era, and reached a **$14 billion valuation in May 2024** on a round including Amazon and Meta. Appen's numbers moved the other way over the same years: **revenue fell to US$273 million in 2023**, and headcount dropped to roughly 1,000 by 2024, with three CEO changes in three years.

Then the contest resolved in a way no simple "who won" framing captures cleanly. **In June 2025, Meta purchased a 49% non-voting stake in Scale AI for approximately $14.8 billion**; founder Alexandr Wang joined Meta directly, and Jason Droege took over as CEO. The company that beat the crowdsourcing-era incumbent was then substantially absorbed by its own largest customer — a different resolution than a duel with a clean winner, and worth naming as such rather than forcing it into the shape of the airlines or programmatic-ad fights elsewhere in this vault.

## The Binding Constraint — the asymmetric hold, inherited whole and unimproved

This is the part of the file that matters most, because it is the same failure class documented in [[history/crowdsourcing-platforms|Crowdsourcing Platforms]], carried forward with the stakes raised rather than resolved.

**Remotasks**, Scale AI's crowd-labour subsidiary, saw per-task pay fall below one cent under competitive pressure; a Fairwork/Oxford Internet Institute study found it met only 1 of 10 fair-work criteria; late payments were reported as commonplace. **Three worker lawsuits filed in late 2024 and early 2025** alleged wage theft, worker misclassification, and psychological harm from exposure to disturbing content. Remotasks **shut down operations in Kenya, Nigeria and Pakistan in early 2024** — a withdrawal from scrutiny, not a remedy to it.

**Sama** — founded 2008 by Leila Janah as the non-profit Samasource, converted to a hybrid for-profit model in 2019 — provided content-moderation labelling to OpenAI for ChatGPT's safety systems and to Meta for both content moderation and Ray-Ban Meta AI-glasses review. A Time investigation found Kenyan workers earning under $2 an hour labelling toxic text; subsequent litigation documented wages between $1.46 and $3.74 an hour. **Daniel Motaung's 2022 lawsuit** alleged unsafe conditions, low pay and union-busting following his 2019 termination for organising a strike; workers formed the African Content Moderators Union in 2023, with Fairwork scoring the company 5 out of 10. In 2026, Sama employees reviewing Meta AI-glasses footage encountered private, intimate recordings; Meta terminated the contract, Sama laid off more than 1,000 Kenyan workers, and **Sama ceased its Kenyan and Ugandan operations on 15 September 2026**.

State the pattern plainly, because Wave 12 is this file's primary wave and it would be dishonest not to: the technology that made expert-tier and RLHF labelling valuable did nothing to change how pay is set, how rejection works, or whether a worker sees the reasoning behind either. **A model that can now read a legal brief or grade a chain of reasoning does not compel a platform to disclose a pay formula or build an appeals process it was already capable of building.** The stakes went up — the material being labelled now includes psychologically harmful content and higher-skill reasoning work — while the asymmetric hold that governs the relationship stayed exactly where [[history/crowdsourcing-platforms|Crowdsourcing Platforms]] found it.

## What's Still Open

- [[problems/data-labeling-services/high-impact|🔴 Measuring Annotation Quality Without Ground Truth]]
- [[problems/data-labeling-services/low-impact-2|🟡 Expert Credential Verification at Speed]]
- [[problems/data-labeling-services/worker-life-1|🟢 Annotator Rejection Disputes]]
- [[problems/data-labeling-services/worker-life-2|🟢 Delivery Manager Quality Escalations]]
- [[niches/data-labeling-services/expert-tier-quality/profile|Expert-Tier Quality]]
- [[niches/data-labeling-services/expert-credential-verification/profile|Expert Credential Verification]]
- [[niches/data-labeling-services/the-annotator/profile|The Annotator]]
- [[niches/data-labeling-services/annotation-corpus-intelligence/profile|Annotation Corpus Intelligence]]
- [[niches/data-labeling-services/workforce-marketplaces/profile|Workforce Marketplaces]]

## The Transferable Pattern

> **Two different problems can occupy the same industry, and only one of them is a technology gap. Diagnose which one is in front of you before proposing a fix.**

Measuring quality without ground truth is genuinely open — nobody, including the vendors sitting on millions of annotation events with reviewer verdicts and downstream model performance attached, has published a consensus-replacement metric that holds up at the expert tier. That is a real research and engineering opportunity, and Wave 12 is directly relevant to closing it, because the same models now capable of expert-level reasoning are candidates for judging it. Pay-setting and rejection without appeal is not that kind of problem. It persisted unchanged through the ImageNet era, the CrowdFlower→Figure Eight→Appen consolidation, and the Scale AI ascent, because it was never a measurement gap to begin with.

**The existential question, framed and not answered:** is this a durable industry — because expert-tier data for reasoning models is a compounding, not a depleting, need — or scaffolding for a building that increasingly generates its own labels? The hub note already records synthetic and model-generated data substituting for the easiest annotation tiers. Whether that substitution climbs the difficulty ladder faster than the demand for genuinely novel human judgement grows is unresolved in the sources checked, and any script should say so rather than pick a side.

**Sources:** Wikipedia, *Amazon Mechanical Turk*, *Crowdsourcing*, *ImageNet*, *Scale AI*, *Appen (company)*, *Sama (company)*; Fei-Fei Li and ImageNet project history (labelling window July 2008–April 2010; CVPR 2009 presentation; ILSVRC from 2010; AlexNet 2012); company histories for CrowdFlower/Figure Eight/Appen (2007, 2017, 2019) and Scale AI (2016 founding, May 2024 and June 2025 funding/ownership events); Fairwork/Oxford Internet Institute assessments of Remotasks and Sama; Time investigation and Motaung v. Sama litigation record; this vault's `industries/data-labeling-services.md`, `problems/data-labeling-services/*.md`, and `history/crowdsourcing-platforms.md`.
