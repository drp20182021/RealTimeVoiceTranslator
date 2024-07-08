import unittest
from backend.synthesize import synthesize_text_coqui
from backend.config import get_recording_path, load_recording
import torch
from backend.transcribe import transcribe_audio


class TestSynthesize(unittest.TestCase):

    def test_synthesize_text_coqui(self):

        recording_path = get_recording_path()
        audio_data, sample_rate = load_recording(recording_path)
        device = "cuda" if torch.cuda.is_available() else "cpu"
        transcription = transcribe_audio(audio_data, sample_rate, device=device)

        text = transcription
        lang = "es"
        speaker_wav = recording_path
        output_path = "output_test.wav"
        try:
            audio_data = synthesize_text_coqui(text, lang, speaker_wav, output_path)
            if audio_data:
                with open(output_path, "wb") as f:
                    f.write(audio_data)
                print(f"Synthesis completed. Check the {output_path} file.")
            else:
                self.fail("No audio data was generated.")
        except Exception as e:
            self.fail(f"Failed to synthesize text: {e}")


if __name__ == "__main__":
    unittest.main()
