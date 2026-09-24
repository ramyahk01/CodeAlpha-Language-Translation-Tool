# 🌐 Language Translation Tool

A web-based Language Translation Tool built with **Python** and **Streamlit**. Users can enter text, choose source and target languages, and get instant translations — powered by the `deep-translator` library.

## ✨ Features

- Enter text to translate
- Select source and target languages from 15+ options
- Real-time translation via translation API
- Copy translated text to clipboard
- Text-to-speech for translated output
- Clean, simple, and responsive UI

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.13 |
| UI Framework | Streamlit |
| Translation API | deep-translator (MyMemory backend) |
| Environment | Virtual Environment (venv) |

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ramyahk01/CodeAlpha_LanguageTranslationTool.git
   cd CodeAlpha_LanguageTranslationTool

## Create and activate a virtual environment:

bash
python -m venv venv
venv\Scripts\activate

## Install dependencies:
  ```bash
pip install -r requirements.txt

## Run the app:
  ```bash
streamlit run app.py

## Open your browser at http://localhost:8501

## 📁 Project Structure
CodeAlpha_LanguageTranslationTool/
├── app.py                 # Main application code
├── requirements.txt       # Dependencies
└── README.md              # Project documentation

## 🎯 How It Works
User enters text and selects source + target languages

The app sends the text to the translation API

The API returns the translated text

Streamlit displays the result instantly

## 👤 Author
Your Name — B.Tech AI & ML Student

## 📜 License
This project is part of the CodeAlpha internship program.
