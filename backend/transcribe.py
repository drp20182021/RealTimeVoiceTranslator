from transformers import pipeline, WhisperForConditionalGeneration, WhisperProcessor
import torch


def transcribe_audio(
    audio_data,
    sample_rate,
    model_name: str = "openai/whisper-base",
    device: str = "cpu",
    language: str = "es",
) -> str:
    """
    Transcribe the provided audio data using a speech-to-text model.

    Args:
        audio_data (np.ndarray): The audio data to transcribe.
        sample_rate (int): The sample rate of the audio data.
        model_name (str): The name of the Hugging Face model to use for transcription.
        device (str): The device to run the model on. Use 'cpu' or 'cuda'.
        language (str): The language to be used for transcription.

    Returns:
        str: The transcribed text from the audio data.
    """
    # Load the processor and model
    processor = WhisperProcessor.from_pretrained(model_name)
    model = WhisperForConditionalGeneration.from_pretrained(model_name).to(device)

    # Process audio data
    inputs = processor(audio_data, sampling_rate=sample_rate, return_tensors="pt").to(
        device
    )

    # Generate prediction with forced language tokens
    forced_decoder_ids = processor.get_decoder_prompt_ids(
        language=language, task="transcribe"
    )
    transcription_ids = model.generate(
        inputs["input_features"].to(device), forced_decoder_ids=forced_decoder_ids
    )

    # Decode the generated ids to text
    transcription = processor.batch_decode(transcription_ids, skip_special_tokens=True)[
        0
    ]

    return transcription
