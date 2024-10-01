# from gtts import gTTS
# import os

# def speak_text(text):
#     # Debugging: Print the model output. Disabled line below for production by putting # in front of code.
#     #print(f"Model Output: {text}")
    
#     # Check if the text is empty and provide a default response
#     if not text:
#         text = "Sorry, I didn't catch that."
    
#     # Convert text to speech using gTTS
#     tts = gTTS(text=text, lang='en')
#     tts.save("output.mp3")
    
#     # Play the generated speech audio on macOS
#     os.system("afplay output.mp3")

import pyttsx3  # Import pyttsx3 for text-to-speech functionality

def speak_text(text):
    try:
        engine = pyttsx3.init(driverName='nsss')  # Initialize the pyttsx3 engine with the macOS 'nsss' driver
        engine.say(text)  # Queue the text to be spoken
        engine.runAndWait()  # Blocks while processing all currently queued commands
    except Exception as e:
        print(f"An error occurred during TTS: {e}")