import streamlit as st
import os
import openai
from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

# Streamlit UI setup
st.set_page_config(page_title="Conversational Q&A Chatbot")
st.header("Hey, Let's Chat")

# Initialize OpenAI client with API key
os.environ["OPENAI_API_KEY"] = "your_api"  # Replace with your actual API key
client = openai.OpenAI()
chat = ChatOpenAI(temperature=0.5)

# Initialize the conversation if it's not already in the session state
if 'flowmessages' not in st.session_state:
    st.session_state['flowmessages'] = [SystemMessage(content="You are a comedian AI assistant")]

# Function to get responses from the chat model
def get_chatmodel_response(question):
    st.session_state['flowmessages'].append(HumanMessage(content=question))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))
    return answer.content

# User input
input = st.text_input("Input: ", key="input")

# Handling the ask button
submit = st.button("Ask the question")
if submit and input:
    response = get_chatmodel_response(input)
    st.subheader("The Response is")
    st.write(response)
