# Grading Small Sites Without a Topographic Survey

**Niche:** [[niches/landscape-architecture-firms/sole-practitioners-micro-firms/profile|Sole Practitioners & Micro-Firms]]
**Industry:** [[industries/landscape-architecture-firms|Landscape Architecture Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Residential and small commercial clients will not pay for a topographic survey, so the landscape architect grades from county contours and a tape measure.
**Tags:** #cnns #semantic-segmentation #gaussian-processes #numerical-methods #worker-facing #quick-win
**Contested on:** Every serious competitor serving this niche is fighting to give a one- to four-person practice the second reviewer and the production capacity of a ten-person firm on every stamped set, at a price a sole practitioner can carry, and whoever does takes the account.

## The Problem
On a backyard renovation or a small commercial pad, a licensed survey can cost a meaningful fraction of the design fee. Practitioners work from county GIS contours at two-foot intervals, spot measurements and photos, and then design patios, steps and drainage whose tolerances are measured in inches. Errors show up as water against the house or steps that do not fit — and land on the person who sealed the plan.

## Why It's Still Broken
Survey-grade data is expensive by design, and the cheap alternatives — phone LiDAR scans, consumer drone photogrammetry — produce point clouds a sole practitioner has no time to clean and no way to trust.

## What a Fix Looks Like
A capture workflow: scan the site with a phone or small drone plus a few measured control points, automatically classify ground versus vegetation and structures, interpolate a surface with an uncertainty estimate, and export a CAD-ready existing-grade surface with the low-confidence zones marked — while making clear where a licensed survey is still required, as boundary work is covered under [[industries/land-surveyors|Land Surveyors]].

## Who Feels the Pain
Sole practitioners and residential design-build designers grading without data; homeowners whose drainage fails.

## Impact If Fixed
Usable existing grades for a few hundred dollars of effort rather than none, and fewer drainage failures on small jobs.
