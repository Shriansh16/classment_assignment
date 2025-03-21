import os
import streamlit as st
import re
from streamlit_chat import message
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
from utils import *


from langchain_groq import ChatGroq
api_key1=st.secrets["GROQ_API_KEY"]
# Streamlit setup

st.subheader("HELPDESK CHAT")

# Initialize session state variables
if 'responses' not in st.session_state:
    st.session_state['responses'] = ["Hi there! Welcome to Classment! 🎉 Want to pursue a tech role? Ask me about the courses you need, skills to learn, and the best learning paths!"]
if 'requests' not in st.session_state:
    st.session_state['requests'] = []

# Initialize the language model
llm=ChatGroq(groq_api_key=api_key1,model_name="llama-3.3-70b-versatile",temperature=0.6)

# Initialize conversation memory
if 'buffer_memory' not in st.session_state:
    st.session_state.buffer_memory = ConversationBufferWindowMemory(k=1, return_messages=True)

# Define prompt templates
system_msg_template = SystemMessagePromptTemplate.from_template(template="""Answer as a friendly helpdesk agent and use the provided context to build the answer and If the answer is not contained within the text, say 'I'm not sure about that, but I'm here to help with anything else you need!'. Do not say 'According to the provided context' or anything similar. Just give the answer naturally.""")                                                                        
human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")

prompt_template = ChatPromptTemplate.from_messages([system_msg_template, MessagesPlaceholder(variable_name="history"), human_msg_template])
link='logo.jpg'
# Create conversation chain
conversation = ConversationChain(memory=st.session_state.buffer_memory, prompt=prompt_template, llm=llm, verbose=True)

# Container for chat history
response_container = st.container()
# Container for text box
text_container = st.container()



with text_container:
    user_query =st.chat_input("Enter your query")

    if user_query:
        with st.spinner("typing..."):
            conversation_string = get_conversation_string()
            refined_query = query_refiner(conversation_string, user_query)
            refined_query = re.sub(r'(?i)refined query', '', refined_query)
            refined_query = re.sub(r'(?i)relevant', '', refined_query)
            refined_query = re.sub(r'(?i)irrelevant', '', refined_query)
            refined_query = re.sub(r'(?i)Refined question:', '', refined_query)
            #refined_query=refined_query+" "+user_query   
            #st.write(refined_query)
            #st.write(conversation_string)
            context = find_match(refined_query)
            response = conversation.predict(input=f"Context:\n{context}\n\nQuery:\n{user_query}")
            response = re.sub(r'(?i)according to the provided context,', '', response)
            response = re.sub(r'(?i)according to the provided documents,', '', response)
            response = re.sub(r'(?i)mentioned in the document', '', response)
            response = re.sub(r'(?i)according to the document', '', response)
            response = re.sub(r'(?i)based on the provided context,', '', response)
            response = re.sub(r'(?i)based on the provided document,', '', response)
            response = re.sub(r'(?i)according to the context,', '', response)


        
        # Append the new query and response to the session state  
        st.session_state.requests.append(user_query)
        st.session_state.responses.append(response)
st.markdown(
    """
    <style>
    [data-testid="stChatMessageContent"] p{
        font-size: 1rem;
    }
    </style>
    """, unsafe_allow_html=True
)


# Display chat history
with response_container:
    if st.session_state['responses']:
        for i in range(len(st.session_state['responses'])):
            with st.chat_message('Momos', avatar=link):
                st.write(st.session_state['responses'][i])
            if i < len(st.session_state['requests']):
                message(st.session_state["requests"][i], is_user=True, key=str(i) + '_user')