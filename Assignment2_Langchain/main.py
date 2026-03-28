import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper

load_dotenv()

# 1. LLM (Groq)
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# 2. Tools
search = DuckDuckGoSearchRun()
wiki = WikipediaAPIWrapper()

# 3. Input
topic = input("Enter topic: ")

# 4. Get data from tools
web_data = search.run(topic)
wiki_data = wiki.run(topic)

# 5. Combine everything into prompt
final_prompt = f"""
You are an AI Research Assistant.

Topic: {topic}

Web Data:
{web_data}

Wikipedia Data:
{wiki_data}

Generate a structured report with:
- Cover Page
- Title
- Introduction
- Key Findings
- Challenges
- Future Scope
- Conclusion
"""

# 6. Generate report
response = llm.invoke(final_prompt)

print("\n===== FINAL REPORT =====\n")
print(response.content)

import datetime

# Create a clean filename
safe_topic = topic.replace(" ", "_")
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"{safe_topic}_{timestamp}.txt"

# Save to file
with open(filename, "w", encoding="utf-8") as file:
    file.write("Topic: " + topic + "\n\n")
    file.write(response.content)

print(f"\n✅ File saved successfully: {filename}")