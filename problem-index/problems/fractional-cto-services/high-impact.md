# Forming a Consequential Technical Opinion in Three Weeks From Interviews

**Industry:** [[fractional-cto-services|Fractional CTO Services]]
**Type:** High Impact
**One-liner:** A fractional CTO must decide whether to rebuild or refactor, hire or restructure, on a system nobody documented and a team they have just met, and nothing they use measures any of it.
**Tags:** #graph-neural-networks #gradient-boosting #change-point-detection #bert #confidence-intervals #evaluation-metrics #tacit-knowledge-ml #survival-analysis

## The Problem
A fractional CTO joins a company in trouble or in transition. The engagement typically begins with an assessment: what state is the technology in, what state is the team in, what should change. That assessment drives decisions worth a great deal — a rebuild commitment, a hiring plan, an architecture change, sometimes a judgement about individuals.

The inputs are thin. There is usually no architectural documentation, or documentation describing a system that has since diverged. The decisions embedded in the codebase were made for reasons nobody recorded and frequently nobody remembers. The team's account is partial and shaped by their position in it. The founder's account is sincere and reflects what they were told. The practitioner reads code, asks questions, forms a picture, and commits to a recommendation within weeks because that is what the engagement is for.

Meanwhile the evidence is substantially available and unused. Repository history shows where change actually concentrates, which files are touched together, which areas have high churn and high defect correlation, and how long components have been stable. Issue and ticket history shows where work stalls, how estimates compare to actuals, and which areas generate rework. Delivery data shows flow, batch size and cycle time. Collectively these describe the system's real behaviour far more reliably than an architecture diagram drawn from memory in a workshop.

And the assessment is never validated. The practitioner leaves, the company follows or ignores the recommendation, and what happened over the following two years is not fed back. A practitioner with thirty engagements has thirty experiences and no record of which assessments held.

## Why It's Unsolved
The engagement is short and the tooling investment does not obviously fit inside it. Setting up analysis on a client's repositories and trackers takes time that the client is paying for at a senior rate to get an opinion, and there is a reasonable instinct that reading the code personally is what the client is buying.

Access is genuinely constrained in some contexts. In due diligence particularly, code access is limited, time-boxed and sometimes restricted to a supervised session, which rules out anything requiring sustained analysis.

The validation problem is structural. Nobody pays for a look-back two years after an engagement, the practitioner has usually moved on, and the counterfactual is unknowable — a company that followed a rebuild recommendation and struggled might have struggled worse without it.

And there is a professional culture factor. This work is sold on judgement and experience, and a practitioner leaning on tooling can feel like a practitioner with less judgement. That is the same instinct that has kept several advisory fields from instrumenting themselves, and it is strongest exactly where the individual's reputation is the product.

## What a Solution Looks Like
Derive the assessment's factual base rather than interviewing for it. Change concentration, coupling from co-change patterns, churn and its correlation with defects, component age and stability, ownership concentration and bus-factor exposure, and delivery flow characteristics are all computable from repository and tracker history in days. That is not a replacement for judgement; it is the evidence judgement should be applied to, and it arrives before the interviews rather than after.

Ask better questions with it. Knowing that one module has been rewritten three times in eighteen months and consumes a quarter of all commits changes what the practitioner asks the team, and produces a conversation about the actual problem rather than a general one.

Calibrate against a corpus. A practitioner or firm that retains assessment data across engagements — what the metrics looked like, what was recommended, what happened — can begin to say which patterns predict which outcomes. That is the only route from experienced intuition to evidenced advice, and it is buildable from tens of engagements rather than thousands.

Contract for the look-back. A brief follow-up at twelve and twenty-four months, agreed at the outset, costs little and produces the only validation this profession can obtain. It is also a service clients value, because they too would like to know.

## Impact If Solved
The recommendations produced by this work commit companies to expensive and often irreversible paths, and they rest on a few weeks of reading and conversation. A derived factual base makes the assessment faster and better-grounded without replacing the judgement clients are paying for, and a retained corpus turns a career's pattern recognition into something a firm owns and can hand on — which is also the difference between a practice and a person.
