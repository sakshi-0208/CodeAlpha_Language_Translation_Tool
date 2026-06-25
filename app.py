import streamlit as st
from googletrans import Translator, LANGUAGES
from gtts import gTTS

translator = Translator()

st.title("Language Translation Tool")

# Input text
text = st.text_area("Enter Text")

# Language list
languages = list(LANGUAGES.values())

# Select languages
source_lang = st.selectbox("Source Language", languages)
target_lang = st.selectbox("Target Language", languages, index=1)

if st.button("Translate"):

    if text.strip() == "":
        st.warning("Please enter text to translate.")
    else:
        # Get language codes
        source_code = list(LANGUAGES.keys())[languages.index(source_lang)]
        target_code = list(LANGUAGES.keys())[languages.index(target_lang)]

        # Translation
        translated = translator.translate(
            text,
            src=source_code,
            dest=target_code
        )

        st.success("Translation Completed!")

        # Output text
        st.text_area("Translated Text", translated.text, height=150)

        # Copy/downlod button
        st.download_button(
            label="📥 Download / Copy Translation",
            data=translated.text,
            file_name="translation.txt",
            mime="text/plain"
        )

        # Text to Speech
        try:
            tts = gTTS(text=translated.text, lang=target_code)
            tts.save("audio.mp3")

            audio_file = open("audio.mp3", "rb")
            st.audio(audio_file.read(), format="audio/mp3")

        except Exception as e:
            st.error("Text-to-Speech failed: " + str(e))