# Demand Letter Generation and Settlement Negotiation Preparation

**Industry:** [[personal-injury-law|Personal Injury Law Firms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** General LLM tools can draft professional letters but can't produce demand letters that incorporate PI-specific damages formulas, jurisdiction-specific caps, insurer-specific negotiation dynamics, and the persuasive structure that has historically worked against specific adjusters.
**Tags:** #llm #text-generation #nlp #automation

## The Problem
A demand letter in a personal injury case is the first formal settlement communication to the insurer — it establishes the damages claimed, presents the medical evidence, argues liability, and sets a settlement demand amount. Writing a strong demand letter requires: synthesizing the medical chronology into a compelling narrative of the client's suffering and recovery, calculating economic damages (medical specials, lost wages, future care costs), applying jurisdiction-specific multipliers for general damages, and calibrating the demand amount to what the insurer can realistically pay on the specific policy and coverage. A junior associate drafting their first demand letters takes 4-6 hours per letter; an experienced PI attorney does it in 60-90 minutes and produces a significantly more persuasive document.

## What Already Exists
General-purpose LLMs (GPT-4, Claude) can produce professional legal letters from input facts. Filevine and Clio have some document assembly capability. Legal document assembly tools (HotDocs, Contract Express) handle templates. None of these are calibrated to the specific persuasive structure of PI demand letters — which follow a learned format (incident summary → liability analysis → injury description → medical records reference → damages calculation → demand amount) that differs from general legal correspondence. None incorporate jurisdiction-specific damage caps, insurer behavioral data, or the firm's historical settlement outcomes.

## The Customisation Gap
A PI-specific demand letter generator needs to: integrate the medical chronology output as the factual basis; apply jurisdiction-specific damages formulas (the "three-times specials" rule of thumb is actually jurisdiction and case-type dependent); incorporate insurer-specific framing (some insurers respond better to documented economic damages; others to narrative descriptions of pain and suffering); and calibrate the demand amount based on the firm's historical data on what this insurer settles at for similar injuries in this jurisdiction. This intelligence layer requires training on the firm's case history — not available in generic LLMs.

## Impact If Solved
Reduces demand letter drafting time from 2-6 hours to 30-60 minutes of review and customization. More importantly, improves demand letter quality consistency across the firm — junior associates produce letters closer to senior attorney quality, reducing the need for supervisory revision.
