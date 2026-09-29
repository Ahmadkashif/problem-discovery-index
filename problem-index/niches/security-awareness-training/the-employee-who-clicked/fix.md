# Fix: The List Is Visible and the Difficulty Is Not

**Niche:** The Employee Who Clicked
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Fix (Pain Point)
**One-liner:** The person's name appears on a report; the fact that two thirds of their colleagues clicked the same message, and that it was designed to be indistinguishable from real internal mail, does not.
**Tags:** #evaluation-metrics #confidence-intervals #worker-facing #compliance #descriptive-statistics
**Contested on:** Whether being deceived by a professionally designed message is treated as information about the message or as a failing of the person.

## The Problem

A campaign runs. Sixty-two per cent of the finance department clicks, because the message referenced a real internal payment system, used the correct internal terminology, and arrived during month-end close.

The report lists the individuals. Their managers may see it. Some organisations circulate departmental comparisons. The people concerned receive a training assignment.

What the report does not say is that this campaign was substantially harder than the previous one, that a majority of a highly capable department clicked, that the lure exploited an internal process the organisation itself created, or that the timing coincided with the busiest week of the finance calendar.

So a result that is mostly a statement about the campaign and the organisation is presented as a list of individuals who failed. The individuals experience it that way. Their managers, who see a name on a list without the context, frequently do too.

The context is available. The platform knows the campaign-wide click rate, the difficulty of the template and the timing. Including it would reframe the same data entirely, and it is left out because the report is built around identifying who clicked.

## Why It's Still Broken

**The report is designed to identify individuals.** Assignment of remedial training requires knowing who, so the individual list is the product and the context is supplementary.

**Difficulty is unmeasured, so context cannot be stated precisely.** Without a difficulty parameter the report cannot say this was a hard campaign, only that many people clicked — which is weaker and is still more than is currently shown.

**Comparative framing sells the programme.** Departmental comparison creates engagement and a sense of accountability, and it also turns a measurement into a competition between teams.

**Managers want the names.** A manager asking who in their team clicked is asking a reasonable question, and the answer without context produces an unreasonable conclusion.

**Nobody represents the individual.** The report is designed for the programme owner. The person named has no input into how they are represented.

**The organisation's own role is invisible.** A lure exploiting an internal process the organisation created is partly a finding about that process, and the report frames it entirely as individual behaviour.

## What a Fix Looks Like

**Put the campaign context on every individual result.** This campaign's overall click rate, its difficulty relative to previous ones, and the proportion of the person's peer group who also clicked. Three numbers, and they change the meaning entirely.

**Show the person their own record with the context.** The individual should see what the report says about them and the context that qualifies it, before anyone else acts on it.

**Report to managers in aggregate, not by name.** A manager needs to know their team's exposure, not which individual clicked. Naming individuals to managers is the specific practice that produces most of the harm and delivers almost no operational benefit.

**Stop departmental leaderboards.** They convert a measurement into a competition, produce pressure that lands on individuals, and add nothing a rate would not.

**State when the lure exploited an internal process.** A message referencing a real internal system, terminology or workflow is partly a finding about the organisation. Saying so shifts attention to a fixable cause.

**Account for timing.** A campaign landing during month-end close or a major deadline is testing load as much as awareness. Recording it prevents the wrong conclusion.

**Let the person add context.** A single field where someone can say why the message was indistinguishable. Frequently they are right, and it is free information about the organisation's own mail practices.

## Who Feels the Pain

The individual, named on a list for a result that was mostly a property of the campaign, with no context accompanying their name and no route to add any.

Their manager, receiving a name without context and drawing the conclusion the presentation invites.

The department that happened to receive a well-targeted campaign, and now appears worse than departments that received a generic one.

And the programme, whose standing with the workforce is set by exactly these moments.

## Impact If Fixed

Three context numbers on every individual result cost nothing and transform what the result means to everyone who reads it.

Reporting to managers in aggregate rather than by name removes the practice that causes most of the harm while retaining everything operationally useful.

And noting when a lure exploited the organisation's own internal process would redirect attention from the person who clicked to the process that made the lure convincing — which is frequently the more fixable problem.
