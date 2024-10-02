
from setuptools import setup, find_packages

setup(
    name="Spitfire_LMM_Speech_Assistant",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "whisper",
        "pyttsx3",
        "pyobjc;platform_system == 'Darwin'",
        "ollama",
        "setuptools",
        "speechrecognition",
        "soundfile",
        "librosa"
    ],
    entry_points={
        'console_scripts': [
            'spitfire = pyttsx3_main:main',
        ],
    },
)
