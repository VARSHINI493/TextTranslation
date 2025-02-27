import streamlit as st
from googletrans import Translator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Ensure consistent language detection
DetectorFactory.seed = 0

# Streamlit UI
st.title("NLP-Based Language Translator")
st.write("Enter text (minimum 50 words) to detect the language and translate it.")

# Input Text Box
text_input = st.text_area("Enter your text:", height=200)

# Validate text length
if st.button("Detect Language & Translate"):
    words = text_input.split()
    if len(words) < 50:
        st.error("Error: Please enter at least 50 words.")
    else:
        try:
            detected_lang = detect(text_input)
            st.write(f"Detected Language: `{detected_lang}`")

            # Ask for destination language
            dest_lang = st.text_input("Enter the target language (e.g., 'en' for English, 'ta' for Tamil):").strip()

            if dest_lang:
                translator = Translator()
                translated_text = translator.translate(text_input, dest=dest_lang)
                st.success("Translated Text:")
                st.write(translated_text.text)
        except LangDetectException:
            st.error("Could not detect the language. Please enter a valid text sample.")

