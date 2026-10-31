# 🤖 Agentic AI Assistant

An AI-powered assistant built using **Python, LangChain, Groq, and Streamlit**. It uses external tools to answer general knowledge questions, search the web, and retrieve current weather information.

## 🚀 Features

- **Groq LLM:** Generates natural-language responses using Groq.
- **Wikipedia Search:** Retrieves educational and general knowledge information.
- **Tavily Search:** Searches the web for relevant information and recent updates.
- **Weatherstack:** Retrieves current weather information for a specified city.
- **LangChain Agent:** Selects and executes tools based on user queries.
- **Streamlit UI:** Provides an interactive chat interface.
- **Environment Variables:** Stores API keys securely using `.env`.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | Agent development and tool integration |
| Groq | Large Language Model (LLM) |
| Streamlit | User interface |
| Tavily | Web search |
| Wikipedia API | Knowledge retrieval |
| Weatherstack API | Weather information |
| Requests | HTTP API requests |
| python-dotenv | Environment variable management |

## 🏗️ Project Architecture

```text
Agentic-AI-Assistant/
│
├── tools/
│   ├── search_tool.py
│   ├── weather_tool.py
│   └── wikipedia_tool.py
│
├── prompts/
│   └── system_prompt.py
│
├── main.py
├── app.py
├── .env
├── .env.example
├── .gitignore
└── requirements.txt
```

### Architecture Overview

1. The user submits a question through the Streamlit interface.
2. The LangChain agent receives the question.
3. Groq processes the request and selects an appropriate tool.
4. The selected tool retrieves information from its external service.
5. Groq generates a response using the available tool results.
6. Streamlit displays the final answer.

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/akhileshr24/Agentic-AI-Assistant.git
```

### 2. Navigate to the project directory

```bash
cd Agentic-AI-Assistant
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows PowerShell:**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root directory.

Add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
WEATHERSTACK_API_KEY=your_weatherstack_api_key
```

**Get API keys:**

- Groq: https://console.groq.com/
- Tavily: https://tavily.com/
- Weatherstack: https://weatherstack.com/

Never upload your `.env` file or expose your API keys publicly.

## ▶️ Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

## 💬 Example Queries

Try asking:

- What is Python list?
- Explain LangGraph.
- What are AI agents?
- Search for the latest AI news.
- What is the current weather in Chennai?

## 🔐 Security

- API keys are stored in environment variables.
- `.env` is excluded using `.gitignore`.
- `.env.example` provides a configuration template.
- Never commit API keys or other sensitive credentials.

## 🔮 Future Improvements

- Improve intelligent tool selection and routing.
- Add tool execution tracing in the Streamlit interface.
- Implement persistent conversation history.
- Improve error handling and input validation.
- Add automated tests.
- Dockerize the application.
- Deploy the application to the cloud.

## 👨‍💻 Author

**Akhilesh R**

GitHub: https://github.com/akhileshr24

---

⭐ If you find this project useful, consider giving the repository a star!

**Project:** [Agentic AI Assistant](https://github.com/akhileshr24/Agentic-AI-Assistant)