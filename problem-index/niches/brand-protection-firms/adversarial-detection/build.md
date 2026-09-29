# Build: Detection That Assumes an Opponent

**Niche:** Adversarial Detection
**Industry:** [[industries/brand-protection-firms|Brand Protection Firms]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** Detection trained against the evasions operators actually use, keyed on signals that are expensive for them to change, and operating across surfaces rather than per listing.
**Tags:** #cnns #contrastive-learning #graph-neural-networks #gradient-boosting #evaluation-metrics #confidence-intervals #transfer-learning #automation
**Contested on:** Whether detection finds the listings of operators who have learned exactly what it matches on.

## The Problem

Detection is built as though the listings were passive. Match the image, match the name, flag the price. It performs well against sellers who are not trying to avoid it and poorly against the ones who are — which is the population that matters.

The evasions are well understood by anyone who looks. Images cropped, recoloured slightly, re-photographed, composited or watermarked, enough to break perceptual matching and not enough to deter a buyer. Brand names absent from the title, present in an image, in a description, in a hashtag, in a seller's reply to a question, or rendered as a lookalike string. Prices set within the plausible range for genuine goods. Accounts aged, rated and varied.

What makes this tractable is that the firm holds the record of the arms race. Every listing detected, every listing that survived and was later found by other means, every seller actioned and every account that reappeared. That history is a training set for evasion and is used for nothing — models are built against current listings rather than against the adaptation.

And the strongest available signals are structural rather than content-based. An operator running hundreds of accounts leaves patterns in registration timing, shipping origin, image provenance, pricing behaviour and cross-surface coincidence that are far more expensive to alter than an image is.

## Why Nobody Has Built This

**Volume rewards the easy detections.** A pipeline optimised for count is optimised for the naive listings, which are plentiful and cheap to find. Finding the hard ones is expensive and produces fewer notices per unit of effort.

**Recall is unmeasured.** Nobody knows what fraction is missed, so there is no evidence that the hard population is under-detected and no metric that would improve.

**Adversarial training requires labelled evasions.** The firm's own history contains them and they are not labelled as such, so the training set exists and is unusable without work nobody has done.

**Cross-surface signals require joining data nobody joins.** An operator's presence across marketplaces, social platforms and domains is visible in aggregate and the systems are separate.

**Structural signals need operator attribution.** Keying on account clusters requires knowing the clusters, which is the capability in [[niches/brand-protection-firms/operator-attribution/profile|🟠 Operator Attribution]].

**Improvement is temporary by nature.** Operators adapt to whatever is deployed, which makes detection investment feel like a treadmill and reduces enthusiasm for a step change.

## What to Build

**Train against the evasions in the firm's own history.** Listings that were detected late, listings found by other means after surviving detection, and the account reappearance record. This is an adversarial training set the firm already generated and has never labelled.

**Key on signals that are expensive to change.** Shipping origin, fulfilment patterns, image provenance metadata, registration and account-creation timing, pricing dynamics, and cross-surface coincidence. An operator can recolour an image cheaply; changing their fulfilment network is expensive.

**Detect at account and cluster level, not listing level.** A newly created account with characteristics matching a previously actioned cluster is detectable before it lists anything. This is a fundamentally stronger position than matching each listing as it appears.

**Join across surfaces.** The same operator on a marketplace, a social platform and a domain is one entity, and detection on any surface should inform the others. The signals are strongest where the surfaces meet.

**Measure recall against a ground truth you construct.** Test purchases, brand-supplied seizure data, and periodic deep manual sweeps of a sample category produce an estimate of what detection missed. Without it there is no objective, which is why detection optimises volume by default.

**Monitor adaptation explicitly.** Track how the detected population's characteristics shift after a detection change. Operators adapt within weeks and nobody measures the adaptation, so nobody knows how long an improvement lasts.

**Prioritise by harm, not by match confidence.** A detection system whose objective is count will find easy listings. One whose objective is estimated infringing volume removed will find operations.

## Target Customer

Brand protection firms competing on capability rather than on price, particularly those serving brands whose counterfeit problem is dominated by sophisticated operations rather than casual sellers.

Brands with high-value products, for whom the sophisticated operators represent nearly all the actual loss and the casual listings represent nearly all the current takedown count.

Marketplace platforms, whose own seller integrity teams face the same adversary with better data and could use the same techniques.

## Impact If Built

Detection starts finding the population that causes the loss rather than the population that is easiest to find, which is a reallocation of the same effort toward a different outcome.

Keying on expensive-to-change structural signals changes the economics of the arms race, because an operator who must change their fulfilment network to evade detection faces a real cost where recolouring an image is free.

And measuring recall against a constructed ground truth would give detection an objective other than volume, which is the change that makes every other improvement in this niche worth making.
