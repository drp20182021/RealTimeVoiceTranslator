import streamlit as st


def main_page():
    st.title("Select Languages for Real-Time Translation")

    languages = {
        "English": "en",
        "Spanish": "es",
        "French": "fr",
        "German": "de",
        "Italian": "it",
        "Portuguese": "pt",
        "Russian": "ru",
        "Chinese": "zh",
        "Japanese": "ja",
        "Arabic": "ar",
    }

    first_language = st.selectbox("Source Language:", list(languages.keys()))
    second_language = st.selectbox("Target Language:", list(languages.keys()))

    st.session_state.first_language = languages[first_language]
    st.session_state.second_language = languages[second_language]
    st.session_state.first_language_text = first_language
    st.session_state.second_language_text = second_language

    if st.button("Continue"):
        st.session_state.page = "translate"


def translate_page(handle_translation):
    st.title("Translation Page")

    first_language = st.session_state.get("first_language", "en")
    second_language = st.session_state.get("second_language", "es")

    first_language_text = st.session_state.get("first_language_text", "English")
    second_language_text = st.session_state.get("second_language_text", "Spanish")

    col1, col2 = st.columns(2)

    with col1:
        if st.button(f"Speak in {first_language_text}"):
            st.session_state.current_speak_language = first_language
            st.session_state.current_translate_language = second_language

    with col2:
        if st.button(f"Speak in {second_language_text}"):
            st.session_state.current_speak_language = second_language
            st.session_state.current_translate_language = first_language

    handle_translation()

    if st.button("Go Back"):
        st.session_state.page = "main"
