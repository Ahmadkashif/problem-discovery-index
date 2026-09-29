# The Answer From the Employee's Own Record

**Niche:** [[niches/hr-tech-platforms/employee-facing-hr-tools/profile|Employee-Facing HR Tools]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** An employee's question about their own employment has an exact answer derivable from their record and the policy in force, and the product returns a policy document for them to interpret.
**Tags:** #large-language-models #bert #evaluation-metrics #confidence-intervals #compliance #workflow-orchestration #worker-facing #automation
**Contested on:** Every serious competitor building employee-facing HR software is fighting to let an employee answer a question about their own employment without asking a person — and whoever answers accurately from the employee's own record takes the deployment.

## The Problem
An employee asks how much parental leave they are entitled to. The correct answer depends on their location, their tenure, their employment type, the company policy version applicable to them, the statutory entitlement in their jurisdiction and how the two interact, and whether they have taken any already. The portal returns a six-page policy document written for all employees in all locations. The employee reads it, is unsure, and emails HR, who computes the answer in four minutes and replies the next day. This exchange happens thousands of times a year in a large organisation, and the underlying computation is deterministic.

## Why Nobody Has Built This
Personal answers require reasoning over the individual's record against a policy, which means the policy has to be represented as something executable rather than as a document — which is the same representation problem that appears in the compliance sub-niche and in rate filing and court rules elsewhere in this vault. It also requires being right, since an incorrect answer about a statutory entitlement has consequences and the organisation is accountable for it. The chatbot deployments that retrieved policy text avoided both problems and delivered correspondingly little value, which has left the category with a credibility problem that a better product has to overcome.

## What to Build
An answering layer that reasons over the employee's own record. Policies are represented as parameterised rules with their applicability conditions — location, tenure, employment type, plan, effective dates — rather than as documents, which is the load-bearing investment. The employee's record supplies the parameters. The answer is specific and includes the arithmetic and the provenance: this is your entitlement, computed from these facts, under this policy version and this statutory floor, and here is the clause. Where an answer depends on a judgement or an exception, it routes to a person with everything assembled rather than guessing — and the product's willingness to say it does not know is what makes the rest trustworthy. The answer is delivered in the employee's language. Every answer is logged with its inputs, which gives the organisation something it has never had: a record of what it told an employee, when, and on what basis.

## Target Customer
HCM vendors, HR service delivery platforms, and large employers whose HR service desks handle high volumes of personal lookup questions.

## Impact If Built
The volume is large and the answers are deterministic, so the capacity return to the HR function is substantial. The employee-side benefit is larger and less often counted: an immediate, correct, traceable answer to a question about your own employment, in your own language, at the moment you need it, replaces a wait and an interpretation of a document written for somebody else.
