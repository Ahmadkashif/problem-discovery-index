# The Suggestion That Arrives Mid-Thought

**Niche:** [[niches/developer-tools-vendors/developer-adopted-assistants/profile|Developer-Adopted Assistants]]
**Industry:** [[industries/developer-tools-vendors|Developer Tools Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Assistants suggest continuously regardless of what the developer is doing, so a developer composing a thought is interrupted by a plausible wrong answer and many of them turn the feature off.
**Tags:** #descriptive-statistics #logistic-regression #hidden-markov-models #evaluation-metrics #confidence-intervals #worker-facing #quick-win #automation
**Contested on:** Every serious competitor here is fighting to be the assistant a developer keeps switched on after week three — and whoever wins that takes the account regardless of what was procured, because an unused licence is a cancelled one.

## The Problem
A developer is halfway through working out how to structure something. Grey text appears offering a complete implementation of what it guessed they meant. Reading it costs attention; it is wrong; the thought is gone. This happens several times an hour. The developer either learns to ignore the suggestions, which wastes the feature, or turns it off, which is common and is reported by vendors as low engagement rather than as a design failure. The same suggestion offered ninety seconds later, when the developer has decided what they want and is typing it out, would have been welcome.

## Why It's Still Broken
Suggesting on every pause is the simplest trigger and it maximises the acceptance denominator, which is the metric being optimised. Nothing models what the developer is doing — exploring, deciding, transcribing a decision already made — although the signals are available in the editing behaviour. Interruption cost is not measured by anyone, and the developers most affected are the ones doing the hardest work. And the fix is a restraint, which is hard to sell and impossible to demo.

## What a Fix Looks Like
Model the moment, not just the code. Classify the developer's current activity from editing behaviour — sustained typing, navigating and reading, deleting and rewriting, long pauses after a partial expression — since these are distinguishable and correspond to very different receptiveness. Suppress during composition and offer during transcription, which is the core behaviour change and the one developers describe wanting when asked. Require a higher confidence threshold to interrupt than to appear when explicitly requested, since an unsolicited suggestion must earn its interruption and a requested one need not. Make explicit invocation excellent, because a developer who knows they can ask will tolerate far less unsolicited behaviour. Let the developer set the aggressiveness in terms they understand and remember it per project, since the right answer differs between exploratory and routine work. And measure sustained voluntary use as the metric rather than acceptance, because that is what the business actually depends on and it is currently not reported.

## Who Feels the Pain
Developers doing the hardest thinking, who are interrupted most and benefit least; teams whose licences are paid and features disabled; and vendors reading disabled features as low engagement rather than as a specific design complaint.

## Impact If Fixed
Activity classification from editing behaviour is straightforward and addresses the most common complaint about these tools directly. Measuring sustained use rather than acceptance would reorient the product toward the property the business actually depends on.
