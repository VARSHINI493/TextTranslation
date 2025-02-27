import streamlit as st
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Set seed for consistent language detection
DetectorFactory.seed = 0

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "input"

# Page 1: Text Input
if st.session_state.page == "input":
    st.title("🌍 NLP-Based Language Translator")
    st.write("Enter your text (minimum 50 words) to detect the language and translate it.")

    text_input = st.text_area("✍ Enter your text below:", height=200)

    if st.button("Next ➡"):
        words = text_input.split()
        if len(words) < 50:
            st.error("❌ Error: Please enter at least 50 words.")
        else:
            try:
                detected_lang = detect(text_input)
                st.session_state.detected_lang = detected_lang
                st.session_state.text_input = text_input
                st.session_state.page = "select_language"
                st.experimental_rerun()
            except LangDetectException:
                st.error("❌ Could not detect the language. Please enter a valid text sample.")

# Page 2: Language Selection
elif st.session_state.page == "select_language":
    st.title("🌐 Choose Destination Language")
    st.write(f"🔍 Detected Language: `{st.session_state.detected_lang}`")

    # Language options
    lang_options = {
        "English": "en",
        "Tamil": "ta",
        "Hindi": "hi",
        "German": "de"
    }

    dest_lang = st.radio("🌏 Select a language:", list(lang_options.keys()))

    if st.button("Translate 📝"):
        st.session_state.dest_lang = lang_options[dest_lang]
        st.session_state.page = "translation"
        st.experimental_rerun()

# Page 3: Show Translated Text
elif st.session_state.page == "translation":
    st.title("🔄 Translation Result")
    
    try:
        translated_text = GoogleTranslator(source=st.session_state.detected_lang, 
                                           target=st.session_state.dest_lang).translate(st.session_state.text_input)
        st.success("✅ Translated Text:")
        st.write(f"📝 {translated_text}")
    except Exception as e:
        st.error(f"⚠️ Translation Error: {str(e)}")

    if st.button("Finish 🎉"):
        st.session_state.page = "thank_you"
        st.experimental_rerun()

# Page 4: Thank You Page
elif st.session_state.page == "thank_you":
    st.title("🎊 Thank You!")
    st.subheader("Your text has been successfully translated.")
    st.write("We hope this helps you in your communication. Have a great day! 😊")

    if st.button("🔄 Translate Again"):
        st.session_state.page = "input"
        st.experimental_rerun()
