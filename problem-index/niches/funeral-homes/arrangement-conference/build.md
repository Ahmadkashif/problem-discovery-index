# Voice-Driven Arrangement Capture System

**Niche:** [[niches/funeral-homes/arrangement-conference/profile|Arrangement Conference Workflow]]
**Industry:** [[industries/funeral-homes|Funeral Homes]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** No tool captures arrangement conference decisions via voice and ambient recording, allowing the funeral director to stay fully present with the family instead of typing or writing.
**Tags:** #speech-recognition #named-entity-recognition #nlp #ai-agent

## The Problem
During the arrangement conference, the funeral director must capture: decedent biographical data (30+ fields for the death certificate), service selections (casket, vault, flowers, music, readings), logistical details (pallbearer names, clergy name, cemetery, reception venue), and family preferences — all while maintaining emotional presence with a grieving family. The director faces an impossible choice: type into a laptop (breaking eye contact and emotional connection) or take handwritten notes (requiring 30-60 minutes of post-meeting transcription). Either way, details get missed or incorrectly recorded.

## Why Nobody Has Built This
Voice-driven data capture in emotionally sensitive contexts is a challenging UX problem. The conversation is unstructured — families don't report data in the order a form expects. Names of decedent, family members, pallbearers, clergy, and venues are interspersed with emotional conversation that shouldn't be recorded. Building this requires both speech recognition accurate enough for proper nouns (names, church names, cemetery names) and an NLP layer that can extract structured data from unstructured grief-heavy conversation. Privacy concerns add complexity — the system must be opt-in and handle raw audio responsibly.

## What to Build
An ambient recording system (with family consent) that captures the arrangement conference conversation and extracts structured data: biographical details, service selections, venue and vendor information, and family preferences. The system presents a structured summary to the funeral director after the meeting for review and correction, then populates the case management system automatically. Key requirement: the director must be able to stay fully present — no typing, no screen interaction during the meeting.

## Target Customer
Funeral directors conducting 3-5+ arrangement conferences per week who spend 30-60 minutes per case on post-meeting data entry and still miss details that result in errors (wrong middle name on death certificate, forgotten flower order, incorrect pallbearer spelling).

## Impact If Built
Eliminates 30-60 minutes of post-conference transcription per case (saving 2-5 hours per week), reduces data entry errors by 70-80%, and allows directors to be fully emotionally present — improving both family experience and director well-being.
