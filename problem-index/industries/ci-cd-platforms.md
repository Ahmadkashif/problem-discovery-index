# CI/CD Platforms

## Profile
**Category:** Developer Tools & Infrastructure
**Market Size:** ~$4B US continuous integration, delivery and build infrastructure
**Tech Maturity:** Universal and quietly expensive — GitHub Actions, GitLab CI, CircleCI, Buildkite, Jenkins and the cloud providers' native services run the pipelines of essentially every software organisation. Pipelines have become slow, flaky and costly through accretion, and almost nobody measures any of the three.
**Workforce:** Build and release engineers, platform engineers, support engineers, pipeline template maintainers, solutions architects

## Key Pain Themes
The flaky test is the category's defining and least-addressed problem. A test that fails intermittently for reasons unrelated to the change teaches engineers to re-run pipelines rather than investigate, and once that habit forms the entire signal degrades — real failures get re-run too. Alongside it, pipeline duration grows monotonically because every team adds steps and nobody removes them, and the cost of waiting is paid in engineer attention rather than in a budget line, so it is never prioritised. Compute spend has become substantial and is attributed to nobody in particular, so it is optimised by whoever notices the bill. Caching and dependency management are configured by copying a template and rarely tuned. Build engineers spend their days as an internal support desk for pipelines they did not write, and every developer loses fragments of the day waiting on a build they cannot speed up.

## Current Tech Landscape
GitHub Actions has taken enormous share through proximity to the repository; GitLab CI serves the integrated platform; CircleCI and Buildkite compete on performance and control; Jenkins persists in large enterprises with deep customisation. Build systems (Bazel, Gradle, Nx, Turborepo) provide caching and incremental builds where adopted. Test impact analysis exists in a few products and is not widely used. Ephemeral and preview environments are increasingly standard. Flaky test detection features exist in several platforms at a basic level.

## Problems
- [[problems/ci-cd-platforms/high-impact|🔴 High Impact: Flaky Tests and the Collapse of Trust in the Signal]]
- [[problems/ci-cd-platforms/low-impact-1|🟡 Low Impact: Pipeline Duration and Test Selection]]
- [[problems/ci-cd-platforms/low-impact-2|🟡 Low Impact: Build Compute Cost Attribution]]
- [[problems/ci-cd-platforms/worker-life-1|🟢 Worker Life: Build Engineer as Internal Support Desk]]
- [[problems/ci-cd-platforms/worker-life-2|🟢 Worker Life: Waiting on the Build]]
- [[problems/ci-cd-platforms/ml-opportunity|🧠 ML Opportunities]]
- [[problems/ci-cd-platforms/ai-agents-platforms|🤖 AI Agents & Platforms]]

## Analysis
CI platforms hold every test execution result for every change across enormous numbers of repositories, joined to the code that changed, the environment it ran in and whether the change eventually shipped or was reverted. That is the complete empirical record of which tests are worth running, which are lying, and which changes are dangerous — the three questions every engineering organisation asks and answers by convention. The platforms bill by the minute and compute none of them.
