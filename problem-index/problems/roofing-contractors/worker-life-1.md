# Job Photo Organization and Labeling Automation

**Industry:** [[roofing-contractors|Roofing Contractors]]
**Type:** Worker Life Changing
**One-liner:** Roofing crews who take 80–150 photos per job across inspection, installation progress, and completion documentation — and then spend 20-30 minutes organizing them into labeled folders by phase and roof zone — get that organization done automatically from the photo metadata and visual content.
**Tags:** #cnn #multiclass-classification #computer-vision #automation #worker-facing

## The Problem

Photo documentation is essential in roofing for three reasons: insurance claim evidence (photos must be organized by damage type for adjuster review), liability protection (before/after documentation of existing conditions), and quality control (installation milestone photos for manufacturer warranty compliance). Most roofing firms use CompanyCam or similar apps that attach photos to the job, but organization within the job — which photos show hail damage vs. installation progress vs. final completion, which zone of the roof each photo covers — is done manually by the estimator or office admin.

On a typical insurance job with 100+ photos, the organizational task takes 20-30 minutes. On a firm doing 10 jobs per week, this is 3-5 hours of weekly admin labor that adds no value — the organizing itself is the task, not the photos.

## Why It Matters to the Worker

Field technicians take photos continuously during an inspection without stopping to label them. Requiring them to label photos at the time of capture creates enough friction that they skip it. Post-job organization falls to whoever processes the job for invoicing — a task they resent because it's slow and requires them to recall what was happening in each photo.

## What a Solution Looks Like

A CompanyCam integration (or standalone mobile app) that: (1) automatically classifies each photo into categories — pre-existing damage, hail impact, wind damage, installation progress, flashing detail, ridge completion, final overall — using a CNN trained on labeled roofing inspection photos; (2) tags photos with the roof zone (front slope, rear slope, left hip, right hip, ridge, valley) based on orientation metadata and visual classification; (3) organizes the job's photo set into a standard folder structure before the crew leaves the site. The estimator reviews the auto-organized set, makes corrections to misclassified photos (2-3 minutes), and submits.

## Impact If Solved

Returns 20-30 minutes per job to estimators and office admin. More importantly, produces consistently organized photo sets across all jobs — enabling quality control review, insurance adjuster submission, and manufacturer warranty documentation without job-specific reorganization.
