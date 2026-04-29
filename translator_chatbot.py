import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import tempfile

st.set_page_config(page_title="Free Translator Chatbot")
st.title("🌍 Free Translator Chatbot")

# Languages you want to allow
LANGUAGES = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese": "zh-cn",
    "Arabic": "ar",
    "Hindi": "hi",
    "Turkish": "tr",
    "Russian": "ru",
    "Japanese": "ja",
    "Korean": "ko",
    "Punjabi": "pa"
}

# Input
text = st.text_input("Enter your text:")
target = st.selectbox("Translate to:", list(LANGUAGES.keys()))

if st.button("Translate"):
    if text.strip() == "":
        st.warning("Please enter text.")
    else:
        try:
            translated = GoogleTranslator(
                source='auto',
                target=LANGUAGES[target]
            ).translate(text)

            st.success(f"**Translated Text:** {translated}")

            # 🔊 TEXT TO SPEECH PART
            tts = gTTS(text=translated, lang=LANGUAGES[target])

            # Save temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as fp:
                tts.save(fp.name)
                audio_file = open(fp.name, "rb")
                audio_bytes = audio_file.read()

            # Play audio in Streamlit
            st.audio(audio_bytes, format="audio/mp3")

        except Exception as e:
            st.error(f"Error: {e}")