
import time

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

# Initialize request tracking
if "request_timestamps" not in st.session_state:
    st.session_state.request_timestamps = []


# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
question = st.chat_input("Ask me anything...")

if question:

    # Validate message length
    if len(question) > 4000:
        st.warning("Message too long. Maximum 4,000 characters.")

    else:
        # Check requests in the last 60 seconds
        current_time = time.monotonic()

        st.session_state.request_timestamps = [
            timestamp
            for timestamp in st.session_state.request_timestamps
            if current_time - timestamp < 60
        ]

        # Allow maximum 5 requests per session per minute
        if len(st.session_state.request_timestamps) >= 5:
            st.warning(
                "Rate limit reached. Please wait one minute before trying again."
            )

        else:
            # Record accepted request
            st.session_state.request_timestamps.append(current_time)

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
                        error_message = str(error).lower()

                        if (
                            "429" in error_message
                            or "rate_limit" in error_message
                            or "rate limit" in error_message
                        ):
                            st.warning(
                                "The AI service is temporarily busy. "
                                "Please try again later."
                            )
                        else:
                            st.error(
                                "Something went wrong. Please try again."
                            )
