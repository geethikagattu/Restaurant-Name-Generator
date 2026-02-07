# 🍽️ Restaurant Name Generator (RAG)

An AI-powered web app that generates **creative restaurant names** and **detailed menus** based on cuisine type.  
Built using **Google Gemini**, **LangChain**, and **Streamlit**.

---

## ✨ Features

- 🧠 Generates **fancy restaurant names** using AI  
- 📋 Creates a **complete menu** for the generated restaurant  
- 🎨 Simple and clean **Streamlit UI**  
- ⚡ Powered by **Google Gemini (Generative AI)**  

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – UI
- **LangChain**
- **Google Gemini API**
- **Pydantic**

---

## 📂 Project Structure

├── main.py                # Streamlit app
├── langchain_helper.py    # LLM + prompt logic
├── requirements.txt       # Dependencies
├── runtime.txt            # Python version

##  🚀 How It Works
User selects a cuisine
AI generates:
A restaurant name
A custom menu
Results are displayed instantly in the app

##  🔐 Environment Variables
This project requires a Google Gemini API key.
Local
Create a .env file:
GOOGLE_API_KEY=your_api_key_here
Streamlit Cloud
Add the key in App Settings → Secrets:
GOOGLE_API_KEY = "your_api_key_here"

##  ▶️ Run Locally
pip install -r requirements.txt
streamlit run main.py

##  🌍 Deployment

This app is designed to be deployed on Streamlit Cloud.

##  💡 Future Improvements

Add multiple name suggestions
Cuisine-based menu styling
Downloadable menu (PDF)
UI animations & themes

##  🙋‍♀️ Author
Geethika Reddy Gattu
B.Tech CSE Student | Aspiring AI & GenAI Engineer

##  ⭐ If you like this project, give it a star!
