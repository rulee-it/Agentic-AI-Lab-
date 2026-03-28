# Autonomous Research Agent (LangChain)

## 📌 Overview

This project implements an **Autonomous Research Agent** using LangChain that can automatically research a given topic and generate a structured report.

The agent gathers information from multiple sources like web search and Wikipedia, processes the data, and produces a well-organized output.

---

## 🎯 Objective

To build an AI-powered system that:

* Searches information from the web 🌐
* Extracts and analyzes key insights 🧠
* Generates a structured research report 📄

---

## ⚙️ Tech Stack

* Python 🐍
* LangChain
* Groq API (LLM - LLaMA 3.1)
* DuckDuckGo Search Tool
* Wikipedia API

---

## 🧩 Features

* 🔍 Web search integration (real-time data)
* 📚 Wikipedia knowledge extraction
* 🧠 AI-based summarization using LLM
* 📄 Structured report generation
* 💾 Automatic saving of reports as `.txt` files
* ⚠️ Error handling for API failures

---

## 🏗️ Project Structure

```
autonomous-research-agent/
│
├── main.py
├── .env
├── requirements.txt
├── README.md
└── reports/
```

---

## 🚀 How It Works

1. User enters a research topic
2. System fetches data from:

   * Web Search
   * Wikipedia
3. LLM processes and summarizes the data
4. Final structured report is generated
5. Report is saved as a `.txt` file

---

## 📥 Installation

### 1. Clone the repository

```bash
git clone <your-repo-link>
cd autonomous-research-agent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API Key

Create a `.env` file and add:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Run the program:

```bash
python main.py
```

Enter a topic when prompted:

```
Enter topic: AI in Healthcare
```

---

## 📄 Output Format

The generated report includes:

* Cover Page
* Title
* Introduction
* Key Findings
* Challenges
* Future Scope
* Conclusion

---

## 💾 Sample Output Files

Reports are saved automatically in the project folder (or `/reports` directory):

```
AI_in_healthcare_20260328_154210.txt
AI_in_education_20260328_160500.txt
```

---

## 🧠 Key Concepts Used

* LangChain Tools
* LLM Integration (Groq - LLaMA 3.1)
* Prompt Engineering
* Autonomous Agent-like Workflow

---

## ⚠️ Error Handling

* Handles API failures gracefully
* Continues execution even if one data source fails

---

## 📌 Future Improvements

* 🌐 Web-based UI (Streamlit / React)
* 📄 Export reports as PDF
* 🗂️ Store reports in database
* 🔁 Multi-step reasoning agent (ReAct)

---

## 👨‍💻 Author

* Ashmit Naik
* CS-I 
* 2023428345

---

## ⭐ Acknowledgment

This project was built as part of an academic assignment on **Autonomous AI Agents using LangChain**.

---
