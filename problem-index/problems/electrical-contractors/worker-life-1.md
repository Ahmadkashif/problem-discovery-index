# Electrical Fault Diagnosis Assistant

**Industry:** [[electrical-contractors|Electrical Contractors]]
**Type:** Worker Life Changing
**One-liner:** An apprentice or journeyman electrician standing in front of an intermittent electrical problem — flickering lights, a GFCI that keeps tripping, a breaker that trips under specific loads — gets a structured diagnostic checklist that surfaces the most likely causes based on the symptom pattern, instead of guessing or waiting for the master to come over.
**Tags:** #large-language-models #transformers #attention-mechanisms #transfer-learning #loss-functions #evaluation-metrics #conditional-probability-and-bayes-theorem #worker-facing

## The Problem
Electrical fault diagnosis is one of the most experience-dependent skills in the trade. An intermittent fault (a light that occasionally flickers, a circuit that trips under specific conditions, an outlet that works sometimes) can have 5-15 different root causes, and the correct diagnosis requires understanding the symptom pattern, the circuit's topology, the building's age and wiring history, and the specific failure signatures associated with each cause type. An experienced master electrician hears "the lights flicker when the refrigerator starts" and immediately knows this is likely a loose neutral connection or an undersized service conductor — they've seen this pattern hundreds of times. An apprentice hears the same symptom description and has no framework for what to check first, leading to random testing that wastes time and sometimes fails to find the problem at all.

## Why It Matters to the Worker
Troubleshooting is the highest-skill, highest-anxiety work situation for junior electricians. They are expected to diagnose a problem they haven't encountered before, often with a frustrated homeowner watching them, and the combination of time pressure, performance anxiety, and genuine uncertainty is stressful. Apprentices who struggle with troubleshooting lose confidence, make more mistakes, and are reluctant to take on service calls without supervision — slowing the firm's capacity to deploy them independently. Senior electricians who have to babysit junior staff on every troubleshooting call have less time for the work that benefits from their expertise.

## What a Solution Looks Like
A mobile app where the electrician describes the fault symptom in natural language or selects from a structured symptom menu (circuit type, symptom type, when symptom occurs, other observations). The system returns: the top 3-5 most likely causes ranked by probability for this symptom pattern; a step-by-step diagnostic test sequence starting with the most likely cause; what to measure at each test point and what the expected good vs. fault reading is; and what the finding at each step implies for the diagnosis. The apprentice follows the diagnostic tree, reports findings at each step, and the system narrows to the specific fault. The master electrician reviews the diagnostic process later, not during it.

## Impact If Solved
Enables journeymen and senior apprentices to handle 60-70% of service call troubleshooting independently, reducing master electrician oversight calls by an estimated 3-5 per week. Reduces average troubleshooting time per service call by 20-40% by eliminating random testing and replacing it with evidence-based diagnosis sequences. Accelerates apprentice skill development by embedding the master's diagnostic reasoning into a tool they use on every troubleshooting call.
