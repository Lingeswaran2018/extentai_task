# 🎙️ Fine-Tuned Whisper-Tiny Model for Tamil ASR

This repository contains a fine-tuned version of OpenAI's [Whisper-Tiny](https://huggingface.co/openai/whisper-tiny) model for **Tamil Automatic Speech Recognition (ASR)**. The model was trained using the [Mozilla Common Voice](https://commonvoice.mozilla.org) dataset and is publicly available on Hugging Face for easy integration.

---

## 📦 Model Summary

- **Base Model**: Whisper-Tiny
- **Dataset**: Mozilla Common Voice (Tamil)
- **Training Samples**: 10,000
- **Training Duration**: ~2.15 hours
- **Hosted Model**: [Lingalingeswaran/whisper-tiny-extentai](https://huggingface.co/Lingalingeswaran/whisper-tiny-extentai)

---

## 🚀 Usage

You can use the fine-tuned model via the `transformers` pipeline:

```python
from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", model="Lingalingeswaran/whisper-tiny-extentai")
result = pipe("your_audio_file.wav")
print(result["text"])
