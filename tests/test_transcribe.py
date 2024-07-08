import unittest
from backend.transcribe import transcribe_audio
from backend.config import get_recording_path, load_recording
import torch


class TestTranscribe(unittest.TestCase):

    def test_transcribe_audio(self):
        try:
            recording_path = get_recording_path()
            audio_data, sample_rate = load_recording(recording_path)
            device = "cuda" if torch.cuda.is_available() else "cpu"
            transcription = transcribe_audio(audio_data, sample_rate, device=device)
            print("Transcription:", transcription)
        except Exception as e:
            self.fail(f"Failed to transcribe audio: {e}")


if __name__ == "__main__":
    unittest.main()
