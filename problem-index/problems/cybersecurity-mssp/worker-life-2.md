# Security Engineer Repetitive Playbook Execution

**Industry:** [[cybersecurity-mssp|Cybersecurity MSSPs]]
**Type:** Worker Life Changing
**One-liner:** Security engineers stop being human SOAR platforms — copying IOCs between consoles, running the same containment steps for the hundredth phishing incident, and manually updating tickets with timestamps they already know.
**Tags:** #llm #automation #nlp #worker-facing #workflow-orchestration

## The Problem
When an alert escalates to incident response, security engineers execute predefined playbooks: isolate the endpoint via EDR, block the source IP at the firewall, disable the compromised user account in Active Directory, pull forensic artifacts, query threat intel for IOC enrichment, update the ticket with each action and timestamp, and notify the client. For common incident types — phishing with credential compromise, malware download, brute force attempt — these playbooks are well-documented and nearly identical every time. Yet engineers execute them manually, alt-tabbing between 4-6 tool consoles, copying IOCs from one interface to another, and writing the same incident narrative with slightly different IPs and usernames. A single phishing response playbook takes 45-90 minutes of manual execution, and an engineer might run 3-5 per day.

## Why It Matters to the Worker
Security engineers trained in threat analysis, forensics, and architecture spend 60-70% of their day on mechanical playbook execution rather than engineering work. They describe feeling like "clipboard operators" — copying data between systems that should talk to each other. The repetitive nature leads to errors: a missed containment step, a wrong IP pasted into a firewall rule, a client notification sent with the wrong incident details. These errors create rework and erode the engineer's professional confidence. Engineers who wanted to build detection logic, architect security infrastructure, or hunt advanced threats find themselves stuck in an execution loop.

## What a Solution Looks Like
An LLM-orchestrated automation layer that takes a confirmed alert with its context, identifies the appropriate playbook, executes each step via API (EDR isolation, firewall block, AD disable, threat intel lookup), compiles a timestamped incident narrative, and presents the complete response package to the engineer for review and approval before client notification. The engineer reviews a summary of actions taken rather than performing them one by one. For novel or complex incidents that don't match a standard playbook, the system drafts a proposed response plan that the engineer can modify.

## Impact If Solved
Reclaims 4-5 hours per engineer per day from mechanical execution, redirecting it to detection engineering, threat hunting, and client advisory — the high-value work that retains talent and grows MSSP revenue. Reduces playbook execution errors by 90% by eliminating manual copy-paste across consoles.
