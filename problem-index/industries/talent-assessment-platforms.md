# Talent Assessment Platforms

## Profile
**Category:** Platform Labour & Digital Work
**Market Size:** ~$4B US in pre-employment assessment, spanning cognitive and personality instruments, structured interviews, technical skills testing and video interview platforms
**Tech Maturity:** Mature psychometrics in part of the market and very little of it in the rest. SHL, Criteria and the established test publishers carry genuine validation traditions; the newer entrants selling game-based, video-based and machine-learned assessments frequently assert validity from vendor-run studies that would not survive independent scrutiny, and almost nobody establishes criterion validity at the client where the instrument is actually used.
**Workforce:** Industrial-organisational psychologists, assessment content developers, data scientists, implementation consultants, and the recruiters and hiring managers who interpret the scores

## Key Pain Themes
The instrument's validity is asserted and rarely established where it matters. A vendor demonstrates that a test correlates with job performance in a validation study on some population; a client deploys it for a specific role in a specific organisation and almost never checks whether the score predicts anything about their own hires. Criterion validation at the client requires performance data, sample size and patience, and the procurement cycle supplies none of them.

Adverse impact is the second and most consequential theme. Assessments that produce different pass rates across demographic groups create legal exposure under US employment law and, more importantly, exclude people. New York City's Local Law 144 requires annual independent bias audits of automated employment decision tools with published results — the first regime of its kind — and the broader regulatory direction is toward more of this. The industry's response has been uneven, and some vendors have withdrawn features under scrutiny, as HireVue did when it removed facial analysis from its assessments in 2021.

The third theme is the candidate's position. A person is scored by an instrument they cannot see, on criteria they are not told, with no feedback and no appeal, in a process that determines whether they are considered for work. Completion rates suffer accordingly, and the candidates who abandon are not a random sample.

## Current Tech Landscape
Established publishers — SHL, Criteria, Hogan, Talogy — supply cognitive, personality and situational judgement instruments with documented validation. Technical assessment runs on HackerRank, Codility and CodeSignal. Video interview platforms including HireVue provide structured interviewing with varying degrees of automated scoring. Game-based assessment from Harver and others offers alternative formats. Bias audit services have emerged specifically in response to Local Law 144. Applicant tracking systems consume the scores and are where the actual decisions get made.

## Problems
- [[problems/talent-assessment-platforms/high-impact|🔴 High Impact: The Instrument's Validity Is Asserted by the Vendor and Established Nowhere]]
- [[problems/talent-assessment-platforms/low-impact-1|🟡 Low Impact: Adverse Impact Measurement and Audit]]
- [[problems/talent-assessment-platforms/low-impact-2|🟡 Low Impact: Assessment Content Development and Item Security]]
- [[problems/talent-assessment-platforms/worker-life-1|🟢 Worker Life: The Candidate Scored by Something They Cannot See]]
- [[problems/talent-assessment-platforms/worker-life-2|🟢 Worker Life: The Psychologist Whose Validity Concerns Lose to the Deal]]
- [[problems/talent-assessment-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/talent-assessment-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
This industry sells prediction of job performance and almost never measures whether its predictions came true at the place they were used. The data required — assessment scores joined to subsequent performance, tenure and progression for the people who were hired — exists inside the client's own systems, and the join is rarely made, partly because performance ratings are themselves noisy and biased, and partly because a negative finding would invalidate a purchased instrument. Meanwhile the regulatory environment has begun requiring bias auditing, which is a partial and welcome accountability mechanism that measures fairness without measuring validity. An instrument can be perfectly balanced across groups and predict nothing at all, and the industry currently has more pressure to demonstrate the first than the second.
