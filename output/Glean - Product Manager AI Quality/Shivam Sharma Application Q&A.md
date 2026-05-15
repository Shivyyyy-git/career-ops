# Application Q&A: Glean, Product Manager, AI Quality

Pre-filled answers for the Glean application form and likely screen-1 questions. Same human-tone rules as the resume (no em-dashes, no AI tells, plain English, concrete examples). Update freely as the conversation evolves.

---

## Why Glean?

Glean is the rare AI company where the platform thesis and the product reality have actually caught up to each other. $200M ARR, Series F at $7.2B, 1,000+ employees, 50+ industries. The Work AI category exists because Glean shipped it. That is the kind of velocity I want to be inside.

Model Hub specifically is the bet I have already been making one customer at a time. At ESC I built Maya AI's routing layer across Claude Opus, Sonnet, and Nova on AWS Bedrock for a 200K-resident utility. Picking the right model for the right query, watching confidence, surfacing cost, giving operators a one-click takeover. The platform version of that is exactly Model Hub. Doing it for thousands of enterprises instead of one is the natural next step.

The leadership stack matters too. Arvind shipped Search at Google for a decade. Tamar ran the same surface plus Slack's CPO seat. Emrecan came up at Stripe, LinkedIn, and Amazon. That is product gravity I want to learn from.

---

## Why this role?

Five things from the JD line up exactly with how I already work:

1. **"Evaluate LLM models, define roadmap for growing LLM portfolio."** Maya AI evaluates Bedrock model selection daily for intent and response routing. I have built the evaluation framework, the routing logic, and the cost-tracking dashboard.
2. **"Manage relationships with inference and model providers."** Direct working experience with AWS Bedrock and 11 Labs in production. I have not led a contract, but I have shipped the integration layer that the contract governs.
3. **"Own projections of LLM usage, cost, and capacity planning."** Two-phase pre-filter at SALL cut API costs by 70%. Maya AI tracks cost-per-call and projected savings (~$225K/month at NEP).
4. **"Drive customer enablement and upgrade adoption journey for latest LLMs."** ESC: supervisor cockpit onboarding for non-technical operators. Rolling Maya AI from NEP to Moreno Valley to Delta is the same upgrade-adoption motion.
5. **"Build processes that scale through rapid growth."** ESC: first AI hire, built backlog, eval framework, UAT process, supervisor onboarding flow from scratch. CloudApproach: ran two ventures simultaneously, sales-delivery-hiring-ops process from zero.

The AI Quality framing is also the right one for me. Simon Vision Consulting on the City of Rochester fraud-detection engagement was about lifting accuracy from 62% to 73% with XGBoost + SHAP, and making the model's decisions auditable. Quality metrics and explainability were the deliverable, not the by-product.

---

## Tell me about a time you took ownership and delivered results.

Maya AI is the cleanest example. ESC had no AI track when I joined. The CRO wanted Oracle CCS to be smarter, faster, and multi-channel. There was no design doc, no eval framework, no team.

I started with two weeks of customer discovery at NEP. Sat with supervisors. Watched them dig through Oracle CCS to answer a single resident question. Mapped the workflow. Found the failure points: language barriers, response time, manual data entry, no escalation path.

I wrote a one-page product narrative. Picked the stack: AWS Bedrock for model routing, n8n for workflow orchestration, FastAPI for the integration layer, React for the supervisor cockpit, Microsoft Teams adaptive cards for human approval, 11 Labs for 26-language voice.

I built it on Claude Code, end-to-end, in 2.5 months. Single AI hire. Maya AI is live at NEP with 200K+ residents, rolling out at Moreno Valley Electrical, piloting at Delta Utilities. It handles 70 to 80% of first-touch support autonomously and removes 100+ manager emails per day. Projected savings at NEP are around $225K per month.

Founder mode is how I worked then. It is how I work now.

---

## How do you think about building with LLMs at scale?

Three opinions from shipping Maya AI:

**Confidence is the first-class signal.** Every Maya call returns a confidence score. Below threshold, the agent does not act. It drafts and routes to a supervisor via Teams. We track confidence distributions per intent, per channel, per model. That is how we know whether to invest in prompt engineering, retraining, or a different model.

**Cost is a product decision, not an engineering one.** SALL's two-phase pre-filter cut API costs by 70% by running a cheap classifier first. At Maya AI, we route easier queries to Nova and reserve Opus for the hard ones. Picking the model is a product call because it shapes the user experience.

