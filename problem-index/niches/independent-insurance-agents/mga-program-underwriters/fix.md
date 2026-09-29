# Appetite Is a One-Page Guide and a Senior Underwriter's Memory

**Niche:** [[niches/independent-insurance-agents/mga-program-underwriters/profile|MGAs & Program Underwriters]]
**Industry:** [[industries/independent-insurance-agents|Independent Insurance Agents]]
**Type:** Fix (Pain Point)
**One-liner:** What the programme will actually write bears only a family resemblance to the appetite guide, and the difference is in the underwriters.
**Tags:** #tacit-knowledge-ml #text-classification #large-language-models #worker-facing #data-integration

## The Problem
Every MGA publishes an appetite guide: classes written, states, limits, a list of ineligible risks. Retail agents use it to decide what to send, and Pass 1 describes producers spending 30-60 minutes an account working against fifteen to thirty of these.

What the programme actually writes is different, and every experienced underwriter knows how. That this class is technically in appetite but nothing gets written above a certain size. That a particular combination of construction and protection class is a decline regardless of what the guide says. That a risk from this producer gets more benefit of the doubt because their submissions have been accurate for years. That this state's account is workable only with a specific endorsement.

That knowledge is the difference between the published appetite and the real one. It is not written down, so retail agents send risks that will never be written, underwriters spend their scarcest hours declining them, and business that would have been welcome never gets submitted because the guide did not make clear it was wanted.

## Why It's Still Broken
The guide is a marketing document. It is written to attract submission flow, so it is broad and optimistic by design, and being precise about what the programme will not write reads as narrowing the funnel. That logic is exactly backwards at the margin — a wide guide buys volume of the wrong kind — but it is the prevailing view.

Underwriting authority documents cover limits, classes, and referral triggers. They are legal instruments about what an underwriter may bind, not descriptions of what the programme judges to be a good risk, and the gap between those two is where all the judgment lives.

And the knowledge is genuinely valuable to its holders. An underwriter who knows the real appetite is hard to replace, and nothing in the structure rewards making that portable.

## What a Fix Looks Like
Derive the real appetite from behaviour and let underwriters correct it.

**Mine decisions for the implicit rules.** With submissions and outcomes structured, the actual pattern of what gets quoted and bound is computable — by class, size, geography, construction, loss history, and producer. That is the real appetite, stated as evidence rather than as intention.

**Show underwriters the gap.** Where behaviour diverges from the published guide, someone should decide which is wrong. Sometimes the guide should narrow; sometimes the underwriters have drifted into declining business the programme wants. Neither conversation happens today because nobody can see the divergence.

**Capture the reasons as structured rules.** When an underwriter declines something nominally in appetite, a coded reason and a short note takes seconds and turns a private judgment into an institutional one. Over a year this is the real appetite, written down by the people who hold it.

**Publish a sharper guide to producers.** A retail agent who knows precisely what will be written sends better submissions, and better submission flow is worth more than broader submission flow. The reason to keep the guide vague evaporates once you can quantify what the vagueness costs in wasted underwriter hours.

**Flag drift.** Appetite should change deliberately, in response to market conditions or loss experience. When it changes because underwriters have quietly become more cautious, management should know.

## Who Feels the Pain
Underwriters, declining the same unsuitable risks repeatedly. New underwriters, who take a year to learn what the guide does not say. Retail agents, guessing at fifteen to thirty appetites. And the MGA, losing good business it never learned it could have had.

## Impact If Fixed
Submission quality is the lever on everything in delegated underwriting — underwriter capacity, speed to quote, and ultimately selection. Making the real appetite explicit improves the flow at the source and converts the knowledge that currently defines a senior underwriter's value into something the programme owns and can teach.
