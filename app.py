import streamlit as st
import os
from groq import Groq
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain_groq import ChatGroq
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def init_session_state():
    """Initialize session state variables."""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

def get_avatar(role):
    """Return avatar based on role."""
    if role == 'user':
        return '👤'  # User avatar (person icon)
    else:
        return '🤖'  # Chatbot avatar (robot icon)

def main():
    # Page configuration
    st.set_page_config(
        page_title="Ask me Anything!",
        page_icon="🤖",
        layout="wide"
    )

    # Initialize session state
    init_session_state()

    # Sidebar for model selection and memory length
    st.sidebar.title('Chatbot Configuration')
    model = st.sidebar.selectbox(
        'Choose a model',
        ['mixtral-8x7b-32768', 'llama3-8b-8192']
    )
    
    # Conversational memory slider
    conversational_memory_length = st.sidebar.slider(
        'Conversational memory length:', 
        1, 10, 
        value=5
    )

    # Create memory and initialize chat objects
    memory = ConversationBufferWindowMemory(k=conversational_memory_length)
    
    # Populate memory from existing chat history
    for message in st.session_state.chat_history:
        memory.save_context(
            {'input': message['human']}, 
            {'output': message['AI']}
        )

    # Initialize Groq Langchain chat object
    groq_chat = ChatGroq(
        groq_api_key=os.environ['GROQ_API_KEY'], 
        model_name=model
    )
    conversation = ConversationChain(
        llm=groq_chat,
        memory=memory
    )

    # Main chat interface
    st.title("🤖 Ask me Anything!")

    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message("user"):
            st.write(f"{get_avatar('user')} {message['human']}")
        with st.chat_message("assistant"):
            st.write(f"{get_avatar('assistant')} {message['AI']}")

    # Chat input
    if prompt := st.chat_input("Enter your message"):
        # Display user message
        with st.chat_message("user"):
            st.write(f"{get_avatar('user')} {prompt}")

        # Get response
        response = conversation(prompt)
        ai_response = response['response']

        # Display AI response
        with st.chat_message("assistant"):
            st.write(f"{get_avatar('assistant')} {ai_response}")

        # Update chat history
        message = {'human': prompt, 'AI': ai_response}
        st.session_state.chat_history.append(message)

if __name__ == "__main__":
    main()