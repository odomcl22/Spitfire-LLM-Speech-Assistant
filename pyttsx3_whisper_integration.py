import whisper
import speech_recognition as sr
import torch
import numpy as np
from io import BytesIO
import soundfile as sf
import librosa  # Import librosa for resampling

def transcribe_audio(audio_data):
    # Force use of CPU and FP32 to avoid half-precision errors
    device = "cpu"
    model = whisper.load_model("small").to(device).float()

    recognizer = sr.Recognizer()

    try:
        audio_wav = BytesIO(audio_data.get_wav_data())
        audio_wav.seek(0)
        audio_np, sample_rate = sf.read(audio_wav)

        if sample_rate != 16000:
            print(f"Resampling audio from {sample_rate} Hz to 16000 Hz.")
            audio_np = librosa.resample(audio_np, orig_sr=sample_rate, target_sr=16000)

        audio_tensor = torch.tensor(audio_np).to(device).float()

        result = model.transcribe(audio_tensor, language="en")
        text = result["text"]

        if text.strip() == "":
            raise ValueError("No speech detected.")
        
        return text

    except Exception as e:
        print(f"An error occurred: {e}")
        return "Sorry, an error occurred while processing the audio."