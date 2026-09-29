# Technical Due Diligence

**Parent Industry:** [[industries/fractional-cto-services|Fractional CTO Services]]
**Category:** High Market Share
**Contested on:** Whether a technical opinion formed in two weeks, under restricted code access, from a management team with an interest in the answer, can be made defensible enough to price an eight-figure decision.

## Profile

**Market Size:** ~$600M
**Share of Parent Industry:** ~20%
**Digital Adoption:** Low — interviews, a data room and a few days of reading
**Target Buyer:** Private equity and venture investors, corporate development teams, acquirers
**Automation Potential:** High for evidence gathering, low for the risk opinion

## What Makes This a Distinct Niche

Technical due diligence is assessment with the constraints turned up and the stakes made explicit. Two weeks, often less. Code access that is restricted, sometimes to a supervised read in a data room. A management team that knows the answer affects the price and is present for every conversation. A report that will inform a decision measured in tens or hundreds of millions, and that will be read by people who cannot evaluate its technical content and will take its confidence at face value.

It is a distinct market rather than a variant because the buyer is different and the failure is different. The buyer is the investor, not the company, which means the practitioner's obligation runs to someone who was not in the room for any of the engineering. And the failure mode is asymmetric: missing a real risk is a career event, while flagging a risk that turns out to be manageable costs almost nothing — a structure that produces reports full of hedged findings and a category-wide reputation for saying everything and concluding little.

The access constraint is what makes it technically interesting. An advisor with a repository clone can derive a great deal. A diligence practitioner often cannot clone anything, and must form the same opinion from a supervised session, a set of documents the seller chose, and a small number of interviews with people who have prepared.

## Current Tools & Gaps

Diligence practice runs on checklists and templates — architecture review, scalability, security posture, technical debt, key-person risk, licensing and open-source compliance, infrastructure cost. Software composition analysis and licence scanners are genuinely well adopted here and are the one area where the category uses tooling properly, because the question has a machine-checkable answer. Security scanners and cloud cost analysers appear occasionally. Data rooms are document repositories with access logging.

The gaps are large. Nothing operates under the access constraint: every analysis product assumes an integration the seller will not grant. Nothing converts a supervised read into a structured record. The seller's own artefacts — architecture documents, incident history, roadmap slippage — are taken as presented rather than cross-checked against each other for internal consistency, which is where prepared material most reliably fails. Risk findings carry no severity calibration, so a report's twenty flagged items give the investment committee no ordering. And nothing anywhere records which flagged risks subsequently materialised, which is why the category cannot improve.

## Problems

- [[niches/fractional-cto-services/technical-due-diligence/build|🔨 Build: Diligence Under Restricted Access]]
- [[niches/fractional-cto-services/technical-due-diligence/buy|🛒 Buy: The Data Room That Analyses Its Own Contents]]
- [[niches/fractional-cto-services/technical-due-diligence/fix|🔧 Fix: Twenty Risks, No Ordering]]
