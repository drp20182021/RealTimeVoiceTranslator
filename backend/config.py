import os
import librosa


def get_recording_path() -> str:
    """
    Get the absolute path to the recording.wav file, searching in the current directory,
    parent directory, and grandparent directory.

    Returns:
        str: The absolute path to the recording.wav file if found.
    Raises:
        FileNotFoundError: If the recording.wav file is not found in any of the directories.
    """
    filenames = ["recording.wav"]
    search_paths = [
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..")),
        os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")),
        os.path.abspath(os.path.dirname(__file__)),
    ]

    for search_path in search_paths:
        for filename in filenames:
            full_path = os.path.join(search_path, filename)
            if os.path.exists(full_path):
                return full_path

    raise FileNotFoundError(
        "recording.wav not found in current, parent, or grandparent directories."
    )


def get_file_size(file_path: str) -> int:
    """
    Get the size of the file in bytes.

    Args:
        file_path (str): The path to the file.

    Returns:
        int: The size of the file in bytes.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    return os.path.getsize(file_path)


def load_recording(recording_path: str) -> tuple:
    """
    Load the recording.wav file.

    Args:
        recording_path (str): The path to the recording.wav file.

    Returns:
        tuple: A tuple containing the audio data (np.ndarray) and the sample rate (int).
    """
    if not os.path.exists(recording_path):
        raise FileNotFoundError(f"File not found: {recording_path}")

    try:
        audio, sr = librosa.load(recording_path, sr=16000, mono=True)
    except Exception as e:
        raise ValueError(f"Error loading audio file: {e}")

    return audio, sr
