# Helpdesk Chatbot with Streamlit & ChromaDB

📌 Overview

The Helpdesk Chatbot is an AI-powered conversational agent designed to assist users with their queries in a friendly and natural way. Built using Streamlit, ChromaDB, and LangChain, it integrates Groq's LLaMA 3.3 70B Versatile model to provide accurate responses with memory retention.

🚀 Features

- Conversational Memory: Maintains context using ConversationBufferWindowMemory.

- ChromaDB Integration: Retrieves the most relevant context to answer queries.

- Refined Query Processing: Enhances user input before passing it to the LLM.

- Customizable UI: Streamlit-powered user interface with a chat history display.

- Optimized Responses: Cleans up redundant AI-generated phrases for more natural interaction.

🛠️ Tech Stack

- Frontend: Streamlit

- Backend: Python, LangChain

- Database: ChromaDB

- LLM: Groq's LLaMA 3.3 70B Versatile

- Libraries:

   1. streamlit

   2. streamlit_chat

   3. langchain

   4. re (Regex for text cleanup)

 ## How It Works

1. The chatbot greets the user and maintains a buffer memory of past interactions.

2. User input is processed and refined before retrieving the most relevant context.

3. The LLaMA 3 model generates a response based on the context and input query.

4. The chatbot cleans up AI-generated filler phrases for more natural responses.

5. User queries and responses are displayed in the chat UI.

🎨 UI Design

1. Uses st.chat_input() for text input.

2. Displays chatbot responses with a custom avatar.

3. Uses st.chat_message() and streamlit_chat.message() for structured display.

## How to run?       

Use the following commands
- streamlit run app.py
