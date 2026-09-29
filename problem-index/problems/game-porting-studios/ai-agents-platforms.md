# AI Agents & Platform Opportunities — Game Porting Studios

**Industry:** [[game-porting-studios|Game Porting Studios]]

---

## 1. Bid Assessment Platform
#ai-platform #gradient-boosting #graph-neural-networks #confidence-intervals #bayesian-inference #bert #evaluation-metrics #revenue-impact

**Concept:** A platform that turns the sector's core commercial risk into a measured quantity. It runs an automated codebase assessment in hours rather than weeks — inside the publisher's environment if required, reporting only aggregate risk indicators, which addresses the access problem directly since publishers object to handing over code rather than to being told what the code implies. It predicts effort by work category from that assessment, calibrated on the studio's own completed ports, and returns a distribution rather than a point, so the business knows whether the plausible range runs to double.

**Inputs:** Static analysis of the candidate codebase — structure, dependency and call graphs, platform-specific code concentration, renderer feature usage, threading and allocation patterns, custom module footprint; target platform characteristics; the studio's completed projects with realised hours recorded by cause.

**Outputs / Actions:** Effort by category with intervals, which is what makes an estimate defensible and improvable rather than a single number defended by seniority. A risk profile naming the specific properties driving the uncertainty. A bid recommendation that includes declining to bid, and — where the uncertainty is genuinely wide — a case for a shared-risk contract structure rather than a fixed price with a large margin.

**Why now:** Nobody in this sector treats completed projects as data, so a studio with forty ports has forty unused observations. The prerequisite is recording effort by cause, which is a process change any studio can start immediately and which pays for itself before any model exists.

**Market:** Porting and co-development studios, the publishers commissioning them who currently receive bids they cannot compare on anything but price, and the co-dev arms of larger studios facing the same estimation problem internally.

---

## 2. Optimisation Agent
#ai-agent #gradient-boosting #graph-neural-networks #change-point-detection #transfer-learning #confidence-intervals #evaluation-metrics #worker-facing

**Concept:** An agent for the phase where port schedules are lost. It maps a profile signature plus the surrounding codebase structure to a ranked set of likely causes with the evidence, drawing on the studio's own portfolio of previous optimisation work — which is the expertise that currently lives in a handful of engineers and transfers only by apprenticeship. It estimates what each fix would return in frame time before the work is done, accounting for interaction between fixes rather than treating them as additive, which turns an open-ended search into a planned sequence with a projected end state. And it compares against genre-matched titles on the same platform, so a team knows whether they are near the achievable limit or missing something large.

**Inputs:** Platform profiler captures with subsystem and GPU breakdowns; codebase structure around implicated systems; asset budgets and streaming behaviour; the studio's record of previous causes found and returns realised; comparable titles on the same platform.

**Outputs / Actions:** Three ranked hypotheses with evidence rather than a verdict, because an engineer evaluates hypotheses in minutes and a confidently wrong attribution costs days on a platform with limited debugging tooling. Expected frame time return per fix, which is what makes the phase schedulable. A cross-title baseline. And a growing portfolio record that makes the next project on the same engine start ahead.

**Why now:** The performance phase is the least estimable part of these projects and the one that consumes the scarcest people, and the mapping from profile to cause is exactly the pattern recognition that a portfolio of completed work can support and a single engineer's memory currently does.

**Market:** Porting studios, co-development shops, and the internal platform and performance teams at larger studios who face the same problem on their own titles.

---

## 3. Port Operations Agent
#ai-agent #large-language-models #graph-neural-networks #time-series-forecasting #change-point-detection #cnns #workflow-orchestration #worker-facing

**Concept:** An agent covering the two things that make these projects attritional: an unfamiliar codebase and a client one that will not stop moving. On comprehension, it produces architectural summaries of an inherited codebase — subsystem structure, ownership boundaries, platform-specific concentration, threading and allocation patterns — and explains constructions that look wrong but are deliberate, which is the difference between a day of investigation and a paragraph. On churn, it measures the cost of every client update in integration hours, invalidated testing and reintroduced performance work, predicts what an incoming update will touch before it is merged, and continuously re-forecasts completion including the congestion of certification submission windows.

**Inputs:** The inherited codebase with version history where supplied; incoming client diffs; test coverage and its invalidation mapping; integration effort records; platform certification requirements and submission calendars; velocity and remaining optimisation work.

**Outputs / Actions:** Architecture summaries that compress the orientation phase nobody schedules. Explanations of deliberate oddities with the likely reason inferred. Merge impact predicted on arrival rather than discovered after integration. A measured churn cost — the number that makes the commercial conversation about update cadence possible rather than adversarial, since most clients would accept a scoped arrangement if the cost were demonstrable. Continuous cross-platform regression checking with perceptual tolerance, so visual comparison is usable rather than switched off in week one. A completion forecast shared with the client, which removes much of the adversarial structure created by two sides holding different pictures.

**Why now:** Concurrent development is now the norm rather than the exception for ports, and the cost it imposes is absorbed silently out of fixed-price margin because nobody measures it.

**Market:** Porting studios and their producers, publishers commissioning ports alongside live development, and QA organisations carrying the verification load these projects generate.
