# Knowledge Elicitation and Rubric Design

**Niche:** [[niches/ai-model-evaluation-firms/domain-grading-criteria/profile|Domain Grading Criteria]]
**Industry:** [[industries/ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Expert systems, educational assessment and clinical guideline development each spent decades on extracting criteria from specialists, and this industry runs unstructured interviews.
**Tags:** #tacit-knowledge-ml #hypothesis-testing #confidence-intervals #evaluation-metrics #descriptive-statistics #compliance #worker-facing #probability-distributions
**Contested on:** Every serious competitor in this niche is fighting to capture what a specialist means by correct in their own field, once, in a form that can grade at scale — and whoever does that takes the account, because the harness is free and the criteria are the product.

## The Problem
Getting decision criteria out of an expert who cannot fully articulate them is a studied problem with a literature. Knowledge engineering developed structured elicitation techniques and learned exactly why interviews fail. Educational assessment developed analytic rubric design with validated construction procedures and inter-rater reliability practice. Clinical guideline development built formal consensus methods for exactly the situation where experts disagree and a standard is still needed. This industry books a call with a specialist and takes notes.

## What Already Exists
Structured knowledge elicitation techniques including repertory grids, critical decision method and card sorting; analytic rubric construction and validation practice from educational assessment; inter-rater reliability methodology with appropriate agreement statistics; formal consensus methods including Delphi and nominal group technique; and cognitive task analysis for capturing expert decision-making.

## The Customization Gap
The adaptation is to criteria that must be executable by a grader at scale. It requires: (1) rubrics precise enough for a model or a non-expert to apply consistently, which is a much harder constraint than a human expert rubric and is where most of the design effort actually goes; (2) formal consensus where experts genuinely disagree, since the current practice of using one expert's opinion as ground truth conceals real disagreement that the consensus literature knows how to surface and handle — adopting this would materially change what these firms can claim; (3) elicitation focused on boundary cases rather than typical ones, because the typical case is easy and the rubric's value is entirely at the margin; (4) iterative validation against held-out cases with measured agreement, which assessment does routinely and evaluation firms do informally if at all; and (5) capturing the expert's confidence and the case's inherent ambiguity, since some cases have no agreed answer and a rubric that pretends otherwise manufactures precision.

## Target Customer
Evaluation firms, regulated industry buyers, the domain experts being interviewed, and the assessment and knowledge engineering communities.

## Impact If Solved
Decades of elicitation and rubric methodology exist and the practice is an unstructured interview. Formal consensus methods would surface the expert disagreement that single-expert ground truth currently hides, which changes what these firms can honestly claim.
