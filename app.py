
import streamlit as st

from main import build_agent


# Page configuration
st.set_page_config(
    page_title="Agentic AI Assistant",
    page_icon="🤖",
    layout="centered",
)

st.title("🤖 Agentic AI Assistant")
st.caption("Powered by Groq, LangChain and custom tools")


# Create agent only once
@st.cache_resource
def get_agent():
    return build_agent()


agent = get_agent()


# Initialize conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
question = st.chat_input("Ask me anything...")

if question:

    # Display user question
    st.session_state.messages.append({
        "role": "user",
        "content": question,
    })

    with st.chat_message("user"):
        st.markdown(question)

    # Generate AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):

            try:
                response = agent.invoke({
                    "messages": st.session_state.messages
                })

                answer = response["messages"][-1].content

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                })

            except Exception as error:
                st.error(f"Something went wrong: {error}")
