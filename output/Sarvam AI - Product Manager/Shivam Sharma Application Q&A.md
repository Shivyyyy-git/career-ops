# Application Q&A: Sarvam AI Product Manager

*Pre-filled answers for the Sarvam application form and likely screen-1 questions. Same human-tone rules as the resume: no em-dashes, no AI tells, plain English, concrete examples. Update as the conversation evolves.*

## Why Sarvam AI?

Sovereign Indian AI is the most important infrastructure bet on the subcontinent for the next decade. Global frontier models treat Indic languages as a long tail. The only way that gets fixed is by Indians shipping Indic-first foundation models, deploying them across consumer, enterprise, developer tools, voice, and edge, then iterating in production with paying customers. Sarvam-105B (Indus), the Sarvam Kaze hardware launch, the Tata Capital and SBI Life deployments, and the NVIDIA + Accel + HCLTech round are the clearest signal that Sarvam is shipping at unicorn velocity, not pitching.

The generalist PM seat is the one that touches the most surfaces. That is the seat where I can compound the fastest given how I already work.

## Why this role?

Six lines from the JD describe how I run a product:

1. **Own a product area end-to-end: talk to users, write specs, define success metrics, ship, measure.** Maya AI from vision to live in 2.5 months at ESC. Customer discovery with NEP supervisors. INVEST stories. UAT. Production. SLOs.
2. **Analyze AI system behavior in production: prompt design, model selection, latency, failure modes.** Bedrock routing across Opus, Sonnet, Nova; shadow-channel A/B; takeover frequency as the regression signal.
3. **Write code, prompts, and copy when needed.** Daily. FastAPI handlers, n8n workflows, React cockpit, Teams adaptive cards, supervisor-facing strings. Claude Code is my drafting tool.
4. **Establish funnels and instrument events.** Maya AI dashboards on DynamoDB telemetry. SALL: 8-factor scoring + two-phase pre-filter validated against advisor consultations.
5. **Work directly with engineering, design, leadership. No layers.** ESC engineering, NEP operations, Moreno Valley Electrical, Delta Utilities. CRO weekly. No middle.
6. **Ship product every week, not plans.** Maya AI shipped a working surface weekly for 10 weeks straight. The first paid pilot started in week 6.

## Tell me about a time you owned a product end-to-end.

Maya AI is the cleanest example. ESC had no AI track when I joined in January 2026. The CRO wanted Oracle CCS to be smarter, faster, and multi-channel. There was no spec, no eval framework, no team.

I started with two weeks of customer discovery at NEP. Sat with supervisors. Watched them dig through Oracle CCS to answer a single resident question. Mapped the workflow. Picked the stack: AWS Bedrock for model routing, n8n for orchestration, FastAPI for the integration layer, React for the supervisor cockpit, Teams adaptive cards for HITL approval, 11 Labs for 26-language voice.

I built it on Claude Code, end-to-end, in 2.5 months as the only AI hire. The eval framework tracks confidence, sentiment, and takeover frequency as service-level objectives. When Bedrock launched a new Claude model, I A/B'd it on a shadow channel for two weeks, watched takeover-frequency for regressions, then rolled by channel. Live at NEP with 200K+ residents, rolling out at Moreno Valley Electrical, piloting at Delta Utilities. Handles 70 to 80% of first-touch support autonomously. Projected savings at NEP are around $225K per month.

## What AI tools do you use today and how?

- **Claude Code:** daily driver. Maya AI's supervisor cockpit, the email-triage agent, the React console, and the FastAPI handlers all started as Claude Code sessions before any code shipped.
- **AWS Bedrock:** production routing layer for Maya AI across Claude Opus (hard agent-of-record), Sonnet (default conversational), Nova (cheap intent classification).
- **n8n:** orchestrator for three production agentic workflows: Conference Outreach, Maya email-triage, supervisor approval.
- **11 Labs:** voice surface for Maya AI's 26-language coverage.
- **Cursor and GitHub Copilot:** in-editor pair programming inside long-lived codebases.
- **Claude (web), ChatGPT, Perplexity:** mixed deliberately for thinking, research, and red-team work.
- **XGBoost + SHAP:** Simon Vision Consulting fraud detection (62% to 73% accuracy lift).

## How do you think about cost-latency-accuracy tradeoffs?