**Upgrade adoption is a UX problem.** When Bedrock launched a new Claude model, we did not flip a switch. We A/B'd it on a shadow channel for two weeks, watched the takeover-frequency metric for regressions, then rolled it out by channel. Customer enablement is sequencing, not communication.

---

## How do you use AI in your own product craft?

I prototype on Claude Code daily. The supervisor cockpit at ESC, the email-triage agent, and the React console all started as Claude Code sessions before any code shipped. The 8-factor scoring algorithm at SALL was sketched in Markdown specs, prompted into Claude, then refined. My PRDs are usually conversations with a model first, written documents second.

If you want a code-level demo, I'm happy to walk through Maya AI's routing layer or share a Loom of one of the n8n workflows.

---

## What AI tools are you currently using today and how are you using them?

- **Claude Code:** my daily driver. Maya AI's supervisor cockpit, email-triage agent, React console, and FastAPI handlers all started as Claude Code sessions before any code shipped. PRDs are usually Claude conversations first, written documents second. The 8-factor scoring algorithm at SALL was sketched in Markdown, prompted into Claude, then refined into production code over a weekend.
- **AWS Bedrock:** production routing layer for Maya AI. I route across Claude Opus (hard agent-of-record decisions), Claude Sonnet (default conversational tier), and Nova (cheap classifier-style intent extraction). Confidence distributions and cost-per-call drive the routing. This is exactly the work the Model Hub PM seat would do at platform scale.
- **n8n:** orchestrator for three production agentic workflows. Conference Outreach (AI drafts, Microsoft Teams approval cards, Outlook auto-send), Maya AI's email-triage routing, and the supervisor approval flow with adaptive cards. Lets me give non-technical operators a clear surface to see, edit, and pause every agent action.
- **11 Labs:** voice surface for Maya AI's 26-language coverage. Non-English speakers call the utility and reach an agent who answers in their first language without translation friction.
- **Claude (web app), ChatGPT, Perplexity:** mixed deliberately for thinking work. Claude for product brainstorming and writing, ChatGPT for second-opinion checks, Perplexity for fact-finding with citations. Same routing logic as Maya AI, applied to my own product craft.
- **Cursor and GitHub Copilot:** in-editor pair-programming when I am working inside a long-lived codebase rather than sketching from scratch.

What changed when I started shipping with these tools daily: I went from waiting on engineering capacity to shipping most product ideas in hours instead of weeks. The 2.5-month Maya AI build is the proof. I do not think a PM can lead AI product anymore without operating these tools at the production layer.

---

## What is your biggest accomplishment?

**Career-wise:** Bootstrapping and selling CloudApproach + Approachables for $575K combined. Two ventures across UK and MENA, 200+ agency clients, 80+ real-estate partners, $5M+ in deals influenced, 95% client retention post-acquisition. Two exits before I turned 25.

**Last six months:** Maya AI live at NEP with 200K+ residents in 2.5 months as the sole AI on staff. The team had never shipped AI before. They have shipped it now.

---

## Why are you leaving your current role?

Scope and stage. ESC has been a great place to build Maya AI, but my next role should put me inside a Work AI platform where the LLM strategy I have been shipping one customer at a time becomes the product. Glean is the team for that.

---

## Compensation expectations?

The posted range ($160K to $240K base + equity + benefits) is in line with what I am looking for. I would target the upper end given the substance match with Model Hub and the Series F context. Open to discussing structure once we are aligned on scope.

---

## When can you start?

Immediately. I would give ESC two weeks for a clean handoff on Maya AI's roadmap and supervisor cockpit, and start day-one work in parallel.

---

## Are you authorized to work in the United States?

I am on STEM OPT (F-1 visa) through 2027 and am H-1B eligible. Glean's scale (1,000+ employees, 25+ countries) suggests an established sponsorship program. Happy to walk through timing in our first conversation.

---

## How did you hear about this role?

Found through LinkedIn. Glean is one of the few enterprise-AI companies whose JD reads like the job I already do, so I applied same day.

---

## Open to relocation?

Yes. Open to San Francisco within 30 days of offer. Comfortable with hybrid 3 to 4 days in office.

---

## Anything else you want us to know?

Three proof links if you want to see the work:

- SALL live: https://ai-sales-assistant-frontend.onrender.com/
- SALL walkthrough: https://www.youtube.com/watch?v=eCkP7_ZI348
- Portfolio: https://shivamsportfolio.webflow.io/

Happy to walk through a code-level Maya AI dive at any point in the loop, especially the routing-and-confidence layer that maps cleanly to Model Hub.
