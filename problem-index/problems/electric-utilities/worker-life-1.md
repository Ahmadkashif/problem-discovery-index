# The Control Room Operator on Night Three of a Storm

**Industry:** [[electric-utilities|Electric Distribution Utilities]]
**Type:** Worker Life Changing
**One-liner:** A distribution operator working twelve-to-sixteen-hour storm shifts writes and checks switching orders by hand while an outage system floods them with alarms, calls and executive requests for restoration times, and gets back clarity and a safer margin if the routine work is drafted for them.
**Tags:** #large-language-models #gradient-boosting #graph-theory #time-series-forecasting #worker-facing #workflow-orchestration #automation

## The Problem
Distribution system operators are a small, scarce workforce: about 9,040 power distributors and dispatchers nationally (BLS May 2023). In normal weather an operator manages planned work: writing switching orders to isolate a section for a crew, issuing and releasing clearances, and watching SCADA alarms. In a major storm the same operator faces hundreds of outage events at once. The outage management system groups customer calls and smart-meter last-gasp messages into predicted device outages, often wrongly when damage is widespread. Crews call in by radio for switching instructions, and every request to open a switch or ground a line has to be checked against the real state of the network so that nobody is energised while working.

Meanwhile customer service, the storm centre and executives want estimated times of restoration, and those times are posted publicly. Operators work twelve- to sixteen-hour shifts for days (estimate), sometimes sleeping at the control centre.

## Why It Matters to the Worker
A switching error can kill a lineworker or a member of the public, and the operator carries that responsibility personally. The more tired they are, the more the mechanical parts of the job (drafting sequences, cross-checking tags, re-keying crew status) crowd out the attention the safety-critical decisions need. Restoration times are blamed on them when they slip, though they are guesses made with too little information. Experienced operators retire, and newer ones learn storm work only in real storms.

## What a Solution Looks Like
An assistant inside the control room workflow. It drafts switching sequences from the connectivity model and the crew's request, then checks each step against current device status, tags and clearances and flags conflicts. It regroups outage predictions as AMI pings and crew reports arrive, so the operator sees likely fault locations rather than raw calls. It proposes restoration times per area from damage patterns and crew assignments, with a confidence range the operator can accept or adjust. It also keeps a running log, so shift handovers stop depending on memory.

## Impact If Solved
Taking the drafting and re-keying off operators could give back perhaps an hour or two per storm shift (estimate) and cut switching-order errors caught at review. It would also give newer operators a guide through their first big storm. Customers would get restoration times grounded in data rather than guessed under pressure.
