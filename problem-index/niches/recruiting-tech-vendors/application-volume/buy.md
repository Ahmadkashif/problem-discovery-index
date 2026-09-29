# Buy: Spam and Abuse Tooling Adapted to Applications That Are All Real

**Niche:** [[niches/recruiting-tech-vendors/application-volume/profile|Application Volume & Generative Noise]]
**Industry:** [[industries/recruiting-tech-vendors|Recruiting Tech Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Spam and abuse infrastructure separates legitimate traffic from illegitimate; here almost every application is from a real person who genuinely wants the job.
**Tags:** #gradient-boosting #graph-theory #evaluation-metrics #confidence-intervals #large-language-models #compliance #automation #descriptive-statistics
**Contested on:** Whether abuse tooling designed to find bad actors helps when there are almost none.

## The Problem

Spam, bot and abuse detection is a mature field. Rate limiting, reputation scoring, behavioural analysis, device fingerprinting, content classification and network analysis are all available and effective at separating legitimate from illegitimate traffic.

Applied to application volume the premise fails. The applications are overwhelmingly from real people who really want a job and really submitted them. A small fraction are genuinely fraudulent — identity misrepresentation, credential fabrication, coordinated schemes — and the rest are simply numerous. Treating volume as abuse, which is what importing this tooling does, ends with real applicants blocked.

## What Already Exists

Bot detection and rate limiting. Device and network fingerprinting. Content classification and duplicate detection. Reputation and risk scoring platforms. Graph analysis for coordinated behaviour. Generative text detectors, newly arrived and of questionable accuracy. Identity verification services.

## The Customization Gap

**Volume is not abuse and the tooling assumes it is.** The base rate of illegitimate applications is very low, so a detector tuned for abuse produces overwhelmingly false positives among a population of real job seekers with real consequences.

**Generated text is not fraud.** A candidate using generative tooling to write a better application is doing what every careers service recommends in a new form. Treating it as illegitimate conflates assistance with deception, and the detectors that would enforce that distinction cannot make it and misfire on non-native speakers.

**The genuine abuse is narrow and specific.** Identity misrepresentation, fabricated credentials, coordinated application schemes, and interview proxying. These are real, they are small, and they are addressed by verification of specific claims rather than by traffic-level detection.

**Rate limiting hits the wrong population.** A candidate applying to forty roles at one large employer is conducting a serious job search, not attacking. Limits imposed as an abuse control filter for desperation, which is a characteristic of the applicants an employer should most want to treat well.

**The measurement is inverted.** Abuse systems measure what they blocked. The number that matters here is what was wrongly blocked — real applicants excluded by a volume control — which is an absence and is measured nowhere.

## Target Customer

ATS vendors reaching for abuse tooling to manage volume, who need the premise examined before they deploy it. Also the verification vendors, for whom specific claim verification is the durable answer, and employers whose volume controls are quietly excluding real candidates.

## Impact If Solved

The rate limiting, fingerprinting and graph analysis get used against the narrow band of genuine fraud, and the volume-is-not-abuse framing, assistance-versus-deception distinction, claim verification, rate-limit reconsideration and false-exclusion measurement get built. Concretely: controls aimed at the small real abuse rather than at the large real applicant population.
