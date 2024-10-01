
from setuptools import setup, find_packages

setup(
    name='AI_Speech_App',
    version='1.0',
    packages=find_packages(),
    install_requires=['whisper', 'pyttsx3', 'subprocess', 'speech_recognition', 'torch', 'numpy', 'soundfile', 'librosa'],
    entry_points={
        'console_scripts': [
            'speech-app=pyttsx3_main:main',
        ]
    },
    description='A Python-based speech-to-text and text-to-speech app with Whisper and LLaMA model integration',
    author='Your Name',
    author_email='your-email@example.com',
    url='https://github.com/your-repo',
    classifiers=[
        'Programming Language :: Python :: 3.11',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows'
    ],
)
