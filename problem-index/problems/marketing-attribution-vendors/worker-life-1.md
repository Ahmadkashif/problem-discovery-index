# The Marketing Scientist Defending the Number

**Industry:** [[marketing-attribution-vendors|Marketing Attribution Vendors]]
**Type:** Worker Life Changing
**One-liner:** A trained statistician spends their quarter explaining to channel owners why the model reduced their contribution, knowing the estimate is less certain than the chart implies and being unable to say so.
**Tags:** #bayesian-inference #confidence-intervals #hypothesis-testing #large-language-models #evaluation-metrics #worker-facing #tacit-knowledge-ml #cross-validation

## The Problem
A marketing scientist at an attribution vendor builds and maintains models for a portfolio of clients. The technical work — data preparation, specification, fitting, diagnostics — is a minority of the job. The majority is the quarterly cycle of presenting results and defending them.

The defence is structurally awkward. A model that reduces a channel's contribution is challenged by the person who runs that channel, who will point to platform-reported numbers that say otherwise, and who is measured on those numbers. The scientist knows the model's estimate has wide uncertainty, that the specification choices could have produced a different answer, and that the correct response is often "the data cannot separate these two channels". Saying that plainly undermines the product and invites the client to conclude the engagement is not worth its fee. So the uncertainty gets compressed into a confident chart, and the scientist carries the gap privately.

Around it sits the recurring work: refits each quarter, re-explaining why results moved when the model was updated, handling data feed changes that break pipelines, and producing bespoke analyses for whichever stakeholder asks. Refits that change last quarter's answer are especially difficult, because the client reasonably asks which version was right.

## Why It Matters to the Worker
This is a professional asked to be more certain in public than they are in private, repeatedly, about work they take seriously. That is a specific and corrosive form of pressure, and it is the reason people leave this field for roles where they can qualify their findings.

The technical isolation compounds it. Marketing scientists are often the only statistically-trained person in the room, and the room contains people whose incentives favour particular answers. There is no peer review in the ordinary sense — no colleague checks the specification, no external standard says whether the model is good — so the scientist is simultaneously the author, the reviewer and the defendant.

And the work does not accumulate into knowledge. Every client is a fresh model, every quarter a refit, and the judgement built over dozens of engagements — which specifications behave, what priors are reasonable for this vertical, when a result should be distrusted — stays tacit and leaves with the person. Nobody is building the empirical base that would make the next model better.

## What a Solution Looks Like
Give the scientist evidence instead of authority. A validation record — how this model's predictions fared against subsequent experiments, for this client and for comparable ones — converts an argument about credibility into a conversation about evidence, which is a far better position for both the scientist and the client.

Report specification uncertainty as a feature. Fitting the ensemble of defensible specifications and showing the contribution range under all of them lets the scientist say "this channel is between these bounds under any reasonable model, and this other one is specification-dependent" with the product supporting rather than undermining them. That is the honest statement they currently cannot make.

Pool the portfolio into empirical priors. A vendor's accumulated experimental results by vertical and spend level should be the source of priors, which both improves estimates and means the scientist defends an evidence base rather than a personal judgement.

Automate the cycle. Refits, diagnostic runs, data feed validation and the first draft of the quarterly narrative are mechanical, and removing them returns the time to the specification and interpretation work that is the actual expertise.

## Impact If Solved
The bottleneck in this category is trained people who burn out on defending numbers they cannot fully stand behind. Giving them a validation record, honest uncertainty reporting and empirical priors changes the job from advocacy back to analysis — and turns the tacit judgement accumulated across a portfolio into an asset the firm keeps rather than one that walks out when a scientist has had enough.
