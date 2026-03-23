# MEP Clash Triage and Auto-Resolution Engine

**Niche:** [[niches/engineering-consultants/mep-design-firms/profile|MEP Design Firms]]
**Industry:** [[industries/engineering-consultants|Engineering Consultants]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A system that automatically classifies BIM clashes by severity, groups related clashes into actionable clusters, and proposes routing alternatives for the 70% of clashes that follow repeatable resolution patterns.
**Tags:** #cnn #multiclass-classification #computer-vision #automation #tacit-knowledge-ml

## The Problem
Navisworks clash detection on a mid-size commercial building generates 2,000-10,000 clash instances, of which 60-80% are false positives (cosmetic overlaps, tolerance violations, or clashes that will resolve during construction). MEP coordinators spend 15-25 hours per project manually reviewing each clash, classifying severity, grouping related clashes into resolution clusters, and proposing routing changes. Experienced coordinators can glance at a clash and instantly know whether it is a real conflict requiring rerouting or a false positive to dismiss — this pattern recognition, built over thousands of reviews, is never captured.

## Why Nobody Has Built This
BIM clash detection tools report geometry intersections but lack the engineering context to judge severity. A duct crossing a structural beam by 2mm is a Navisworks clash but not a real-world problem. Classifying severity requires understanding MEP system hierarchy (gravity drains can't move; flex ducts can), construction sequencing, and trade priority — domain knowledge that lives in senior coordinators' heads, not in software. Building this requires labeled datasets of clash resolutions from real projects, which firms have never systematically captured.

## What to Build
A classification model that ingests Navisworks clash reports (with 3D coordinates, element types, and system metadata) and outputs: severity rating (critical / minor / false-positive), cluster grouping (related clashes that resolve together), and for minor clashes, a proposed resolution (reroute path or offset adjustment). The model trains on historical clash resolution logs where coordinators recorded their decisions. An interactive 3D viewer highlights only critical clashes, reducing the coordinator's review set from thousands to dozens.

## Target Customer
MEP coordination leads and BIM managers at 15-50 person MEP firms running 10+ active projects with Navisworks or BIM 360 clash detection, currently spending 1-2 full days per project on clash review.

## Impact If Built
Reduces clash review time from 15-25 hours to 3-5 hours per project. For a firm running 20 projects/year, this recovers 200-400 hours of senior coordinator time annually — worth $30,000-60,000 in billable capacity at typical MEP billing rates.
