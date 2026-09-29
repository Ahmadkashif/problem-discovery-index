# Creative Decisioning and Dynamic Assembly

**Industry:** [[programmatic-ad-platforms|Programmatic Ad Platforms]]
**Type:** Low Impact (Customisation Opportunity)
**One-liner:** Dynamic creative optimisation has existed for a decade and still mostly swaps a product image and a headline, because the systems that assemble the ad know nothing about why a creative works.
**Tags:** #cnns #transformers #bert #contrastive-learning #gradient-boosting #evaluation-metrics #feature-engineering #revenue-impact

## The Problem
Creative is consistently measured as the largest single driver of advertising effectiveness and is the part of the programmatic stack with the least intelligence applied to it. A campaign ships with a handful of creative variants; the platform rotates them, measures click-through, and settles on a winner within days on a metric nobody believes. Dynamic creative optimisation assembles ads at request time from a feed — product, price, headline, background — which works well for retail catalogue advertising and poorly for anything else, because the assembly rules are written by hand and the optimisation learns per-campaign from scratch.

Nothing in the loop understands the creative as content. The system knows variant B outperformed variant A; it does not know that B had a face, a price in the first line, and higher contrast, and it therefore cannot carry anything it learned into the next campaign, the next advertiser, or the next format.

## What Already Exists
The DCO category is mature: Google Studio, Flashtalking, Celtra, Innovid and Smartly all assemble creative dynamically and are widely deployed. Meta's Advantage+ and Google's Performance Max have moved further, generating and selecting creative automatically inside walled gardens, with an explicit trade of control for performance. Generative tooling now produces variants cheaply — Adobe Firefly, Meta's ad generation, a dozen startups — and creative analytics vendors like VidMob and Vidsy score assets against tagged attributes. Brand safety and suitability tooling reads page content but not creative content.

## The Customisation Gap
The walled gardens' versions work because they see billions of impressions of one advertiser's creative against one identity graph and one objective. The open-web version cannot copy that, and shouldn't: an independent platform's advantage is breadth across advertisers and formats, which is precisely what a per-campaign rotation model throws away.

What is missing is a representation of creative that transfers. Encode assets by their content — composition, faces, colour, motion, copy structure, the position and phrasing of the offer, brand prominence — and performance becomes a function of attributes rather than of variant IDs. That model can then say something on day one of a new campaign, which is when it matters, instead of after a fortnight of burn. It can also say it per context: the same creative attribute that lifts response on CTV sinks it in a mobile banner, and the interaction between creative and placement is where nearly all the remaining upside sits.

The customisation that each advertiser needs on top is brand constraint. Generated or assembled creative has to respect a brand system — allowed marks, colour, tone, legal copy, claim substantiation — and that rulebook is different for every advertiser, lives in a PDF, and is currently enforced by a human reviewer who sees the output after it has run.

## Impact If Solved
Creative attribute models turn every campaign into training data for the next one, which is the compounding asset an independent platform can build and a per-campaign rotation cannot. For advertisers it shortens the learning period that currently consumes a meaningful share of every flight's budget, and it gives creative teams the one thing they have never had from programmatic: a reason, rather than a winner.
