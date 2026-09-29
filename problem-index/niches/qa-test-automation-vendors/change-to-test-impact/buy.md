# Change Impact Analysis From Program Analysis

**Niche:** [[niches/qa-test-automation-vendors/change-to-test-impact/profile|Change-to-Test Impact]]
**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Type:** Buy & Customize (Vertical Adaptation)
**One-liner:** Change impact analysis is a studied program analysis problem with published techniques, and the testing category approximates it with file paths.
**Tags:** #graph-theory #spectral-graph-theory #gradient-boosting #bert #evaluation-metrics #confidence-intervals #cross-validation #automation
**Contested on:** Every serious competitor here is fighting to model the relationship between an application change and the tests it affects — and whoever does that takes the category, because that relationship is its central object and is modelled nowhere.

## The Problem
Determining what a change affects is change impact analysis, studied in software engineering research with static, dynamic and historical approaches and a body of empirical evaluation. Applied to tests, it answers which tests a change could affect. The commercial state of the art is either coverage-based, which requires instrumentation, or path-based, which uses directory structure as a proxy for dependence and is roughly as accurate as that sounds.

## What Already Exists
Static change impact analysis with call and dependence graph traversal; dynamic impact analysis from execution traces; historical co-change mining from version control, which needs no analysis infrastructure at all; program slicing; and the regression test selection literature that builds on all of it. Published, evaluated and with open implementations for several languages.

## The Customization Gap
The adaptation is to modern applications where much of the impact is not in code. It requires: (1) covering interface changes, since the majority of end-to-end test breakage comes from markup, styling and component structure rather than from program logic, and the code-oriented techniques do not see any of it — this is the gap that matters most and needs an interface-element dependence model; (2) combining historical and structural evidence, because historical co-change is free and imprecise while structural analysis is precise and unavailable in many stacks, and the combination is better than either; (3) cross-boundary impact, since a change to a service affects tests of a different service through an interface, which single-repository analysis misses entirely; (4) change classification as an output, not just impact, since knowing which tests are affected is half the need and knowing whether the change was behavioural is the other; and (5) fleet learning, since the vendors observe the same frameworks and change patterns across thousands of applications and the general relationship between a change type and its test impact is learnable across customers in a way it is not within one.

## Target Customer
Test automation vendors, build system vendors, platform engineering teams, and the research community whose techniques have not been commercialised for this use.

## Impact If Solved
A studied analysis problem is approximated with directory paths in the commercial products. Extending the analysis to interface changes is what makes it cover the dominant breakage cause, and fleet learning is an advantage available only to the vendors.
