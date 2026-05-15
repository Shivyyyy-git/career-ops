# Application Q&A: Sarvam AI, Product Manager (Models)

Pre-filled answers for the Sarvam application form and likely screen-1 questions. Same human-tone rules as the resume (no em-dashes, no AI tells, plain English, concrete examples). Update freely as the conversation evolves.

---

## Why Sarvam AI?

Sovereign Indian AI is the most important infrastructure bet on the subcontinent for the next decade. Global frontier models treat Indic languages as a long tail (4 to 8 tokens per word vs 1.4 for English), and the only way that gets fixed is by Indians shipping Indic-first foundation models. Sarvam-105B (Indus), the Sarvam Kaze hardware launch, and the NVIDIA / Accel / HCLTech round are the clearest signals that Sarvam is shipping at unicorn velocity, not pitching.

The Model PM seat sits at the layer where the decisions compound. ASR and TTS quality for Tamil, Hindi, Bengali, and Marathi will define whether a billion people get to use AI in their first language or stay locked out. That is a mission worth working at the line level.

---

## Why this role?

Five lines from the JD match how I already work:

1. **Define and drive roadmaps for ASR, TTS, and evaluation systems.** Maya AI runs 26-language voice through 11 Labs in production for a 200K-resident utility. I own the voice-quality roadmap end-to-end on the customer side.
2. **Partner with teams on data collection, training cycles, and model release planning.** ESC: partnered with engineering on Bedrock model selection across Opus, Sonnet, Nova. SALL: 8-factor scoring trained on 5-advisor consultation data.
3. **Set up and own evaluation frameworks and quality metrics.** Maya AI: confidence, sentiment, and takeover frequency tracked as service-level objectives. Simon Vision: XGBoost + SHAP for explainability and quality.
4. **Run structured experiments (offline, A/B, human evaluation).** ESC: rolled new Bedrock models on a shadow channel for two weeks before full deployment. SALL: two-phase pre-filter validated against advisor-recommended communities.
5. **Translate business needs into measurable model goals.** Daily at ESC. Translated NEP supervisor pain into the eval framework Maya AI now uses.

---

## Tell me about a time you owned a model lifecycle end-to-end.

Maya AI is the cleanest example. ESC had no AI track when I joined. The CRO wanted Oracle CCS to be smarter, faster, and multi-channel. There was no design doc, no eval framework, no team.

I started with two weeks of customer discovery at NEP. Sat with supervisors. Watched them dig through Oracle CCS to answer a single resident question. Mapped the workflow. Picked the stack: AWS Bedrock for model routing, n8n for workflow orchestration, FastAPI for the integration layer, React for the supervisor cockpit, Microsoft Teams adaptive cards for human approval, 11 Labs for 26-language voice.

I built it on Claude Code, end-to-end, in 2.5 months. Single AI hire. The eval framework tracks confidence distributions, sentiment shifts, and takeover frequency per intent and per channel. When Bedrock launched a new Claude model, I A/B'd it on a shadow channel for two weeks, watched takeover-frequency for regressions, then rolled by channel.

Maya AI is live at NEP with 200K+ residents, rolling out at Moreno Valley Electrical, piloting at Delta Utilities. It handles 70 to 80% of first-touch support autonomously. Projected savings at NEP are around $225K per month.

Founder mode is how I worked then. It is how I work now.

---

## How do you think about model evaluation for speech systems?

Four opinions:

- **Latency is a quality metric, not an engineering one.** If a supervisor waits 4 seconds for a response, the agent has already failed. Latency budgets sit in the PRD.
- **Confidence has to be a first-class signal.** Maya AI returns a confidence score on every action. Below threshold, the agent does not act. It drafts and routes to human review. We tune thresholds per intent, not globally.
- **WER / CER / MOS are necessary but not sufficient.** They miss conversational context, mid-utterance corrections, and code-switching. For Indic languages with heavy code-switching (Hinglish, Tanglish), human evaluation has to be in the loop.
- **Upgrade adoption is a UX problem.** A better model that surprises an operator is worse than a slightly weaker model the operator trusts. Shadow-channel A/B with takeover-frequency as the regression signal is the right rollout pattern.

---

## What AI tools are you currently using today and how are you using them?

- **Claude Code:** my daily driver. Maya AI's supervisor cockpit, email-triage agent, React console, and FastAPI handlers all started as Claude Code sessions before any code shipped.
- **AWS Bedrock:** production routing layer for Maya AI across Claude Opus (hard agent-of-record), Claude Sonnet (default conversational), Nova (cheap classifier-style intent extraction).
- **n8n:** orchestrator for three production agentic workflows (Conference Outreach, Maya email-triage, supervisor approval).
- **11 Labs:** voice surface for Maya AI's 26-language coverage.
- **Claude (web), ChatGPT, Perplexity:** mixed deliberately for thinking work.
- **Cursor and GitHub Copilot:** in-editor pair-programming inside long-lived codebases.
- **XGBoost + SHAP:** Simon Vision Consulting fraud detection (62% to 73% accuracy lift).

---

## What is your biggest accomplishment?

**Career-wise:** Bootstrapping and selling CloudApproach + Approachables for $575K combined. Two ventures across UK and MENA, 200+ agency clients, 80+ real-estate partners, $5M+ in deals influenced. Two exits before I turned 25.

**Last six months:** Maya AI live at NEP with 200K+ residents in 2.5 months as the sole AI on staff. The team had never shipped AI before. They have shipped it now.

---

## Why are you leaving your current role?

Scope and stage. ESC has been a great place to ship Maya AI, but my next role should put me inside a team where the model work I have been shipping for one customer at a time becomes the product at platform scale.

---

## Compensation expectations?

Open to the Sarvam range. My priority is total package plus equity at unicorn stage given the velocity. Happy to discuss INR or USD denomination depending on the relocation outcome.

---

## When can you start?

Immediately for remote. Two-week handoff at ESC for the Maya AI roadmap and supervisor cockpit. If Bengaluru on-site is required, I can be on the ground within 30 to 45 days of offer (visa logistics permitting).

---

## Work authorization and location?

I am Indian by nationality. Currently US-based on STEM OPT through 2027, H-1B eligible. If Sarvam is hard-Bengaluru on-site for this seat, I would relocate to India for the right role. If there is any remote-from-US flexibility for the first year while the role ramps, I would love to discuss. Either way, the substance match is real and I would rather have the conversation in screen one.

---

## How did you hear about this role?

Found through the Sarvam careers page directly. Sovereign-AI work is what I have been watching closely; this role surfaced naturally.

---

## Open to relocation?

Yes. Open to relocating to Bengaluru for the right role and the right structure. The question is the seat's flexibility on the first 6 to 12 months, not the willingness.

---

## Anything else you want us to know?

Three proof links if you want to see the work:

- SALL live: https://ai-sales-assistant-frontend.onrender.com/
- SALL walkthrough: https://www.youtube.com/watch?v=eCkP7_ZI348
- Portfolio: https://shivamsportfolio.webflow.io/

Happy to walk through Maya AI's routing layer in code, or share a one-page eval framework for Sarvam-105B on Hindi plus Tamil plus Bengali.
