# Implant Surface Defect Detection System with FDA-Validatable Architecture

**Niche:** [[niches/medical-device-mfg/class-ii-implantable-devices/profile|Class II Implantable Device Manufacturers]]
**Industry:** [[industries/medical-device-mfg|Medical Device Manufacturing]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No vision-based inspection system exists that is architected from the ground up for FDA computer system validation (21 CFR Part 11/Part 820), enabling implant manufacturers to deploy ML-assisted inspection without a 12-month validation project.
**Tags:** #cnns #object-detection #tacit-knowledge-ml #compliance #worker-facing

## The Problem
Quality inspectors examine implant surfaces (polished titanium hip stems, PEEK spinal cages, cobalt-chrome knee components) under 10-40x magnification for scratches, pitting, particulate inclusions, and dimensional anomalies. This inspection takes 2-5 minutes per unit and accuracy degrades after 2-3 hours due to visual fatigue. The skill itself takes 12-18 months to develop — an experienced inspector recognizes acceptable surface variation versus rejectable defects at a glance, while a new inspector over-rejects, consuming rework capacity on units that are actually acceptable.

## Why Nobody Has Built This
General-purpose machine vision companies (Cognex, Keyence) sell defect detection hardware, but their software is not designed for FDA-regulated environments — deploying them as quality-critical inspection tools requires a full computer system validation (CSV) that device companies lack the internal expertise to execute. The validation requires documented model performance specifications, ongoing monitoring of model drift, and change control procedures for model updates. No vendor has built this regulatory wrapper natively into a vision inspection product.

## What to Build
A vision inspection platform specifically designed for FDA-regulated manufacturing: pre-validated model architecture with documented performance specs per device family, built-in monitoring for model drift with automatic alerting, change control workflow for model retraining that generates the validation documentation (IQ/OQ/PQ protocols and reports) automatically, and an audit trail compliant with 21 CFR Part 11. The system operates as a screening aid (human inspector makes final accept/reject decision on flagged units), sidestepping the most burdensome validation requirements while still reducing inspector workload by 60-70%.

## Target Customer
VP Quality and Quality Directors at implantable device manufacturers with 50+ production inspectors. Approximately 400-500 US manufacturers produce Class II implantable devices at scale. Average contract value: $150-300K/year including hardware and software.

## Impact If Built
Inspector throughput increases 40-60% by pre-screening clearly acceptable units. Defect escape rate decreases by 30-50% by eliminating fatigue-driven misses. Time-to-deploy drops from 12+ months (current CSV burden) to 8-12 weeks with pre-validated architecture.
