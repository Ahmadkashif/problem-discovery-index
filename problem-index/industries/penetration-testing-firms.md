# Penetration Testing Firms

## Profile
**Category:** Trust, Safety & Security
**Market Size:** ~$6B US in offensive security testing — penetration testing, red teaming, application assessment and adversary simulation — split between large consultancies, specialist boutiques and the services arms of security product vendors
**Tech Maturity:** Deep individual expertise, undeveloped as an industry. The best testers in this field are genuinely exceptional and the practice around them has barely changed in fifteen years: a time-boxed engagement, a manual assessment, a report of findings, and no mechanism for the firm to learn whether any of it was fixed.
**Workforce:** Penetration testers and red teamers, application security specialists, engagement managers and scopers, report writers and quality reviewers, sales engineers translating between clients and testers

## Key Pain Themes
A penetration test is a sample and is reported as an assessment. Two weeks against an estate that would take months to cover produces a list of what was found, and the document does not state what was not reached, how much of the attack surface was examined, or what confidence the absence of a finding carries. Clients read a clean report as evidence of security, testers know it is evidence of two weeks, and the gap between those readings is the industry's central honesty problem.

The second theme is that the outcome never returns. A firm delivers findings and leaves. Whether they were remediated, whether the fix worked, whether the same class recurred in the next release — all of it happens inside the client and is never joined back, so a firm that has run thousands of engagements cannot say which of its finding types actually get fixed or which remediation advice works.

The third is that compliance drives the volume. A large share of testing is procured to satisfy an audit requirement rather than to find problems, which shapes scope toward what is auditable and pushes price toward a commodity — and puts the firms who do the deepest work in competition with the ones producing the thinnest acceptable deliverable.

## Current Tech Landscape
Testing runs on a mixture of commercial and open tooling — Burp Suite, Metasploit, Cobalt Strike and a long tail of specialist tools — plus substantial manual work. Automated scanners cover the shallow end and are a poor substitute for the deep work. Penetration testing as a service platforms from Cobalt, Synack and HackerOne's structured offerings have industrialised scheduling, delivery and finding tracking. Report production is largely manual, assisted by templating. Attack surface management vendors have grown alongside and are rarely integrated with testing. Compliance frameworks specify testing frequency and scope, which drives much of the demand.

## Problems
- [[problems/penetration-testing-firms/high-impact|🔴 High Impact: A Time-Boxed Sample Reported as an Assessment]]
- [[problems/penetration-testing-firms/low-impact-1|🟡 Low Impact: Scoping Against an Unknown Attack Surface]]
- [[problems/penetration-testing-firms/low-impact-2|🟡 Low Impact: Report Production and Finding Triage]]
- [[problems/penetration-testing-firms/worker-life-1|🟢 Worker Life: The Tester With Three Reports Owed]]
- [[problems/penetration-testing-firms/worker-life-2|🟢 Worker Life: The Engineer Handed Eighty Findings]]
- [[problems/penetration-testing-firms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/penetration-testing-firms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
A testing firm accumulates, across thousands of engagements, the most complete record anyone holds of how real systems actually fail: which weaknesses appear in which technology stacks, which recur after remediation, which remediation advice works. It uses that record to staff engagements and writes each report as though it were the first. The two things the industry cannot currently do — state the coverage a test achieved and demonstrate that its findings get fixed — are both derivable from that corpus plus a remediation feedback loop that clients would grant if asked. Their absence is why a genuinely expert profession sells a document whose meaning the buyer misreads.
