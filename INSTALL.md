
# Installation Instructions for Spitfire LMM Speech Assistant

## Prerequisites:
1. **Install Python 3.11** or higher. 
    - Download Python from: https://www.python.org/downloads/
    - Alternatively, for command line installation (macOS/Linux), use:
      ```bash
      brew install python@3.11
      ```
      For Windows, you can install it from the official website or use `choco` (if Chocolatey is installed):
      ```bash
      choco install python --version 3.11.5
      ```

2. Make sure you have `pip` installed, which comes with Python.

## Installation on macOS:
1. Clone the repository to your local machine.
2. Navigate to the project directory in the terminal.
3. Run the following commands to install dependencies:

    ```bash
    pip install -r requirements.txt
    python setup.py install
    ```

4. Ensure that Whisper and the LLaMA model are installed:

    ```bash
    pip install whisper
    pip install torch
    ```

5. For macOS-specific dependencies (e.g., pyobjc):

    ```bash
    pip install pyobjc
    ```

## Installation on Windows:
1. Make sure Python 3.11 or higher is installed.
2. Install required libraries using pip:
    ```bash
    pip install -r requirements.txt
    python setup.py install
    ```

3. Ensure that Whisper and pyttsx3 dependencies are installed:
    ```bash
    pip install whisper
    pip install pyttsx3
    ```

## OLLAMA and LLaMA Model Setup
1. You must install OLLAMA by visiting the [OLLAMA website](https://ollama.com/download). Follow the instructions there for your operating system.
2. To change the model in the `pyttsx3_model_integration.py`, modify the model command line in the following line:

    ```python
    command = f"ollama run llama3.2:1b  "{prompt_text}""
    ```

3. Once you run the code for the first time, the model will be downloaded. It may be slower initially, but will be faster on subsequent runs.

## Running the App:
Once everything is installed, you can run the app using:
    ```bash
    python pyttsx3_main.py
    ```

This will launch the speech-to-text and text-to-speech application.
