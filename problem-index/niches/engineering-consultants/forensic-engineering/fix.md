# Historical Code and Standard Lookup for Date-of-Construction Compliance

**Niche:** [[niches/engineering-consultants/forensic-engineering/profile|Forensic Engineering Consultants]]
**Industry:** [[industries/engineering-consultants|Engineering Consultants]]
**Type:** Fix (Pain Point)
**One-liner:** Forensic engineers must determine which building code edition was in effect when a structure was built — a research task that requires tracking down the adoption history of 50+ jurisdictions across 40+ years of code editions, currently done from memory or manual research.
**Tags:** #nlp #bert #text-classification #compliance #tacit-knowledge-ml

## The Problem
When a forensic engineer evaluates whether a building deficiency constitutes a code violation, they must apply the code that was in effect at the time of construction — not the current code. A roof installed in 1998 in Miami-Dade County must be evaluated against the South Florida Building Code (pre-Florida Building Code adoption), not the 2023 FBC 8th Edition. Determining which code edition was enforceable in a specific jurisdiction at a specific date requires knowing: (1) when the jurisdiction adopted each code cycle, (2) which amendments or local supplements were in effect, and (3) whether the specific section at issue changed between editions. Senior forensic engineers carry this knowledge in their heads — they know that "Florida adopted the FBC in 2002, but Broward County used its own code until 2004" — while junior engineers spend 2-6 hours per case researching code adoption timelines.

## Why It's Still Broken
No centralized database of historical building code adoptions exists. ICC (International Code Council) publishes current adoption maps but not historical ones. Individual jurisdictions may or may not have adoption ordinances available online. The code editions themselves are copyrighted by ICC, NFPA, and ASCE, so even if adoption dates are known, accessing the actual historical code language requires purchasing old editions ($100-200 each) or visiting a library. The combination of fragmented adoption data and copyrighted code text makes this a research problem that senior engineers solve from accumulated experience and personal code libraries.

## What a Fix Looks Like
A searchable database of building code adoption history by jurisdiction: "Enter jurisdiction + date of construction → get the applicable code edition, any local amendments, and direct links to the relevant code sections." The database is assembled from municipal adoption ordinances, state statute databases, and ICC historical records. For the most commonly litigated code sections (wind load, water intrusion, structural connections, fire separation), the tool provides a comparison view showing how the requirement changed across editions. This doesn't replace the engineer's judgment — it replaces the 2-6 hours of research to identify which code to apply.

## Who Feels the Pain
Junior forensic engineers assigned the research task of identifying applicable code editions, and senior engineers who carry this knowledge but risk errors when working in unfamiliar jurisdictions.

## Impact If Fixed
Saves 2-6 hours per case on code research. Reduces the risk of applying the wrong code edition in an expert report — an error that can result in a discredited opinion and malpractice exposure. For a firm handling 250 cases/year, this saves 500-1,500 hours annually.
