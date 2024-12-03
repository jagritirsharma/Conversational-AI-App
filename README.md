
# Conversational AI App 🤖
Conversational AI App using Gen AI (Chatbot)
This is a chatbot application leveraging Groq API and Streamlit for an interactive conversational experience.

## Getting Started

Follow these steps to set up and run the chatbot on your local machine.

### Prerequisites
1. **API Key**  
   - Go to [Groq Console](https://console.groq.com/keys) and generate an API key.
   - Save the key in a `.env` file in the project directory as follows:
     ```plaintext
     GROQ_API_KEY=your_api_key_here
     ```

2. **Install Conda**  
   Make sure Conda is installed on your system. [Download Conda here](https://docs.conda.io/en/latest/miniconda.html).

---

### Installation Steps

1. **Create a New Environment**
   ```bash
   conda create -p env python=3.10 -y
   ```

2. **Activate the Environment**
   ```bash
   conda activate env/
   ```

3. **Install Required Packages**
   ```bash
   pip install -r requirements.txt
   pip install streamlit
   pip install langchain
   pip install datetime
   pip install langchain-groq
   ```

---

### Running the Application

1. **Run the Chatbot Application**
   ```bash
   streamlit run main.py
   ```

2. **Alternative Start (if using `app.py`)**
   ```bash
   streamlit run app.py
   ```

---

### Features

- **Interactive Chat Interface:** Real-time conversational AI using Groq.
- **Customizable Memory and Persona:** Tailor the chatbot's responses to your needs.
- **Easy Setup:** Simple environment setup and package installation.

---

---
