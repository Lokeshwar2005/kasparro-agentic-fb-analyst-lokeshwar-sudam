# 📊 Kasparro Agentic Facebook Performance Analyst: Lokeshwar Sudam

This project implements a multi-agent system to autonomously diagnose Facebook Ads performance (ROAS fluctuation) and propose data-backed creative improvements. It uses a **Planner-Evaluator loop** to ensure quantitative validation of all hypotheses[cite: 17].

---

## 🛠️ Quick Start

### 1. Setup Environment

```bash
# Clone the repository
git clone https://github.com/Lokeshwar2005/kasparro-agentic-fb-analyst-lokeshwar-sudam.git
cd kasparro-agentic-fb-analyst-lokeshwar-sudam

# Setup environment using the Makefile
make setup
```

### 2. Configure API Key

Ensure your OpenAI API key is set as an environment variable (required by the agents):
```bash
export OPENAI_API_KEY='your-api-key-here'
```

### 3. Run the Analysis

Execute the main orchestration script with the exact CLI command used for evaluation:

```bash
# Exact CLI command for evaluation
python run.py 'Analyze the 20% ROAS drop observed in the last 7 days and propose new messaging for campaigns below 0.8% CTR.'
```
The output files will be saved in the `reports/` and `logs/` directories.

---

## 🏛️ Agent Architecture Diagram

The system's core architecture enforces a rigorous, multi-step process for generating and validating insights.

| Agent | Role | Input | Output |
| :--- | :--- | :--- | :--- |
| **Planner Agent** | Decomposes the user query into sequenced tasks. [cite: 14] | User Query | Structured Task Sequence (JSON) |
| **Data Agent** | Loads and processes the synthetic data. | Task Sequence, Full DataFrame | Targeted Data Summaries (Markdown/Text) |
| **Insight Agent** | Generates preliminary explanations (hypotheses). | Data Summaries | `insights.json` (unvalidated hypotheses) |
| **Evaluator Agent** | **Validates hypotheses quantitatively.** [cite: 17] | `insights.json`, Data Slices | `insights.json` (validated with confidence scores) |
| **Creative Improvement Generator** | Proposes new messaging grounded in data. | Validated `insights.json`, Low-CTR Data | `creatives.json` (Structured Ideas) |

