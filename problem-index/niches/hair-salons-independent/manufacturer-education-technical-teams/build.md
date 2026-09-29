# Six Hundred Technical Experts Teach Colour Formulation and Never Find Out What Came Out

**Niche:** [[niches/hair-salons-independent/manufacturer-education-technical-teams/profile|Professional Brand Education & Technical Teams]]
**Industry:** [[industries/hair-salons-independent|Hair Salons (Independent)]]
**Type:** Build (Greenfield Opportunity)
**One-liner:** The professional colour brands run the largest technical education workforce in the industry to teach a formulation system whose real-world results they have almost never observed — except through the correction calls, which are a labelled failure set nobody has treated as data.
**Tags:** #cnns #transfer-learning #gradient-boosting #tacit-knowledge-ml #evaluation-metrics

## The Problem
Professional hair colour is sold through education. The major brands each employ hundreds of educators, technical artists and colour chemists who teach stylists a formulation system: how to read the hair's starting level, account for underlying pigment, choose a shade and developer volume, and predict what will result. The education is the reason a salon stays with a brand — the tubes themselves are close to substitutable, and everyone in the business knows it.

Formulation is a genuinely hard prediction problem. The outcome depends on the natural level and porosity of the hair, everything chemically done to it before — box colour, previous lightening, relaxers, minerals in the water — the shade chosen, the developer volume, the processing time, the ambient temperature, and how the stylist applied it. Experienced colourists develop real skill at this. It takes years, it is largely tacit, and it is exactly the knowledge the education organisation exists to transfer.

The organisation transferring it has never observed the outcome.

A stylist attends a class, learns the system, returns to the salon, and mixes formulas on real heads for the next decade. What resulted — the colour that actually appeared, whether it matched the prediction, whether it held — is never recorded anywhere the brand can see. The feedback loop that would let the education improve does not exist.

There is one exception, and it is the interesting one. When a colour result goes badly wrong, the stylist calls the brand's technical support line. That call captures the whole context: the starting condition, the chemical history, the formula used, the developer, the timing, and what went wrong. Across a large brand, over years, that is hundreds of thousands of labelled failures with full covariates.

It is stored as call notes for the purpose of resolving the individual call.

## Why Nobody Has Built This
The invoice is a tube of colour. Education and technical support are a cost of selling it, budgeted against sales in a territory, and measured by classes delivered and stylists reached. Nothing pays for a formulation outcome study.

The distribution structure hides the customer. Professional colour reaches salons through distributors, and the brand often cannot see salon-level purchasing, let alone chair-level use. That gap is old, commercially entrenched, and it is the reason the brand's view of its own product ends at the distributor's warehouse.

The technical support call is understood as a service interaction, not an observation. It is handled, closed and reported as a resolution time. The idea that the correction queue is the brand's only outcome dataset has not been the frame anyone worked in.

There is also a defensiveness about failure. A systematic analysis of colour corrections is, read uncharitably, a catalogue of the product not doing what the brand said it would, and it would be visible internally to people who present the formulation system as reliable.

And colour measurement is genuinely hard. Assessing a result objectively requires either instrumentation at the chair or photographs under uncontrolled salon lighting, and the second has historically been unusable. That has changed more than the industry has noticed.

## What to Build
**Treat the correction queue as a labelled dataset.** Structure the technical support corpus — starting condition, history, formula, developer, timing, outcome — and the most common failure modes become measurable rather than anecdotal. Which shade families under-deposit on which starting conditions, where the system's prediction is systematically off, which instructions are being misread: all answerable, immediately, from records already held.

**Predict the result from the starting state.** Given a documented starting level, porosity and chemical history, and a proposed formula, what actually results. This is the core question of the entire discipline and it is currently answered by experience. Even a well-calibrated uncertainty estimate — this formula is reliable here, unpredictable there — would be new.

**Solve the measurement problem properly.** Colour assessment from images under salon lighting is a calibration problem before it is a recognition problem, and it is tractable now in a way it was not a decade ago. Reference cards, controlled capture and a model trained on the brand's own shade library make the outcome recordable at the chair, which is the precondition for everything else.

**Measure the education.** Which stylists attended which class, and what changed afterwards in their formulation behaviour, correction rate and product mix. The organisation runs thousands of classes a year and evaluates them on attendance and satisfaction sheets.

**Capture the experts before they retire.** The technical artists hold the tacit knowledge of the discipline. Structuring it — as a case corpus with reasoning, not a shade chart — is a capture project with a real deadline attached.

**Give the stylist the tool, not the class.** A chairside formulation aid that accounts for a specific head's history is a far stronger reason to stay with a brand than an annual education day, and it collects the outcome data that makes it better.

## Target Customer
VP of Education or Technical Director at a professional colour brand. The commercial argument is the one the organisation already believes: education is what defends the brand against substitution, it is the largest line in the professional division, and it is currently delivered without any measurement of what it changed.

## Impact If Built
Hundreds of thousands of stylists formulate colour daily on skill acquired through years of trial on paying clients, taught by an organisation that has never seen a result. The one record of what goes wrong sits in a support queue, closed ticket by ticket.
