# Eliciting the Worst Outputs as a Job

**Niche:** [[niches/ai-red-teaming-firms/the-red-team-researcher/profile|The Red Team Researcher]]
**Industry:** [[industries/ai-red-teaming-firms|AI Red Teaming Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Red team researchers spend their working days deliberately eliciting the worst outputs a model can produce, and the industry has largely not addressed what that does to people.
**Tags:** #worker-facing #descriptive-statistics #evaluation-metrics #automation #compliance #confidence-intervals #survival-analysis #hypothesis-testing
**Contested on:** Every serious competitor in this niche is fighting to keep skilled researchers able to do this work for years rather than months — and whoever does that holds the scarce input the entire industry runs on.

## The Problem
A researcher spends six weeks on an engagement covering a harm category involving depictions of violence against children. Their job is to find the sequences that produce the worst output, read each result to judge whether it crossed a line, and iterate toward worse ones. They do this for eight hours a day. The firm treats it as security research, the researcher identifies as a security researcher, and neither frames it as sustained exposure to harmful material — which it is, in a more concentrated form than most moderation work, because the researcher is actively optimising toward the worst case rather than encountering it in a queue.

## Why Nobody Has Built This
The work is framed as adversarial research rather than as content exposure, which places it outside the practice built for moderation. The researchers are senior, autonomous and self-selecting, and are not inclined to describe the work as harmful to them. The industry is young and small, and the reckoning that came to content moderation arrived through litigation and journalism that this sector has not yet attracted. And the cost appears as attrition attributed to career moves.

## What to Build
Treat exposure as a measurable occupational factor. Measure exposure — hours per harm category per researcher per period — which is the precondition for managing it and which no firm currently records. Set limits and rotate researchers across categories, so no individual spends months in the hardest material, which is the practice the moderation industry arrived at and is straightforwardly adoptable. Automate the most repetitive exposure, using automated classification to filter results so a researcher reviews the outputs that need judgement rather than every result — this is where the most exposure is removed for the least loss of research quality, and it is the fix note's subject. Provide blurring, previewing and staged reveal in the tooling, so a researcher chooses when to look rather than being shown. Offer specialist support appropriate to the material rather than generic employee assistance, since the moderation experience is that generic provision is not used and specialist provision is. Build the effect into workload planning explicitly, including recovery time after heavy engagements. Measure retention and time-to-attrition, since the capability is the business and its loss is currently invisible. And make it an explicit part of how engagements are scoped and priced, because a client asking for six weeks in the hardest category is buying something with a human cost that should be stated rather than absorbed.

## Target Customer
The firms employing researchers and their leadership, the researchers themselves, and the clients whose assessments depend on this capability existing in five years.

## Impact If Built
The work is more concentrated exposure than moderation because the researcher is optimising toward the worst case, and it is not framed as exposure at all. Measuring hours per harm category is the precondition for managing it, and rotation is directly adoptable from an industry that learned it the hard way.
