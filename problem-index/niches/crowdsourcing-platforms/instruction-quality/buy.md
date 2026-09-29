# Buy: Survey and Experiment Design Tools Adapted to Paid Microtasks

**Niche:** [[niches/crowdsourcing-platforms/instruction-quality/profile|Instruction & Task Design Quality]]
**Industry:** [[industries/crowdsourcing-platforms|Crowdsourcing Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Survey platforms have decades of question-design guidance built in; none of it addresses a task where the respondent is paid per item and penalised for a wrong answer.
**Tags:** #large-language-models #evaluation-metrics #confidence-intervals #hypothesis-testing #descriptive-statistics #workflow-orchestration #automation #compliance
**Contested on:** Whether survey design methodology transfers to a paid task with a quality penalty attached.

## The Problem

Questionnaire design is a mature discipline with real tooling. Survey platforms offer question-type guidance, double-barrelled question detection, scale construction advice, piping and branching logic, pilot facilities and response quality checks, backed by a substantial methodological literature.

Much of it applies here and is unused, because crowdsourcing requesters mostly do not come from a survey background — they are ML engineers, researchers in other fields and product teams, writing labelling instructions rather than questionnaires. And the parts that do not apply are the parts that matter most: a survey respondent is not paid per item, not penalised for disagreeing with the majority, and not making a hundred judgements an hour under time pressure.

## What Already Exists

Qualtrics, SurveyMonkey and the survey platform category with design guidance and pilot tooling. Experiment design platforms serving academic research. The questionnaire methodology literature. Annotation guideline templates from the ML community. Readability and plain-language checkers.

## The Customization Gap

**The instruction is a specification, not a question.** Survey design guidance addresses individual question wording. A labelling task's instructions are a category scheme with boundaries, edge cases and a decision procedure, and the failure mode is an unspecified boundary rather than a leading question. Different defects, different detection.

**The respondent is paid per item and penalised for deviating.** That changes behaviour in ways survey methodology does not model: satisficing toward the expected majority answer rather than the considered one, speed pressure, and avoidance of items that look risky. Design guidance that ignores the incentive structure will miss the dominant effect.

**Piloting is cheap here and almost nobody does it.** Survey platforms encourage pilots and researchers run them. A crowdsourcing requester could pilot fifty items for a few dollars and find every ambiguity, and the platform flow does not prompt it. Making a pilot the default path rather than an option is a product change with a large effect.

**The requester is not a methodologist.** Survey tooling assumes some familiarity with the discipline. Here the guidance has to be delivered as specific in-context suggestions on the actual text, not as documentation or best-practice articles nobody reads.

**The quality evidence comes back from the platform, not from the survey tool.** Response patterns, agreement, timing and abandonment live in the crowdsourcing platform. Feeding them back into the design tool so the next batch is better requires an integration that does not exist.

## Target Customer

Survey and experiment tooling vendors, for whom crowdsourced task design is an adjacent market with the same underlying discipline and no incumbent. Also crowdsourcing platforms building a requester-side design experience, and academic requesters who already use both categories and get no connection between them.

## Impact If Solved

The question-design methodology, pilot facilities, branching logic and readability tooling get reused, and the specification-shaped defects, incentive-aware design, default piloting, in-context guidance and response-pattern feedback get built. Concretely: a requester who writes clear instructions the first time because the tool told them what was ambiguous.
