# Enterprise Business Automation & Pipeline Architecture Suite

An enterprise-grade collection of event-driven automation engines designed to protect executive focus, streamline internal operational pipelines, and automate market intelligence.

---

## Technical Architecture Overview

This repository demonstrates advanced asynchronous workflows, modular micro-workflow patterns, and structured data serialization across three functional domains:

1. **[Project 1: The Executive "Deep Work" Inbox Triage & CRM Engine](./project-1-crm-triage/)**  
   *Event-driven intent classification, interactive human-in-the-loop Slack UI states, and pipeline automation.*
2. **[Project 2: The Autonomous Meeting Intelligence & Task Dispatcher](./project-2-meeting-intelligence/)**  
   *Decoupled Parent-Child sub-workflow scaling, native JavaScript/Node.js ingestion CLI, and relational database provisioning.*
3. **[Project 3: Automated Competitor Intelligence & Marketing Pipeline](./project-3-competitor-intelligence/)**  
   *Scheduled web scraping arrays, heuristic content triage, programmatic campaign scheduling, and structured media asset staging.*

---

## Key Engineering Methodologies Demonstrated

* **Decoupled Workflow Topologies:** Implementing Parent-Child sub-workflow splits to isolate data streams and optimize memory footprints during array processing.
* **Deterministic Structured Extraction:** Constraining unstructured LLM outputs to rigid JSON schemas without conversational or markdown noise.
* **Interactive Webhook States:** Leveraging asynchronous block-kit payloads to introduce low-latency user validation steps into fully automated loops.

---

## Repository Structure

```text
├── project-1-crm-triage/
│   ├── README.md                 # Project 1 Documentation
│   └── workflows/
│       └── crm_triage_engine.json # Exported n8n workflow JSON
├── project-2-meeting-intelligence/
│   ├── README.md                 # Project 2 Documentation
│   ├── scripts/
│   │   └── ingest_meeting.py     # Standalone Python ingestion CLI
│   └── workflows/
│       ├── parent_ingest.json     # Main orchestration canvas JSON
│       └── child_task_loop.json   # High-throughput processing loop
└── project-3-competitor-intelligence/
    ├── README.md                 # Project 3 Documentation
    └── blueprints/
        └── campaign_dispatcher.json # Exported Make blueprint
        └── competitor_intel.json # Exported Make blueprint

```

License
MIT License. See project subdirectories for specific installation and configuration prerequisites.