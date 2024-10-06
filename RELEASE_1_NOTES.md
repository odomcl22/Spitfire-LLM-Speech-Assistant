
# Release 1 - Speech AI Application

## Summary

This release focuses on delivering basic real-time speech-to-text and text-to-speech functionality using the Whisper model for speech recognition and the OLLAMA-backed Llama 3.2 for text generation.

## Key Changes and Improvements

- **Model Integration**: 
   OLLAMA integration was done using the Llama 3.2 model for text generation, allowing dynamic interaction based on real-time inputs.
- **Real-Time Speech Recognition**:
   Adjustments were made to ensure real-time speech capture using the Whisper model. Audio is now processed efficiently with minimal latency.
- **TTS Improvements**:
   Text-to-speech functionality was updated with support for macOS's `say` command and cross-platform functionality using `pyttsx3`. 
- **Error Handling**:
   Enhanced error handling was implemented to better manage cases where speech is not recognized or there is an issue with text generation.
- **Dependency Installation**:
   Instructions for installing dependencies such as Whisper, OLLAMA, and pyttsx3 were refined for seamless setup on both macOS and Windows.

## Installation Instructions

For detailed installation instructions, please refer to the provided installation file (INSTALL.md).
