# Lineage: Conversion Optimization Firms

**Industry:** [[industries/conversion-optimization-firms|Conversion Optimization Firms]]
**Wave:** [[series/eras/wave-05-commercial-web|5 — The Commercial Web]]
**The tool:** the Optimizely JavaScript snippet and visual editor — one script tag that lets a non-engineer rewrite a live page in the visitor's browser and split traffic between versions
**Builder:** Optimizely
**Builder in vault:** **ABSENT**
**Verification:** partial — see Sources

## The Problem That Came First

Running a test cost an engineer.

By the mid-2000s the statistics of a split test were not the hard part. The hard part was the plumbing: building each variant as real page code, randomising visitors, logging which version each saw, and joining that to the outcome. Google Website Optimizer existed and was free, but a test still meant tagging pages and building variants through whoever controlled the site's code.

So tests were rationed by developer time. The person with the hypothesis — a marketer, a campaign director — could not run it without joining an engineering queue, and most hypotheses died there.

## What Got Built

A single line of JavaScript pasted into the page's header, plus a point-and-click editor.

Optimizely launched in private beta in **July 2010**. The editor loaded the customer's own website, highlighted elements as the mouse moved over them, and let the user change position, size, image, text or script from a menu. The snippet then applied those changes in each visitor's browser at load time, assigned the visitor to a variation, and reported which one converted better.

The decisive design choice is where the variant lives. It is not in the site's code. It is a set of instructions replayed on top of the page after the page arrives. That is what removed the engineer — and it is also what made every variant fragile.

## Who Built It, And Why Them

**Dan Siroker** and **Pete Koomen**, both formerly of Google, founded Optimizely in 2010 and went through Y Combinator's winter 2010 batch. Koomen had been a product manager on Google App Engine.

Siroker's reason is on record. As director of analytics for the Obama campaign, in **December 2007** he ran a multivariate test of the splash page on Google Website Optimizer: four buttons against six images and videos. The "Learn More" button with a family photograph lifted sign-ups from 8.26% to 11.6%, a 40.6% improvement. In Optimizely's own later write-up he says the campaign "were only able to run a small fraction of the experiments we wanted to run… because of the time and hassle needed," and that Optimizely existed to make such experiments "easier to do."

**Why them rather than Google:** Google already gave the testing tool away, so the constraint Siroker had lived through was not price or statistics. It was that the marketer depended on engineering to build every variant. Someone who had been the marketer in that queue built the product around deleting it. Visual Website Optimizer, covered by TechCrunch in September 2010, took the same approach within weeks, so the idea was not unique; what Optimizely had was a founder who had personally paid the cost it removed.

## What It Cost

**Two things, both still billed to this industry.**

First, the variant is a patch on someone else's page. When the client's developers change the underlying markup, the selectors the editor recorded stop matching and the test silently breaks or flickers. The engineer was removed from building the test, not from maintaining it.

Second, making a test cheap made *reading* one cheap too, and dashboards invited people to watch results in real time and stop at the first significant-looking number. Optimizely itself later replaced fixed-horizon significance with sequential "always valid" inference — the Stats Engine, published by Johari, Pekelis and Walsh in 2015 — precisely because customers peeked. The founding anecdote carries the same flaw in miniature: the "$60 million" figure is an extrapolation, multiplying extra sign-ups by an assumed average donation, not a measured result.

## What You Still Touch

Every agency deck showing a stack of test "wins" is the snippet's output — cheap tests, cheaply read, summed without a holdout.

- [[problems/conversion-optimization-firms/high-impact|🔴 The Reported Wins Do Not Add Up and Nobody Checks]] — extrapolated uplift, summed
- [[problems/conversion-optimization-firms/worker-life-2|🟢 The Developer Building Variants Against a Site That Moves]] — the patch-on-a-page cost
- [[problems/conversion-optimization-firms/worker-life-1|🟢 The Strategist Reporting a Win They Privately Doubt]]
- [[niches/conversion-optimization-firms/variant-implementation/profile|Variant Implementation Quality]]
- [[niches/conversion-optimization-firms/holdback-validation/profile|Cumulative Holdback Validation]]
- [[niches/conversion-optimization-firms/statistical-practice/profile|Experiment Design & Statistical Practice]]

**Sources:** Optimizely blog, "How Obama raised $60 million by running a simple experiment", Dan Siroker, 29 November 2010 (now at optimizely.com/insights; tool used, December 2007, 8.26%/11.6%/40.6%, the $21-per-address extrapolation, "time and hassle" quote — the builder's own account, not independent); Wikipedia, *Optimizely* (2010 founding, both ex-Google, Y Combinator winter 2010, November 2010 $1.2M angel round, 2020 Episerver acquisition); TechCrunch, "YC-Funded Optimizely Makes It Remarkably Easy To Run A/B Tests On Your Website", 15 July 2010 (private beta, snippet, visual editor behaviour); TechCrunch, 2 September 2010, on Visual Website Optimizer; Johari, Pekelis & Walsh, "Always Valid Inference: Bringing Sequential Analysis to A/B Testing", arXiv 1512.04922 (2015), which states it is deployed by Optimizely. ⚠️ **Not established:** the launch date of Google Website Optimizer (secondary accounts give 2006 beta / 2007 general release; not checked against a Google primary source, so no year is asserted above). A widely repeated claim that Stats Engine cut Optimizely's false-positive rate from over 20% to under 5% was found only on a blog and is omitted.
