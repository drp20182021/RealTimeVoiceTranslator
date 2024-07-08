import unittest
from backend.config import get_recording_path, get_file_size, load_recording


class TestConfig(unittest.TestCase):

    def test_get_recording_path(self):
        try:
            path = get_recording_path()
            print(f"Recording path: {path}")
        except FileNotFoundError as e:
            self.fail(f"get_recording_path raised FileNotFoundError unexpectedly: {e}")

    def test_get_file_size(self):
        try:
            path = get_recording_path()
            file_size = get_file_size(path)
            print(f"File size of {path}: {file_size} bytes")
        except Exception as e:
            self.fail(f"get_file_size raised an exception unexpectedly: {e}")

    def test_load_recording(self):
        try:
            path = get_recording_path()
            audio_data, sample_rate = load_recording(path)
            print(f"Loaded audio data with sample rate: {sample_rate}")
        except Exception as e:
            self.fail(f"load_recording raised an exception unexpectedly: {e}")


if __name__ == "__main__":
    unittest.main()
