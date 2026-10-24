# The Child Whose Treatment Stopped Working Unnoticed

**Niche:** [[niches/optometry-practices/pediatric-myopia-management/profile|Pediatric Myopia Management Programmes]]
**Industry:** [[industries/optometry-practices|Optometry Practices]]
**Type:** Fix (Pain Point)
**One-liner:** A child's eye keeps lengthening faster than expected on treatment, but without a forecast to compare against, nobody notices for a year.
**Tags:** #time-series-forecasting #gaussian-processes #worker-facing #quick-win #evaluation-metrics
**Contested on:** Every serious competitor in this niche is fighting to slow eye growth in children enrolled in myopia control, and whoever shows the lowest measured axial elongation per child per year across a practice's programme takes the account.

## The Problem
Six-monthly visits record axial length and refraction. A change of a few tenths of a millimetre looks small on a printout. Without an expected value for this child on this treatment, a poor response is easy to miss.

## Why It's Still Broken
The expected value depends on age, ethnicity, baseline myopia and treatment, and no tool computes it. Busy ODs judge by eye, and families do not know what to ask.

## What a Fix Looks Like
At every visit, show the child's measured growth against the forecast band for their treatment, and flag growth outside it with suggested options.

## Who Feels the Pain
Children whose myopia, and their lifetime risk of myopic eye disease, ends higher than necessary, and families paying for a programme that is not working.

## Impact If Fixed
Catching a poor response one visit (six months) earlier saves roughly ~0.1 mm of excess growth per affected child (estimate) and keeps families' trust in the programme.
