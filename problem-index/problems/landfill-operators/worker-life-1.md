# The Compactor Operator Working Blind

**Industry:** [[landfill-operators|Landfill Operators]]
**Type:** Worker Life Changing
**One-liner:** The compactor operator spends every shift trying to pack waste tighter without ever seeing whether it worked, and gets back clarity and credit when each pass, lift and shift's density is shown to them in the cab.
**Tags:** #worker-facing #semantic-segmentation #gaussian-processes #feature-engineering #automation #revenue-impact

## The Problem
On the working face, trucks tip their loads and a landfill compactor — a ~40–60-ton machine (estimate) with steel-toothed wheels — spreads the waste in thin layers and rolls over it again and again, then the face is covered with soil, tarps or spray at the end of the day. The operator decides lift thickness, number of passes, slope and where to push each load, for shifts of ~10 hours or more (estimate), while trucks queue, spotters wave and the wind changes. Density is the whole point: the difference between ~1,200 and ~1,800 pounds per cubic yard (search summary) is half as much waste again in the same permitted airspace. But the operator never sees the result. Density is calculated weeks later by comparing two drone or ground surveys against scale tonnage, for the whole face, not for anyone's shift.

So the operator works by feel — the sound of the machine, how the wheels sink, how the face looks after a pass. When the quarterly survey comes back low, the manager wants to know why, and the operator has nothing to show for the passes they made. When the face runs behind, the pressure is to spread faster, which costs density. Meanwhile the job is physically hard: sitting in a bouncing cab, working side slopes where a rollover is possible, watching for buried hazards, hot loads and battery fires, and breathing dust and odour.

## Why It Matters to the Worker
Good compactor operators are valued and know it, but their skill is invisible. They cannot prove they are good, cannot show a new operator what they do differently, and absorb blame for numbers that also depend on waste mix, weather and how many trucks arrived at once. The feedback loop that would let them get better — seeing which lift thickness and pass count worked on which waste — is weeks long and site-wide. Shifts are long and repetitive, and fatigue is a safety issue on slopes.

Being shown their own result changes the job. An operator who can see density by lane and lift can manage it, explain it, and teach it.

## What a Solution Looks Like
The compactor already carries GNSS machine-control or telematics on many sites. The cab shows a live map of the face with pass counts and lift thickness per cell, colour-coded against the target, and an estimated density for the shift from machine elevation changes and the scale tonnage tipped on that face. Trouble spots — thin coverage, over-thick lifts, a slope getting too steep — are flagged as the operator works. At the end of the shift the operator sees their own numbers, and the weekly drone survey confirms or corrects the estimate, so the in-cab number becomes trustworthy over time.

## Impact If Solved
An operator who can see density per lift instead of per quarter can close much of the gap to the site's best operator; raising average density from ~1,500 to ~1,600 lb per cubic yard (estimate) at a 1,000-ton-a-day face saves ~6% of the airspace consumed, ~25,000 cubic yards a year over ~300 operating days, and gives the operator a record of their own skill.
