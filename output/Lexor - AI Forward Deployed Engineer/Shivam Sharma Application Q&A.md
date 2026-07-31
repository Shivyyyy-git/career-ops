# Application Q&A - Lexor, AI Forward Deployed Engineer

Pre-drafted answers for the application form and screening calls. Tone: confident, specific, honest.

---

## Are you a US citizen? (required)

No. I'm work-authorized in the US today on F-1 STEM OPT and I'm H-1B eligible. I understand that routes me to the civilian agency team rather than the top-secret team, and I'm open to the O-1 path if the profile fit is there. I'd rather settle this in the first conversation than the last one.

## Are you willing to relocate to Washington, DC and be in-person 5 days/week? (required)

Yes to both. I'm in Rochester, NY today and can relocate as soon as needed. In-person is my preferred way to work; the fastest system I've shipped was built sitting next to the people who used it.

## Why are you looking to leave your current role? (required)

I took my current role for the scope, and it delivered: as the first AI hire I architected and shipped Maya AI, a production agent handling 70 to 80% of first-touch volume for a 200K-resident utility, in 2.5 months. What I want next is a mission where the stakes match that pace. Recovering misspent public money at the scale Lexor is going after is that mission, and a first-cohort seat at a seed company is the right amount of ownership.

## Why Lexor?

Two reasons, one personal and one structural.

The personal one: the most satisfying project I've done was building a fraud-detection model for the City of Rochester. XGBoost with SHAP attribution, accuracy from 62% to 73%, but the real product was the reason codes; loan officers could defend every flag in review. Lexor's thesis, that auditors need an evidence chain and not just a score, is the same lesson at a thousand times the scale. Medicare and Medicaid fraud is a $500 billion problem, and the government is finally buying product-led answers to it.

The structural one: Lexor needs forward deployed engineers who can build agentic systems and sit across from non-technical government stakeholders without a translator. That's my exact shape. I build tool-calling agents, RAG pipelines, and human-in-the-loop autonomy in production, and I spent five years as a founder being the person clients call when it breaks.

## Tell us about a relevant project or achievement

Maya AI. A production agent on Oracle CCS that unifies voice, chat, SMS, email, and mobile for a utility serving 200K+ residents. Intent classification routes each request to tool calls that execute billing, payment plans, start/stop service, and outage transactions autonomously. Low-confidence cases go to supervisors as Microsoft Teams approval cards, and a live console tracks sentiment, scores response confidence, and hands control to a human in one click. Python and FastAPI on AWS Bedrock with model routing across Claude Opus, Sonnet, and Nova; DynamoDB for conversation state and tenant governance. I shipped it in 2.5 months as the only AI person at the company, and it now handles 70 to 80% of first-touch volume.

## What makes you a good fit for this position?

The role sits at the intersection of agentic engineering and partner-facing delivery, and I've done both for real. The engineering: production tool-calling agents, RAG over pgvector, eval and confidence scoring, air-gapped deployment inside a customer VPC. The delivery: I embedded with utility supervisors to ship Maya AI, and before that I ran two bootstrapped companies where I was sales, delivery, and support in one person. I've also done government fraud detection specifically, which I know is a rare card in this deck.

## What are your compensation expectations?

The posted band of $150K to $250K plus equity works for me. Within it, I care more about the equity slice and the scope than about maxing base; this is a first-cohort seat at a seed company and I want to be paid like an owner.

## When can you start?

Fast. I'd need to wrap up responsibly at ESC, realistically two to three weeks, and I can begin relocation planning immediately. ASAP works.

## Are you authorized to work in the US?

Yes. F-1 STEM OPT, active today, with H-1B eligibility. One practical note for your ops team: the STEM OPT extension requires the employer to be enrolled in E-Verify, which is free and fast to set up if Lexor isn't already.

## Do you have experience with fine-tuning or reinforcement learning?

Straight answer: my track record is in agentic systems, RAG, evals, and production deployment, not in fine-tuning or RL pipelines. I run model evaluation and confidence scoring in production today, so the eval half is real. Fine-tuning is a ramp area, and I ramp fast; I went from zero Oracle CCS knowledge to a live production agent in 2.5 months.
