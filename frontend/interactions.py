import streamlit as st
import os
import subprocess
from st_audiorec import st_audiorec


def record_audio():
    st.write("Recording...")
    wav_audio_data = st_audiorec()
    if wav_audio_data is not None:
        with open("recording.wav", "wb") as f:
            f.write(wav_audio_data)
        return "recording.wav"
    return None


def call_backend(src_lang, tgt_lang):
    result = subprocess.run(
        ["python", "backend/main.py", src_lang, tgt_lang],
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        st.error(f"Error in backend processing: {result.stderr}")
        return None
    else:
        st.success("Backend processing completed successfully.")
        return "output_translated.wav"


def handle_translation():
    recording_path = record_audio()
    if recording_path:
        src_lang = st.session_state.current_speak_language
        tgt_lang = st.session_state.current_translate_language
        translated_audio_path = call_backend(src_lang, tgt_lang)
        if translated_audio_path and os.path.exists(translated_audio_path):
            st.audio(translated_audio_path, format="audio/wav")
        else:
            st.error("Failed to process the audio.")
