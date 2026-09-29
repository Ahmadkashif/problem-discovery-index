# The Bordereau Everybody Rebuilds

**Niche:** [[niches/insurtech-platforms/mga-program-business/profile|MGA & Programme Business]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** An MGA sends a bordereau, the carrier's analyst rebuilds it into their own format, the reinsurer's analyst rebuilds it again, and all three parties spend the month maintaining three versions of the same facts.
**Tags:** #data-integration #descriptive-statistics #evaluation-metrics #hypothesis-testing #compliance #workflow-orchestration #automation #quick-win
**Contested on:** Every serious competitor serving MGAs is fighting to give a programme a reliable loss ratio signal early enough to correct it — and whoever shortens the time from inception to a trustworthy performance picture takes the programme.

## The Problem
The same programme's policy and claim records exist in the MGA's system, in the carrier's data warehouse after transformation, and in the reinsurer's after another transformation. They disagree — on counts, on premium, on the treatment of endorsements and cancellations, on which claims are in which period — and reconciling the disagreements is a recurring monthly conversation between three analysts who all believe their own version. Nobody's version is authoritative because no arrangement designated one, and each transformation introduced its own assumptions that were never written down.

## Why It's Still Broken
Each party built its ingestion independently, to answer its own questions, at a time when the relationship was new and nobody anticipated the reconciliation burden. The transformations encode assumptions — how a mid-term endorsement is attributed to a period, how a reopened claim is treated, how reinstatement premium is handled — that live in code and in analysts' heads rather than in the delegated authority agreement, which specifies commercial terms and says little about data semantics. So the disagreement is structural and recurs every month.

## What a Fix Looks Like
Agree the semantics once and reconcile automatically. The definitions that cause the disagreements — period attribution, endorsement treatment, claim status transitions, currency and timing conventions — are written down as part of the programme's data specification rather than discovered through argument, which is a document nobody currently produces and which takes an afternoon. Automated reconciliation runs each cycle and reports differences by cause rather than as a total, so the conversation starts from "these fourteen endorsements are attributed differently" rather than from "our numbers do not match." Designate an authoritative source per field explicitly, which is usually the MGA for policy data and the carrier or administrator for claims, and stop maintaining parallel derivations of the other party's data. Retain the reconciliation history, since a recurring difference type is a specification gap rather than an error and should be closed rather than re-argued.

## Who Feels the Pain
Analysts at three organisations reconciling the same programme monthly; MGA leadership whose performance conversations begin with a data dispute; and the underwriting decisions that wait for a number three parties are arguing about.

## Impact If Fixed
A written data specification and automated reconciliation removes a recurring monthly dispute from every delegated authority relationship and shortens the path to an agreed number, which is the precondition for acting on it. The specification is the cheap part and is the one thing every one of these arrangements lacks.
