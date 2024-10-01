import threading
import speech_recognition as sr
from pyttsx3_whisper_integration import transcribe_audio
from pyttsx3_model_integration import process_text_with_llm
import subprocess

# Function to capture speech
def capture_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Please start speaking...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
            input_text = transcribe_audio(audio).lower()
            print(f"Recognized speech: {input_text}")
            return input_text
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError as e:
            print(f"Speech recognition service error: {e}")
            return None

# Function to trim conversation history
def get_recent_history(conversation_history, limit=2):
    conversation_lines = conversation_history.strip().split("\n")
    return "\n".join(conversation_lines[-limit*2:])

# Updated speak_text function using Option 1
def speak_text(text):
    try:
        subprocess.run(['say', text])
    except Exception as e:
        print(f"An error occurred during TTS: {e}")

# Main function
def main():
    conversation_history = ""

    while True:
        input_text = capture_speech()

        if input_text:
            conversation_history += f"You: {input_text}\n"
            recent_history = get_recent_history(conversation_history)

            output_text = process_text_with_llm(recent_history)
            conversation_history += f"Model: {output_text}\n"
            print(f"Model Output: {output_text}")

            speak_text(output_text)

if __name__ == "__main__":
    main()