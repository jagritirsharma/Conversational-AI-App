Here’s the improved README without Markdown formatting:

---

# Conversational AI App 🤖  

This is a chatbot application leveraging the Groq API and Streamlit for an interactive conversational experience.  

---

## Getting Started  
Follow these steps to set up and run the chatbot on your local machine.  

---

## Prerequisites  

### 1️⃣ API Key  
- Go to the Groq Console and generate an API key.  
- Save the key in a `.env` file in the project directory as follows:  
  `GROQ_API_KEY=your_api_key_here`  
**Note:** Ensure you have `python-dotenv` installed or manually set the API key in your script.  

### 2️⃣ Install Python  
- Ensure you have **Python 3.10** installed. You can download it from the official Python website.  

---

## Installation Steps  

### Option 1: Using Virtual Environment (venv)  

1️⃣ **Create a Virtual Environment:**  
   `python -m venv env`  

2️⃣ **Activate the Virtual Environment:**  
   - For PowerShell (Windows): `env\Scripts\Activate`  
   - For CMD (Windows): `env\Scripts\activate.bat`  
   - For Git Bash (Windows): `source env/Scripts/activate`  
   - For macOS/Linux: `source env/bin/activate`  

3️⃣ **Install Dependencies:**  
   `pip install -r requirements.txt`  
   If `streamlit` is missing, install it separately: `pip install streamlit`  

---

### Option 2: Using Conda  

1️⃣ **Create a New Conda Environment:**  
   `conda create -p env python=3.10 -y`  

2️⃣ **Activate the Conda Environment:**  
   `conda activate ./env`  

3️⃣ **Install Required Packages:**  
   `pip install -r requirements.txt`  
   `pip install streamlit langchain datetime langchain-groq`  

---

## Running the Application  

Ensure your environment (`venv` or `Conda`) is activated, then start the app:  
`streamlit run main.py`  

If using `app.py`:  
`streamlit run app.py`  

---

## Features  

✅ **Interactive Chat Interface** – Real-time conversational AI using Groq.  
✅ **Customizable Memory and Persona** – Tailor the chatbot's responses.  
✅ **Easy Setup** – Choose between `venv` or `Conda` for installation.  
