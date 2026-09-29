# Retrieval and Grounding Infrastructure Already Commodity

**Niche:** [[niches/hr-tech-platforms/employee-facing-hr-tools/profile|Employee-Facing HR Tools]]
**Industry:** [[industries/hr-tech-platforms|HR Tech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Grounded question answering over a customer's own records and documents is standard infrastructure across consumer support, and HR deployed the previous generation of it as a chatbot that returns policy paragraphs.
**Tags:** #large-language-models #bert #transformers #evaluation-metrics #confidence-intervals #workflow-orchestration #compliance #automation
**Contested on:** Every serious competitor building employee-facing HR software is fighting to let an employee answer a question about their own employment without asking a person — and whoever answers accurately from the employee's own record takes the deployment.

## The Problem
The HR chatbot deployed three years ago matches keywords to knowledge base articles and returns them. Employees learned quickly that it does not answer their question and route around it to a person. The organisation records low adoption and concludes employees prefer human support, which is the wrong conclusion — they prefer correct answers, and a retrieval system that returns documents when asked a personal question is not answering.

## What Already Exists
Retrieval-augmented generation over a customer's own data is standard practice with mature tooling, and the pattern for grounding an answer in retrieved records with citation is well established. Multilingual support is commodity. Escalation with context preservation is a solved workflow. Evaluation frameworks for grounded question answering — faithfulness, answer correctness, citation accuracy — are published and implementable. Everything needed is available and most of it is newer than the chatbot deployments it would replace.

## The Customization Gap
The adaptation is to a domain where a wrong answer affects someone's entitlements. It requires: (1) grounding in the employee's structured record as well as in policy text, since almost every real question is personal and a document-only retrieval cannot answer it — this is the distinction the previous generation missed; (2) a hard boundary between stating a policy and giving advice, particularly on anything touching statutory rights, benefits elections or employment terms, where the system should inform and route rather than counsel; (3) policy versioning with effective dates, so an answer about a past period uses the policy that applied then, which matters for leave, accrual and equity questions and is routinely wrong today; (4) evaluation against a curated question set with known correct answers, run continuously, because an HR answering system's error rate is a number the organisation must know and currently nobody measures; and (5) escalation that carries the full context and the attempted answer, so an employee who needs a person does not start over.

## Target Customer
HCM and HR service delivery vendors, large employers with HR service centres, and the shared services functions whose ticket volume is dominated by lookups.

## Impact If Solved
The infrastructure is commodity and the previous generation's failure was a design choice rather than a capability limit. Grounding in the individual's record is the specific change that converts a disliked chatbot into something employees use, and continuous evaluation against known answers is what makes it safe to deploy on questions that affect people's entitlements.
