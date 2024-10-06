import threading
import speech_recognition as sr
from pyttsx3_whisper_integration import transcribe_audio
from pyttsx3_model_integration import process_text_with_llm
import subprocess
from emotion import detect_emotion, load_emotion_model  # Import the emotion detection functions

# Load the emotion model once at the beginning
emotion_model = load_emotion_model()

# Function to capture speech
def capture_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Please start speaking...")
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Increase noise adjustment duration to better handle background noise
        try:
            # Listening with increased timeout and phrase time limit for better recognition of speech patterns
            audio = recognizer.listen(source, timeout=6, phrase_time_limit=10)  # Increased timeout and phrase time limit
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

# Updated speak_text function using Mac's TTS with 'Samantha' voice
def speak_text(text):
    try:
        # Using Mac's 'say' command with the 'Samantha' voice for better clarity
        subprocess.run(['say', '-v', 'Samantha', text])  # Adjust 'Samantha' to the best-sounding voice
    except Exception as e:
        print(f"An error occurred during TTS: {e}")

# Main function with emotion detection integration
def main():
    conversation_history = ""

    while True:
        input_text = capture_speech()

        if input_text:
            # Step 1: Detect emotion in the input text
            emotion, confidence = detect_emotion(input_text, emotion_model)
            print(f"Detected emotion: {emotion}, Confidence: {confidence:.2f}")

            # Add input text to conversation history
            conversation_history += f"You: {input_text}\n"
            recent_history = get_recent_history(conversation_history)

            # Step 2: Pass both the recent history and detected emotion to the LLM
            # (The emotion can be passed into your LLM's processing if it's designed to handle it)
            output_text = process_text_with_llm(recent_history, emotion=emotion)  # Modify process_text_with_llm to accept emotion

            conversation_history += f"Model: {output_text}\n"
            print(f"Model Output: {output_text}")

            # Step 3: Speak the model's response
            speak_text(output_text)

if __name__ == "__main__":
    main()