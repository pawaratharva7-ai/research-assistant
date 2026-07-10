## 🔧 TEST UPDATE
# 🧠 Multi-Agent AI Research Assistant

> A production-ready AI system that orchestrates 4 specialised agents to automatically research topics and generate structured reports with citations.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.95+-green.svg)
![CrewAI](https://img.shields.io/badge/CrewAI-0.30+-purple.svg)
![LangChain](https://img.shields.io/badge/LangChain-0.3+-orange.svg)

---

## 📌 Project Overview

This project demonstrates a **multi-agent AI system** that accepts a research question, deploys 4 AI agents in sequence, and produces a structured, cited report.

### What It Does
1. ❓ Accepts a **research question** (e.g., "What are the latest developments in AI regulation?")
2. 🤖 Deploys **4 specialised AI agents**:
   - 🔍 **Researcher**: Gathers information from sources
   - 🧠 **Analyst**: Synthesises findings into key themes
   - ✍️ **Writer**: Produces a professional report
   - ✅ **Reviewer**: Validates quality and citations
3. 📄 Generates a **structured report** with executive summary, key findings, and references
4. 🌐 Exposes functionality via a **REST API** (FastAPI)
5. 💾 Stores job status and results in **SQLite**

---

## 🏗️ Architecture
┌─────────────┐ ┌──────────────┐ ┌─────────────────────────────┐
│ User │────▶│ FastAPI │────▶│ Background Task │
│ (POST / │ │ Gateway │ │ (Async job processing) │
│ research) │ │ │ │ │
└─────────────┘ └──────────────┘ └──────────────┬──────────────┘
│
▼
┌─────────────────────────┐
│ CrewAI Orchestrator │
│ │
│ ┌─────────────────────┐│
│ │ Researcher Agent ││
│ │ Analyst Agent ││
│ │ Writer Agent ││
│ │ Reviewer Agent ││
│ └─────────────────────┘│
└──────────┬──────────────┘
│
▼
┌─────────────────────────┐
│ SQLite │
│ (Job store) │
└─────────────────────────┘

text

---

## 🛠️ Tech Stack

| Category | Technology | Purpose |
|----------|------------|---------|
| **Language** | Python 3.11+ | Core programming |
| **Web Framework** | FastAPI | REST API + Swagger docs |
| **Agent Framework** | CrewAI | Multi-agent orchestration |
| **LLM Framework** | LangChain | LLM connectivity |
| **Database** | SQLite | Persistent job storage |
| **Data Validation** | Pydantic | Request/response validation |
| **Containerisation** | Docker | Reproducible deployment |
| **Cloud** | AWS EC2 (optional) | Deployment |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- OpenAI API key (or use mock mode)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/pawaratharva7-ai/research-assistant.git
cd research-assistant

# 2. Create virtual environment
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up API keys
# Create a .env file
echo "OPENAI_API_KEY=your-openai-key-here" > .env

# 5. Run the API server
python -m uvicorn app.main:app --reload
📡 API Endpoints
Endpoint	Method	Description	Example
/research	POST	Submit a research query	{"topic": "AI regulation"}
/research/{id}	GET	Get job status and result	/research/abc-123
/health	GET	Health check	/health
/docs	GET	Swagger UI	/docs
Example Prediction Request
bash
curl -X POST http://localhost:8000/research \
  -H "Content-Type: application/json" \
  -d '{"topic": "What are the latest developments in AI regulation?"}'
Example Response
json
{
  "id": "abc-123",
  "status": "pending",
  "created_at": "2026-07-10T12:00:00"
}
Poll for Results
bash
curl http://localhost:8000/research/abc-123
🤖 Agent Details
Agent	Role	Tools
Researcher	Gathers information from sources	Web search, document retrieval
Analyst	Synthesises findings into themes	None (pure reasoning)
Writer	Produces professional reports	None (generation)
Reviewer	Validates quality and citations	None (fact-checking)
📂 Project Structure
text
research-assistant/
├── app/
│   ├── agents/             # CrewAI agents
│   │   ├── researcher.py
│   │   ├── analyst.py
│   │   ├── writer.py
│   │   ├── reviewer.py
│   │   └── crew.py
│   ├── api/                # FastAPI routes and schemas
│   ├── core/               # Configuration
│   ├── storage/            # SQLite operations
│   └── main.py             # Entry point
├── tests/                  # Unit tests
├── .env.example            # Environment template
├── .gitignore              # Git ignore rules
├── README.md               # This file
└── requirements.txt        # Dependencies
📋 Current Status
Phase	Status	Description
✅ FastAPI	Working	REST API with Swagger
✅ CrewAI Agents	Working	4 agents orchestrated
✅ Async Jobs	Working	Background processing
✅ SQLite Storage	Working	Job persistence
✅ Mock Mode	Working	No LLM calls needed
⬜ Real LLM	In Progress	Needs OpenAI key
🔮 Future Enhancements
Real LLM Integration – Connect to OpenAI/Groq/Ollama

RAG Pipeline – Add ChromaDB for document retrieval

Web Search – Integrate Tavily/SerpAPI

Docker – Containerise the application

AWS Deployment – Deploy with CI/CD

👨‍💻 Author
Atharva Pawar

GitHub: @pawaratharva7-ai

LinkedIn: linkedin.com/in/atharvapawar

🙏 Acknowledgements
FastAPI – Web framework

CrewAI – Agent orchestration

LangChain – LLM framework

SQLite – Lightweight database

📝 License
MIT License – see LICENSE file for details.

text

---
## 🔧 Test Update - Remove this line
