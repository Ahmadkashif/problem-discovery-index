# Urgency Asserted by the Sender at No Cost

**Niche:** [[niches/work-collaboration-tools/attention-and-notification/profile|Attention & Notification]]
**Industry:** [[industries/work-collaboration-tools|Work Collaboration Tools]]
**Type:** Fix (Pain Point)
**One-liner:** Anybody can mark a message urgent, tag everyone in a channel or send at eleven at night, and none of it costs the sender anything — so the signals that were meant to distinguish the important have been exhausted.
**Tags:** #descriptive-statistics #evaluation-metrics #hypothesis-testing #confidence-intervals #workflow-orchestration #worker-facing #quick-win #automation
**Contested on:** Every serious competitor that takes this seriously is fighting to make the total interruption load a measured quantity with an owner — and whoever gives an organisation control over the aggregate takes the attention nobody is currently accountable for.

## The Problem
A channel mention that alerts everyone is free to send and costs the organisation a hundred interruptions. Marking a message as urgent is free and costs whatever the recipients' attention is worth. Sending at eleven at night is free and costs a recipient's evening. In each case the sender bears none of the cost and receives all of the benefit, which is the structure that guarantees overuse — and the predictable result is that the urgent marker now carries no information, the everyone-mention is used for announcements nobody needed, and people either disable the signals entirely or live permanently interrupted.

## Why It's Still Broken
Making these signals costly is a product decision that reduces engagement, which no vendor's metrics reward. Organisations treat it as a culture problem and issue guidance, which does not survive the first genuinely urgent situation. And there is no measurement: nobody counts how many everyone-mentions were sent last month, by whom, and how many recipients acted on them, so the norm has no evidence behind it in either direction.

## What a Fix Looks Like
Attach a visible cost to the signal and measure its use. Show the sender the reach before they send: this mention will interrupt two hundred and forty people, which is a single line of interface and empirically changes behaviour more than any policy. Report usage — who sends broad interruptions, how often, and what proportion were acted upon — at the team level, since the pattern is usually concentrated in a small number of senders who have no idea of their aggregate effect. Rate-limit the strongest signals rather than prohibiting them, which preserves genuine urgency while making routine overuse impossible. Default out-of-hours sending to scheduled delivery with an explicit override, since most late-night messages are not urgent and the sender rarely intends the interruption. And make the urgent marker mean something by measuring it: a marker with a published acted-upon rate recovers its information content, and one used indiscriminately visibly does not.

## Who Feels the Pain
Everyone on the receiving end of a signal that has lost its meaning; the people with genuinely urgent messages who can no longer be distinguished; and senders who have no idea that their routine announcement interrupted a working day for two hundred people.

## Impact If Fixed
Showing reach before sending is a single interface line and is the cheapest behavioural intervention available in this whole industry. Scheduled out-of-hours delivery by default is similarly small and addresses a large share of the evening interruption load, and measuring the acted-upon rate on urgent markers is what would restore a signal the category has entirely exhausted.
