# The On-Call Engineer at Three in the Morning

**Industry:** [[observability-vendors|Observability Vendors]]
**Type:** Worker Life Changing
**One-liner:** The person the entire category exists to help is woken by a page, hands a wall of correlated dashboards, and left to work out the causal story alone at the worst hour of the day.
**Tags:** #graph-neural-networks #change-point-detection #gradient-boosting #large-language-models #confidence-intervals #evaluation-metrics #automation #worker-facing

## The Problem
On-call means carrying a phone that can wake you. When it does, an engineer has minutes to establish what is happening, at whatever hour, with whatever cognitive capacity that hour permits.

The tooling presents everything. Dashboards across dozens of services, all moving. Traces. Logs beyond reading. Deployment markers. The engineer must decide, quickly, what is cause and what is consequence, and they must do it while people are being affected and while a status page decision waits.

Frequently the incident is one they have seen before, or one a colleague has seen, or one that has occurred at a thousand other companies in the same shape. That knowledge is in someone's memory, or in a runbook that is out of date, or in a Slack thread from eight months ago that nobody will find.

Then the page turns out to be false. A threshold somebody guessed, a deploy-related blip, a flapping check. The engineer is awake anyway, and the next real page arrives with slightly less trust attached.

## Why It Matters to the Worker
On-call is one of the most consistently cited sources of dissatisfaction in software engineering, and its harms are physiological as well as professional. Interrupted sleep on a rotating schedule is a documented health cost, and the anticipation of being paged degrades rest even on quiet nights.

The competence pressure is specific. Being woken, being expected to reason clearly under time pressure about a complex system, and knowing that people can see how long it took, is an unusual burden. Engineers describe the anxiety of on-call weeks as worse than the incidents themselves.

The false page is the most corrosive part, because it converts a health cost into a pointless one. And the repeated incident is the most demoralising: being woken for the eleventh instance of something that could have been prevented is a signal about organisational priorities that engineers read accurately.

## What a Solution Looks Like
A page that arrives with a hypothesis. Not a verdict — a ranked set of candidate explanations with the evidence, so a tired person can evaluate rather than construct. This is the single largest available improvement and it is what the corpus of incidents makes possible.

Change correlation first, since most incidents follow a change and the candidates are enumerable: deployments, configuration, feature flags, infrastructure events, dependency releases.

Prior incident matching, so that the eleventh instance arrives with the previous ten and their resolutions attached. That requires nothing more than matching signatures and is the highest-value use of an organisation's own history.

Alert quality maintained so the page is trustworthy: thresholds backtested, alerts that have never fired usefully retired, and flapping conditions suppressed automatically.

And blast radius stated at page time — who is affected, how many, which regions — because the first questions asked of an on-call engineer are exactly those and answering them currently takes ten minutes.

## Impact If Solved
On-call is where the observability category's value is either delivered or not, and it is currently the moment at which the tooling helps least. Arriving with hypotheses, prior incidents and blast radius turns the first ten minutes from construction into evaluation — which is the difference between a manageable rotation and the burnout the industry complains about constantly.
