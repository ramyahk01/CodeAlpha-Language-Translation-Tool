import streamlit as st
import streamlit.components.v1 as components
from deep_translator import MyMemoryTranslator

st.set_page_config(page_title="Language Translation Tool", page_icon="🌐")

st.title("🌐 Language Translation Tool")
st.write("Translate text between multiple languages.")

languages = {
    "English": "english",
    "Hindi": "hindi",
    "Spanish": "spanish",
    "French": "french",
    "German": "german",
    "Italian": "italian",
    "Portuguese": "portuguese",
    "Russian": "russian",
    "Japanese": "japanese",
    "Korean": "korean",
    "Chinese (Simplified)": "chinese simplified",
    "Arabic": "arabic",
    "Turkish": "turkish",
    "Dutch": "dutch",
    "Greek": "greek",
}

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Source Language", list(languages.keys()), index=0)

with col2:
    target_lang = st.selectbox("Target Language", list(languages.keys()), index=1)

text = st.text_area("Enter text to translate", height=150)

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter some text to translate.")
    elif source_lang == target_lang:
        st.info("Source and target languages are the same. Nothing to translate.")
    else:
        try:
            translated = MyMemoryTranslator(
                source=languages[source_lang],
                target=languages[target_lang]
            ).translate(text)

            st.subheader("Translated Text")
            st.success(translated)

            # Copy button (uses browser clipboard API)
            components.html(
                f"""
                <button onclick="navigator.clipboard.writeText(`{translated.replace('`','')}`);this.innerText='✅ Copied!';"
                style="padding:8px 16px;border-radius:6px;border:1px solid #ccc;
                       background:#f0f2f6;cursor:pointer;font-size:14px;">
                📋 Copy Translated Text
                </button>
                """,
                height=60,
            )

            # Text-to-speech button (uses browser SpeechSynthesis API)
            components.html(
                f"""
                <button onclick="speechSynthesis.speak(new SpeechSynthesisUtterance(`{translated.replace('`','')}`));"
                style="padding:8px 16px;border-radius:6px;border:1px solid #ccc;
                       background:#f0f2f6;cursor:pointer;font-size:14px;">
                🔊 Speak Translated Text
                </button>
                """,
                height=60,
            )

        except Exception as e:
            st.error(f"Translation failed: {e}")