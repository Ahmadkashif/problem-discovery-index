# Re-Processes Nobody Counts

**Niche:** [[niches/aerospace-parts-suppliers/engine-components-rotating-parts/profile|Engine Components & Rotating Parts]]
**Industry:** [[industries/aerospace-parts-suppliers|Aerospace Parts Suppliers]]
**Type:** Fix (Pain Point)
**One-liner:** Inspectors send doubtful parts back through the penetrant line on instinct, and the plant never learns how often, on which features, or why.
**Tags:** #change-point-detection #descriptive-statistics #evaluation-metrics #worker-facing #quick-win #compliance
**Contested on:** Every serious competitor in this niche is fighting to turn more of the industry's scarce castings and forgings into accepted engine parts, and whoever proves the lowest scrap and re-process rate at final inspection with no rise in escapes takes the account.

## The Problem
A re-process (clean, re-penetrate, re-inspect) is the experienced inspector's hedge when the background is too bright or an indication looks like trapped penetrant. It is the right call, but it costs line time and is often logged only as a second pass. Plants that do not count re-processes cannot see a wash station drifting, a part feature that always traps penetrant, or a shift where calls get more cautious.

## Why It's Still Broken
The traveller has no field for it, the inspection line is judged on throughput, and nobody owns the number.

## What a Fix Looks Like
Record every re-process as an event with a reason code (background, suspected trapped penetrant, borderline indication) and line parameters. Chart re-process rate by line, feature and shift with change-point alerts. Review the top features with the Level III and the manufacturing engineer monthly.

## Who Feels the Pain
Inspectors who absorb blame for slow lines; Level III managers who suspect process drift and cannot prove it; plant managers short of inspection capacity.

## Impact If Fixed
Counting re-processes typically surfaces two or three line or feature causes within a quarter (estimate) and can recover ~5–10% of penetrant-line capacity without new equipment.
