# AI Research Copilot

AI Research Copilot is a multi-agent AI system that autonomously researches technical topics by retrieving academic papers from arXiv, analyzing research findings, generating structured reports, and evaluating report quality using large language models.

The system demonstrates how multiple AI agents can collaborate to perform complex research workflows automatically.

---

## Features

• Autonomous research pipeline powered by multiple AI agents
• Retrieves relevant academic papers from arXiv
• Generates structured research reports automatically
• Reviews and evaluates report quality using LLM feedback
• Interactive Streamlit interface for research queries
• Modular architecture that supports adding new tools or agents

---

## Architecture

User Query
↓
Research Agent (arXiv Search)
↓
Analysis Agent
↓
Report Writer Agent
↓
Report Reviewer Agent
↓
Quality Evaluation
↓
Streamlit Web Interface

---

## Tech Stack

Python
LangChain
Groq LLM
Streamlit
arXiv API
Multi-Agent Architecture

---

## Project Structure

```
ai-research-copilot
│
├── agents
│   ├── researcher.py
│   ├── analyst.py
│   ├── writer.py
│   └── reviewer.py
│
├── app
│   ├── main.py
│   └── orchestration.py
│
├── evaluation
│   └── quality_check.py
│
├── vector_db
│
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository

```
git clone https://github.com/kannanhora/ai-research-copilot.git
cd ai-research-copilot
```

Create virtual environment

```
python -m venv venv
```

Activate environment

Windows:

```
venv\Scripts\activate
```

Install dependencies

```
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

Example:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## Run the Application

Start the Streamlit server:

```
python -m streamlit run app/main.py
```

Open in browser:

```
http://localhost:8501
```

---

## Example Workflow

1. User enters a research topic
2. System retrieves relevant papers from arXiv
3. AI agents analyze research summaries
4. Report is generated automatically
5. Report quality is reviewed and evaluated

---

## Example Use Cases

• Rapid literature review
• Research topic exploration
• AI-assisted academic summaries
• Technical report generation

---

## Future Improvements

• Add citation extraction
• Export reports as PDF
• Integrate vector databases for RAG
• Add paper recommendation system
• Improve report formatting and visualization

---

