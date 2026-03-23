# Alert Fatigue from False-Positive Findings

**Niche:** [[niches/cloud-infrastructure-consultants/cloud-security-compliance-auditors/profile|Cloud Security & Compliance Auditors]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** 40-60% of CSPM findings are false positives or irrelevant in context, but consultants cannot suppress them without risking missed real issues, so they review every finding manually.
**Tags:** #binary-classification #anomaly-detection #tabular-ml #worker-facing #automation

## The Problem
CSPM tools flag everything that deviates from best practices, regardless of context. A security group allowing port 443 from the internet is flagged as "High" even though it's intentionally serving a web application. An unencrypted EBS volume is flagged even though it contains only ephemeral build artifacts. Consultants review 500-2,000 findings per engagement and suppress 40-60% as false positives or accepted risks — but they must evaluate each one individually because the tools don't learn from previous suppression decisions.

## Why It's Still Broken
CSPM vendors don't build suppression intelligence because false-positive classification is context-dependent — the same configuration is acceptable in one environment but not another. Consultants maintain suppression lists per client in spreadsheets, but these lists go stale as environments change. There's no feedback loop from "this finding was suppressed last quarter" to "this finding should be auto-suppressed this quarter if the context hasn't changed."

## What a Fix Looks Like
A suppression intelligence layer that sits between CSPM tools and the consultant's review workflow. It learns from historical suppression decisions across engagements, identifies findings that match previously suppressed patterns (same resource type, same configuration, same business context), and auto-categorizes findings as "likely true positive," "likely false positive," or "new — requires review." Consultants review only the "new" and "likely true positive" categories, with the option to override any auto-classification.

## Who Feels the Pain
Junior security consultants who spend 2-3 full days per engagement reviewing findings they already know are irrelevant, before they can start doing the actual analysis work they were trained for.

## Impact If Fixed
Reduces finding review time by 50-60%, cuts per-engagement labor by 8-12 hours, and improves job satisfaction for junior consultants who currently spend more time on triage than on actual security analysis.
