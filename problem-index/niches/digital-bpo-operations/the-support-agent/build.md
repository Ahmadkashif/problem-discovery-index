# Build: Load-Aware Scheduling and a Real Performance Record

**Niche:** [[niches/digital-bpo-operations/the-support-agent/profile|The Support Agent]]
**Industry:** [[industries/digital-bpo-operations|Digital BPO Operations]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Route and schedule against the emotional and cognitive load an agent has absorbed, and give them a performance record built from every contact rather than four.
**Tags:** #gradient-boosting #time-series-forecasting #evaluation-metrics #confidence-intervals #descriptive-statistics #survival-analysis #worker-facing #automation
**Contested on:** Whether accumulated contact difficulty can be tracked and used to route work without becoming another surveillance metric.

## The Problem

Routing in contact operations considers skill, availability and queue priority. It does not consider what the agent has just been through.

An agent who has taken four consecutive escalated, abusive or emotionally heavy contacts is measurably less able to handle a fifth well, and the system routes the fifth to them because they are next available. Break scheduling is an occupancy calculation performed hours earlier by a workforce management system that knows nothing about the morning's contacts.

The composition shift makes this worse continuously. Deflection has removed the easy contacts that used to provide natural recovery between hard ones, so the difficult ones now arrive consecutively.

Meanwhile the performance picture the agent receives is four sampled contacts, which tells them almost nothing about how they are actually doing.

## Why Nobody Has Built This

Routing optimises service level and occupancy, both of which any load-aware constraint reduces in the short term. The benefit — lower attrition, better handling of difficult contacts, fewer escalations — is diffuse and delayed, and attrition in this industry is budgeted for rather than fought.

Load is also not measured. Contact difficulty is not a field; emotional intensity is not scored; and cumulative exposure across a shift is tracked by nobody. Building the measure is a prerequisite that nobody has had a reason to build.

And there is a legitimate concern that a difficulty score becomes another surveillance metric used against agents, which is a real risk and is a design constraint rather than a reason not to build it.

## What to Build

A load measure, load-aware routing, and a full-coverage performance record.

**Score contact difficulty and emotional intensity.** From the transcript: customer distress and hostility, complexity, escalation, duration, and how it ended. This is a routine classification task over the corpus and it produces a per-contact load value.

**Accumulate it across the shift with decay.** An agent's current load is the weighted sum of recent contacts, decaying over time and resetting with a break. This is the state variable routing should consider and it does not currently exist.

**Route and schedule against it.** Where the queue permits, an agent above a load threshold gets an easier contact next, or a short recovery break, or a switch to back-office work. Break timing responds to accumulated load rather than to a schedule set at 6am. The service level cost is small and measurable; the alternative is paying for it in attrition.

**Protect it from misuse explicitly.** The load score describes the work, not the agent, and must never enter performance evaluation. Committing to that in writing and in access control is what makes the measure acceptable to the workforce, and without that commitment it will be resented and gamed.

**Build the real performance record.** From full-coverage scoring: how this agent handles each contact type, how they do on difficult contacts specifically, their resolution rate, their trend, with intervals. This is what an agent has never had — an account of their own performance based on their whole month rather than four draws — and it is the foundation for coaching that is believed.

**Make it portable.** Contact volumes by type, tenure, resolution performance, languages, systems, specialisms — a professional record the agent owns and can take with them. In an industry with very high attrition, a workforce that can evidence its experience is a workforce with some leverage, and that is precisely why it does not exist.

## Target Customer

BPO operations and people leadership, where the case is attrition — the single largest cost in the business, routinely above thirty percent annually, and driven substantially by the conditions this addresses. Also clients with supplier labour standards, which increasingly include wellbeing provisions.

## Impact If Built

Difficult contacts stop arriving back to back at whoever is next available. Break timing responds to what actually happened rather than to a forecast. Agents get a performance account based on their whole month. And the industry's defining cost — attrition — gets addressed at one of its actual causes rather than budgeted for.
