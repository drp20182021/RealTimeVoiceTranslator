from config import get_recording_path, load_recording
from transcribe import transcribe_audio
from translate import translate_text
from synthesize import synthesize_text_coqui
import torch
import sys


def main():
    """
    Main function to process the audio: load, transcribe, translate, and synthesize.

    Steps:
        1. Load the audio recording.
        2. Transcribe the audio to text.
        3. Translate the transcribed text to another language.
        4. Synthesize the translated text to audio using a reference speaker.
    """
    try:
        # Get the source and target languages from the command-line arguments
        src_lang = sys.argv[1]
        tgt_lang = sys.argv[2]

        # Step 1: Load the recording
        recording_path = get_recording_path()
        audio_data, sample_rate = load_recording(recording_path)
        print(f"Loaded recording from {recording_path} with sample rate {sample_rate}")

        # Step 2: Transcribe the audio to text
        device = "cuda" if torch.cuda.is_available() else "cpu"
        transcribed_text = transcribe_audio(
            audio_data, sample_rate, device=device, language=src_lang
        )
        print(f"Transcription: {transcribed_text}")

        # Step 3: Translate the transcribed text to another language
        translated_text = translate_text(transcribed_text, src_lang, tgt_lang)
        print(f"Translated text: {translated_text}")

        # Step 4: Synthesize the translated text to audio using a reference speaker
        speaker_wav = get_recording_path()  # Use the same recording as reference
        output_path = "output_translated.wav"
        synthesized_audio = synthesize_text_coqui(
            translated_text, tgt_lang, speaker_wav, output_path
        )
        if synthesized_audio:
            with open(output_path, "wb") as f:
                f.write(synthesized_audio)
            print(f"Synthesis completed. Check the {output_path} file.")
        else:
            print("No audio data was generated.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
