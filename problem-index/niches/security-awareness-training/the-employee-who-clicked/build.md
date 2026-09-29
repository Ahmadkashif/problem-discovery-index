# Build: A Result That Is Fair and a Response That Helps

**Niche:** The Employee Who Clicked
**Industry:** [[industries/security-awareness-training|Security Awareness Training]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Record results with the difficulty of the item attached, give the person a route to contest, and design the post-click experience to produce reporting rather than shame.
**Tags:** #bayesian-inference #evaluation-metrics #confidence-intervals #compliance #worker-facing #hypothesis-testing
**Contested on:** Whether being deceived by a professionally designed message is treated as information about the message or as a failing of the person.

## The Problem

A click is recorded as a click. The record does not carry how difficult the item was, how many colleagues also clicked it, what the person's overall pattern looks like, or what was happening at the time.

So two people with very different situations get identical records. One clicked an obviously fraudulent message with a misspelled sender. The other clicked a message referencing a real internal system, apparently from a colleague, arriving in the middle of a genuinely busy period, which two thirds of their department also clicked. Both are on the list. Both are assigned the same training. Both are counted the same way in any escalation policy.

There is no route to contest. The person cannot see the record, cannot see the difficulty rating, and has no mechanism to say that the message was indistinguishable from real internal mail — which may be true and may be a finding about the organisation's own mail practices rather than about them.

And the response is a training assignment, which is experienced as a consequence. The thing the organisation actually wants from this person next time is that they report the message, and nothing in the post-click experience is designed to produce that.

## Why Nobody Has Built This

**The click is the unit of the whole system.** The platform is built to count clicks, and attaching context to each one is a data model change nobody has needed.

**Difficulty is not measured.** Recording difficulty with a result requires difficulty to be a measured property, which is the gap in [[niches/security-awareness-training/difficulty-calibration/profile|🎯 Difficulty Calibration]].

**A contest mechanism creates work.** Allowing people to challenge results means somebody must adjudicate, which is a workflow nobody has resourced.

**The individual is not the customer.** The platform serves the programme owner. The person being measured has no standing in the product.

**Escalation looks like rigour.** Repeat-clicker policies with consequences read as a serious programme, and the argument that they are counterproductive is indirect.

**Nobody measures the effect on reporting.** The cost of the punitive experience lands as reduced willingness to come forward, which nothing tracks.

## What to Build

**Record difficulty with every result.** The item's calibrated difficulty, the proportion of recipients who also clicked, and the individual's estimated susceptibility separated from the items they happened to receive. This makes the record fair and it makes any subsequent decision defensible.

**Show the person their own record.** What they clicked, how difficult it was, how many colleagues also did, and what it means. Transparency about a record attached to you is the minimum, and almost no programme provides it.

**Provide a route to contest.** A short form saying why the message was indistinguishable from legitimate mail, reviewed, with the outcome recorded. Frequently the contest is correct and is a finding about the organisation's own communication practices.

**Design the post-click experience to produce reporting.** Explain how the deception worked, state plainly that it was designed to be difficult and that many colleagues also clicked, and make the next step obvious — here is how to report something like this. This is a content change and it is most of the fix.

**Never escalate on count alone.** A repeat clicker is a signal about exposure, workflow or item difficulty rather than about discipline. Route them to a conversation, not to a consequence.

**Reward reporting visibly and individually.** The person who reports gets an acknowledgement and, where it mattered, a note that it did. This is free and it is the strongest available lever on the behaviour that helps.

**Measure what the experience did.** Subsequent reporting rate for people who clicked, compared to those who did not. If clicking predicts reduced reporting, the post-click experience is actively harmful and the programme should know.

## Target Customer

HR and employee relations, who own the workforce relationship, increasingly field the complaints, and would recognise the fairness argument immediately.

Works councils and employee representation, particularly where consultation is required, who are the constituency most able to force the change.

Security leadership at organisations that want the reporting behaviour more than they want the low click rate — which is most of them once the trade is named.

## Impact If Built

Recording difficulty with the result makes an individual record fair, which matters because that record is used to assign training and sometimes more.

A post-click experience designed to produce reporting rather than shame is a content change with no cost and directly addresses the behaviour the programme most needs.

And measuring whether clicking predicts reduced subsequent reporting would establish whether the programme's own design is undermining its objective — which is the most important unanswered question in this category.
