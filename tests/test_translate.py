import unittest
from backend.translate import translate_text
from backend.transcribe import transcribe_audio
from backend.config import get_recording_path, load_recording
import torch


class TestTranslate(unittest.TestCase):

    def test_translate_text(self):

        try:
            recording_path = get_recording_path()
            audio_data, sample_rate = load_recording(recording_path)
            device = "cuda" if torch.cuda.is_available() else "cpu"

            text = transcribe_audio(audio_data, sample_rate, device=device)

            src_lang = "es"
            tgt_lang = "en"
            print(f"Text: {text}")

            translated_text = translate_text(text, src_lang, tgt_lang)
            print(f"Translated text: {translated_text}")

        except Exception as e:
            self.fail(f"Failed to translate transcription: {e}")


if __name__ == "__main__":
    unittest.main()
