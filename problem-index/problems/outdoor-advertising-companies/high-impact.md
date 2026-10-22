# The Location Only the Real Estate Manager Can Price

**Industry:** [[outdoor-advertising-companies|Outdoor Advertising Companies]]
**Type:** High Impact
**One-liner:** The decisions that set an outdoor company's returns for a decade (which parcel to lease, which bulletin to convert to digital, how much rent to concede at renewal) rest on a senior real estate manager's drive-by read of a location, and the company's own billing history is never used to check or teach it.
**Tags:** #tacit-knowledge-ml #gradient-boosting #cnns #transfer-learning #feature-engineering #evaluation-metrics #revenue-impact

## The Problem
An outdoor company makes three kinds of location bet. It leases new sites where a permit is still obtainable. It converts static bulletins to digital at a little over $200,000 a face, plus structure work. And it renews tens of thousands of ground leases, each a negotiation with a landowner who may have a lump-sum buyout offer from a lease aggregator in hand. Lamar alone pays ~$348M a year in site rent across ~71,500 leased sites and added about 500 digital billboards in 2025. Its ~5,500 digital faces, about 3.5% of its ~159,300 billboards, produce about a third of billboard revenue, so choosing the next conversions is the largest capital decision a market manager makes.

The person who makes the call is usually a real estate manager or general manager who has worked the market for many years. They drive the approach at the speed traffic moves and judge how long the face is readable, whether it is a right-hand read, whether trees or a competitor's structure will block it in summer, whether a signal holds traffic in front of it, and which buyers want that corridor: personal injury lawyers on the interstate, casinos on the route to the reservation, quick-service restaurants at the exit. They also judge whether the permit will survive, from spacing rules, nonconforming status and the mood of the council. They say they "know a good board when they see one", and on a given corridor they are usually right.

That read is not recorded. The manager's expectation of what a face would earn is not written down when the lease or conversion is approved. So nobody can check it later against the face's actual occupancy and rate, and when the manager retires the read goes with them.

## Why It's Unsolved
**Data collection.** The judgement is formed in a moving vehicle, from sightlines and context that no database holds. Geopath supplies a modelled audience for each measured face, built from Teralytics roadway circulation and Motionworks device data, but that is an estimate of who passed, not of whether the face sells. Capturing the expert means recording their assessment at decision time (a structured site score, a short voice note, dashcam video of the approach) for hundreds of decisions a year. Field people resist that unless it is faster than what they already do.

**Labelling.** The obvious label is the face's later revenue, and it is badly confounded. A strong account executive can sell out a mediocre board, a recession can empty a good one, and pricing policy differs by market. Experts also disagree with themselves: the same manager scores the same approach differently after a bad year or a big win on a nearby face. A usable label has to be relative, such as occupancy-weighted rate against the market's own faces in the same period, and repeated scoring of a sample of sites is needed to measure how consistent the expert is.

**Deployment.** The model has to be faster than a drive. It is only adopted if it screens hundreds of candidate parcels or conversion candidates at a desk, against spacing and permit rules, so the manager drives only to the top few. It also has to show its reasons in the manager's own terms (read time, obstruction, category demand), or it will be ignored the first time it disagrees with someone senior.

## What a Solution Looks Like
A location-value model trained on the operator's own history. For every face it owns, it joins years of contracts, occupancy, rate and digital loop sell-through to the site's attributes: traffic counts, speed, Geopath impressions, distance and angle to the roadway, signal timing, nearby competitive faces, advertiser categories within a few miles, and imagery from street-level photos and crew dashcams processed for read time and obstruction. It predicts relative yield for a candidate site, the uplift from converting a static face to digital, and the rent a location can carry at renewal. Each prediction comes with the comparable faces that drove it.

The manager's own read is captured alongside the model's: a quick structured score and voice note at each decision, stored with the eventual outcome. Over two or three years this gives a graded record of where the expert beats the model and where they don't. It also gives a training set that holds the retiring manager's pattern recognition.

## Impact If Solved
Conversion capital moves to the faces where digital multiplies revenue rather than merely adding it. A conversion that underperforms ties up ~$200,000 and a loop the sales team cannot fill. Renewal negotiations start from a defensible number rather than the landlord's demand or a lump-sum buyer's offer. The same valuation record supports condemnation claims and property tax appeals, where operators currently argue location value without evidence. For an operator paying hundreds of millions in ground rent, a few percentage points better on renewals and conversions is worth more than any other software it could buy.
