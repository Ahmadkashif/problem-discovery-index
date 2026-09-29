# Lineage: CI/CD Platforms

**Industry:** [[industries/ci-cd-platforms|CI/CD Platforms]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** CruiseControl — the server loop that ran the full build and tests on every check-in and published pass or fail to the team; first released 30 March 2001
**Builder:** ThoughtWorks
**Builder in vault:** [[industries/software-dev-agencies|Software Development Agencies]]
**Verification:** partial — see Sources

## The Problem That Came First

Integration was a phase, and it was the one nobody could estimate.

Developers worked on their own copies of the code for days or weeks, then merged. The merge surfaced every conflicting assumption at once, and untangling them could take longer than writing the code. Each workstation was its own undocumented environment, and no one ran the whole system until the end.

Extreme Programming's answer, taken up by Kent Beck and colleagues on Chrysler's C3 payroll project, was a discipline: integrate many times a day, and treat a broken build as the team's top priority. Beck's line, as Martin Fowler later quoted it: "nobody has a higher priority task than fixing the build." **A discipline, though, depends on someone remembering to run the build.** On a large team, someone always forgot.

## What Got Built

A program that did the remembering.

CruiseControl sat on a server, polled the source repository, and when it saw a new check-in, ran the complete build and test suite in a clean workspace rather than on anyone's desk. It then reported the result — by email and on a web page of build status — naming the change that broke it. Its initial release was **30 March 2001**, under a BSD-style licence; .NET and Ruby ports followed.

The design choice that mattered was the verdict: one bit per commit, green or red, and the team stops to fix red. Everything later in this industry inherits that bit.

## Who Built It, And Why Them

ThoughtWorks, a software consultancy — and the reason is that a consultancy builds large systems for clients, with teams it assembles and reassembles.

Martin Fowler, its chief scientist, published the article "Continuous Integration" on **10 September 2000**, co-written with Matt Foemmel. Fowler credits Foemmel, Dave Rice and others for building and maintaining continuous integration on **Atlas**, a large ThoughtWorks project that "showed the benefits it made to an existing project." Wikipedia says CruiseControl was created by ThoughtWorks employees "to allow for continuous integration on a project they were working on" and later extracted into a stand-alone application.

A consultancy carries the integration risk twice. An unestimable integration phase lands on its delivery commitments; and it moves developers between clients, so the discipline has to survive people who were not there when it was agreed. **Automating the discipline was cheaper than training it into every team.**

Fowler calls CruiseControl "the first CI service" and credits Paul Julius, Jason Yip, Owen Rodgers, Mike Roberts and others with building its variants. That "first" is ThoughtWorks' own claim; the term continuous integration is older, and Urbancode's AnthillPro is dated to the same year.

**Then the inheritor.** Kohsuke Kawaguchi began Hudson at Sun Microsystems in summer 2004, first released in February 2005. After Oracle bought Sun and asserted the name, the community renamed it Jenkins on 29 January 2011. Hudson and its descendants took the market; CruiseControl's last release, 2.8.4, came in 2010.

## What It Cost

**The single bit assumes the tests are deterministic.**

Green-means-good only works if red means the code is broken. As suites grew, tests began failing for reasons unrelated to the change — timing, shared state, the network, an overloaded build machine. A red build stopped meaning "you broke it." Google reported in 2016 a continual rate of about 1.5% of all its test runs coming back flaky; teams answered by rerunning failures until they passed, spending the signal the tool was built to protect.

The second cost is time. "Run everything on every check-in" was affordable for a 2001 codebase and is the reason developers now wait on a queue.

## What You Still Touch

The red or green mark next to your pull request is CruiseControl's verdict, one bit per commit, still asserting that the team will stop and fix red — though the team no longer believes it.

- [[problems/ci-cd-platforms/high-impact|🔴 Flaky Tests and the Collapse of Trust in the Signal]] — the bit, worn out
- [[problems/ci-cd-platforms/worker-life-2|🟢 Waiting on the Build]] — the cost of running everything, every time
- [[niches/ci-cd-platforms/flaky-tests-signal-quality/profile|Flaky Tests & Signal Quality]]
- [[niches/ci-cd-platforms/test-selection-and-duration/profile|Test Selection & Pipeline Duration]]

**Sources:** Wikipedia, *CruiseControl* (ThoughtWorks employees, extraction from a project, initial release 30 March 2001, BSD-style licence, .NET and Ruby ports, 2.8.4 in 2010); Martin Fowler, "Continuous Integration", martinfowler.com (original version 10 September 2000; Beck quotation; credits to Foemmel, Rice and the Atlas project; CruiseControl as "the first CI service" with named contributors); Wikipedia, *Jenkins (software)* and *Hudson (software)*, and Kawaguchi's own blog post "Bye bye Hudson, Hello Jenkins" (11 January 2011) for the Hudson and Jenkins dates; John Micco, "Flaky Tests at Google and How We Mitigate Them", Google Testing Blog, May 2016 (the 1.5% figure). ⚠️ **Not established:** that CruiseControl was extracted specifically from the Atlas project — Fowler links the Atlas team to CI practice and separately names CruiseControl's builders, but I did not find a primary source joining the two. Several secondary pages name Matt Foemmel as CruiseControl's creator; I could not confirm this against a primary source and do not assert it. AnthillPro's 2001 date is from Wikipedia only. The consultancy-economics argument in the third section is this note's inference, not a stated ThoughtWorks rationale.
