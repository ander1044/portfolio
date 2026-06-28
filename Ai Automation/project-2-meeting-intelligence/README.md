# Project 2: The Autonomous Meeting Intelligence & Task Dispatcher

## Objective
An operational data ingestion pipeline that transforms raw conversational meeting transcripts into structured company documentation, indexes project management items, and alerts internal execution teams asynchronously.

## Flow Architecture


```
[Python CLI Script] ➔ POST JSON ➔ [n8n Webhook] ➔ [LLM Extraction] ➔ [Notion Doc Creator]
                                                                        └──> Loop ➔ [ClickUp Task Creator]
```

## Functional Breakdown
* **Client-Side Ingestion CLI:** Includes a native Node.js automation script (`/scripts/ingest_meeting.py`) that safely opens local project transcript data using the file system module (`fs`) and targets the production pipeline via asynchronous runtime `fetch` requests.
* **Decoupled Handoff Pattern:** To prevent execution hangs and canvas UI performance locking, the loop architecture is split across a Parent and Child relationship. The parent dumps raw summaries to Notion, while the child sub-workflow processes the multi-item deliverable array independently.
* **Granular Deliverable Provisioning:** The child node reads the formatted JSON array properties (`task_name`, `assignee`, `due_date`) to build decoupled execution items inside ClickUp automatically.

## Deployment Steps
1. Deploy the background consumer loop: Import `/workflows/child_task_loop.json` into a fresh n8n canvas and note its unique system workflow string.
2. Link the core orchestration engine: Import `/workflows/parent_ingest.json` on a secondary canvas and paste the child string into the `Execute Workflow` properties module.
3. Configure your local runtime profile and pass payloads into the pipeline:
   ```bash
   python3 scripts/ingest_meeting.py
   ```