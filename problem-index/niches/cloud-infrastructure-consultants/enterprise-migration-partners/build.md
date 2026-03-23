# Automated Application Dependency Discovery

**Niche:** [[niches/cloud-infrastructure-consultants/enterprise-migration-partners/profile|Enterprise Migration Partners]]
**Industry:** [[industries/cloud-infrastructure-consultants|Cloud Infrastructure Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool today can automatically map application-level dependencies across heterogeneous enterprise environments without weeks of manual interviews.
**Tags:** #graph-ml #anomaly-detection #data-integration #tacit-knowledge-ml #automation

## The Problem
Enterprise migration consultants spend 30-40% of every engagement manually discovering which applications talk to which databases, APIs, and file shares. This involves interviewing dozens of application owners, parsing outdated CMDB records, and running network flow analysis — then reconciling all three sources. The process takes 6-12 weeks for a 500-server environment and is still wrong 15-20% of the time.

## Why Nobody Has Built This
Existing tools like AWS Application Discovery Service capture network flows but cannot distinguish between active dependencies and incidental traffic (e.g., monitoring pings vs. critical API calls). The real challenge is semantic: understanding which connections are load-bearing requires combining network data with application configuration files, deployment manifests, and runtime behavior — a multimodal problem that crosses too many vendor boundaries for any single cloud provider to solve.

## What to Build
An agent-based discovery platform that installs lightweight collectors on target servers, ingests network flows, parses configuration files (web.config, application.yml, .env), and builds a weighted dependency graph. The system uses graph ML to identify clusters of tightly coupled applications and flag likely missing edges based on structural patterns. Output is a migration-ready dependency map with confidence scores per edge.

## Target Customer
Migration practice leads at consulting firms running 10+ enterprise migrations per year, each with 200+ workloads. These buyers will pay $50K-$150K per engagement for a tool that cuts discovery time by 60%.

## Impact If Built
Reduces discovery phase from 8 weeks to 3 weeks per engagement, saving $200K-$400K in consultant labor per project and improving dependency accuracy from 80% to 95%+.
