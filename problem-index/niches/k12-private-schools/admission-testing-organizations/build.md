# A Score Used to Predict Success Against Outcomes Nobody Collects

**Niche:** [[niches/k12-private-schools/admission-testing-organizations/profile|Admission Testing Organizations]]
**Industry:** [[industries/k12-private-schools|K-12 Private Schools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Schools admit on the score because it is supposed to predict performance, and the organization has never seen how any admitted student did.
**Tags:** #logistic-regression #tabular-ml #causal-inference #evaluation-metrics #hypothesis-testing

## The Problem
An admission test exists to help a school compare applicants from hundreds of sending schools with incomparable grading. Pass 1 says admissions directors otherwise run on gut feel and committee, so the score carries real weight in a decision that shapes a child's education.

The organization measures the test carefully — reliability, item functioning, scale stability, differential item functioning across groups. All of that is about internal quality.

What it does not have is the outcome. Whether students who scored in a given band went on to succeed at the schools that admitted them, whether the score predicts anything above the application file's other contents, and whether it predicts equally well for students from different sending school types are the questions that justify the test's existence, and they are answered by validity studies that are occasional, small, and voluntary.

Member schools hold the outcomes. They have grades, retention, and progression for every student they admitted, and they submitted the test scores in the first place. Nobody has built the mechanism to bring the two together at scale.

## Why Nobody Has Built This
Testing organizations are psychometric institutions, and psychometrics is largely about the instrument. Reliability and item quality are what the profession measures and what the standards require, and predictive validity against real-world outcomes is treated as a periodic research study rather than as continuous measurement.

Collecting outcomes is also a school relationship problem, not a technical one. It requires schools to return performance data on their own students, which touches privacy, effort, and the discomfort of finding out that the score does not predict much. Nobody has made the case strongly enough to overcome that.

And there is no pressure. The test is well established, schools use it because they always have, and nobody is asking for evidence.

## What to Build
A continuous predictive validity programme, run as infrastructure rather than as a study.

**A standing outcome exchange with member schools.** Grades, retention, and progression returned annually under a clear agreement, in exchange for school-specific reports that tell each school how the test performs for its own population. That exchange is the product that makes participation worth a school's effort.

**Report incremental validity, not correlation.** The question is not whether scores correlate with grades but whether they add anything beyond what the school already knows from the transcript and the interview. That is the only number that justifies the test's place in the process, and it has never been reported.

**Segment by sending school type.** A test's whole purpose is comparability across incomparable sending schools. Whether it achieves that — whether it predicts as well for a student from a small parish school as from a well-resourced feeder — is the fairness question that matters most and is answerable with outcome data.

**Give schools their own validity picture.** Each school's admitted cohort, its score distribution, and how scores related to outcomes there. This turns a national instrument into a locally evidenced one and is what makes the exchange sustainable.

## Target Customer
Chief Research Officer or VP of Assessment at an admission testing organization. The strategic pressure is real: test-optional policies have spread through education, and an instrument that cannot demonstrate incremental predictive value is exactly the kind that gets dropped.

## Impact If Built
Admission decisions for hundreds of thousands of children rest partly on this score, and its predictive contribution is asserted from occasional studies. Measuring it continuously either justifies the test's role or identifies where it should carry less weight — and either answer is worth more to schools than the current silence.
