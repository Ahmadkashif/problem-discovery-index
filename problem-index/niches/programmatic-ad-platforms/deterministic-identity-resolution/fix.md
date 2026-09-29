# The Match Rate That Measures Nothing

**Niche:** [[niches/programmatic-ad-platforms/deterministic-identity-resolution/profile|Deterministic Identity Resolution]]
**Industry:** [[industries/programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Graphs are bought and sold on match rate, which rewards matching loosely, and nobody measures whether the matches are right.
**Tags:** #evaluation-metrics #hypothesis-testing #confidence-intervals #descriptive-statistics #compliance #quick-win #graph-theory #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to assemble the largest graph of real people that both buyers and publishers will actually adopt and regulators will accept — and whoever does that sets the addressable currency of the market.

## The Problem
An advertiser evaluates identity providers by uploading a customer file and seeing what share comes back matched. Ninety-two percent sounds better than sixty-eight, so the ninety-two wins. Nothing in that process asks whether the matches are correct. A provider that matches loosely — on a shared household, a stale address, a probabilistic guess presented as deterministic — scores higher than one that matches carefully. The industry's standard procurement test actively selects for the worse product, and every provider knows it, which is why match rates have risen across the market while targeting performance has not.

## Why It's Still Broken
Match rate is observable and accuracy is not, so the observable metric became the standard — a straightforward case of measuring what is easy. Advertisers have no truth set to check against. Providers who match carefully lose deals and eventually adjust. And a wrong match produces a wasted impression that is indistinguishable from an ordinary one.

## What a Fix Looks Like
Measure accuracy, not volume. Run a seeded test with known-correct and known-incorrect records planted in the file, which detects loose matching immediately, costs nothing, and is the fix — it converts an unmeasurable property into a measurable one with a trick every fraud team already knows. Report precision alongside match rate, so the two numbers are seen together and a high rate with poor precision is visibly worse than a modest rate with good precision. Validate against outcomes, since a matched audience that does not respond differently from an unmatched one was not matched to anything real, and this is the strongest available external check. Require providers to state match confidence per record rather than returning a binary, which lets the buyer choose their own threshold instead of inheriting the vendor's. Distinguish person, household and device matches explicitly, because conflating them is the most common way a rate is inflated and the distinction is usually known to the provider. Test the same file across providers, which is cheap and reveals the spread immediately. Publish a standard evaluation method through an industry body, since no single advertiser can change the procurement norm alone. Check stability over time, as a graph matching consistently across months is more trustworthy than one that fluctuates. Penalise false matches contractually, which changes the incentive the whole problem rests on. And ask for the methodology, because a provider who will not describe how a match is made is telling you something.

## Who Feels the Pain
Advertisers buying the loosest graph by construction; careful identity providers losing on a metric that punishes accuracy; and consumers targeted as someone they are not.

## Impact If Fixed
The standard procurement test selects for the worse product, and every provider knows it. Seeding known-correct and known-incorrect records converts an unmeasurable property into a measurable one at no cost, and outcome validation is the check no vendor can game.
