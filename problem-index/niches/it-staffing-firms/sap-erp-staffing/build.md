# ERP Consultant Project Genealogy Graph

**Niche:** [[niches/it-staffing-firms/sap-erp-staffing/profile|SAP/ERP Implementation Staffing]]
**Industry:** [[industries/it-staffing-firms|IT Staffing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No product maps the relationship graph between ERP consultants, the implementations they have worked on, and the teams they have worked with — the most valuable sourcing signal in ERP staffing.
**Tags:** #graph-ml #recommendation #tacit-knowledge-ml #revenue-impact

## The Problem
The strongest signal for a successful ERP implementation placement is not the consultant's resume — it is which projects they have completed and which team leads they have worked under. An SAP FI/CO consultant who did a successful S/4HANA migration at a $2B manufacturer under a specific program director is the ideal candidate for that same director's next engagement. Experienced ERP staffing recruiters carry this "project genealogy" in their heads — they know who worked with whom, on what, and how it went. When the recruiter leaves, this institutional knowledge vanishes.

## Why Nobody Has Built This
The data is distributed across individual consultant resumes, recruiter notes, and LinkedIn endorsements with no structured representation. Building the graph requires extracting project references from unstructured text (resumes, reference checks), disambiguating project names (the same SAP implementation is called different things by different participants), and linking consultants to shared project nodes. The ERP consulting community is also relationship-sensitive — consultants resist being "cataloged" in ways that might bypass their preferred recruiters.

## What to Build
A knowledge graph that links ERP consultants to projects, projects to clients and outcomes, and consultants to each other through shared project experience. The system should ingest consultant resumes and project debriefs, build the graph incrementally, and enable queries like "find me an SAP PP consultant who has worked on S/4HANA brownfield migrations in discrete manufacturing with this team lead." Includes team chemistry signals based on repeated collaborations.

## Target Customer
Specialized ERP staffing firms with 20+ years of placement history sitting in unstructured recruiter notes and legacy databases.

## Impact If Built
Reduces time-to-fill for senior ERP consultant roles from 4-6 weeks to 1-2 weeks by surfacing relationship-qualified candidates. Captures $500K-$1M+ in institutional knowledge per senior recruiter departure.
