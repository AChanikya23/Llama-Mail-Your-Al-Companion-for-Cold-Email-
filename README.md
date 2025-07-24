# Llama-Mail-Your-Al-Companion-for-Cold-Email
Generate highly personalized cold emails for job applications using AI and your portfolio—integrated in a simple, intuitive web app.

🚀 Overview
This Streamlit web application automates the process of composing custom cold emails for job opportunities. The app scrapes job posting data from a URL, leverages cutting-edge AI models (Groq + LangChain), and dynamically incorporates portfolio examples to tailor each email for maximum impact.

✨ Features
Instant Job Data Extraction: Scrape job roles, experience, and required skills directly from any job posting URL.
AI-Powered Email Generation: Generate context-aware, persuasive cold emails using state-of-the-art LLMs.
Portfolio Integration: Highlight your relevant, real-world project portfolio in every outreach.
Modern, Responsive UI: Sleek Streamlit interface with real-time feedback and download options.
Easy Model Selection: Choose from multiple LLMs for optimal performance.
One-Click Email Downloads: Save generated emails with a single click.
🛠️ Tech Stack

Area	Tools / Libraries
Web App	Streamlit
Data Handling	Pandas
AI/LLMs	Groq, LangChain
Portfolio Management	CSV Integration
Database	ChromaDB
Utility	uuid (Python standard library)
See the requirements.txt for all dependencies.

📦 Getting Started
Prerequisites
Python 3.8+
Your own Groq API Key (add appropriately in the script)
Installation
Clone the repository:

git clone https://github.com/<your-username>/cold-email-generator.git
cd cold-email-generator
Install dependencies:

pip install -r requirements.txt
Configure Portfolio:

Update or replace my_portfolio.csv with your technology stacks and links (see sample below).
Run the app:

streamlit run app.py
💾 Portfolio Reference
Your portfolio is pulled directly from my_portfolio.csv. Example entries:


Tech Stack	Portfolio Link
React, Node.js, MongoDB	View
Angular, .NET, SQL Server	View
Python, Django, MySQL	View
Java, Spring Boot, Oracle	View
Flutter, Firebase, GraphQL	View
...	...
Edit or extend your CSV for new technologies and projects you want referenced in emails.

🖥️ Usage Guide
Paste a job posting URL into the main input.
Select your preferred AI model (Groq LLM family supported).
Click "Generate Cold Email":
See extracted job details and the generated, customized cold email.
Download instantly for your application process.
⚙️ Customization
To modify the sender details, portfolio links, or company intro, edit the relevant sections in app.py or update the portfolio CSV.
The email is sent as if from Mohan, Business Development Executive at AtliQ; adjust as needed to personalize for your own identity or organization.
📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

🙏 Attribution
Built with Streamlit
AI powered by Groq & LangChain
Craft your outreach—let AI and your portfolio do the work!
