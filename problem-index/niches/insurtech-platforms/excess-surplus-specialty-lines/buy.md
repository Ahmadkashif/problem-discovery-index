# Contract Analysis Tooling Applied to Policy Wordings

**Niche:** [[niches/insurtech-platforms/excess-surplus-specialty-lines/profile|Excess, Surplus & Specialty Lines]]
**Industry:** [[industries/insurtech-platforms|Insurtech Platforms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Contract analysis — clause extraction, deviation detection against a standard, obligation mapping — is a mature legal technology category, and insurance policies are contracts that nobody analyses with it.
**Tags:** #bert #large-language-models #transformers #word-embeddings #evaluation-metrics #confidence-intervals #compliance #automation
**Contested on:** Every serious competitor in E&S technology is fighting to make manuscript coverage comparable across markets so a broker can tell a client what they are actually buying — and whoever makes coverage comparison reliable takes the account.

## The Problem
Legal teams reviewing commercial agreements have tooling that extracts clauses by type, compares them against a playbook standard, flags deviations and ranks them by materiality. An insurance policy is a commercial agreement with an unusually well-developed vocabulary and a stable clause taxonomy, and the brokers and underwriters who work with them do so with a PDF viewer.

## What Already Exists
Contract lifecycle management and contract analysis vendors provide clause extraction, deviation detection, playbook comparison and obligation extraction, with substantial accuracy on commercial agreements. Long-context language models handle documents of policy length. Legal document comparison tooling is mature. Standard insurance forms — the ISO and equivalent libraries — provide a well-defined baseline that a deviation analysis can work against, even in a segment whose whole character is departing from it.

## The Customization Gap
The adaptation is to insurance's own clause structure and to the specific question a broker asks. It requires: (1) an insurance clause taxonomy rather than a commercial contract one, since the meaningful units are insuring agreements, definitions, exclusions, conditions and endorsements, and their relationships are what determine coverage; (2) deviation measured against a standard form baseline where one applies, which gives the analysis an anchor and lets a manuscript wording be described as "the standard form plus these seven departures" — which is how experienced practitioners actually read them; (3) endorsement resolution, since a policy's operative terms are the base form as modified by a stack of endorsements and reading the base form alone is simply wrong; (4) materiality ranking informed by the client's actual exposures rather than by generic importance, because the exclusion that matters depends entirely on what the client does; and (5) citation to the clause for every assertion, which is both the professional requirement and what makes the output reviewable in the time a broker has.

## Target Customer
Wholesale and specialty brokers, specialty carriers and MGAs, and the contract analysis vendors who could reach a large adjacent market with a taxonomy adaptation.

## Impact If Solved
Endorsement resolution alone — presenting a policy's actual operative terms rather than a base form and a stack — would materially improve practice in a segment where policies are routinely read incompletely. The tooling is bought and the adaptation is a taxonomy and a baseline, which is a far smaller undertaking than building comparison from nothing.
