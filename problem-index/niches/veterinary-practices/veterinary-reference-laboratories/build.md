# The Only Large Clinical Dataset With No Privacy Wall Around It

**Niche:** [[niches/veterinary-practices/veterinary-reference-laboratories/profile|Veterinary Diagnostic Reference Laboratories]]
**Industry:** [[industries/veterinary-practices|Veterinary Practices]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Hundreds of millions of longitudinal clinical results across a national patient population, with no privacy regime over any of it, used to print reference ranges.
**Tags:** #gradient-boosting #survival-analysis #causal-inference #evaluation-metrics #time-series-forecasting

## The Problem
This index has spent a hundred and twelve industries watching valuable clinical data sit behind a wall. In healthcare after healthcare — home health, medical billing, physical therapy, pharmacy, urgent care — the analytical mass is real and fenced, and the only businesses that escape are the ones selling knowledge about medicine rather than data about patients.

Veterinary diagnostics is the exception. The laboratories hold results for a large share of the US companion animal population: chemistry panels, haematology, urinalysis, endocrine testing, infectious disease screening, repeated over years for animals that come back. Patient identity, breed, age, sex, geography and the practice are all attached. And there is no HIPAA for animals, no consent regime over the records, no clearinghouse in between, and no de-identification requirement to work around.

What is built on it is a reference interval and a flag. A result arrives, it is compared to a population range, and it is marked high, low or normal. Some genuinely predictive products exist — early kidney disease indicators are the well-known example — and they are the exception that shows what the corpus supports.

The gap is that almost nothing is longitudinal or predictive. An animal with five years of panels is evaluated one panel at a time against a static population range, when the informative signal is the trajectory: a value drifting within the normal range toward its own patient-specific threshold is the earliest detectable disease signal there is, and it is invisible to a flag. Nothing predicts which animals will develop chronic kidney disease, diabetes, hyperthyroidism or neoplasia from the panels already in the file. Nothing estimates a breed-and-age-specific risk from a national cohort that contains every breed in numbers no research study could recruit.

## Why Nobody Has Built This
The business grew as a laboratory business. Its competitive axes are turnaround time, test menu, analyser placement and price, and its research investment goes into new assays — a new biomarker is a new billable test, while a model over existing results is not obviously one.

Interpretation has also been treated as the veterinarian's job, correctly and conservatively. A laboratory that starts predicting disease is making a clinical claim, and the field has no equivalent of the regulatory pathway that would frame it.

And the data lives in laboratory information systems built for result delivery, not for cohort assembly. Longitudinal patient linkage across practices, analysers and years is a real engineering project that no revenue line asked for.

## What to Build
Prediction over the longitudinal corpus, which is what the corpus is for.

**Model trajectories, not values.** Within-patient change against the patient's own history is far more informative than a static population interval, and every animal with repeat testing supplies it. This alone changes what the product can say.

**Predict incident disease from prior panels.** Chronic kidney disease, diabetes, hyperthyroidism, hepatopathy and neoplasia all have detectable prodromes in routine chemistry. The labels exist in later results and diagnoses; the features exist in earlier ones; the cohort is national.

**Build breed-specific risk from the population.** No academic study can recruit thousands of animals of a single breed. This corpus contains them, for every breed, with age and sex, and breed-conditional risk is one of the most clinically actionable things veterinary medicine lacks.

**Treat time to event properly.** Animals are lost to follow-up constantly — they move, change practice, or die. That is right-censored survival data and modelling it as such is what makes the estimates honest.

**Publish validation.** Prospective performance of any predictive indicator, reported. Veterinary medicine has almost no tradition of this, and a laboratory that establishes one defines the standard for the products that follow.

## Target Customer
Chief Medical Officer or VP of Research and Development at a veterinary diagnostics company. The strategic argument is that the test menu is increasingly matched across competitors, analyser placement is a capital race, and interpretation built on a longitudinal national cohort is the one asset a competitor cannot buy.

## Impact If Built
Companion animal medicine has no equivalent of population health research, because the funding and the cohorts do not exist — except here, in a commercial laboratory, unencumbered. Turning routine panel data into breed-specific, trajectory-aware disease prediction would materially change what a general practice veterinarian can detect early, and it is the clearest case in this entire index of a dataset whose value is limited only by whether anyone decides to use it.
