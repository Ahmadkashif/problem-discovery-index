# Fix: Activity Reported as Assurance

**Niche:** Programme Effectiveness Measurement
**Industry:** [[industries/bug-bounty-platforms|Bug Bounty Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Submission counts, payout totals and triage times are reported upward as evidence of security, and every one of them can improve while nothing gets safer.
**Tags:** #evaluation-metrics #confidence-intervals #hypothesis-testing #compliance #revenue-impact #descriptive-statistics
**Contested on:** Whether a programme can show that its spend bought security, or only that it bought submissions.

## The Problem

The quarterly programme report goes to security leadership and sometimes to a board. It shows submissions up, valid findings up, average triage time down, payouts totalling a number. The conclusion drawn is that the programme is working.

Every metric on that page can move in the reported direction without the organisation being any safer. Submissions rise when scope expands or when a researcher writes a scanner. Valid findings rise when the validity bar softens. Triage time falls when the team hires. Payouts rise when the market rate rises. Severity mix shifts with how one person rates things.

None of this is fabrication. It is the standard problem of a process metric substituting for an outcome, and it persists because the outcome metric is harder and nobody has been asked for it.

The effect compounds upward. A board hears the organisation runs a bug bounty programme with growing engagement. A customer security questionnaire records that a programme exists. An insurer treats it as a positive signal. At each step the nuance disappears and the activity becomes assurance, exactly as it does with a penetration test report.

## Why It's Still Broken

**Nobody is asking for better.** Boards do not know what to ask for, security leaders present what the platform provides, and the platform provides what it can compute from its own data. No party in the chain has requested an outcome measure.

**The activity metrics are genuinely useful operationally.** Triage time and submission volume matter for running the programme. The error is not measuring them; it is presenting them as an answer to a different question.

**The outcome question has an uncomfortable answer.** A novelty rate showing that much of the spend bought findings already known internally would be bad news for the programme owner who championed it, and there is no external pressure forcing its production.

**Comparison against internal findings requires work nobody is assigned.** The join between bounty submissions and internal finding queues is achievable and is nobody's task, sitting between the programme manager, the vulnerability management owner and the application security team.

**Everyone benefits from the current framing.** The platform reports growth, the programme owner reports engagement, leadership reports a control in place. The only loser is the accuracy of the organisation's understanding of its own security, which appears on nobody's objectives.

## What a Fix Looks Like

**Compute the novelty rate, once.** For a year of valid findings, how many corresponded to something already in an internal queue, already reported by a scanner, or already known. It takes an analyst a few weeks with access to both sides and it is the single number that would reframe every subsequent report. Most programmes have never attempted it.

**Report time-to-discovery as the headline.** How long weaknesses existed in production before being reported, and whether that interval is shortening. It is measurable, it moves, it is not gameable by expanding scope, and it corresponds to something a board can act on.

**Separate the operational dashboard from the assurance statement.** Triage time and submission volume belong in a programme operations view. The report going upward should contain novelty, time-to-discovery and what the programme found that nothing else could — and should explicitly state what it does not establish.

**Say what the programme does not cover.** A bounty programme tests what researchers choose to look at within a scope. That is a partial and self-selected sample, and stating it plainly prevents the artefact from being read as comprehensive assurance — the same fix that works for [[industries/penetration-testing-firms|Penetration Testing Firms]] and for the same reason.

**Ask the platform for peer comparison on outcomes.** Platforms benchmark activity across programmes. They could benchmark novelty rate and time-to-discovery, and customers asking for it is what would make them build it.

**Answer the questionnaire honestly.** Where a customer asks whether a bounty programme exists, the answer should include the scope and what it covers, rather than a bare yes. Programmes with genuinely broad scope benefit from the distinction and currently get no credit for it.

## Who Feels the Pain

The organisation, whose leadership believes a control is delivering assurance it may not be delivering, and which allocates budget accordingly.

The security leader, who knows the report is activity and has nothing better to present.

Programmes that are genuinely effective, indistinguishable from ones that are not, and therefore unable to argue for more budget on the strength of results.

And every downstream reader — board, customer, insurer — treating the existence of a programme as a security signal of unknown magnitude.

## Impact If Fixed

Computing the novelty rate once would change how every programme is discussed, and it requires no new technology — only access to both sides of a join and someone assigned to do it.

Time-to-discovery as the headline metric replaces a set of numbers that improve with effort with one that improves only when the organisation actually gets faster at finding its own weaknesses.

And stating what the programme does not cover closes the same interpretive gap that runs through every assurance business in this cluster, at the cost of a paragraph.
