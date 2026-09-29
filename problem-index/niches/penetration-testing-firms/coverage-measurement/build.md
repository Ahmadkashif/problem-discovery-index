# Build: Coverage From the Tester's Own Traffic

**Niche:** Coverage Measurement
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A passive instrumentation layer that turns the proxy logs and tool output a tester already generates into a depth-banded coverage map, with no extra work from the tester.
**Tags:** #graph-theory #evaluation-metrics #confidence-intervals #bayesian-inference #k-means-clustering #automation #data-integration #worker-facing
**Contested on:** Whether an engagement can state how much of the attack surface it actually reached, by what technique and at what depth.

## The Problem

A tester spends two weeks generating an extremely detailed record of exactly what they examined. Every request passes through an intercepting proxy and is logged with its parameters, its method, its authentication context and its response. Every tool run records what it touched. Every manual probe leaves a trace.

At the end of the engagement the tester writes a report from memory and notes, and the record is deleted or archived and never read. The single most complete account of what the engagement covered exists, is machine-readable, and is used for nothing.

So the report has no denominator, and the firm has no way to know its own coverage patterns across engagements — which asset classes its testers consistently under-examine, which techniques get skipped when time runs short, whether coverage differs systematically between its senior and junior staff. All of it is derivable from logs the firm already holds and none of it is derived.

The reason is that nobody has built the aggregation, and any solution that asks testers to record what they covered will fail, because testers are working under time pressure on the thing they are actually paid for and will not maintain a parallel bookkeeping exercise.

## Why Nobody Has Built This

**Any tester-effort solution dies on contact.** Coverage checklists exist and are abandoned within a day of a real engagement. The measurement has to be entirely passive or it will not survive, which is a harder engineering problem than a form.

**The denominator requires modelling choices that invite attack.** Attack surface has no natural total. Whatever enumeration a product chooses — endpoints, parameters, states, roles — a competitor can argue is the wrong one. This is genuinely contestable and is why nobody wants to publish first.

**Depth is the hard part.** Distinguishing an endpoint that was requested once from one that was systematically fuzzed with a hundred payload classes requires classifying the tester's interactions by intent and technique, which is inference over traffic patterns rather than counting.

**Coverage data is commercially double-edged.** It would show clients how much was not reached, and it would show firm management how individual testers actually spend their time — which raises a surveillance objection from exactly the people whose adoption is required.

**Test traffic is sensitive.** Proxy logs from a penetration test contain credentials, session tokens, exploited payloads and client data. Building a product that ingests and retains them creates a serious security and handling obligation, which is an uncomfortable position for a security firm to be in.

## What to Build

**Passive ingestion, zero tester effort.** Read the proxy history, the tool output and the scan results the engagement already produces. The tester changes nothing about how they work, and the product's entire adoption case rests on that.

**Classify interactions by technique and depth.** Infer from traffic patterns what was done to each surface element: requested, enumerated, scanned, fuzzed with which payload classes, manually reasoned about. Map to ATT&CK technique where the pattern supports it, and — critically — record attempted-and-unsuccessful separately from not-attempted, which is the distinction that makes the output a coverage statement rather than a findings summary.

**Build the denominator per asset class, with honest uncertainty.** Enumerated surface from discovery, API specifications, crawling and the client's own inventory, plus an explicit estimate of what enumeration missed, derived from how much of the eventually-discovered surface was absent from the initial enumeration across the firm's past engagements. Report against the enumerated surface, with the unenumerated portion stated rather than assumed away.

**Report four depth bands, not a percentage.** Untested, automated only, manually examined, deeply tested — per area. Four bands are harder to game, easier to act on and more honest than any single number, and the untested list is the output that matters most.

**Calibrate what a clean result is worth.** From the firm's own history: where a later or longer engagement found something in an area a previous one had covered at a given depth, that is a measured miss rate. Every firm with repeat clients has this data. Nobody has computed it, and it is what turns coverage from a description into a confidence statement.

**Handle the traffic like the sensitive material it is.** Local processing by default, aggregate extraction rather than log retention, and a security posture the firm's own testers would sign off on — because they will be asked to.

**Show the tester their own map, live.** The most persuasive adoption path is not management reporting but a live view during the engagement showing what has been covered and what has not, so a tester on day eight can see where the gaps are while there is still time to close them. This makes the tool an ally rather than a monitor, and it is the framing that determines whether it is used.

## Target Customer

Specialist testing boutiques whose work is genuinely deeper and who currently cannot demonstrate it. Coverage is the first credible non-price differentiator available to them, and they are small enough to adopt something new quickly.

Testing platform vendors — the firms building engagement management and delivery platforms — for whom this is a natural feature and who already sit in the data path.

Cyber insurers as the eventual demand-side forcing function, since they price on whether testing occurred and have no way to distinguish thorough from thin.

## Impact If Built

The report acquires a denominator, which is what the whole assurance problem reduces to. Everything else in this niche follows from being able to say what was covered.

The live view changes engagements while they are running. A tester who can see on day eight that an entire authenticated role has gone untouched will cover it, and today they frequently do not notice until the write-up.

And the firm gets a mirror. Systematic coverage gaps — the asset classes its testers habitually skip, the techniques that get dropped under time pressure — are currently invisible to management and are exactly the patterns that produce the misses clients discover later.
