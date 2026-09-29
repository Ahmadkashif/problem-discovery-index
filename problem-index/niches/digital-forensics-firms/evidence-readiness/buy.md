# Buy: Detection Coverage Assessment, Pointed at Investigation

**Niche:** Pre-Incident Evidence Readiness
**Industry:** [[industries/digital-forensics-firms|Digital Forensics Firms]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Detection coverage assessment maps telemetry against attack techniques and asks whether an attack would be seen, never whether it could afterwards be investigated.
**Tags:** #graph-theory #evaluation-metrics #confidence-intervals #gradient-boosting #compliance #data-integration #automation
**Contested on:** Whether an organisation can be told, before anything happens, which of its logging gaps will make the notification question unanswerable.

## The Problem

Detection coverage assessment is an established practice. Map the organisation's telemetry and detection rules against a technique framework, identify which adversary techniques would be detected and which would not, and produce a coverage picture with gaps ranked by likelihood of use.

It answers a real and different question. Would we see this happening? Investigation asks: afterwards, could we establish what happened? The two diverge in ways that matter.

A control that blocks an attack outright leaves minimal record of what was attempted. A detection that fires on initial access says nothing about what was subsequently accessed. Telemetry retained for thirty days supports detection perfectly and supports investigation of a ninety-day intrusion not at all. And the evidence that answers the scope question — file access, database query logs, egress records — is frequently not detection telemetry at all and appears in no coverage assessment.

So an organisation can have strong detection coverage and be unable to investigate, and the assessment that would reveal it does not exist while the one that looks similar does.

## What Already Exists

Detection coverage: ATT&CK-based coverage mapping, tooling such as DeTT&CT and the mapping features in detection platforms; purple team exercises producing coverage evidence; breach and attack simulation measuring detection empirically.

Log source assessment: the detection engineering practice of mapping data sources to detectable techniques, which is the closest existing structure and is oriented to detection.

Logging guidance: vendor and framework recommendations on what to enable, generic and extensive.

Forensic readiness: an established concept in the standards literature, with guidance that is real and largely unoperationalised commercially.

Incident response retainers: readiness assessments bundled with retainers, usually questionnaire-based and light.

## The Customization Gap

**The question is different and the framework is reusable.** ATT&CK-based mapping works for investigation too, with the mapping pointed at evidentiary rather than detective value — which techniques leave what record, and for how long.

**Detection-relevant and investigation-relevant sources diverge.** File access auditing, database query logs and detailed egress records matter enormously for scope and are largely absent from detection coverage assessments because they are poor detection sources.

**Retention is not modelled against dwell time.** Coverage assessments ask whether a source exists. Investigation requires that it existed during the intrusion, which is a retention question nobody assesses against realistic dwell times.

**Blocking is a coverage win and an evidence loss.** A control that prevents an attack scores well in detection coverage and may leave nothing to investigate — a trade no assessment currently surfaces.

**The output is not expressed in consequence.** Detection coverage produces a technique coverage percentage. Investigative readiness needs to produce a statement about what would be unanswerable and what that would cost, which is a different deliverable for a different reader.

**Forensic readiness has standards and no product.** The concept is documented in the standards literature and there is no commercial assessment product implementing it, which is a straightforward gap.

## Target Customer

Detection engineering and purple team vendors, whose coverage mapping framework transfers with the perspective changed and who already sell the adjacent assessment.

Breach and attack simulation vendors, who could extend from measuring whether an attack is detected to measuring what record it leaves — a natural addition to an existing technical capability.

Forensics firms as the providers of the corpus that makes the ranking meaningful, since only they know which gaps have actually been consequential.

## Impact If Solved

An established assessment framework transfers with its perspective changed, which makes this a reframing rather than a new discipline.

Surfacing the blocking-versus-evidence trade would make visible a decision organisations currently make unknowingly — that a control which prevents an attack may also prevent knowing what was attempted.

And modelling retention against realistic dwell time rather than against policy would reveal the most common investigative gap of all, which is telemetry that exists and does not reach back far enough.
