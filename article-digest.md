# Proof-Point Bank

Detailed project descriptions for tailored CVs, cover letters, and interview prep. Each entry maps to target role archetypes so the system can pull the right proof points for each application.

---

### Maya AI

**Full AI operating layer on Oracle CCS unifying voice, chat, SMS, email, and mobile for a 200K-resident utility — built in 2.5 months as the sole AI person.**

**Problem:** Utility companies (Nationwide Energy Partners and similar) run everything on Oracle CCS — billing, outages, service requests, payment plans. When a customer calls, chats, or emails, a human agent logs in, digs through Oracle, and manually responds. At 200K+ residents, this doesn't scale. Response times lag, quality varies by agent, and the cost per interaction climbs. Multi-language support is non-existent for a significant non-English speaking customer base.

**Solution:** Built Maya AI end-to-end: an AI operating layer that sits on top of Oracle CCS and handles customer interactions autonomously across all channels. The agent understands customer intent across voice, chat, SMS, email, and mobile; pulls the right data from Oracle; and executes transactions (billing queries, payment plans, start/stop service, outage reporting) without human intervention. When uncertain, Maya drafts a response, pings a supervisor in Microsoft Teams via an adaptive card, and waits for one-click approval before sending. Also shipped a standalone email-triage agent spun off from Maya's core intelligence that routes, drafts, and sends resident support emails using Claude Code. Supervisor cockpit provides real-time sentiment analysis, agent performance tracking, and one-click human takeover. 11 Labs integration delivers 26-language voice coverage.

**Stack:** AWS Bedrock (Claude Sonnet, Claude Opus, Nova Pro), FastAPI, n8n (production workflows for triage + approval flows), React (supervisor cockpit), Microsoft Teams (adaptive cards + webhooks), Microsoft Outlook, Oracle CCS, AWS DynamoDB (tenant governance), 11 Labs voice, 17 admin APIs for enterprise onboarding, 24-hour key rotation, Claude Code.

**Outcome:** Handles 70-80% of first-touch support volume; removes 100+ manual emails per manager per day. Deployed at NEP (200K+ residents); rolling out at Moreno Valley Electrical Utility; piloting at Delta Utilities. Any Oracle Utilities client can plug in. Projected ~$225K/month savings at NEP. HITL approval flow builds trust with non-technical supervisors — they stay in control without touching the underlying system. Built end-to-end in 2.5 months as the sole AI person at ESC Partners.

**Archetypes this supports:** AI Product Builder, Technical AI PM, Agentic PM, AI Platform/LLMOps PM, Forward Deployed Engineer, Vertical/Enterprise AI PM

---

### VaultIQ

**Internal air-gapped financial intelligence platform running Claude Opus on AWS Bedrock — data never leaves the customer VPC.**

**Problem:** Financial analyst teams work with sensitive documents — earnings files, deal memos, client statements — that cannot leave the customer's private network. Off-the-shelf AI tools require sending data to third-party APIs, which is a compliance non-starter for regulated clients. Manual document review doesn't scale as deal volume grows.

**Solution:** Built an internal financial intelligence platform that runs entirely inside the customer VPC. The platform extracts line items from analyst documents, surfaces trends across periods and entities, and generates forward predictions — all powered by Claude Opus hosted on AWS Bedrock inside the customer's AWS account. Data never leaves the VPC. SSO + role-based access ensures the right analysts see the right slices. Deployed via Terraform for reproducible customer installs.

**Stack:** Claude Opus (AWS Bedrock, in-VPC), Next.js (analyst UI), Postgres with pgvector (document retrieval), Terraform (customer VPC deployment), SSO, role-based access control.

**Outcome:** Compliance-grade AI for regulated financial clients without sending data outside their boundary. Replaces manual analyst document review with automated extraction and trend surfacing. Reusable deployment pattern (Terraform-defined) reduces per-customer onboarding time.

**Archetypes this supports:** AI Product Builder, Forward Deployed Engineer, Technical AI PM, AI Platform/LLMOps PM, Vertical/Enterprise AI PM

---

### Conference Outreach System

**3-workflow n8n pipeline automating AI-generated conference outreach with human approval via Teams.**

**Problem:** The CRO needed to reach Oracle CIS conference attendees with personalized outreach but was doing it manually — writing individual emails, tracking who'd been contacted, following up. Slow, inconsistent, and not scalable for conference-sized contact lists.

**Solution:** Designed and built a 3-workflow system. Workflow A generates personalized outreach emails via AI and posts them as Teams approval cards. Workflow B handles approve/skip webhooks — approved emails send automatically via Outlook, skipped contacts get logged. Workflow C provides an edit form so the CRO can revise AI-generated copy before sending. The approval loop ensures every outgoing email has human sign-off while eliminating the drafting bottleneck.

**Stack:** n8n (3 workflows), Microsoft Teams (approval cards + webhooks), Microsoft Outlook, AI-powered email generation.

**Outcome:** Replaced manual per-email drafting with an AI-first workflow where the human role shifts from writing to reviewing. CRO maintains full control over tone and targeting while moving through contact lists at 10x the manual pace.

**Archetypes this supports:** Agentic PM, Technical AI PM

---

