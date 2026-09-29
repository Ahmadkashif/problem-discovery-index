# The Seed List the Provider Can Recognise

**Niche:** [[niches/email-sms-marketing-platforms/email-inbox-placement/profile|Email Inbox Placement]]
**Industry:** [[industries/email-sms-marketing-platforms|Email & SMS Marketing Platforms]]
**Type:** Fix (Pain Point)
**One-liner:** Placement is measured by sending to a panel of addresses that never open anything and belong to a known monitoring service, and the providers can tell.
**Tags:** #hypothesis-testing #evaluation-metrics #confidence-intervals #descriptive-statistics #quick-win #compliance #bayesian-inference #change-point-detection
**Contested on:** Every serious competitor in this niche is fighting to infer where a message landed inside a mailbox provider that will not say — and whoever does it accurately from a cross-brand corpus owns the number the whole channel should be managed on.

## The Problem
Seed list monitoring works by including a panel of test addresses in a send and checking where the message landed for each. Those addresses receive mail from many senders, engage with none of it, and are frequently identifiable as belonging to a monitoring service. A provider that filters on engagement will treat them differently from a real subscriber, which means the panel's placement may be systematically worse or better than the real audience's, in a direction that varies by provider. The number is then reported as the brand's inbox rate, and decisions about sending practice are made on it.

## Why It's Still Broken
The seed panel is the only direct measurement available, and a direct measurement of the wrong population feels better than an estimate of the right one — that preference is the whole mechanism. The bias is known to practitioners and not quantified. Vendors selling panels have no reason to publish their limitations. And the alternative requires the inference approach the category has not built.

## What a Fix Looks Like
Treat the panel as one biased instrument among several. Quantify the panel's bias by comparing its placement against inferred placement for the real audience, which is the fix and is the first thing anyone should do with both numbers — most practitioners have never seen them side by side. Make panel addresses behave like real subscribers, with varied engagement, which is more expensive and substantially reduces detectability. Report the panel result with its limitations stated rather than as the inbox rate. Weight panel evidence by provider, since the bias differs and some providers' results are far more trustworthy than others. Use the panel for detecting content and authentication problems, where it is genuinely informative, rather than for estimating audience placement, where it is not — the instrument is useful for a narrower purpose than it is sold for. Combine panel and inference into one estimate rather than choosing, since they fail differently and the combination is better than either. Rotate and refresh panel addresses so recognisable ones do not persist. Test the panel against known outcomes where a provider gives feedback, which is the only direct calibration available. Report the divergence between panel and inferred placement as a diagnostic in itself, since a large gap is informative about provider behaviour. And stop presenting a panel number as the brand's inbox rate, because that single presentational habit is what sustains the error.

## Who Feels the Pain
Brands making sending decisions on a measurement of the wrong population; deliverability specialists defending numbers they know are biased; and platforms whose placement reporting rests on a detectable instrument.

## Impact If Fixed
A direct measurement of the wrong population feels more credible than an estimate of the right one, which is why the panel persists. Comparing panel placement against inferred placement quantifies the bias immediately and narrows the instrument to what it is actually good for.
