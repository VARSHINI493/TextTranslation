import streamlit as st
from deep_translator import GoogleTranslator
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Ensure consistent language detection
DetectorFactory.seed = 0

# Streamlit UI
st.title("🌍 NLP-Based Language Translator")
st.write("Enter text (minimum 50 words) to detect the language and translate it.")

# Input Text Box
text_input = st.text_area("Enter your text:", height=200)

# Button to process input
if st.button("Detect Language & Translate"):
    words = text_input.split()
    
    # Check if input has at least 50 words
    if len(words) < 50:
        st.error("❌ Error: Please enter at least 50 words.")
    else:
        try:
            # Detect language
            detected_lang = detect(text_input)
            st.success(f"✅ Detected Language: `{detected_lang}`")

            # Ask for destination language
            dest_lang = st.text_input("Enter the target language code (e.g., 'en' for English, 'ta' for Tamil):").strip()

            if dest_lang:
                try:
                    # Translate text
                    translated_text = GoogleTranslator(source=detected_lang, target=dest_lang).translate(text_input)
                    st.success("✅ Translated Text:")
                    st.write(translated_text)
                except Exception as e:
                    st.error(f"⚠️ Translation Error: {str(e)}")

        except LangDetectException:
            st.error("❌ Could not detect the language. Please enter a valid text sample.")
