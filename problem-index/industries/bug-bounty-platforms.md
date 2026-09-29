# Bug Bounty Platforms

## Profile
**Category:** Trust, Safety & Security
**Market Size:** ~$1.5B US in bounty payouts, platform fees and managed triage services; HackerOne, Bugcrowd, Intigriti, YesWeHack and Synack operate the marketplace layer alongside a tier of self-run vendor programmes
**Tech Maturity:** Excellent marketplace mechanics, no measurement of the product. These platforms handle submission, triage workflow, researcher reputation, payments across jurisdictions and disclosure coordination at scale. Whether a programme's spend bought security — as opposed to paying for findings that internal testing, a scanner or a subsequent release would have surfaced anyway — is not measured by the platform, the programme or anyone else.
**Workforce:** Triage analysts, programme managers and customer success staff, platform and payments engineers, security researchers working as independent participants, disclosure and legal coordination staff

## Key Pain Themes
Triage volume is the operational reality. A public programme receives a large majority of submissions that are duplicates, out of scope, non-issues or automated scanner output, and each must be read by a person qualified to distinguish a real finding from a plausible-looking one. That cost falls on platform triage teams and on programme staff, and it is the reason many organisations run private programmes or none.

The second theme is that the researcher side is economically lottery-shaped. Payment depends on being first to a finding, on the programme's severity assessment, and on scope interpretations that are decided after the work. A researcher can spend a week on a genuine vulnerability and receive nothing because someone submitted it hours earlier, and duplicate and severity disputes are the most common source of grievance in the community.

The third is that nobody measures the programme's effect. Spend, submission counts and time-to-triage are reported; whether the vulnerabilities found were ones that would have been caught otherwise, whether the programme reduced incidents, and what marginal spend buys are not. The category sells assurance and reports activity.

## Current Tech Landscape
HackerOne and Bugcrowd dominate the managed marketplace and both offer triage as a service. Intigriti and YesWeHack are strong in Europe; Synack operates a vetted-researcher model closer to continuous testing. Large technology companies run their own programmes with in-house triage. Duplicate detection is largely keyword and manual. Severity uses standard scoring frameworks applied with judgement. Payments run through platform rails across many jurisdictions. Coordinated disclosure timelines are policy rather than product.

## Problems
- [[problems/bug-bounty-platforms/high-impact|🔴 High Impact: Nobody Measures Whether the Programme Bought Security]]
- [[problems/bug-bounty-platforms/low-impact-1|🟡 Low Impact: Triage Volume and Duplicate Detection]]
- [[problems/bug-bounty-platforms/low-impact-2|🟡 Low Impact: Scope Ambiguity and Severity Disputes]]
- [[problems/bug-bounty-platforms/worker-life-1|🟢 Worker Life: The Researcher Who Was Six Hours Late]]
- [[problems/bug-bounty-platforms/worker-life-2|🟢 Worker Life: The Triager Reading the Two Hundredth Report]]
- [[problems/bug-bounty-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/bug-bounty-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A bounty platform sits between a population of researchers and a population of programmes and holds the complete record of both: every submission, its quality, its outcome, its severity, its payment, and every researcher's history across every programme they have worked. That corpus answers the questions neither side can currently answer — what a programme's marginal bounty dollar buys, which researchers are strong in which technology areas, what a fair severity looks like given how comparable findings were rated elsewhere — and it is used to run a workflow. The measurement gap is the same one that runs through every assurance business in this cluster: an industry selling confidence, reporting activity, because the outcome data was never assembled.
