Dear Firmwide AI and Technology COO team,

Just applied to the AI Product Manager role. Sending this because the posting describes a problem I have already had to solve at much smaller scale, and because there are two things about my background you should know before a screen rather than after it.

I built the supervisor cockpit for Maya AI because "the agent is live" is not a number anyone can act on. So every conversation started carrying a confidence score, a sentiment reading, and a takeover record, and that instrumentation is what let us say with evidence that 70 to 80% of first-touch volume was being handled autonomously rather than just believing it was. I am the first AI hire at ESC Partners. I built Maya AI end to end in 2.5 months on FastAPI, AWS Bedrock, n8n, React, and Claude Code, and it now runs for a 200K-resident utility with two more in rollout. Governance came first, not last: approvals route through Microsoft Teams adaptive cards so a named person signs off before the agent acts, and DynamoDB tenant governance keeps three utility deployments from ever seeing each other's data.

Measuring one AI agent across 200,000 residents taught me the thing that scales: adoption is the easy number, and the hard ones are how often a human had to take over, how confident the system was when it did not, and what the saved time actually turned into.

That is why DevGen.AI is the Morgan Stanley number I keep coming back to. Roughly 280,000 developer hours saved on nine million lines of legacy code is, as far as I can tell, the one hard GenAI figure the Firm has published, and it is a numerator. Saved hours only become value when capacity is deliberately redeployed. Meanwhile 98% of Financial Advisor teams already use the AI @ Morgan Stanley Assistant, which means the adoption question is largely answered and the harder ones are next: weekly actives against enabled seats, depth cohorts instead of headcount, how often an answer gets overridden. And when SR 26-2 replaced SR 11-7 in April, it put generative and agentic AI outside the scope of model risk guidance while leaving the governance obligation fully intact. Nobody outside the Firm can tell you what good looks like here. It has to be defined internally, by someone, which is exactly the work this posting describes.

Two things I will not pretend about. I have never worked inside an organization of Morgan Stanley's size, and I have not used Tableau or Power BI. What I have done is build the reporting surfaces myself in React over a FastAPI service, define the metrics they display, and defend those definitions to the people being measured by them. I also built VaultIQ, an air-gapped financial intelligence platform running Claude Opus on AWS Bedrock entirely inside the customer's VPC, where SSO and role-based access decide which analysts see which slices. It does not make me a financial services veteran. It does mean I have never had the luxury of designing an AI system first and adding the controls afterward.

Before ESC I bootstrapped and exited two ventures across UK and MENA, $575K combined, 95% post-acquisition retention, on a $200K budget I owned and reported on quarterly. I have been the person accountable for the number, not just the person producing it.

Proof of work:
- SALL live: https://ai-sales-assistant-frontend.onrender.com/
- SALL walkthrough: https://www.youtube.com/watch?v=eCkP7_ZI348
- Portfolio: https://shivamsportfolio.webflow.io/

**Shivam Sharma**
shivamsharma2023@gmail.com | (585) 481-9927 | linkedin.com/in/shivamsharma-ai | shivamsportfolio.webflow.io
