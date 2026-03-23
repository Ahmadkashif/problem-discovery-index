# Regulatory-Aware Architecture Templates

**Niche:** [[niches/cloud-infrastructure-consultants/regulated-industry-cloud/profile|Regulated-Industry Cloud]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** AWS Well-Architected Framework and Azure Landing Zones provide reference architectures but don't encode regulatory constraints, forcing consultants to manually layer compliance requirements on top of generic designs.
**Tags:** #compliance #automation #workflow-orchestration #data-integration

## The Problem
Consultants designing cloud architectures for regulated industries start with generic reference architectures (AWS Landing Zone, Azure Enterprise-Scale) and then spend weeks modifying them to meet regulatory requirements — adding encryption, restricting regions, configuring logging, implementing data residency controls. Each regulatory framework (HIPAA, FedRAMP, PCI-DSS) has different requirements, and consultants maintain their own internal libraries of "compliant architecture patterns" as tribal knowledge.

## What Already Exists
AWS provides Well-Architected Framework lenses for specific industries, and Azure has compliance blueprints. Terraform Registry has community modules for compliance-oriented deployments. However, these are starting points, not complete solutions — a FedRAMP-compliant AWS landing zone requires 200+ specific configuration decisions that no single template covers, and consultants must validate each decision against the current version of the regulatory framework.

## The Customization Gap
The missing piece is a library of fully validated, regulation-specific IaC templates that encode every required control as infrastructure code, with inline documentation explaining which regulatory requirement each configuration satisfies. Templates need to be parameterized by regulatory framework, data classification level, and cloud provider — and they need to be maintained as regulations update (NIST 800-53 rev 5 vs. rev 4, HIPAA Safe Harbor updates).

## Target Customer
Cloud architecture consultants specializing in regulated industries who design 5-15 compliant environments per year and currently spend 3-4 weeks on compliance hardening per deployment.

## Impact If Solved
Reduces compliance-hardening phase from 3 weeks to 3 days, eliminates common misconfigurations that cause audit findings, and provides a defensible paper trail showing exactly how each regulatory control is implemented.
