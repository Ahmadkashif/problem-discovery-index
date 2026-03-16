# IaC Template Generation for Common Patterns

**Industry:** [[cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Generic IaC generators produce syntactically correct Terraform/CloudFormation but miss the firm's naming conventions, security baselines, and client-specific module patterns — engineers spend 40% of their time fixing generated code.
**Tags:** #llm #text-generation #nlp #automation

## The Problem
Cloud consultants build Terraform modules, CloudFormation stacks, and Pulumi programs for every client engagement. Common patterns recur — VPC with public/private subnets, EKS cluster with managed node groups, RDS with Multi-AZ failover — but each client has unique requirements around naming conventions, tagging policies, security group rules, and compliance constraints. Engineers either start from scratch or copy-paste from a previous project and spend hours adapting it, introducing drift from the firm's internal standards.

## What Already Exists
GitHub Copilot, Amazon CodeWhisperer, and generic LLM-based code generation tools can produce syntactically valid Terraform or CloudFormation. Terraform Registry provides community modules. However, these tools have no awareness of a firm's internal module library, client-specific variable naming patterns, required tagging schemas (e.g., every resource must carry cost-center, environment, and owner tags), or the firm's security baselines (e.g., no public S3 buckets, all RDS encrypted with customer-managed KMS keys).

## The Customisation Gap
The tool needs to be fine-tuned or RAG-augmented on the firm's existing module library (typically 50-200 internal Terraform modules), client configuration profiles (tagging requirements, naming conventions, approved instance types), and compliance rule sets (CIS benchmarks mapped to specific Terraform resource configurations). It must generate code that passes the firm's existing CI/CD validation pipeline — `tflint`, `checkov`, and custom OPA policies — on the first attempt, not after three rounds of manual fixes.

## Impact If Solved
Engineers save 4-8 hours per new environment setup. A firm running 10 new deployments per month reclaims 40-80 engineering hours — roughly one full-time junior engineer's capacity redirected from boilerplate to architecture work.
