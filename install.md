
# Installation Instructions for Spitfire LMM Speech Assistant

## Prerequisites:
- Ensure **Python 3.11** is installed on your machine.

### Installing Python 3.11:
1. Download and install Python 3.11 from the [official website](https://www.python.org/downloads/).
   - Ensure Python 3.11 is added to your system's PATH.
   - Verify the installation by running the following command:
     ```bash
     python3.11 --version
     ```

## macOS Instructions

1. **Install Python 3.11** (if not already installed) by downloading it from the [official website](https://www.python.org/downloads/).
2. **Install Xcode Command Line Tools** (required for `PyAudio`):
   - Run this command in your terminal:
     ```bash
     xcode-select --install
     ```
3. **Clone the repository** and navigate to the project folder.
4. **Install required dependencies**:
   ```bash
   python3.11 -m pip install -r requirements.txt
   ```
5. **Install `PyAudio` manually** (if needed):
   ```bash
   python3.11 -m pip install pyaudio
   ```
6. **Run the app**:
   ```bash
   python3.11 pyttsx3_main.py
   ```

## Windows Instructions

1. **Install Python 3.11** (if not already installed) from the [official website](https://www.python.org/downloads/).
2. **Install required dependencies**:
   ```bash
   python3.11 -m pip install -r requirements.txt
   ```
3. **Install `PyAudio`** (for Windows):
   ```bash
   python3.11 -m pip install pyaudio
   ```
4. **Run the app**:
   ```bash
   python3.11 pyttsx3_main.py
   ```

## Additional Information
- **Note for macOS**: You must install the Xcode Command Line Tools to ensure `PyAudio` can build correctly.
- **Note for Windows**: `PyAudio` should install directly from pip without additional dependencies.

## Model Configuration (Ollama):
- The application uses the `Ollama` model for language processing.
- Ensure Ollama is installed by visiting [Ollama](https://ollama.com).
- You can configure the model by modifying the `process_text_with_llm` function in the `pyttsx3_main.py` file.
