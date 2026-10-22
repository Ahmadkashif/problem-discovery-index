# The Staff Scientist Sizing Particles by Hand

**Industry:** [[contract-research-labs|Contract Research Labs]]
**Type:** Worker Life Changing
**One-liner:** A staff scientist in a nanomaterials or advanced-materials lab spends hours per sample tracing particle outlines on electron micrographs, and gets back days of skilled time and their eyesight if the measuring is done for them.
**Tags:** #cnns #semantic-segmentation #object-detection #transfer-learning #evaluation-metrics #worker-facing #automation

## The Problem
Almost every nanomaterials project ends in the same measurement. A batch of particles, a coating or a composite is imaged by transmission or scanning electron microscopy, and the sponsor wants a size distribution, a shape description and a statement of agglomeration. For well-separated particles, thresholding in ImageJ or the microscope vendor's software works. For the samples that matter — touching, overlapping, irregular, on a textured support — automatic thresholding fails, and a staff scientist or technician traces hundreds of particles per sample by hand, image after image, because a statistically meaningful distribution needs several hundred counts.

A single synthesis study can generate dozens of samples, each needing the same treatment, and the measurement is repeated whenever a sponsor asks for a different statistic or a reviewer questions the threshold. The research literature on automated segmentation says plainly that agglomerated particles still rely on a human operator.

## Why It Matters to the Worker
The person doing the tracing is usually a PhD-level staff scientist or a skilled technician, hired to design experiments and run instruments, who now spends whole afternoons clicking. The work is tiring on the eyes and the wrist, and it is the part of the week least connected to the science. It also carries a quiet anxiety: two people tracing the same image get different answers, and the scientist knows their own result shifts with fatigue, which is uncomfortable when the number goes into a report a sponsor relies on.

Because the tracing is a bottleneck, it also sets the pace of the lab's experiments: a synthesis route cannot be judged until its particles are measured.

## What a Solution Looks Like
An instance-segmentation model, fine-tuned on a few dozen of the lab's own annotated micrographs, that outlines every particle, separates touching ones, flags agglomerates it cannot split, and produces the size and shape distribution with the per-image overlay saved alongside. The scientist reviews overlays, corrects the few the model got wrong, and those corrections feed the next round of training. The method, model version and review record go into the report so the number is traceable.

## Impact If Solved
Published work shows models trained on as few as 30–40 annotated TEM images reaching roughly 85% F1 and agreeing with manual size measurements; turning a multi-hour manual count into a twenty-minute review gives a busy staff scientist back a day or more each week during a synthesis campaign (estimate), and makes results consistent between people.
