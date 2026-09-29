# Recovery as a Scored Decision

**Niche:** [[niches/crypto-exchanges/account-recovery/profile|Account Recovery]]
**Industry:** [[industries/crypto-exchanges|Crypto Exchanges]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The exchange has years of behavioural history on the account and decides recovery requests from a document and an agent's instinct.
**Tags:** #gradient-boosting #logistic-regression #evaluation-metrics #confidence-intervals #automation #worker-facing #compliance #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to get a locked-out customer back to their funds without opening the door to the attacker running the same play — and whoever resolves the honest cases automatically without raising the takeover rate clears the queue that dominates support.

## The Problem
A recovery request arrives. The exchange knows how this account has behaved for three years — when it logs in, from where, on what device, what it trades, how it funds, what its withdrawal patterns are, how it has recovered before. The decision is made instead from a submitted identity document and whether the agent finds the story plausible. Honest customers wait weeks and some never get back in; attackers who prepare well enough get through; and neither error rate is known.

## Why Nobody Has Built This
Recovery sat in support rather than in risk, so it was staffed as a queue rather than modelled as a decision — the organisational placement determined the approach. Automating it feels dangerous because the failure mode is handing an account to a thief, and that asymmetry froze the problem. The behavioural data lives in systems support cannot reach. And nobody measures recovery outcomes, so there is no baseline to improve against.

## What to Build
Score the request against the account's own history. Model the recovery request as a risk decision using the account's behavioural history, which is the core and is a far stronger evidence base than any document. Use continuity signals — device, location, network, timing, prior recovery behaviour — since a genuine customer usually looks like themselves in several ways at once. Treat the takeover playbook as the negative class, because the attack patterns are known and are what the score must separate. Automate the clear cases in both directions, as a large share are unambiguous once the history is consulted and they currently queue behind everything else. Route the genuinely uncertain to a human with the evidence assembled, which is where agent judgement is worth its cost. Set the decision threshold from stated costs on both sides, since silent conservatism is a choice being made without being named. Add friction proportionate to risk — waiting periods, withdrawal holds, step-up verification — rather than treating recovery as binary, because graduated response is what makes automation safe here. Measure takeover rate and false-denial rate together, as improving one at the other's expense is the trap. Feed confirmed takeovers back into the model, since they are labelled and currently only feed an incident report. Preserve a route for customers whose circumstances defeat every signal, because they exist and are the most vulnerable. And report queue time and outcome by segment, which is how the function becomes manageable.

## Target Customer
Support and risk leadership, customers locked out of their own assets, and identity and takeover vendors whose products assess a session rather than an account's history.

## Impact If Built
Recovery was placed in support and staffed as a queue rather than modelled as a decision. Years of behavioural history is a stronger evidence base than a submitted document, and it resolves most requests in both directions automatically.
