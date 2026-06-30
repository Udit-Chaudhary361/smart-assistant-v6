# Smart Assistant V6 🌐🤖🧠

A Personal Assistant built with **Python, Flask, SQLite, and Groq LLM**, extending Smart Assistant V5 by integrating conversational AI with session-based memory while preserving the project's modular architecture.

## Features

* User Management (Set Name, View Name)
* Task Management (CRUD)
* Notes Management (CRUD)
* Task Statistics
* Random Joke Generator
* Logging System
* Command History Tracking
* Persistent Storage using SQLite Database
* Web Interface built with Flask
* AI Chat Assistant powered by Groq
* Session-Based Conversation Memory
* Modular Design using Packages

## What's New in V6

* Integrated Groq LLM using the OpenAI-compatible SDK.
* Added an AI Chat page to interact with the assistant through the browser.
* Introduced session-based conversation memory using Flask Sessions.
* Refactored AI communication into a dedicated `ai.py` module.
* Secured API credentials using `.env` and `python-dotenv`.
* Designed the AI module as a stateless component that only communicates with the LLM.
* Established the foundation for Tool Calling and AI Agent development.

## Tech Stack

* Python
* Flask
* SQLite
* SQL
* HTML
* Jinja Templates
* OpenAI Python SDK
* Groq API
* python-dotenv
* Flask Sessions
* File Handling
* OOP Design

## Project Structure

```text
smart_assistant_v6/
│
├── app/
│   ├── ai.py
│   ├── database.py
│   ├── logger.py
│   └── tools/
│       └── joke_tool.py
│
├── templates/
│   ├── ai.html
│   ├── base.html
│   ├── home.html
│   ├── notes.html
│   ├── tasks.html
│   ├── history.html
│   ├── joke.html
│   ├── name.html
│   └── ...
│
├── static/
│   └── style.css
│
├── data/
│   ├── assistant.db
│   └── History.txt
│
├── app.py
├── requirements.txt
├── .gitignore
├── .env (not committed)
└── README.md
```

> **Note:** The `.env` file stores sensitive configuration such as API keys and is intentionally excluded from GitHub using `.gitignore`.

## Database Tables

### User

Stores assistant user information.

### Notes

Stores user notes.

### Tasks

Stores tasks and their completion status.

## AI Architecture

```text
Browser
    │
    ▼
Flask Route
    │
    ▼
Conversation History (Session)
    │
    ▼
get_ai_response()
    │
    ▼
Groq API
    │
    ▼
AI Response
    │
    ▼
Browser
```

The AI module is intentionally stateless. Flask manages conversation history using browser sessions, while `ai.py` is responsible only for communicating with the LLM.

## Purpose

This project is part of my journey toward building an AI Personal Assistant and Research Agent.

Smart Assistant V6 extends Smart Assistant V5 by introducing Large Language Model (LLM) integration using Groq. The project now supports conversational AI with per-session memory while maintaining a clean, modular architecture. It serves as the foundation for future capabilities such as Tool Calling, Retrieval-Augmented Generation (RAG), and AI Agents.

## Learning Outcomes

* LLM API Integration
* Environment Variables (`.env`)
* OpenAI-Compatible SDK
* Groq API
* Flask Sessions
* Conversation Memory
* Prompt Engineering
* Stateless Module Design
* Separation of Concerns
* Modular AI Integration

## Future Roadmap

```text
Smart Assistant V6
↓
Tool Calling
↓
Embeddings
↓
Vector Databases
↓
RAG
↓
AI Personal Assistant
↓
Research Agent
↓
AI Agent
```

## Author

Built by a B.Tech student learning Software Engineering, AI Systems, AI Engineering, and Agent Development through project-based learning.
