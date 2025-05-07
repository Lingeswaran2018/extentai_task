# stt_pipeline.py
from transformers import pipeline

class WhisperSTTPipeline:
    def __init__(self, model_name="Lingalingeswaran/whisper-tiny-extentai"):
        self.pipe = pipeline("automatic-speech-recognition", model=model_name)

    def transcribe(self, audio_path):
        result = self.pipe(audio_path)
        return result['text']

# Example usage
if __name__ == "__main__":
    stt = WhisperSTTPipeline()
    audio_file = "testdata_tamil.wav"  # Replace with your file
    transcription = stt.transcribe(audio_file)
    print("Transcription:", transcription)
