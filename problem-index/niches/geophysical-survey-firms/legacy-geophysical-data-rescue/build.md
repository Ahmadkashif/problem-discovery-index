# Navigation Recovered From Scanned Shot-Point Maps

**Niche:** [[niches/geophysical-survey-firms/legacy-geophysical-data-rescue/profile|Legacy Geophysical Data Rescue]]
**Industry:** [[industries/geophysical-survey-firms|Geophysical Survey Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A legacy 2D line is useless without knowing where each shot point was, and that position survives on hand-annotated base maps that technicians digitise point by point.
**Tags:** #cnns #semantic-segmentation #object-detection #transfer-learning #evaluation-metrics #automation
**Contested on:** Every serious competitor in this niche is fighting to turn decades of paper sections, field tapes and observer logs into correctly navigated, loadable digital data with clean licence title, and whoever does it at the lowest cost per line-kilometre without navigation errors wins the archive.

## The Problem
Old surveys came with shot-point maps: paper base maps with line traces, shot-point numbers every few stations, and handwritten annotations in local survey coordinates. To load a rescued line, a technician georeferences the map, traces the line, reads every labelled shot point and interpolates the rest, then reconciles the result with the numbers on the section. It takes hours per line and errors put the data in the wrong place.

## Why Nobody Has Built This
The market is small and episodic; map styles vary by contractor and decade; and generic map-vectorising tools do not understand shot-point labelling conventions or survey datums.

## What to Build
A model that segments line traces on scanned maps, detects and reads shot-point labels, fits station positions along each trace, and proposes a navigation file in a modern datum, with confidence per point and a check against the shot-point range on the matching section or tape header. Low-confidence segments go to a technician.

## Target Customer
Data rescue firms, multi-client libraries monetising legacy 2D, and state geological surveys preserving donated archives.

## Impact If Built
Navigation recovery cut from hours to minutes per line makes rescuing marginal archives economic, and fewer mislocated lines reach interpreters.
