# AI Agents & Platform Opportunities — Sports Teams & Clubs

**Industry:** [[sports-teams|Sports Teams & Clubs]]

---

## 1. Scouting Memory Platform
#ai-platform #large-language-models #survival-analysis #gradient-boosting #tacit-knowledge-ml #revenue-impact

**Concept:** A platform that turns scouts' dictated notes into structured reports at the park, links each report to the video and tracking it describes, and grades every report years later against the player's career, including players the club passed on. It keeps each scout's read and its track record available to the director, the cross-checker and the scout who inherits the territory.
**Inputs:** Scouts' voice notes and grades, schedules of amateur games, video clips, pitch and swing tracking, the public draft and minor-league outcomes, and the club's own signing and development records.
**Outputs / Actions:** Structured reports drafted for one-tap confirmation; a draft-room view of each player with every scout's read and that scout's calibration; alerts when a player a scout flagged starts to break out elsewhere; handover packs when a scout leaves.
**Why now:** Speech-to-structure with LLMs makes report capture cheaper than the scout's current typing, college and amateur tracking coverage has spread, and vendors are consolidating the decision layer: Teamworks bought PFF's enterprise business in March 2026 after Zelus Analytics, Telemetry Sports and Sportlogiq. Teamworks was hiring a Data Scientist II (Soccer, remote US, posted 2026-09-22), a Senior Software Engineer for Coaching & Player Personnel (Noblesville, 2026-09-23) and a Senior Technical Product Manager, AI (remote US, 2026-10-26).
**Market:** 30 MLB clubs, 32 NFL clubs, NBA and NHL clubs and 240+ Division I football programmes, with scouting and R&D budgets in the low millions each (estimate). Teamworks, Hudl and clubs' in-house systems are the incumbents; none grades the scout's read.

---

## 2. Minor-League Revenue Agent
#ai-agent #gradient-boosting #bayesian-inference #time-series-forecasting #quick-win #revenue-impact

**Concept:** An agent for a small club's front office that forecasts demand for every home date, recommends tier prices, warns when a date is under-selling early enough to run a group or promotion push, and drafts the outreach. It starts from the two-week MVP in the ML note (public schedules and attendance, SeatGeek listing prices, synthetic primary sales) and switches to the club's own sales once a pilot shares them.
**Inputs:** Schedule, promotions calendar, weather, local events, resale listing signals, the club's ticketing sales by tier and its group-sales pipeline.
**Outputs / Actions:** Weekly price recommendations per tier with expected revenue; under-selling alerts with suggested actions; drafted emails to past group buyers for soft dates; an end-of-season review of what each price change did.
**Why now:** Public schedule and resale data make a pooled demand model possible without any club's data, and per-game pricing has become routine in the big leagues while ~120 affiliated clubs and the independent, ECHL, AHL and USL clubs have no analyst to run it. SeatGeek, which sells ticketing to clubs, was hiring a Director of Engineering, Enterprise Product (New York or remote US, posted 2026-09-11), a Senior Machine Learning Engineer (first published 2025-09-12) and a Senior Data Analyst, Supply (2026-10-16); its enterprise roles serve concert venues and promoters as well as sports clubs. KORE (Two Circles) showed no US engineering opening, and StellarAlgo could not be checked (bot wall).
**Market:** ~120 affiliated MiLB clubs, of which Diamond Baseball Holdings owns ~42–49 (search summary), plus a few hundred independent-league, hockey and lower-division soccer clubs. Sold at a few hundred dollars a month, or through the ticketing platform as an add-on; ticketers are both the channel and the competitor.

---

## 3. Sponsorship Proof Agent
#ai-agent #object-detection #large-language-models #causal-inference #workflow-orchestration #revenue-impact

**Concept:** An agent that reads each partner contract into a schedule of entitlements, checks every home date's board logs, PA scripts, social posts and measured exposure against it, flags shortfalls while there is still time for a makegood, and drafts the recap. Where a partner shares outcome data, it runs a lift analysis to put in front of the partner's finance team at renewal.
**Inputs:** Partner contracts, video-board and LED logs, PA scripts, social posts, exposure measurement from vendors, licensed broadcast clips, partner outcome data under agreement.
**Outputs / Actions:** Entitlement ledgers per partner; missed-deliverable alerts; makegood proposals; season recap decks with delivery against contract; lift reports with intervals.
**Why now:** LLMs can extract obligations from contract language reliably enough to audit, logo detection is cheap per frame, and partners' finance teams are demanding proof: in Bain's 2026 survey only 41% of marketers felt equipped to tie spend to outcomes. Genius Sports, whose fan-engagement and media arm sells to teams and sponsors, was hiring a Staff Software Engineer, Fan Engagement (New York, posted 2026-07-22) and a VP Sales, Media & Sponsorship (2026-07-24). About 70% of its FY2025 revenue ($471.5M of $669.5M) came from betting, so only the fan-engagement work counts here.
**Market:** Partnership departments at ~150 big-league clubs, ~130 FBS athletic departments and their multimedia-rights partners, plus brands' sponsorship teams. Competes with KORE (Two Circles), SponsorUnited, Relo Metrics and Nielsen Sports; differentiates on contract-line delivery and partner-side outcomes.

---

## 4. Revenue-Share Cap and NIL Clearance Assistant
#ai-agent #large-language-models #gradient-boosting #compliance #workflow-orchestration #data-integration

**Concept:** An assistant for a college athletic department's general manager and compliance office that tracks every revenue-share payment against the cap, prepares third-party NIL deals for NIL Go with comparable-deal evidence of fair market value, and models the roster's retention risk before the transfer portal opens.
**Inputs:** Revenue-share contracts and payment schedules, third-party NIL deal terms, NIL Go submissions and outcomes, roster and depth charts, athletes' playing time and portal history.
**Outputs / Actions:** A live cap ledger; deal packages ready to submit with comparables; flags on deals likely to be disputed; a retention-risk view of returning starters with the cap room available to address it.
**Why now:** The House settlement (agreement dated 2025-06-06) let schools pay athletes from July 2025 up to ~$20M a school in the first year, and the College Sports Commission's 29 staff cleared more than $227M of deals in July and August 2026 alone. Departments are building the function now.
**Market:** ~360 Division I departments, with the Power Four and other revenue-sharing schools paying first. Teamworks (Compliance, GM, Influencer and Wallet products), multimedia-rights holders such as Learfield and smaller advisory firms compete; athlete records are education records, so FERPA and the CSC's confidentiality rules shape the build.
