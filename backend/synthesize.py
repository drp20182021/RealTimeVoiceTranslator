from TTS.api import TTS
import torch


def synthesize_text_coqui(
    text: str, lang: str, speaker_wav: str, output_path: str
) -> bytes:
    """
    Synthesize text to speech using Coqui's XTTS model.

    Args:
        text (str): The text to synthesize.
        lang (str): The language code for synthesis.
        speaker_wav (str): The path to the speaker's reference audio file.
        output_path (str): The path to save the synthesized audio.

    Returns:
        bytes: The synthesized audio in bytes.
    """
    # Initialize the TTS model
    tts = TTS(
        "tts_models/multilingual/multi-dataset/xtts_v2", gpu=torch.cuda.is_available()
    )

    # Generate speech
    tts.tts_to_file(
        text=text, file_path=output_path, speaker_wav=speaker_wav, language=lang
    )

    # Read the audio file and convert it to bytes
    with open(output_path, "rb") as f:
        audio_bytes = f.read()

    return audio_bytes
