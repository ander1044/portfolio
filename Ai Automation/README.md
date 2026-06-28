# Autonomous Business Operations & Pipeline Automation Suite

A collection of enterprise-grade, event-driven automation architectures designed to streamline customer acquisition, operational intelligence, and competitive market research. 

---

## ── PROJECT 1: Executive "Deep Work" Inbox Triage & CRM Engine
**Objective:** Protect executive time by autonomously filtering inbound communication, updating sales pipelines, and staging contextual draft replies.

### System Architecture

'''
[Gmail Trigger] ➔ [Ollama / Local LLM (JSON Schema)] ➔ [Switch Router]
                                                           ├──> Lead ➔ [HubSpot API] ➔ [Slack Block Kit Draft Button]
                                                           └──> Urgent ➔ [Slack Pager/SMS Alert]
'''

### Key Engineering Highlights
* **Intent-Driven Routing:** Implemented zero-shot classification via LLM prompting to route communications with 95%+ accuracy.
* **Interactive Approvals:** Leveraged Slack block kit webhooks to establish a human-in-the-loop validation step before draft transmission.
* **Tech Stack:** n8n, OpenAI API, HubSpot CRM, Slack Block Kit, Gmail API.

👉 [View Project 1 Details & Source Code](./project-1-crm-triage/)

---

## ── PROJECT 2: Autonomous Meeting Intelligence & Task Dispatcher
**Objective:** An operations engine that ingests raw meeting data, parses structured tasks, updates project spaces, and updates company knowledge bases asynchronously.

### System Architecture

'''
[Python CLI Script] ➔ POST JSON ➔ [n8n Webhook] ➔ [LLM Extraction] ➔ [Notion Doc Creator]
                                                                        └──> Loop ➔ [ClickUp Task Creator]
'''

### Key Engineering Highlights
* **Modular Sub-Workflow Design:** Architected a decoupled Parent-Child workflow system to handle variable-length task arrays seamlessly without blocking canvas runtime.
* **Client-Side Trigger Engine:** Built a native JavaScript client utility utilizing the Node.js File System (`fs`) and `fetch` APIs to parse and stream raw transcript payloads locally into cloud endpoints.
* **Tech Stack:** Node.js, n8n, Notion API, ClickUp API, Slack Markdown Engine.

👉 [View Project 2 Details & Source Code](./project-2-meeting-intelligence/)

---

## ── PROJECT 3: Automated Competitor Intelligence & Marketing Pipeline
**Objective:** Automates market positioning monitoring, handles competitor research data ingestion, and staging digital marketing assets.

### System Architecture

'''
[Scheduled Polling / Scraper] ➔ [Airtable Hub] ➔ [Filter: Status Change] ➔ [AI Asset Generator]
                                                                            └──> [Mailchimp Content Pipeline]
'''

### Key Engineering Highlights
* **Competitive Content Aggregation:** Created automated ingestion pipelines that scrape and parse competitor corporate blogs and landing page adjustments.
* **Automated Asset Staging:** Integrated workflows that take raw AI text summaries, write draft newsletter copy segments, and automatically structure asset directories for design handoffs.
* **Tech Stack:** Make (Integromat), Airtable API, Mailchimp API, Google Workspace API.

👉 [View Project 3 Details & Source Code](./project-3-competitor-intelligence/)