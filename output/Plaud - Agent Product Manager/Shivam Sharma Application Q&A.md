# Application Q&A: Plaud Agent Product Manager

Pre-filled answers for the application form and likely screen-1 questions. Same human-tone rules as the resume (no em-dashes, no AI tells, plain English, concrete examples). Update freely as the conversation evolves.

---

## Why Plaud?

Plaud is the rare AI company where the product reality is ahead of the hype. $250M ARR, bootstrapped, profitable, 1.5M+ devices, 170+ countries, all in three years. That is a builder's company. The Agent PM seat sits at the most consequential layer: the tooling ecosystem that turns Plaud's intelligence into things users can do.

I have been shipping the customer-side version of this work at ESC. Maya AI's agent ecosystem (intent classification, multi-channel routing, confidence-based handoff, supervisor cockpit) is the local-scale version of what Plaud is building. Moving from one customer to a global platform is the natural next step.

---

## Why this role?

Three lines from the JD line up:

1. **Architect the Plaud Agent Tooling Ecosystem.** I have done this for Maya AI from 0-to-1 to live at NEP, then rolling out to Moreno Valley and Delta. Same product muscle.
2. **Define "Ground Truth" for User Scenarios.** Maya AI's eval framework (confidence + sentiment + takeover frequency as SLOs) is the Ground Truth surface for utility supervisor scenarios.
3. **Push Prompt Performance to SOTA Standards.** Daily Bedrock prompt design across Opus, Sonnet, Nova. SALL's 8-factor scoring algorithm with two-phase pre-filter cut API costs by 70% on the same model class.

---

## Why are you leaving your current role?

Scope and stage. ESC has been a great place to build Maya AI, but my next role should put me inside a team where the work I have been shipping for one customer at a time becomes the product at platform scale.

---

## Compensation expectations?

Open to the posted range. My priority is total package and equity context given the stage and the scope. If we are aligned on the work, we can find a structure.

---

## Tell me about a time you took ownership and delivered results.

Maya AI is the cleanest example. ESC had no AI track when I joined. The CRO wanted Oracle CCS to be smarter, faster, and multi-channel. There was no design doc, no eval framework, no team.

I started with two weeks of customer discovery at NEP. Sat with supervisors. Watched them dig through Oracle CCS to answer a single resident question. Mapped the workflow. Found the failure points: language barriers, response time, manual data entry, no escalation path.

I wrote a one-page product narrative. Picked the stack: AWS Bedrock for model routing, n8n for workflow orchestration, FastAPI for the integration layer, React for the supervisor cockpit, Microsoft Teams adaptive cards for human approval, 11 Labs for 26-language voice.

I built it on Claude Code, end-to-end, in 2.5 months. Single AI hire. Maya AI is live at NEP with 200K+ residents, rolling out at Moreno Valley Electrical, piloting at Delta Utilities. It handles 70 to 80% of first-touch support autonomously and removes 100+ manager emails per day. Projected savings at NEP are around $225K per month.

Founder mode is how I worked then. It is how I work now.

---

## What AI tools are you currently using today and how are you using them?

- **Claude Code:** my daily driver. Maya AI's supervisor cockpit, email-triage agent, React console, and FastAPI handlers all started as Claude Code sessions before any code shipped. PRDs are usually Claude conversations first, written documents second.
- **AWS Bedrock:** production routing layer for Maya AI. I route across Claude Opus (hard agent-of-record decisions), Claude Sonnet (default conversational tier), and Nova (cheap classifier-style intent extraction). Confidence distributions and cost-per-call drive the routing.
- **n8n:** orchestrator for three production agentic workflows. Conference Outreach (AI drafts, Teams approval cards, Outlook auto-send), Maya AI's email-triage routing, and the supervisor approval flow with adaptive cards.
- **11 Labs:** voice surface for Maya AI's 26-language coverage.
- **Claude (web app), ChatGPT, Perplexity:** mixed deliberately for thinking work. Claude for brainstorming, ChatGPT for second-opinion checks, Perplexity for fact-finding with citations.
- **Cursor and GitHub Copilot:** in-editor pair-programming inside long-lived codebases.

What changed when I started shipping with these tools daily: I went from waiting on engineering capacity to shipping most product ideas in hours instead of weeks. The 2.5-month Maya AI build is the proof.

---

## What is your biggest accomplishment?

**Career-wise:** Bootstrapping and selling CloudApproach + Approachables for $575K combined. Two ventures across UK and MENA, 200+ agency clients, 80+ real-estate partners, $5M+ in deals influenced, 95% client retention post-acquisition. Two exits before I turned 25.

**Last six months:** Maya AI live at NEP with 200K+ residents in 2.5 months as the sole AI on staff. The team had never shipped AI before. They have shipped it now.

---

## Are you authorized to work in the United States?

I am on STEM OPT (F-1 visa) through 2027 and am H-1B eligible. Happy to walk through the timeline in our first conversation.

---

## When can you start?

Immediately. Two-week handoff at ESC for the Maya AI roadmap and supervisor cockpit. Day-one work in parallel.

---

## Open to relocation?

Yes. Open to San Francisco within 30 days of offer.

---

## Anything else you want us to know?

Three proof links if you want to see the work:

- SALL live: https://ai-sales-assistant-frontend.onrender.com/
- SALL walkthrough: https://www.youtube.com/watch?v=eCkP7_ZI348
- Portfolio: https://shivamsportfolio.webflow.io/

Happy to walk through a code-level Maya AI dive at any point in the loop.
