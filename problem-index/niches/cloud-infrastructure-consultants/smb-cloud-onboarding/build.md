# SMB Cloud Readiness Self-Assessment

**Niche:** [[niches/cloud-infrastructure-consultants/smb-cloud-onboarding/profile|SMB Cloud Onboarding]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool lets an SMB owner with zero technical background assess their own cloud readiness and get a migration plan without paying for a consultant's discovery phase.
**Tags:** #llm #text-generation #quick-win #automation #ai-agent

## The Problem
SMB owners know they "should move to the cloud" but have no way to evaluate what that means for their specific setup — a file server under the reception desk, an old Exchange box, three line-of-business applications, and a NAS drive everyone uses for file sharing. Consultants charge $3K-$8K just for the discovery/assessment phase, which prices out most SMBs. The result is paralysis: businesses stay on aging on-prem infrastructure until something breaks.

## Why Nobody Has Built This
Enterprise cloud assessment tools (Movere, CloudSphere) are designed for environments with hundreds of servers and assume a technical operator. Building a self-service tool for non-technical users requires translating infrastructure concepts into business language, handling the enormous variety of SMB setups (every small office is different), and providing actionable recommendations without on-site access to the environment.

## What to Build
A guided self-assessment tool where the SMB owner answers plain-language questions about their IT setup ("Do you have a server in your office?", "How do employees access files?", "What software do you use daily?"). The system maps answers to a standard infrastructure profile, identifies cloud equivalents for each component, estimates migration cost and timeline, and generates a scoped migration plan the owner can hand to any consultant — or use to self-migrate for simple scenarios.

## Target Customer
IT consultants serving the SMB market who want to automate the discovery phase and close deals faster, or SMB owners directly who want to understand their options before engaging a consultant.

## Impact If Built
Reduces SMB assessment cost from $5K to $200, making cloud migration accessible to the 4 million US SMBs currently priced out of consulting-led migrations.
