# 🤖 Agentic AI Assistant

An AI-powered assistant built with **Python, LangChain, Groq and Streamlit**. It uses an LLM-powered agent with external tools to answer questions, search the web, retrieve weather information and access Wikipedia knowledge.

The application demonstrates how an AI agent can understand user queries, select appropriate tools and generate context-aware responses.

## ✨ Features

- **Groq LLM Integration:** Uses Groq's `openai/gpt-oss-120b` model for natural-language generation.
- **Intelligent Tool Selection:** LangChain agent dynamically selects tools based on the user's query.
- **Web Search:** Uses Tavily to retrieve relevant web search results and recent information.
- **Wikipedia Search:** Retrieves educational and general knowledge information.
- **Weather Information:** Uses Weatherstack to retrieve current weather information for a specified city.
- **Interactive Chat Interface:** Streamlit provides a simple conversational interface.
- **Conversation History:** Maintains conversation messages during the active Streamlit session.
- **Request Protection:** Includes basic per-session rate limiting and input-length validation.
- **Environment Configuration:** Uses environment variables to protect API credentials.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | Agent development and tool integration |
| Groq | LLM inference |
| GPT-OSS-120B | Language model |
| Streamlit | Frontend and chat interface |
| Tavily | Web search |
| Wikipedia API | Knowledge retrieval |
| Weatherstack | Current weather information |
| Requests | HTTP requests |
| python-dotenv | Environment variable management |

## 🏗️ Architecture

### Project Workflow

```text
                 USER
                  |
                  v
          STREAMLIT CHAT UI
                  |
                  v
           LANGCHAIN AGENT
                  |
                  v
              GROQ LLM
                  |
          Understands Query
                  |
          Selects Appropriate
                 Tool
                  |
       +----------+----------+
       |          |          |
       v          v          v
    Tavily    Wikipedia  Weatherstack
    Search     Search      Weather
       |          |          |
       +----------+----------+
                  |
                  v
          TOOL RESULTS
                  |
                  v
              GROQ LLM
                  |
                  v
          FINAL RESPONSE
                  |
                  v
           STREAMLIT UI
```

### How It Works

1. The user submits a question through the Streamlit chat interface.
2. The LangChain agent receives the conversation.
3. Groq processes the request and determines whether an external tool is needed.
4. The agent selects and executes the appropriate tool.
5. The selected tool retrieves information from its external service.
6. Groq generates a response using the available information.
7. Streamlit displays the final response to the user.

## 📂 Project Structure

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
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites

- Python installed on your system.
- Git installed on your system.
- API keys for the external services used by the application.

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

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the root directory.

Add your API credentials:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
WEATHERSTACK_API_KEY=your_weatherstack_api_key
```

### Get API Keys

| Service | API Key |
|---|---|
| Groq | https://console.groq.com/ |
| Tavily | https://tavily.com/ |
| Weatherstack | https://weatherstack.com/ |

**Security:** Never upload your `.env` file or expose API credentials in your source code.

## ▶️ Run the Application

Start the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will start locally and provide a URL in your terminal.

Open the local URL in your browser to interact with the assistant.

## 💬 Example Queries

Try these questions to explore the application's capabilities.

**General Knowledge**
- What is Python?
- Explain the difference between lists and tuples.
- What are AI agents?

**Web Search**
- Search for the latest developments in Agentic AI.
- Find recent updates about artificial intelligence.

**Wikipedia**
- Explain the history of artificial intelligence.
- Who invented the Python programming language?

**Weather**
- What is the current weather in Chennai?
- Get the weather information for London.

## 🔐 Security and API Usage Protection

The application includes basic safeguards to reduce unnecessary API usage.

| Protection | Configuration |
|---|---|
| Input validation | Maximum 4,000 characters |
| Session rate limiting | Maximum 5 requests per 60 seconds |
| LLM output limit | Maximum 512 tokens |
| API credentials | Environment variables |
| Error handling | Friendly handling of rate-limit errors |

**Important:** The current rate limiter is session-based. It is intended as basic protection for a portfolio demonstration, not as a global rate limiter or strong authentication system. Multiple sessions can bypass this limit.

Groq API usage is subject to the rate limits of your Groq account. All visitors share the application's configured API credentials and associated quota.

## ☁️ Deployment on Render

The application can be deployed as a Render Web Service.

### Deployment Configuration

| Setting | Value |
|---|---|
| Platform | Render |
| Service Type | Web Service |
| Runtime | Python |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `streamlit run app.py --server.port $PORT --server.address 0.0.0.0` |

### Environment Variables

Configure the following variables in the Render dashboard:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
WEATHERSTACK_API_KEY=your_weatherstack_api_key
```

Do not commit API credentials to GitHub.

**Note:** Render deployment requires compatible dependencies and sufficient memory for the application's runtime. Test the application after deployment and review its service logs.

## 🔮 Future Improvements

- Improve intelligent tool selection and routing.
- Add tool execution tracing.
- Implement persistent conversation history.
- Improve global request limiting.
- Enhance error handling and input validation.
- Add automated tests.
- Improve the Streamlit user interface.
- Dockerize the application.
- Add more useful tools and capabilities.

## 👨‍💻 Author

**Akhilesh R**

- GitHub: https://github.com/akhileshr24
- Project Repository: https://github.com/akhileshr24/Agentic-AI-Assistant

---

⭐ If you find this project useful, consider giving the repository a star!

**Built with Python, LangChain, Groq and Streamlit.**
