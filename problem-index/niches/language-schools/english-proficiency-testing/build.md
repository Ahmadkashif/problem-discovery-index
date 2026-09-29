# Millions of Rated Performances and No Model of What Predicts Success

**Niche:** [[niches/language-schools/english-proficiency-testing/profile|English Proficiency Testing Organizations]]
**Industry:** [[industries/language-schools|Language Schools]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Universities admit on the score because it predicts whether a student can cope, and the organization has never seen a transcript.
**Tags:** #logistic-regression #tabular-ml #causal-inference #evaluation-metrics #survival-analysis

## The Problem
An English proficiency score decides admission, professional registration, and in many cases a visa. Institutions set cut scores — 6.5 here, 90 there — and defend them as the level at which a student can succeed academically.

Those cut scores are largely conventional. They were set years ago from small validity studies, copied between institutions, and adjusted by admissions politics rather than by evidence. The organization that produces the score has extraordinary data about the test and almost none about what happened next: whether students admitted at a given band passed their first year, needed language support, or withdrew.

Meanwhile the corpus on the input side is unmatched — decades of item responses and, crucially, millions of rated speaking and writing performances from a globally distributed population, with candidate first language, country, and repeat-testing history attached. Nobody in applied linguistics has anything comparable, and it is used to score tests and to publish occasional research.

## Why Nobody Has Built This
The organization is a measurement institution, and the professional standard it is held to is about the instrument: reliability, comparability across forms, fairness across groups. Predictive validity against academic outcomes is treated as a periodic research question, usually pursued with one cooperating university at a time.

Collecting outcomes requires institutions to return student performance data, which is a privacy and effort question and, quietly, a political one — a university that discovers its cut score is too low has a problem it did not want.

And there is no commercial pressure. Institutions require the test because they always have, and no competitor is publishing better evidence.

## What to Build
Turn cut score setting into an evidenced service.

**Build a standing outcome partnership programme.** Institutions return first-year performance, language support usage, and progression for admitted cohorts, and receive in exchange an institution-specific analysis of how the score performed for their own students and programmes. That exchange is what makes participation worth the effort.

**Model outcome by score band, by programme, and by first language.** A score that predicts well for engineering may predict differently for a discussion-heavy humanities programme, and sub-skill profiles matter differently — a candidate strong in reading and weak in speaking is a different risk in a seminar than in a laboratory. The organization reports sub-scores and nobody has established what they predict.

**Report incremental validity.** Whether the score adds anything beyond prior education and academic qualifications is the question that justifies its place, and it is unanswered.

**Give institutions a cut score tool.** For this programme and this student population, here is the trade-off between admitting more students and accepting more academic risk, with intervals. That is a genuinely new product and the organization is the only party able to build it.

## Target Customer
Chief Research Officer or VP of Assessment at an English proficiency testing organization. The strategic pressure is direct: newer entrants compete on convenience and price, and evidence of predictive validity is the one axis where an incumbent's decades of data are decisive.

## Impact If Built
Cut scores decide admission for millions of international students a year and are set by convention. Evidencing them would let institutions admit students who would succeed and are currently excluded, and support students who are admitted and struggle — and it would give language schools, whose entire purpose is getting students to a number, a defensible account of what that number means.
