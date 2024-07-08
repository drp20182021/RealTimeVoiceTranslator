from transformers import pipeline


def translate_text(text: str, src_lang: str, tgt_lang: str) -> str:
    """
    Translate text from one language to another.

    Args:
        text (str): The text to translate.
        src_lang (str): The source language code.
        tgt_lang (str): The target language code.

    Returns:
        str: The translated text.
    """
    translator = pipeline(
        "translation", model=f"Helsinki-NLP/opus-mt-{src_lang}-{tgt_lang}"
    )
    translated_text = translator(text)[0]["translation_text"]

    return translated_text
