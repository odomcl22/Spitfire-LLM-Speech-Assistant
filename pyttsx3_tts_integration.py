import pyttsx3

# Initialize pyttsx3 engine
engine = pyttsx3.init()

# Fetch available voices
voices = engine.getProperty('voices')

# Set default to Alex (voice selection for macOS)
for voice in voices:
    if "Alex" in voice.name:
        engine.setProperty('voice', voice.id)
        break
else:
    print("Alex voice not found. Using default voice.")

# Set voice properties
engine.setProperty('rate', 160)  # Conversational rate between 150-175 WPM
engine.setProperty('volume', 0.9)  # Volume level (0.0 to 1.0)

# Text-to-speech function (speak the provided text)
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Example usage: speak some text
if __name__ == "__main__":
    speak_text("Hello, this is Alex speaking at a conversational speed.")