### Maya AI Console + Chat Widget

**Real-time conversation monitoring dashboard with live agent takeover capability.**

**Problem:** Once Maya AI was handling customer conversations across email, chat, and voice, there was no way for the operations team to see what was happening in real time. If the AI mishandled a conversation or a customer escalated, no one knew until the complaint came in. The team needed visibility into live AI interactions and the ability to intervene instantly.

**Solution:** Shipped two products: a customer-facing chat widget embedded on the client's site, and an internal Maya AI Console. The console provides a real-time feed of all active AI conversations with status indicators, sentiment signals, and a one-click agent takeover button. When a human takes over, the AI steps back and the conversation continues seamlessly in the same thread. The console also surfaces conversation history, classification decisions, and response confidence scores for post-hoc review.

**Stack:** React (frontend), FastAPI (backend), AWS Bedrock (AI engine), AWS DynamoDB (conversation state and history), deployed on Render.

**Outcome:** Operations team gained real-time visibility into all AI-handled conversations. Agent takeover capability means the AI handles the volume while humans handle the exceptions — without the customer ever noticing a handoff. Confidence scoring enables continuous improvement of the AI's classification and response quality.

**Archetypes this supports:** AI Platform/LLMOps PM, Technical AI PM

---

### Senior Assisted Living Locators

**AI recommendation product matching senior families to care communities in under 2 seconds.**

**Problem:** Five advisors were manually researching 250+ senior living communities for every consultation — checking budget fit, care levels, proximity, amenities, and partner revenue potential. With 300+ consultations per week, the manual process was the bottleneck. Advisors spent more time researching than advising, and recommendation quality varied by who picked up the call.

**Solution:** Built an AI-powered recommendation engine with an 8-factor scoring algorithm combining hard business rules (budget, care level, proximity) with AI-driven analysis (family preference matching, partner revenue optimization). Designed a two-phase architecture: first pass pre-filters by hard constraints to reduce the candidate set, second pass runs the full scoring model. Four input methods — web form, phone intake, real-time voice transcription, and CRM import — feed into the same scoring pipeline. System auto-logs to CRM and runs AI-driven follow-up that identifies missing client requirements before generating final recommendations.

**Stack:** AI scoring engine, real-time voice transcription, CRM integration, automated follow-up pipeline.

**Outcome:** 300+ weekly consultations processed. Matching time cut from minutes of manual research to under 2 seconds. API costs reduced ~70% through two-phase pre-filtering. All 5 advisors on the same recommendation quality baseline. Eliminated manual research entirely — advisors now spend their time advising.

**Archetypes this supports:** Vertical/Enterprise AI PM, Technical AI PM

---

### Vollie

**AI-powered employee coaching platform launched to first client as sole PM, from 0 to working prototype.**

**Problem:** Companies want structured peer coaching — it builds accountability, surfaces blind spots, and improves retention — but it requires trained human facilitators. At $200-500 per session, it doesn't scale past senior leadership. Mid-level employees, who benefit most from coaching, never get it.

**Solution:** Designed and shipped a voice AI moderator that runs structured coaching conversations between employee pairs. The AI facilitates the session — prompts discussion topics, manages turn-taking, ensures both participants engage — and auto-generates post-session reports covering sentiment, engagement levels, and commitments made. Reports go to the participants and optionally to their manager. Built with a privacy-first data model: conversation content stays ephemeral, only structured outputs persist. Owned the entire 0-to-1 journey as sole PM — product strategy, data model design, prototype development, and first client launch (30 employees).

**Stack:** Voice AI, structured conversation engine, automated report generation (sentiment analysis, engagement scoring, commitment tracking).

**Outcome:** Launched to first client with 30 employees. Enabled peer coaching at zero marginal facilitator cost. Privacy-first design was a key selling point for HR stakeholders concerned about recorded conversations.

**Archetypes this supports:** Technical AI PM, Forward Deployed/Solutions PM

---

### CloudApproach + Approachables Exit

**Bootstrapped two ventures from zero, scaled to 200+ clients and $5M+ deals influenced, sold both for $575K.**

**Problem:** Two different market gaps. CloudApproach: SMBs in UK and MENA needed design, web, and marketing services but couldn't afford agency retainers. Approachables: real-estate agencies needed CRM automation and marketing but were buying fragmented point solutions.

**Solution:** Built CloudApproach as a design/web and marketing agency serving 200+ clients across UK and MENA. Built Approachables as a specialized real-estate marketing and CRM automation business serving 80+ agencies. Managed a combined $200K marketing and automation budget. Ran both businesses simultaneously, handling everything from sales and client delivery to hiring and operations. When exit opportunities arose, led acquisition diligence and transition for both — complete records handoff, retention compliance, client communication.

**Stack:** Agency operations, CRM automation, digital marketing, client management at scale.

**Outcome:** $575K in combined exit value ($325K CloudApproach + $250K Approachables). $5M+ in client deals influenced across the portfolio. 95% client retention post-acquisition — buyers kept the entire operation running. Proof that the PM skillset (scoping, prioritizing, shipping, iterating) works outside of tech companies too.

**Archetypes this supports:** AI PM who can think like a founder — understands unit economics, customer acquisition, and when to exit
