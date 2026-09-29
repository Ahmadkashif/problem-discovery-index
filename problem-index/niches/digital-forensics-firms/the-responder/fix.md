# Fix: The First Week Requires the Most Senior Person

**Niche:** The Responder
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Fix (Pain Point)
**One-liner:** Every engagement needs its most experienced practitioner in the first days, there are not enough of them, and nothing has been done to make the first days need them less.
**Tags:** #evaluation-metrics #confidence-intervals #worker-facing #tacit-knowledge-ml #workflow-orchestration #revenue-impact
**Contested on:** Whether a working pattern the field has called unsustainable for a decade is fixed, or a consequence of how engagements are staffed.

## The Problem

The first days of an incident require judgement. What questions must be answered, what evidence exists, where to look, what the early picture is consistent with, what to tell the client about scope. Getting this wrong in the first days costs the whole engagement, because collection decisions made on day one determine what can be established on day twenty.

Only senior practitioners can do it. So every engagement, regardless of size, consumes senior attention in its opening days, and a firm's capacity to take engagements is bounded by the number of people who can lead an opening — which is a small number that grows slowly.

The consequences cascade. Senior people are always on an opening or recovering from one. They cannot be spared for training, which slows the pipeline. Their reports are written in the evenings during the next engagement's opening. And when several incidents arrive at once, which happens, the same few people cover all of them.

The field treats this as a fact about the work. It is substantially a fact about how the knowledge is held. The judgement required in the opening days is largely a structured assessment — which questions, which evidence, which gaps — that a mid-level responder could execute if it existed as anything other than an experienced practitioner's mental model.

## Why It's Still Broken

**The knowledge is tacit and stays that way.** The opening assessment is built in a senior head under pressure and never recorded, which is the problem described in [[niches/digital-forensics-firms/evidence-bounded-inference/profile|🎯 Evidence-Bounded Inference]].

**Training happens on engagements and engagements have no spare capacity.** Junior responders learn by observing, which requires a senior practitioner with attention to spare during an opening, which is exactly when they have none.

**Clients and insurers expect seniority.** Panel terms and client expectations frequently specify experienced leads, which removes the option of fielding a mid-level opening even where one would be adequate.

**Mistakes in the opening are expensive and visible.** A collection decision missed on day one is discovered on day twenty, which makes any firm cautious about fielding less experience.

**Seniority is the firm's product.** Firms sell their practitioners' experience, so reducing the seniority required looks like reducing the product.

**Nobody has tried to decompose the opening.** The assumption that it requires holistic senior judgement has not been tested against the possibility that most of it is a structured checklist with a few genuinely judgement-dependent steps.

## What a Fix Looks Like

**Decompose the opening into structured and judgement components.** Access provisioning, inventory assembly, collection scoping, source enumeration and the question-evidence map are largely structured. Interpretation and client communication are judgement. Separating them lets a mid-level responder run the structured majority with a senior practitioner reviewing.

**Write down the opening checklist properly.** What must happen in the first forty-eight hours, in what order, with what decisions and who makes each. Firms have partial versions; nobody has the version that would let a less experienced person execute it.

**Have the senior practitioner review rather than run.** A structured opening executed by a mid-level lead and reviewed twice a day by a senior consumes a fraction of the senior time and is a better development experience than observation.

**Make the question-evidence map the handover artefact.** With the model recorded rather than held, a senior practitioner can set direction and step back, which is impossible while the model exists only in their head.

**Fix mobilisation so less of the opening is logistics.** A large share of the first days is access and inventory work that pre-agreed readiness would eliminate, and that work does not need seniority at all — it needs preparation.

**Tell clients and insurers what is actually happening.** A structured opening with senior oversight is a defensible model and is arguably better than an exhausted senior practitioner running everything. The expectation of continuous senior presence is worth renegotiating explicitly.

**Measure where senior time actually goes.** Firms assume it goes to judgement. Measuring would likely show a substantial share going to logistics and correlation, which is the finding that would justify the investment.

## Who Feels the Pain

The senior practitioners, who are always either opening an engagement or recovering from one, and who leave the field at a rate it cannot sustain.

Junior and mid-level responders, whose development is slow because the people who would teach them have no capacity.

The firm, whose delivery capacity is capped by a small number of individuals and whose growth is therefore capped too.

And clients, particularly during periods when several incidents coincide and the same few people are covering all of them.

## Impact If Fixed

Decomposing the opening into structured and judgement components is the intervention with the largest effect on the industry's binding constraint, and it requires writing down what is currently held in heads.

Senior review rather than senior execution multiplies the capacity of the scarcest resource in the field and develops the next generation faster than observation does.

And measuring where senior time actually goes would very likely show that a large share is spent on work requiring no seniority at all — which is the finding that would make the case for fixing it.
