# Audition Feedback From the Jobs That Actually Booked

**Niche:** [[niches/recording-studios/home-booth-voice-actors/profile|Home-Booth Voice Actors]]
**Industry:** [[industries/recording-studios|Recording Studios]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A voice actor submits hundreds of auditions a month and hears back on a handful, so they never learn which jobs they could win or why they lost the rest.
**Tags:** #gradient-boosting #contrastive-learning #transformers #evaluation-metrics #revenue-impact #worker-facing
**Contested on:** Every serious competitor in this niche is fighting to put a home-booth actor's audition in front of the casting decisions it can win, and whoever turns auditions into bookings at the highest rate keeps the actor's membership fees and the client's jobs.

## The Problem
Casting sites post jobs with a script, a brief ("warm, conversational, mid-30s, not announcery") and a budget. Actors audition on as many as they can, often dozens a day (estimate), each taking minutes to read, record, clean and upload. The booking rate is low and unexplained. Actors waste hours on jobs where their voice was never a fit, and casting clients wade through hundreds of mismatched auditions.

## Why Nobody Has Built This
Marketplaces hold the data, which jobs, which auditions, which booked, but their revenue model rewards audition volume and memberships, not precision. Actors see only their own thin outcomes. Briefs are free text and voice qualities are hard to describe.

## What to Build
A matching model trained on a marketplace's history: voice embeddings of each actor's auditions, job brief text and script, budget and client type, and which audition booked. For actors it ranks open jobs by their likelihood of booking and shows the briefs they win and lose; for clients it surfaces the auditions most like the voices they shortlisted. Explanations stay at the level of brief features ("you book 'warm, conversational' corporate work, not 'energetic' retail spots") rather than scoring the person.

## Target Customer
Voice casting marketplaces looking to reduce churn among paying actors, and agents managing rosters.

## Impact If Built
Actors spend audition time where they can win, booking rates rise for the same effort, and clients hear a shortlist rather than a flood.
