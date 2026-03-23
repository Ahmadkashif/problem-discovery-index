# Compliance-as-Code Documentation Generator

**Niche:** [[niches/cloud-infrastructure-consultants/regulated-industry-cloud/profile|Regulated-Industry Cloud]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool today can read a Terraform/CloudFormation deployment and automatically generate the regulatory compliance documentation (System Security Plan, risk assessments, control matrices) that auditors require.
**Tags:** #llm #text-generation #nlp #compliance #automation

## The Problem
When consultants deploy cloud infrastructure for regulated clients, they must produce compliance documentation that maps every infrastructure component to specific regulatory controls. A FedRAMP System Security Plan runs 200-400 pages. A HIPAA risk assessment requires mapping each AWS service to specific safeguard requirements. Consultants write these documents manually in Word, cross-referencing Terraform code and AWS console screenshots — a process that takes 80-160 hours per engagement and must be repeated whenever infrastructure changes.

## Why Nobody Has Built This
Compliance documentation requires understanding both the technical infrastructure (what was deployed) and the regulatory framework (what controls apply). Mapping between these domains is contextual — the same S3 bucket may require different compliance justifications depending on what data it stores. Previous automation attempts produced templates, not contextual documentation, because they couldn't reason about the relationship between infrastructure design decisions and regulatory requirements.

## What to Build
A tool that ingests IaC definitions (Terraform, CloudFormation, Pulumi), maps each resource to the applicable regulatory framework's controls, and generates audit-ready documentation with specific justifications for each control. The system understands that an encrypted S3 bucket with versioning enabled satisfies HIPAA §164.312(a)(2)(iv) and can articulate why in the language auditors expect. Output is a living document that auto-updates when infrastructure changes.

## Target Customer
Cloud compliance consultants producing 10+ System Security Plans or risk assessments per year for regulated clients, currently spending 100+ hours per document.

## Impact If Built
Reduces compliance documentation from 120 hours to 20 hours per engagement, saving $20K-$40K in consultant labor per project and ensuring documentation stays current with infrastructure changes.
