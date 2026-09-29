# Domain-Specific Grading Criteria

**Industry:** [[ai-model-evaluation-firms|AI Model Evaluation Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Evaluation harnesses are mature and free, and the grading criteria that decide whether an answer is actually correct in radiology or tax or contract review must be authored by a domain expert every single time.
**Tags:** #large-language-models #bert #hypothesis-testing #confidence-intervals #evaluation-metrics #transfer-learning #tacit-knowledge-ml

## The Problem
Running an evaluation is easy. Frameworks handle prompt templating, model invocation, retries, parallelism, result storage and comparison across model versions. Several are open source and good.

Deciding whether an output is correct is the entire difficulty, and it is domain-specific in a way no framework can absorb. For a maths problem the answer is checkable. For a radiology report, correctness depends on whether the clinically significant findings are present, whether an incidental finding was appropriately flagged, and whether the hedging matches the diagnostic uncertainty — judgements a radiologist makes and a rubric struggles to encode.

So each new domain begins with a domain expert authoring criteria. What counts as a correct tax position given ambiguous facts. Which contract clause omissions are material. Which parts of a legal summary must be present. This takes weeks, produces a rubric that is immediately found to be underspecified when graders disagree, and gets revised repeatedly during the evaluation itself.

The rubric then feeds an LLM-as-judge, which applies it inconsistently in ways that are hard to characterise, or human raters, who apply it inconsistently in ways that are hard to characterise.

## What Already Exists
Open evaluation harnesses (lm-evaluation-harness, HELM, OpenAI Evals, Inspect) handle mechanics comprehensively. Braintrust, Langfuse, Patronus and Galileo provide commercial platforms with tracing, regression testing and judge orchestration. LLM-as-judge is well studied with its biases documented. Rubric-based human evaluation methodology is mature in education and psychometrics. Clinical quality measures encode correctness criteria in some medical contexts.

## The Customisation Gap
The harness is the commodity and the rubric is the product, and nothing helps with the rubric. Criteria are authored on a blank page by someone whose expertise is the domain rather than assessment design, and the resulting rubrics have the predictable faults — ambiguous language, criteria that are not independent, no guidance on edge cases.

Nothing learns across domains. The structure of a good rubric is largely domain-general, the firm has authored hundreds, and the four-hundredth starts from nothing.

Rubric quality is unmeasured. Whether criteria produce reliable grading is directly testable — inter-rater reliability per criterion, criterion-level disagreement analysis — and a criterion that generates systematic disagreement is defective, not merely difficult. That diagnosis exists in psychometrics and is not applied here.

Judge validation is the third gap. An LLM-as-judge is deployed against a rubric with, at best, a small agreement check against human grades. Whether it applies each criterion consistently, whether it exhibits position or length or self-preference bias on this rubric, and where its errors concentrate are all measurable and rarely measured.

## Impact If Solved
Rubric construction sits on the critical path of every domain evaluation and determines the validity of everything downstream. Generating draft criteria from prior rubrics and diagnosing criterion reliability turns weeks of expert authoring into review, and it fixes the defective criteria that currently corrupt results silently.
