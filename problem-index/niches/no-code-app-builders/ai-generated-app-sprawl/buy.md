# Policy-as-Code Applied to Generated Applications

**Niche:** [[niches/no-code-app-builders/ai-generated-app-sprawl/profile|AI-Generated App Sprawl]]
**Industry:** [[industries/no-code-app-builders|No-Code App Builders]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Infrastructure as code is checked against policy before it is applied, by mature open tooling, and generated applications go live with no check at all.
**Tags:** #graph-theory #large-language-models #decision-trees #logistic-regression #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor here is fighting to make a generated application ownable — attributable, reviewable and maintainable — at the rate generation now produces them, and whoever does that takes the enterprise account, because generation without ownership is a governance problem arriving faster than any governance process.

## The Problem
Cloud infrastructure defined as code is evaluated against policy before it is provisioned: no public storage buckets, no unencrypted volumes, no overly permissive roles. The tooling is mature, open and standard practice. A generated application, which is also a declarative definition being applied to a running environment, is subject to no equivalent check anywhere, and can go live with a public form collecting personal data in under a minute.

## What Already Exists
Policy-as-code engines with declarative rule languages and large rule libraries; admission control patterns from container orchestration; infrastructure-as-code scanning tools; data classification for identifying sensitive fields; and secrets detection. All open, all mature, all designed for exactly the shape of problem — evaluating a declarative definition against rules before it takes effect.

## The Customization Gap
The adaptation is to application definitions and non-technical authors. It requires: (1) a policy model over app concepts — sharing scope, field sensitivity, external connections, automation side effects, credential usage — which is a different vocabulary from infrastructure and needs defining once per platform; (2) field-level data classification, since the highest-value rules concern what is collected and a rule engine cannot evaluate that without knowing a field holds a national identifier; (3) remediation in plain language, because the author cannot act on a policy violation message and the useful output is "this form is publicly accessible and collects dates of birth; make it internal?" with a one-click fix; (4) advisory-by-default enforcement with a small blocking set, since hard-blocking a business user drives them to a personal account and loses the visibility entirely, which is the failure every governance attempt in this category has made; and (5) evaluation at generation time as part of the flow rather than as a later scan, because the moment of creation is the only point where correction is free.

## Target Customer
No-code platform vendors, cloud security posture and policy vendors with an adjacent market, and enterprise governance teams.

## Impact If Solved
A mature pre-deployment policy discipline maps directly onto declarative app definitions and has not been applied. Field-level classification and plain-language remediation are the adaptations, and advisory-first enforcement is what keeps the estate visible.
