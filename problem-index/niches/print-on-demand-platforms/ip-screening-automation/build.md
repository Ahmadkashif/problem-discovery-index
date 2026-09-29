# Exact Matches Caught, Everything Else Through

**Niche:** [[niches/print-on-demand-platforms/ip-screening-automation/profile|IP Screening Automation]]
**Industry:** [[industries/print-on-demand-platforms|Print on Demand Platforms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Automated content screening handles obvious infringement and misses the substantial grey area, which is where every enforcement notice the platform receives comes from.
**Tags:** #cnns #contrastive-learning #large-language-models #evaluation-metrics #confidence-intervals #compliance #object-detection #k-nearest-neighbors
**Contested on:** Every serious competitor in this niche is fighting to catch the infringing uploads that exact matching misses — and whoever does that manages the exposure, because the obvious cases are already handled and the liability lives entirely in what gets through.

## The Problem
A design reproduces a well-known character in a slightly different pose and style, with no logo and no name. The text screen finds no brand name. The image hash finds no match, because it is a new drawing. It is listed, sells for four months, and generates an enforcement notice, a takedown, a potential claim and a damaged relationship with a rights holder who now watches the platform closely. The screening did exactly what it was built to do. What it was built to do — match text and hashes — addresses the class of infringement that stopped being the problem years ago.

## Why Nobody Has Built This
Text and hash matching were built first because they were feasible first, and the capability to detect stylistic and structural similarity has only recently become practical. The rights-holder corpus needed to detect a character or a trade dress is substantial and nobody has assembled it. Screening is measured on volume processed rather than on notices received. And the misses are discovered by rights holders rather than by the platform, which means the feedback arrives as a legal letter.

## What to Build
Detect similarity rather than identity. Build visual similarity detection against a maintained rights-holder corpus — characters, trade dress, distinctive stylistic elements — which is now practical and is the capability the current screening lacks entirely. Assemble and maintain the corpus deliberately, since it is the asset the detection depends on and is currently ad hoc; rights holders will frequently supply it, and the ones who enforce will supply it eagerly. Detect textual variation — a slogan with a word changed, a phonetic respelling, a deliberate misspelling — which is straightforward and is a common evasion the exact match misses. Detect stylised text treatments, since a brand's typographic identity is protectable and is invisible to a word match. Screen the generated mockup rather than only the file, since context sometimes changes the assessment. Use enforcement notices received as training labels, which are the most valuable and most neglected data the platform has and which arrive pre-labelled by a rights holder. Score rather than gate, so the output is a prioritised queue rather than a block list, which the fix note develops. Monitor listed products continuously rather than only at upload, since the corpus and the rights landscape change. And measure recall against enforcement notices received, because that is the only honest measure of whether the screening works.

## Target Customer
Platforms carrying the liability, trust and safety functions, rights holders, and the brand protection vendors serving them.

## Impact If Built
Text and hash matching address the class of infringement that stopped being the problem years ago, and every enforcement notice comes from what they miss. Enforcement notices are pre-labelled training data arriving from rights holders and are the most neglected asset in the screening.
