# The Car Key Job That Might Not Work

**Industry:** [[locksmiths|Locksmiths]]
**Type:** Worker Life Changing
**One-liner:** An automotive locksmith drives to an all-keys-lost job with thousands of dollars of programmers and still doesn't know whether this VIN will program until the tool is plugged in, and a failed attempt can cost an hour or a damaged module.
**Tags:** #gradient-boosting #survival-analysis #logistic-regression #data-integration #evaluation-metrics #worker-facing

## The Problem
A customer has lost every key to a four-year-old SUV and calls because the dealer quoted days and several hundred dollars. The locksmith quotes on the phone, drives out and starts work. They pull the key code through the NASTF registry with an electronic authorisation, cut the blade, then connect a programmer to add a new smart key to the immobilizer. Whether that works depends on details the locksmith cannot see from the phone call. It depends on the exact model year and build, the immobilizer generation, whether the manufacturer has changed encryption mid-year, which of the locksmith's tools covers this variant, and whether the module needs to be removed, read and written back on the bench. Tool vendors publish coverage lists, but they are coarse and optimistic. Forums are full of "worked on mine" and "bricked mine" for the same model.

So the locksmith carries two or three programmers from different vendors (an estimated ~$2,000–$10,000 each plus yearly update subscriptions and per-job tokens), tries them in turn, and sometimes leaves after an hour with nothing to bill. The worst case is a corrupted module and a car that won't start at all. Then the locksmith owes a tow to the dealer and a repair bill.

## Why It Matters to the Worker
The financial risk sits on one person. Most automotive locksmiths are owner-operators, and a single bricked body control module can wipe out a week's margin. The time risk is just as real. An all-keys-lost job quoted at an hour that runs to three, at night in a customer's driveway, is the norm, not the exception. And NASTF rules forbid the locksmith from keeping the security data they pulled, so a job on the same model next month starts from scratch. What they learned stays only in their memory.

## What a Solution Looks Like
A job-feasibility check that runs when the call comes in. From the VIN (or year, make, model and key type) it returns the likely immobilizer system and key part. It says which of the locksmith's own tools and software versions have succeeded on this variant, and how often. It gives the expected time on site, whether a bench read of the module is likely, and the known failure modes with the precautions to take, such as backing up the EEPROM before writing. The answer draws on outcome logs that participating locksmiths and tool vendors contribute (VIN pattern, tool, version, procedure, success or failure, minutes taken). It never touches the security codes themselves. The quote and the decision to take the job then rest on evidence rather than a guess.

## Impact If Solved
Fewer wasted trips and failed attempts turn all-keys-lost work from a gamble into a priced product. For a busy automotive locksmith doing ~10–20 key jobs a week, cutting failed or abandoned attempts from an estimated ~10–15% of jobs to ~5% saves ~3–5 unbillable hours a week (estimate). It also avoids the occasional damaged module, whose repair or replacement at a dealer can run ~$500–$1,500, more than the job itself (estimate). It also lets newer technicians take on vehicles they would otherwise send back to the dealer.
