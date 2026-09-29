# Substantiation Narrative Engine Trained on the Firm's Own Study Corpus

**Niche:** [[niches/accounting-firms-smb/rd-tax-credit-study-firms/profile|R&D Tax Credit Study Firms]]
**Industry:** [[industries/accounting-firms-smb|SMB Accounting Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An engine that turns a firm's archive of prior R&D credit studies into a retrieval and drafting system, so a new project narrative starts from the twelve structurally similar narratives the firm has already defended rather than from a blank page.
**Tags:** #large-language-models #transformers #bert #transfer-learning #word-embeddings #evaluation-metrics #tacit-knowledge-ml #compliance #revenue-impact

## The Problem
The substantiation narrative is where an R&D credit study succeeds or fails, and it is written from scratch every time. A specialist interviews the client's engineers about a project, then composes several pages establishing technological uncertainty, a process of experimentation, a permitted purpose, and technological in-nature — the four-part test — in language specific enough to be credible and general enough to be defensible. A firm doing 400 studies a year has written many thousands of these, covering the same recurring engineering situations across manufacturing, software, food science, and aerospace. None of that accumulated craft is retrievable. A senior specialist writes a strong narrative because they personally remember how to frame a tooling-qualification project; a junior specialist writes a weak one and nobody notices until examination.

## Why Nobody Has Built This
The corpus is small by machine learning standards, highly confidential, and unlabeled in the ways that matter — nothing in a document management system records whether a narrative was ever tested by the IRS or how it fared. Generic drafting tools produce plausible four-part-test prose, which is precisely the danger: fluent language that does not track the specific engineering facts is worse than no draft, because it invites a substantiation challenge on facts the firm cannot support. What makes the problem tractable is exactly what makes it firm-specific — the value is not in a general model of §41, it is in this firm's own validated mappings from real engineering activities to accepted statutory framing, which cannot be bought and cannot be shared between competitors.

## What to Build
An engine that ingests the firm's complete study archive and builds a structured index over it: project type, industry, technology domain, the engineering activity described, the four-part-test framing used, and — where it can be recovered from engagement records — the examination outcome. For a new project, the specialist enters the client's industry and a short description of the engineering work, and the system retrieves the closest prior narratives with their outcomes attached, showing which framings held up under scrutiny and which drew adjustments. It then drafts the new narrative grounded in those retrieved precedents and in the specific interview transcript and project documentation for this engagement, marking every factual assertion with its source so the reviewer can verify rather than trust. Where the interview record does not support a required element, the system says so explicitly instead of writing around the gap — the most valuable output is often a list of the questions the specialist still needs to ask.

## Target Customer
Managing directors and national technical directors at R&D credit specialist firms running 50-500 technical staff, and the R&D credit practice leaders inside mid-size and regional CPA firms who deliver 100+ studies a year.

## Impact If Built
Compresses narrative drafting from the largest single time block in a 20-60 hour study to a review-and-verify task. More consequentially, it makes narrative quality independent of who was assigned — the firm's best defended framing becomes the starting point for every specialist rather than the property of its most senior people. Because outcomes feed back into retrieval, the corpus improves with every examination cycle, which is a compounding advantage no competitor can replicate without the same archive.