Three opinions:

- **Latency is a quality metric.** If a supervisor waits 4 seconds for an answer, the agent has failed. Latency budgets sit in the PRD.
- **Cost has to be modeled per intent, not per call.** Maya AI routes routine billing questions to Nova, complex outage triage to Sonnet, and the rare high-stakes escalation to Opus. Same architecture, three cost profiles.
- **Accuracy without confidence calibration is dangerous.** A 90% accurate agent that does not know when it is wrong is worse than a 75% accurate agent that defers correctly. Confidence has to be a first-class signal.

## Have you shipped side projects or open-source?

Yes. **Career-Ops** is a Claude Code harness I run for my own job search: scans portals, evaluates JDs against my profile, generates tailored CVs and cover letters, tracks outcomes. Public on GitHub. Built end-to-end in evenings. The development loop is the product. **VaultIQ** is an air-gapped Claude Opus financial-intelligence platform I prototyped at ESC and spun off as a deployable customer product. **Conference Outreach Automation** is a 3-workflow agentic system shipped to the ESC CRO; lives in production now.

## What's the deepest impact you've shipped in 2 to 3 personal or professional initiatives?

- **Maya AI at NEP (last 5 months):** 200K residents touched. 26-language voice. ~$225K/month projected savings. 70 to 80% autonomous on first-touch. Single AI hire.
- **CloudApproach + Approachables (4.5 years):** bootstrapped and exited two ventures. $575K combined exit. 95% post-acquisition retention. $5M+ in deals influenced on a $200K marketing budget. 200+ agency clients, 80+ real-estate partners.
- **Career-Ops harness (3 months, side project):** the system that scans 45+ job portals and runs my entire pipeline. Built on Claude Code. Productionised against my own job search.

## SQL and data analytics fluency?

SQL is daily. Maya AI's DynamoDB telemetry is queried through Athena for funnel work and confidence-distribution analysis. Postgres with pgvector on VaultIQ. SALL's two-phase pre-filter is a SQL-style join over advisor history. On analytics tools: I have built funnels and dashboards from scratch in Maya AI's React cockpit on telemetry I instrumented myself, rather than as a buyer of PostHog or Mixpanel. The reflex is the same; the tool is a one-day pickup.

## What is your biggest accomplishment?

**Career-wise:** Bootstrapping and selling CloudApproach + Approachables for $575K combined. Two ventures across UK and MENA. 200+ agency clients. 80+ real-estate partners. $5M+ in deals influenced. Two exits before I turned 25.

**Last six months:** Maya AI live at NEP with 200K+ residents in 2.5 months as the sole AI on staff. The team had never shipped AI before. They have shipped it now.

## Why are you leaving your current role?

Scope and stage. ESC has been a great place to ship Maya AI, but my next role should put me inside a team where the product spread I have been running for one customer at a time becomes the platform charter at unicorn-stage velocity. Sarvam is that team.

## Compensation expectations?

Open to the Sarvam range. Priority is total package plus equity at unicorn stage given the velocity. Happy to discuss INR or USD denomination depending on the relocation outcome.

## When can you start?

Immediately for remote. Two-week handoff at ESC for the Maya AI roadmap and supervisor cockpit. If Bengaluru on-site is required, I can be on the ground within 30 to 45 days of offer (visa logistics permitting).

## Work authorization and location?

I am Indian by nationality, currently US-based on STEM OPT through 2027, H-1B eligible. If Sarvam is hard-Bengaluru on-site for this seat, I would relocate to India for the right role. If there is any remote-from-US flexibility for the first 6 to 12 months while the seat ramps, I would love to discuss. Either way, I would rather raise this in screen one than miss the role over it.

## How did you hear about this role?

Found through the Sarvam careers page directly. Sovereign-AI work is what I have been watching closely; the seat surfaced naturally.

## Anything else you want us to know?

Three proof links if you want to see the work:

- SALL live: https://ai-sales-assistant-frontend.onrender.com/
- SALL walkthrough: https://www.youtube.com/watch?v=eCkP7_ZI348
- Portfolio: https://shivamsportfolio.webflow.io/

Happy to walk through Maya AI's routing layer in code, or share a one-page funnel-and-SLO framework for whatever Sarvam product area the seat lands in.
