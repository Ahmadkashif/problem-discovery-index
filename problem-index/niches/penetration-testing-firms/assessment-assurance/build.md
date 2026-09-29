# Build: The Report With a Denominator

**Niche:** Assessment Assurance
**Industry:** [[industries/penetration-testing-firms|Penetration Testing Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** A reporting layer that states what was tested, at what depth, and what a clean result in each area is actually worth — turning a findings list into an assessment with a denominator.
**Tags:** #evaluation-metrics #confidence-intervals #bayesian-inference #graph-theory #hypothesis-testing #compliance #automation #data-integration
**Contested on:** Whether a test report states what its clean results actually mean, or leaves the client to read two weeks of sampling as evidence of security.

## The Problem

Every penetration test report is a numerator without a denominator. It lists findings. It does not say how many hosts, endpoints, parameters, roles or workflows were examined, out of how many existed, using which techniques, at what depth, and where the tester ran out of time.

The consequence is that the report cannot support the inference everybody draws from it. A clean result in an area could mean the tester probed it thoroughly with the right techniques and it held. It could mean they ran an automated pass and moved on. It could mean they never reached it, because the authentication flow they needed was broken on day three and by the time it was fixed the engagement had four days left and a different priority. All three produce identical silence in the document.

Clients act on that silence. Boards are told the system was tested. Insurers and enterprise customers accept a clean report as assurance. Security budgets are allocated away from areas that appear fine. And a tester who knows the report gives a false impression has no field in which to say so — the format has no place for "we did not reach this", and raising it in the debrief sounds like an excuse for not having finished.

## Why Nobody Has Built This

**Coverage reporting is commercially unattractive at first glance.** A firm that states it reached forty per cent of the attack surface looks worse than one that stays silent, and the buyer cannot yet tell that the silent competitor covered twenty. Honesty is penalised until enough of the market is honest, which is the classic first-mover problem and the reason this has not happened on its own.

**The denominator is genuinely hard to establish.** Total attack surface is not a well-defined quantity. Counting hosts is easy and nearly meaningless; counting reachable states, parameter combinations or business logic paths is the thing that matters and has no natural unit. Any coverage measure involves defensible modelling choices that a competitor can attack.

**Depth is not binary.** An endpoint can be touched, scanned, fuzzed, manually probed or deeply reasoned about, and a coverage number that treats these as equivalent is worse than nothing. The measure has to be multi-dimensional, which makes it harder to present.

**The remediation half requires data from after the engagement.** Whether findings were fixed lives in the client's ticketing and release systems, on the other side of a relationship that ends at handover, and no contract asks for it.

**The business model resists it.** Firms sell days. A measure that quantifies how much an engagement did not cover invites the client to ask why they are not buying more days — which is actually the correct response and the commercial opportunity, but it does not feel that way from inside a competitive bid.

## What to Build

**Instrument the engagement rather than asking the tester.** Coverage derived from the tester's own proxy traffic, tool output, and interaction logs — which endpoints were requested, which parameters manipulated, which roles exercised, which hosts probed and by what technique. The tester should not have to record anything; the measurement should be a by-product of working. This is the design constraint that determines whether it is ever adopted.

**Model the denominator honestly and per-asset-class.** Enumerated attack surface from discovery, plus an explicit estimate of what discovery itself is likely to have missed. Report coverage against the enumerated surface with a stated caveat about the unenumerated part, rather than pretending to a total.

**Report depth as a band, not a percentage.** Per area: untested, automated only, manually examined, deeply tested. Four bands, plainly stated, convey more than any single number and are far harder to game. The single most valuable output of the whole system is a list of areas marked untested, because that is the information the report currently hides.

**Express confidence in negatives.** For each area at each depth band, what the absence of a finding is worth — ideally calibrated from the firm's own corpus, by asking how often a longer engagement in a comparable area subsequently found something the shorter one missed. This turns a vague honesty problem into a number the firm can improve.

**Close the remediation loop contractually.** A scheduled check at ninety days and one year, written into the engagement at signing as part of the deliverable, capturing what was fixed, what was not and why. Clients accept it readily because it is useful to them, and it is what converts the firm's archive into a record of whether its work mattered.

**Build the corpus and use it.** Across thousands of engagements: which finding types get remediated and which are perennially ignored, which remediation advice holds and which produces a recurrence in the next release, which weaknesses appear in which stacks. This is the asset the industry already generates and discards, and it is what would let a firm advise on the basis of evidence rather than experience.

## Target Customer

Testing firms with a quality position to defend — the specialist boutiques whose work is genuinely deeper and who currently have no way to demonstrate it against a commodity competitor. Coverage reporting is the first credible non-price differentiator this industry could have.

Client security leadership are the pull side, particularly those who have to present testing results to a board or an auditor and know they are overstating what the report supports.

Cyber insurers are the most interesting third party: they price risk partly on whether testing was performed, with no way to distinguish a thorough test from a thin one, and a coverage standard would let them.

## Impact If Built

The report starts supporting the inference people already draw from it. Today the gap between what a clean result means and what it is taken to mean is the industry's largest honesty problem, and it is closed by adding information rather than by anyone behaving differently.

The untested list changes client behaviour immediately. A security leader who learns that a third of their estate was never reached will buy more testing, which makes the honest firm's position commercially better rather than worse once the measure is visible.

And remediation linkage would finally let a firm answer the question its buyers most want answered: does what we do result in things getting fixed, and do our fixes hold.
