# Insurance Third-Party Administrators (TPAs)

## Profile
**Category:** Insurance
**Market Size:** ~$15B US third-party administrator market handling workers' compensation, group health, property/casualty, and specialty claims on behalf of insurance carriers and self-insured employers
**Tech Maturity:** Medium — ClaimVantage, Origami Risk, BriteCore, and FINEOS provide claims management platforms, but many TPAs operate on legacy mainframe systems (COBOL-based) or heavily customized off-the-shelf solutions with manual workarounds
**Workforce:** Claims examiners, adjusters, medical case managers, account managers, compliance officers, data analysts, and administrative support staff

## Key Pain Themes
Claims adjudication speed is the central competitive metric — TPAs are contractually bound to SLAs (typically 15-30 day turnaround for initial decisions) and face financial penalties for missed targets. A claims examiner reviews 150-200 claims per month, each requiring extraction of relevant facts from medical records, policy review, coverage determination, and reserve estimation. The work is cognitively demanding and repetitive — examiners develop pattern recognition for suspicious claims, coverage gaps, and reserve accuracy, but this expertise is tacit and fragile to turnover. Account management involves serving multiple carrier and employer clients simultaneously, each with unique reporting requirements, benefit structures, and escalation protocols. Regulatory compliance spans federal (ERISA, ACA, HIPAA) and state-specific workers' compensation rules, creating a matrix of requirements that changes quarterly.

## Current Tech Landscape
ClaimVantage handles group disability and absence claims. Origami Risk provides enterprise risk management with claims modules. BriteCore serves P&C claims processing. FINEOS dominates life, accident, and health claims for large carriers. Many TPAs use legacy systems customized over decades with brittle integrations. Guidewire serves the broader P&C market but is too expensive for mid-size TPAs. AI adoption is early — some TPAs use basic rules engines for auto-adjudication of simple claims, but complex claims (60-70% of volume) still require full manual review.

## Problems
- [[problems/insurance-tpa/high-impact|🔴 High Impact: Claims Adjudication Speed and Accuracy]]
- [[problems/insurance-tpa/low-impact-1|🟡 Low Impact: Client Reporting and SLA Management]]
- [[problems/insurance-tpa/low-impact-2|🟡 Low Impact: Provider Network Management and Credentialing]]
- [[problems/insurance-tpa/worker-life-1|🟢 Worker Life: Claims Examiner Decision Fatigue]]
- [[problems/insurance-tpa/worker-life-2|🟢 Worker Life: Account Manager Client Escalation Overload]]
- [[problems/insurance-tpa/ml-opportunity|🔵 ML Opportunities]]
- [[problems/insurance-tpa/ai-agents-platforms|🤖 AI Agents & Platforms]]
