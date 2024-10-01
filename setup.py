
from setuptools import setup, find_packages

setup(
    name='Spitfire_LMM_Speech_Assistant',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'whisper',
        'torch',
        'pyttsx3',
        'speechrecognition',
        'soundfile',
        'librosa',
        'subprocess'
    ],
    description='A conversational AI speech assistant using Whisper and LLaMA models for speech-to-text and text-to-speech',
    author='Your Name',
    author_email='your.email@example.com',
)
