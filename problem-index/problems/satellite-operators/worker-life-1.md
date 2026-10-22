# The Payload Engineer Chasing Interference at 3 a.m.

**Industry:** [[satellite-operators|Satellite Operators]]
**Type:** Worker Life Changing
**One-liner:** When a customer's carrier degrades, the on-call payload engineer has to read a spectrum trace, guess the interferer, and phone around the world's NOCs until someone switches off a misaligned dish — and gets back the night when the guessing and phoning are done for them.
**Tags:** #cnns #k-nearest-neighbors #large-language-models #feature-engineering #worker-facing #automation #workflow-orchestration

## The Problem
A broadcaster's contribution feed or an enterprise network's carrier starts to degrade. The customer calls the operator's NOC; the carrier monitoring system shows something sitting on top of the customer's signal. The on-call payload engineer opens the spectrum analyser trace and starts reasoning: is it a cross-polarised carrier from a new VSAT that was installed with the wrong polarisation, adjacent-satellite interference from a small dish pointed a degree off, an intermodulation product from the operator's own amplifiers, a terrestrial 5G signal leaking into C-band, or a deliberate jammer? Each looks slightly different on the trace, and the experienced engineer recognises most of them at a glance.

Then the real work starts. Geolocation needs a second satellite and a reference carrier, which takes hours to set up. If the source is another operator's customer, the engineer must reach that operator's NOC, explain the problem, and persuade them to find and switch off their own customer's terminal. Most interference is accidental — Eutelsat put human error at about 58% and deliberate signals at about 10% in 2012 — so the fix is usually a technician re-pointing a dish somewhere, after a chain of phone calls and emails that can run through the night. Carrier ID, the embedded identifier that names the uplink, would shortcut this, but adoption has lagged for a decade.

## Why It Matters to the Worker
The interference engineer's nights are spent on calls, not engineering. A case can stay open for hours or days (estimate), with the customer's account manager asking for updates, while the engineer chases people in other time zones who have no obligation to answer. The judgement they bring — recognising the interference type from the trace — is used for a minute; the rest is logistics. The same handful of misbehaving terminals and careless uplink operators come back again and again, and the engineer remembers them while the case system doesn't.

The stress is real because the customer's service is down while they work, and the engineer is the one the customer blames. In the last large industry survey (IRG/Newtec, 2013, ~500 respondents), 93% of respondents had suffered interference in the past year and about one in six dealt with it continuously.

## What a Solution Looks Like
A case assistant that classifies the interference type from the trace as soon as the carrier monitor raises it, retrieves the most similar past cases (same satellite, beam, frequency, signature) with their outcomes and the terminals or operators involved, and proposes the likely source. It starts geolocation automatically where the setup allows, drafts the notification to the other operator's NOC in the format the industry's interference groups use, and keeps the timeline the customer's account manager can read without calling the engineer.

## Impact If Solved
Cutting the hours spent identifying the source and chasing contacts turns a night-long case into a short one for most accidental interference, gives the engineer back sleep and the engineering part of the job, and builds the case history that lets an operator deal with repeat offenders instead of rediscovering them.
