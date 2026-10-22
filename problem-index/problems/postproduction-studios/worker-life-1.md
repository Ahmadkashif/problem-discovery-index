# The Assistant Editor Rebuilding the Turnover Overnight

**Industry:** [[postproduction-studios|Postproduction Studios]]
**Type:** Worker Life Changing
**One-liner:** Every time the edit changes after turnover, an assistant editor rebuilds the change lists, VFX pulls and sound turnovers by hand, usually at night, and one wrong frame cascades to every vendor downstream.
**Tags:** #large-language-models #seq2seq #feature-engineering #evaluation-metrics #worker-facing #automation #workflow-orchestration

## The Problem
When an episode or film locks, editorial "turns over" the cut to everyone downstream: the online editor gets an EDL or AAF to conform from camera originals, the VFX vendors get pull lists and reference clips with handles, sound gets an AAF and guide track, the colorist gets a conformed timeline, and music gets cue timings. Locks rarely hold. A network note, a test screening, a legal clearance problem or a director's late idea changes the cut, and every downstream department needs to know exactly what moved: which shots were trimmed, which VFX shots are new or omitted, which sound edits now drift out of sync.

The assistant editor does that work. They compare versions in Avid, generate change lists, re-export AAFs, rebuild VFX pull spreadsheets, rename shots that changed, and write emails explaining it all. Tools like Avid's change list and third-party conform utilities help, but the reconciliation across vendors (who has which version, which VFX shot numbers changed, which sound turnovers are stale) is done by hand. It happens at the end of the day, after the editor and director have finished cutting.

## Why It Matters to the Worker
Assistant editors work long hours for modest pay, often on hourly rates under the Motion Picture Editors Guild agreement or as non-union freelancers. The turnover is the part of the job most likely to produce a visible mistake. A missed shot in a VFX pull means a vendor bills for, or misses, work, and the error traces back to them. It is also the part least connected to why they took the job: they want to learn to cut, and the turnover leaves no time to sit with the editor.

## What a Solution Looks Like
A turnover assistant that diffs any two versions of the cut at clip level and produces each department's change list in that department's format. It updates VFX shot lists (new, omitted, retimed, handle changes), flags sound turnovers that are now out of sync, tracks which vendor holds which version, and drafts the change notes. The assistant editor reviews and sends. Every export is linked to the version it came from.

## Impact If Solved
On a series with weekly recuts, an assistant editor could get back roughly 8–15 hours a week (estimate) of after-hours reconciliation. Downstream errors from stale turnovers, a common source of VFX rework and conform fixes, would fall sharply. And the hours go back to the apprenticeship the job is supposed to be.
