# IaC Drift Remediation

**Parent Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Category:** Highly Automatable

## Profile
**Market Size:** $1.5B
**Share of Parent Industry:** 3%
**Digital Adoption:** Medium — most teams use Terraform or CloudFormation but lack drift detection and auto-remediation pipelines
**Target Buyer:** Platform Engineering Manager / DevOps Lead at organizations with 50+ IaC-managed resources
**Automation Potential:** High — drift detection is fully automatable, and 70% of drift events can be auto-remediated by re-applying the declared state

## What Makes This a Distinct Niche
IaC drift — when the actual cloud infrastructure state diverges from the declared IaC state — is a universal problem that consultants encounter in every engagement but few specialize in. Drift occurs when engineers make console changes, automated processes modify resources, or provider-side changes alter configurations. Left unaddressed, drift erodes the reliability of IaC, making future deployments unpredictable and audit evidence unreliable. This niche is distinct because it's a continuous operational problem, not a one-time project — creating a recurring consulting engagement model.

## Current Tools & Gaps
Terraform plan detects drift at apply time, and tools like Driftctl, Spacelift, and env0 provide drift detection. However, detection is only half the problem — remediation requires understanding whether the drift was intentional (an engineer made a hotfix) or accidental (a misconfigured automation modified a resource). No tool handles the "intent classification" step between detection and remediation.

## Problems
- [[niches/cloud-infrastructure-consultants/iac-drift-remediation/build|🔨 Build: Intent-Aware Drift Classification]]
- [[niches/cloud-infrastructure-consultants/iac-drift-remediation/buy|🛒 Buy: Continuous Drift Monitoring Dashboards]]
- [[niches/cloud-infrastructure-consultants/iac-drift-remediation/fix|🔧 Fix: Console-Click Configuration Leakage]]
