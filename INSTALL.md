
# Installation Instructions for Spitfire LMM Speech Assistant

## Prerequisites:
- Ensure **Python 3.11** is installed on your machine.
- Install Homebrew on macOS, as it will be needed to install certain dependencies.

## Homebrew Installation (macOS):
1. **If Homebrew is not installed, you can install it by running the following command in your terminal:**
- Run this command in your terminal:
   ```bash 
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. **After installation, ensure Homebrew is in your PATH:**
- Run this command in your terminal:
   ```bash 
   echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile
   eval "$(/opt/homebrew/bin/brew shellenv)"
   ```

3. **Use Homebrew to install portaudio, which is required for PyAudio:**
   ```bash 
   brew install portaudio
   ```
### Installing Python 3.11:
1. **Download and install Python 3.11 from the [official website](https://www.python.org/downloads/).**
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
7. ** If you encounter SSL certificate errors, especially on macOS, update your certificates by running:
   ```bash
   /Applications/Python\\ 3.11/Install\\ Certificates.command
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

## Troubleshooting:
- **If you encounter issues with audio dependencies on macOS, ensure that portaudio is installed via Homebrew.**
- **SSL certificate issues can often be resolved by updating certificates as shown above.**

## Additional Information
- **Note for macOS**: You must install the Xcode Command Line Tools to ensure `PyAudio` can build correctly.
- **Note for Windows**: `PyAudio` should install directly from pip without additional dependencies.

## Model Configuration (Ollama):
- The application uses the `Ollama` model for language processing.
- Ensure Ollama is installed by visiting [Ollama](https://ollama.com).
- You can configure the model by modifying the `process_text_with_llm` function in the `pyttsx3_main.py` file.

## Audio Recognition Timeout

- By default, the audio recognizer in the application times out after 2 seconds of silence. If you want to extend this timeout, you can adjust it in the pyttsx3_main.py file under the capture_speech() function. Look for the following line:
   ```bash
   audio = recognizer.listen(source, timeout=2, phrase_time_limit=15)
   ```
- If you would like to increase the timeout, modify the listen method’s timeout parameter to your desired value (default is set to 5 seconds).