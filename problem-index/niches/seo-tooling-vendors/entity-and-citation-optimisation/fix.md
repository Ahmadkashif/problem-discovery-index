# The Brand the Model Has Wrong

**Niche:** [[niches/seo-tooling-vendors/entity-and-citation-optimisation/profile|Entity & Citation Optimisation]]
**Industry:** [[industries/seo-tooling-vendors|SEO Tooling Vendors]]
**Type:** Fix (Pain Point)
**One-liner:** Asked about the company, the generated answer states a product they discontinued, a founder who left and a controversy that was about a different firm with a similar name.
**Tags:** #large-language-models #graph-theory #evaluation-metrics #compliance #quick-win #confidence-intervals #word-embeddings #descriptive-statistics
**Contested on:** Every serious competitor in this niche is fighting to work out what makes a generated answer cite one source rather than another — and whoever establishes that gets to sell the practice that replaces a twenty-year-old one.

## The Problem
Customers increasingly ask a generative system about a company before dealing with it. For a large number of companies the answer is partly wrong: an old product line, a former executive, an outdated price, a merger that did not happen, or a confusion with a similarly named business. The company has no idea this is happening, no way to see what is being said, and no route to correction — the systems have no editorial process for this and the errors originate in a training corpus and a retrieval layer the brand cannot address. Meanwhile the answer is being given to their prospective customers thousands of times a day.

## Why It's Still Broken
There is no correction mechanism, which is the immediate cause, and no brand has treated the model's representation as a monitorable asset because until recently it was not one. Errors originate in stale or incorrect web sources the brand may not know exist. Legal and communications teams have no process for a channel with no publisher. And nobody is monitoring, so most companies do not know.

## What a Fix Looks Like
Monitor the description and correct the sources. Ask the systems about the brand regularly and record what they say, which is the fix's starting point, is trivial to implement, and is how a company discovers a problem it currently learns about from a customer. Classify errors by type and severity, since an outdated price and a false controversy require different responses and different urgency. Trace each error to its likely sources in the web corpus, which is the practical route to correction because the corpus is the only thing a brand can actually change. Correct at source — update the stale pages, correct third-party profiles, publish clear authoritative statements — which is slow and is the only mechanism that exists. Use every available feedback and correction channel the systems provide, even where the effect is uncertain, since the cost is low. Publish an authoritative machine-readable description of the entity, which gives the retrieval layer something correct to find. Distinguish confusion with a similar entity, which is a common and specific failure with a specific remedy in disambiguation. Track whether corrections propagate, since the loop from source change to answer change is long and nobody currently measures it. Prepare a response for the errors that cannot be corrected quickly, which is a communications problem more than a technical one. And report the accuracy of the brand's generated description as a standing metric, because it is now part of how the company is perceived and almost nobody is looking at it.

## Who Feels the Pain
Companies described inaccurately to prospective customers thousands of times a day; communications teams with no channel to a publisher that does not exist; and small businesses confused with larger similarly named ones.

## Impact If Fixed
There is no correction mechanism and no brand treated the model's description as a monitorable asset, so most learn about errors from a customer. Regular querying plus tracing errors to their source pages is the only available route and it starts with a check nobody is running.
