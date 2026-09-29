# Fix: The Data Is in the Building and Nobody Joins It

**Niche:** Programme Outcome Measurement
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Fix (Pain Point)
**One-liner:** Simulation results, gateway telemetry, incident records and employee reports all sit inside the same organisation, and no one has ever put two of them side by side.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #data-integration #descriptive-statistics #worker-facing
**Contested on:** Whether simulated performance predicts resistance to real attacks.

## The Problem

The awareness manager has simulation results. The email security team has gateway telemetry showing real phishing volumes and which messages were delivered. The security operations team has the reporting queue of real suspicious messages employees flag. And the incident team has the record of actual compromises.

Four datasets, four teams, one organisation, no join.

So the awareness programme is evaluated on its own data. The gateway team reports blocks. Operations reports alert volumes. The incident team reports incidents. And the question that spans them — is the awareness programme making any difference to the real ones — is not asked, because it belongs to nobody.

Some of the joins are trivially available. Reporting rate on simulations and reporting rate on real suspicious messages are both counts of the same behaviour by the same people, and comparing them requires one query across two systems. Real phishing volume and difficulty from the gateway would tell the awareness team whether its simulations resemble the actual threat. And the initial access vector on incidents would say whether phishing is even the organisation's main exposure.

None of it needs a research programme. It needs somebody to ask.

## Why It's Still Broken

**The datasets belong to different teams.** Awareness, email security, operations and incident response are separate functions with separate systems and separate reporting lines.

**Nobody owns the joined question.** Each team reports its own metric upward and the cross-cutting question has no owner.

**The awareness manager has no access.** They are frequently the most junior of the four and cannot obtain gateway or incident data on their own authority.

**Nobody has asked for it.** Leadership receives four reports and has never asked how they relate.

**The answer might be awkward for someone.** A finding that the awareness programme does not correlate with real behaviour is difficult for the awareness manager; one that phishing is not the main incident vector is difficult for the whole programme's justification.

**It looks like a research project.** Framed as outcome research it seems large. Framed as comparing two numbers it is an afternoon.

## What a Fix Looks Like

**Compare simulation reporting to real reporting.** The same behaviour, the same people, two systems. Do the people who report simulations report real messages? This is one query and it is the single most informative thing the organisation could learn about its programme.

**Look at the initial access vectors on actual incidents.** If phishing is not among the main routes, the programme's size relative to other controls is worth revisiting. This is a five-minute check against the incident record.

**Compare simulation difficulty to real received phishing.** Sample what the gateway caught and ask whether campaigns resemble it. This tells the awareness team whether it is testing the real threat.

**Check whether high-click individuals interact with real phishing.** Where the gateway records interaction, this is the sharpest available test of whether the simulation identifies anything real.

**Put the four teams in a room quarterly.** A standing meeting where the four datasets are discussed together, which is an organisational fix requiring no technology and no budget.

**Give the awareness manager access.** Read access to gateway and incident summaries, so the person running the programme can see the environment it operates in.

**Report the joined view upward.** One page combining simulation performance, real phishing volume, real reporting rate and phishing-attributed incidents. This is the programme's actual context and leadership has never seen it on one page.

## Who Feels the Pain

The awareness manager, running a programme in isolation from every piece of evidence about the threat it addresses.

The organisation, funding a programme whose relationship to its actual risk has never been examined, possibly at a scale disproportionate to the exposure.

Employees, receiving simulations of a difficulty unrelated to the phishing that actually reaches them.

And the security function as a whole, which has four teams reporting four numbers and no view of whether they add up to anything.

## Impact If Fixed

Comparing simulation reporting to real reporting is one query and would tell an organisation more about its programme than a year of click-rate trends.

Checking the incident record's initial access vectors is a five-minute question that occasionally reveals the programme is sized for a risk that is not the organisation's largest.

And a quarterly meeting between four teams who already have the data costs nothing and is the organisational fix that makes every other measurement in this niche possible.
