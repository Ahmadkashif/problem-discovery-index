# Startup-Scale IaC Blueprints

**Niche:** [[niches/cloud-infrastructure-consultants/startup-devops-teams/profile|Startup DevOps Teams]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Gruntwork and Terraform Registry provide production-grade IaC modules, but they're designed for enterprise environments and are over-engineered for a 5-person startup that needs a simple, cheap, maintainable setup.
**Tags:** #automation #workflow-orchestration #quick-win

## The Problem
Startup DevOps engineers cobble together Terraform from blog posts, StackOverflow, and Gruntwork modules to build their infrastructure. The result is either over-engineered (multi-AZ, auto-scaling, full service mesh for an app with 100 users) or dangerously under-engineered (single instance, no backups, root credentials in environment variables). There's no "right-sized" starting point that matches a startup's actual needs and grows with them.

## What Already Exists
Gruntwork's Reference Architecture provides enterprise-grade IaC. Terraform Registry has thousands of community modules. Render, Railway, and Fly.io offer PaaS alternatives. But Gruntwork costs $8K+/year and is overkill for seed-stage startups, community modules vary wildly in quality, and PaaS platforms create lock-in that becomes painful at Series B scale.

## The Customization Gap
The missing product is a curated set of stage-appropriate IaC blueprints — "Series A on AWS" gives you a single-AZ ECS setup with RDS, basic monitoring, and automated backups for $800/month. "Series B on AWS" upgrades to multi-AZ, adds a CDN, proper secrets management, and CI/CD. Each blueprint includes a migration path to the next stage, so the startup never has to tear down and rebuild. The blueprints must be simple enough for a junior DevOps engineer to understand and modify.

## Target Customer
DevOps consultants serving startup portfolios who want to standardize their delivery across clients and reduce per-client setup time from 40 hours to 8 hours.

## Impact If Solved
Reduces initial infrastructure setup from 2 weeks to 2 days, saves startups $5K-$15K in consulting fees, and provides a clean upgrade path that prevents the "rip and replace at Series B" pattern that wastes 2-3 months of engineering time.
