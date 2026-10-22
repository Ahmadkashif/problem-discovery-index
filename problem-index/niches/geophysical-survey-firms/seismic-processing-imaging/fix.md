# The Processing Flow Nobody Wrote Down

**Niche:** [[niches/geophysical-survey-firms/seismic-processing-imaging/profile|Seismic Processing & Imaging]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Fix (Pain Point)
**One-liner:** When a survey is reprocessed ten years on, the original flow and parameters survive only as a thin PDF report, so the new team cannot tell what was done or why the old image looks the way it does.
**Tags:** #large-language-models #transformers #data-integration #workflow-orchestration #quick-win
**Contested on:** Every serious competitor in this sub-niche is fighting to deliver a depth image whose velocity model ties the wells and that the client's interpreters trust, before the lease sale or drilling decision, and whoever gets there with the fewest re-runs takes the reprocessing work.

## The Problem
Reprocessing begins by understanding the previous processing: which statics solution, which noise attenuation, which velocity model and migration, which traces were killed. Processing reports summarise this loosely; the actual job files are often gone or in a format the new system cannot read. Teams re-derive what they can and repeat tests that were run before.

## Why It's Still Broken
Processing reports are written at the end of a project to a template that satisfies the client, not the next processor; the detailed parameter record stays in a system that is retired with the project.

## What a Fix Looks Like
Generate a machine-readable flow record automatically from the job logs at delivery — every step, parameter and input — stored with the data, plus a narrative report drafted from that record. For legacy projects, extract what is recoverable from old reports and headers into the same structure.

## Who Feels the Pain
Processors starting a reprocessing project, libraries trying to explain to licensees what changed between vintages, and clients comparing images.

## Impact If Fixed
Weeks saved at the start of each reprocessing project, and a provenance record libraries can show licensees.
