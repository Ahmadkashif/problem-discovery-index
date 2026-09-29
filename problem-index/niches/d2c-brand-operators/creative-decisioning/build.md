# Cheap to Make and Unknown What to Make

**Niche:** [[niches/d2c-brand-operators/creative-decisioning/profile|Creative Decisioning]]
**Industry:** [[industries/d2c-brand-operators|D2C Brand Operators]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Design tools, stock libraries and generative image models have made producing an asset trivially cheap, and brands still cannot sustain the volume paid social consumes because the constraint is knowing what to make, not making it.
**Tags:** #cnns #evaluation-metrics #gradient-boosting #confidence-intervals #hypothesis-testing #causal-inference #feature-engineering #revenue-impact
**Contested on:** Every serious competitor in this niche is fighting to tell a brand what to make next rather than how to make it faster — and whoever does that takes the account, because production became cheap and the decision did not.

## The Problem
A brand needs forty new assets a month to keep paid social performing. They can produce forty. What they cannot do is decide what the forty should be. So they make variations of the best performer from last month, a few imitations of a competitor's campaign, and some ideas somebody liked. Roughly three work. Nobody can say why those three worked, because the test was at the whole-asset level and each asset differs from the others in a dozen ways at once. Next month the same process runs again, with the three winners as the new base, and the brand's creative gets narrower rather than better.

## Why Nobody Has Built This
Creative testing was inherited from the platforms, which report performance per asset because that is the unit they deliver. Decomposing assets into attributes requires tagging them, which nobody wanted to do by hand and which is only recently automatable from the asset itself. Creative teams resist reduction of their work to attributes, sometimes rightly. And the platform's delivery algorithm confounds the comparison, since it decides which asset gets shown to whom.

## What to Build
Decompose the creative and learn at the attribute level. Tag every asset automatically with its attributes — format, hook type, first-frame content, presence of a person, pace, text treatment, offer framing, product prominence, setting — which is now straightforward from the asset itself and is the precondition for learning anything transferable. Model performance at the attribute level, so a result says that first-frame product close-ups with a price hook outperform lifestyle openers for this audience, which is a brief, rather than that asset forty-seven did well, which is not. Correct for the platform's delivery, since the algorithm's allocation decisions confound naive comparison and a like-for-like test needs design rather than observation. Generate the next brief from the findings, listing the attributes to include and the untested combinations worth exploring, which is the product the creative team actually wants. Maintain a durable library of what has worked, with the attributes attached, so a brand's knowledge accumulates rather than resetting when the growth lead changes. Test deliberately rather than only observing, running structured variation so the attribute effects are identifiable. Predict fatigue per asset, which the fix note develops. And preserve room for the unexplained, since the biggest winners are frequently outside what the attribute model would have suggested and a system that only exploits will narrow the brand to nothing.

## Target Customer
Creative and growth teams, the agencies producing for them, and the brands whose creative output is expanding while its variety shrinks.

## Impact If Built
Production is cheap and the decision is not, and testing whole assets teaches nothing transferable. Automatic attribute tagging makes performance learnable at the level a brief is written at, and correcting for platform delivery is what makes the comparison mean anything.
