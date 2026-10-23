# Capture With a Provenance Record Attached

**Niche:** [[niches/investigation-and-screening-firms/social-media-evidence-capture/profile|Social Media & Open-Source Evidence Capture]]
**Industry:** [[industries/investigation-and-screening-firms|Investigation & Background Screening Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A screenshot of a claimant's post is easy to challenge at a hearing; a capture with hashes, metadata, page context and an account-attribution record is not, and few investigators produce one.
**Tags:** #gradient-boosting #word-embeddings #cnns #evaluation-metrics #compliance #automation
**Contested on:** Every serious competitor in this niche is fighting to find a subject's public posts and preserve them with provable authenticity before they are deleted or locked, and whoever delivers the most captured posts that survive an authentication challenge takes the account.

## The Problem
An investigator finds a public post showing a workers' compensation claimant carrying a kayak. They screenshot it, note the URL and date, and include it in a report. At a hearing the claimant's attorney asks how the investigator knows the account is the claimant's, whether the image was altered, and what the post said in full. The investigator's answer is their recollection and a cropped image.

## Why Nobody Has Built This
Desk investigation is priced per report and done fast; tooling budgets are small. Archiving tools capture pages for compliance teams but do not attribute accounts to people or package evidence for a hearing.

## What to Build
A capture tool that records the full page and media, computes hashes, stores platform metadata, timestamps and the capture environment, and produces a certification-ready record (the Federal Rules of Evidence allow certified electronic data to self-authenticate by hash under Rule 902(14)). Alongside it, an account-attribution model that scores how likely an account belongs to the subject from photos, names, locations, connections and posting history, with the evidence listed, so the investigator's judgement is documented rather than asserted.

## Target Customer
Owners of claims investigation firms and desk-investigation units; SIU directors who receive the reports.

## Impact If Built
More online evidence survives challenge, investigators spend less time defending captures, and carriers can rely on desk reports instead of ordering surveillance to prove the same thing.
