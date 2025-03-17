### **README (with Conda and venv options)**  
```md
# Conversational AI App 🤖

This is a chatbot application leveraging the Groq API and Streamlit for an interactive conversational experience.

---

## **Getting Started**
Follow these steps to set up and run the chatbot on your local machine.

---

## **Prerequisites**
### **1️⃣ API Key**
- Go to the [Groq Console](https://groq.com) and generate an API key.
- Save the key in a `.env` file in the project directory as follows:
  ```
  GROQ_API_KEY=your_api_key_here
  ```

### **2️⃣ Install Python**
- Ensure you have **Python 3.10** installed. You can download it from [here](https://www.python.org/downloads/).

---

## **Installation Steps**
### **Option 1: Using Virtual Environment (`venv`)**
✅ **1. Create a Virtual Environment**
```sh
python -m venv env
```

✅ **2. Activate the Virtual Environment**
- **For PowerShell (Windows):**  
  ```sh
  env\Scripts\Activate
  ```
- **For CMD (Windows):**  
  ```sh
  env\Scripts\activate.bat
  ```
- **For Git Bash (Windows):**  
  ```sh
  source env/Scripts/activate
  ```
- **For macOS/Linux:**  
  ```sh
  source env/bin/activate
  ```

✅ **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

---

### **Option 2: Using Conda**
✅ **1. Create a New Conda Environment**
```sh
conda create -p env python=3.10 -y
```

✅ **2. Activate the Conda Environment**
```sh
conda activate env/
```

✅ **3. Install Required Packages**
```sh
pip install -r requirements.txt
pip install streamlit langchain datetime langchain-groq
```

---

## **Running the Application**
### **Run the Chatbot Application**
Ensure your environment (venv or Conda) is activated, then start the app:

```sh
streamlit run main.py
```

### **Alternative Start (if using `app.py`)**
```sh
streamlit run app.py
```

---

## **Features**
✅ **Interactive Chat Interface**: Real-time conversational AI using Groq.  
✅ **Customizable Memory and Persona**: Tailor the chatbot's responses.  
✅ **Easy Setup**: Choose between `venv` or Conda for installation.  
```
