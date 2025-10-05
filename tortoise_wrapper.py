from io import BytesIO
from typing import Optional


_tts = None


def _lazy_load():
    global _tts
    if _tts is not None:
        return _tts
    from tortoise.api import TextToSpeech

    _tts = TextToSpeech()
    return _tts


def synthesize_to_bytes(text: str, voice: Optional[str] = None) -> BytesIO:
    tts = _lazy_load()
    # Tortoise commonly writes to file; here we generate into a temp WAV then return as BytesIO
    import tempfile
    import os

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        temp_path = tmp.name

    try:
        tts.tts_to_file(text=text, file_path=temp_path, voice=voice)
        with open(temp_path, "rb") as f:
            data = f.read()
        bio = BytesIO(data)
        bio.seek(0)
        return bio
    finally:
        try:
            os.remove(temp_path)
        except OSError:
            pass


