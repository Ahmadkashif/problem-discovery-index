# Email Security Classification Pointed at Pitches

**Niche:** [[niches/public-relations-agencies/the-beat-reporter/profile|The Beat Reporter]]
**Industry:** [[industries/public-relations-agencies|Public Relations Agencies]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Newsroom email already passes through classifiers that sort spam and phishing; none sorts PR pitches by relevance to the recipient's beat.
**Tags:** #bert #naive-bayes #transformers #evaluation-metrics #automation #worker-facing
**Contested on:** Every serious competitor serving the beat reporter is fighting to become the channel through which reporters choose to receive pitches and find sources, and whoever filters the inbox well enough to earn reporters' trust controls access to them for every PR firm.

## The Problem
Pitches are not spam to the filter: they come from real agencies, pass authentication, and land in the primary inbox. To the reporter most of them are noise.

## What Already Exists
Email security gateways (Microsoft Defender, Google Workspace's filters, Proofpoint, Mimecast) classify mail for spam, phishing and priority, and offer "focused" or "important" sorting based on the user's behaviour.

## The Customization Gap
The adaptation needs: a pitch detector (distinguishing PR outreach from reader email, sources and editors); beat representation from the reporter's own published work; embargo and exclusive extraction; duplicate grouping across agencies pitching the same news; and newsroom-level policies (for example, never suppress pitches from government press offices). Generic importance ranking learns from replies, and reporters rarely reply to pitches even when they use them.

## Target Customer
Newsroom IT and editors, through existing email security contracts.

## Impact If Solved
Relevance filtering delivered through software newsrooms already run, with no new tool for reporters to adopt.
