# Lineage: QA & Test Automation Vendors

**Industry:** [[industries/qa-test-automation-vendors|QA & Test Automation Vendors]]
**Wave:** [[series/eras/wave-06-cloud-saas|6 — Cloud & SaaS]]
**The tool:** Selenium — first written in 2004 as "JavaScriptTestRunner", a JavaScript harness that drove a real browser by locating page elements and clicking and typing into them; later merged with WebDriver and standardised by the W3C
**Builder:** ThoughtWorks
**Builder in vault:** [[industries/software-dev-agencies|Software Development Agencies]]
**Verification:** partial — see Sources

## The Problem That Came First

A consultancy that sold automated testing as a methodology could not automate the part of its own product the customer actually saw.

By the early 2000s agile shops tested their server code on every check-in — ThoughtWorks' own CruiseControl ran exactly that loop (see [[lineage/ci-cd-platforms|Lineage: CI/CD Platforms]]). But a web application's user interface lived in a browser, and the browser was outside the harness. Testing it meant a person clicking through pages, or buying a commercial functional-testing suite from vendors such as Mercury Interactive, priced per seat for QA departments, not for every developer on every build.

## What Got Built

A test runner that lived inside the browser.

In **2004**, in ThoughtWorks' **Chicago** office, Jason Huggins wrote what the Selenium project's own history calls the Core mode, as **"JavaScriptTestRunner"**, to test **an internal Time and Expenses application (Python, Plone)**. Because it ran as JavaScript in the page, it could drive any browser that ran JavaScript: find an element, click it, type into it, assert what appeared. Colleagues liked it, the project says, for its "immediate and intuitive visual feedback". It was open-sourced the same year.

The name was a joke at the incumbent: selenium supplements were said to cure mercury poisoning.

Then the layers:

| Tool | Builder | Place | Year | What it was for |
|---|---|---|---|---|
| Selenium RC | Dan Fabulich, Nelson Sproul, Pat Lightbody | — | 2005 | driving the browser from a test written in any language via a proxy server |
| WebDriver | Simon Stewart, at ThoughtWorks | — | by 2009 | controlling the browser natively rather than from injected JavaScript |
| Selenium 2.0 | the merged projects | agreed at Google's Test Automation Conference | 2009 | one API over both |
| Sauce Labs | Jason Huggins and co-founders | — | 2008 | Selenium runs on hosted browsers, sold as a service |
| W3C WebDriver | Simon Stewart and David Burns of Mozilla, via the W3C | — | working draft July 2012; Recommendation June 2018 | the browser-control protocol, shipped by browser makers themselves |

## Who Built It, And Why Them

ThoughtWorks, because it was a services firm whose methodology made automated tests central, and it had web applications — its own included — that its existing test loop could not reach.

A tool vendor sold testing to QA departments and priced accordingly. A consultancy's economics ran the other way: it wanted every developer on every project to run browser tests on every build at zero marginal cost, and it had no interest in licence revenue. So the tool it built was free, scriptable, embeddable in a build, and good enough for an internal expense-tracking app. Open-sourcing it cost ThoughtWorks nothing it sold. Huggins later took the idea to Google in 2007, and in 2008 co-founded Sauce Labs to sell what the open tool lacked — the browsers themselves, hosted.

## What It Cost

**The test binds to the page's implementation, not to its behaviour.** Selenium's primitive is "find this element" — by id, name, XPath or CSS selector — "then act on it". That made tests easy to write against any HTML, which is why it spread. It also means every change to markup that a user would never notice can break a test that was correct yesterday.

Keeping those locators true across two years of front-end rewrites is the permanent cost the industry now sells "self-healing" to reduce.

## What You Still Touch

Every `findElement(By.cssSelector(...))`, every Playwright or Cypress locator, and every grid of hosted browsers descends from a JavaScript runner written to test a consultancy's timesheet app. The locator is the unit; so is its fragility.

- [[problems/qa-test-automation-vendors/high-impact|🔴 The Maintenance Burden That Kills Test Suites]] — the bill for binding to selectors
- [[problems/qa-test-automation-vendors/worker-life-1|🟢 Test Engineer Repairing Rather Than Designing]]
- [[niches/qa-test-automation-vendors/ai-generated-and-self-healing/profile|AI-Generated & Self-Healing Tests]]
- [[niches/qa-test-automation-vendors/browser-device-grids/profile|Browser & Device Grids]] — the Sauce Labs half of the lineage

**Sources:** Selenium project, "History", selenium.dev/history (Huggins; Chicago; 2004; "JavaScriptTestRunner"; internal Time and Expenses application in Python/Plone; visual-feedback quotation); Wikipedia, *Selenium (software)* (open-sourced 2004; Selenium RC 2005 with Fabulich, Sproul and Lightbody; Huggins to Google 2007; Stewart's WebDriver; 2009 GTAC merger; W3C working draft July 2012 and Recommendation June 2018 with David Burns; Mercury name joke); Wikipedia, *Sauce Labs* (2008; Huggins with Steven Hazel, John Dunham and Al Sargent); Wikipedia, *Mercury Interactive* (HP acquisition announced 25 July 2006, ~$4.5B). The CruiseControl link is to a vault note, cited as vault material, not independent corroboration. ⚠️ **WebSearch was unavailable this session (session cap reached)**; research was by direct fetch only. ⚠️ **Not established:** the year Stewart began WebDriver (placed here only as "by 2009"); Mercury's pricing model, which is characterised in general terms and not from a price list; any claim that Mercury's tools specifically motivated Huggins — the project history does not say so, and only the name joke is attested.
