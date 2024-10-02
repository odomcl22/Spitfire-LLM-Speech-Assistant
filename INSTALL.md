# Installation Instructions for Spitfire LMM Speech Assistant

## Prerequisites:
1. Install **Python 3.11** (if not already installed).
    - You can download Python 3.11 from the official [Python website](https://www.python.org/downloads/release/python-311/).
    - **For macOS/Linux:** Use the following command to verify if Python 3.11 is installed and available:
      ```bash
      python3.11 --version
      ```
    - **For Windows:** Ensure Python 3.11 is added to the `PATH` during installation.

2. Ensure `pip` is installed:
   - `pip` comes pre-installed with Python 3.11. To verify:
      ```bash
      python3.11 -m pip --version
      ```

## Creating a Virtual Environment (Optional but Recommended)
1. Create a virtual environment using Python 3.11:
   ```bash
   python3.11 -m venv spitfire_env
   ```

2. Activate the virtual environment:
   - **macOS/Linux:**
     ```bash
     source spitfire_env/bin/activate
     ```
   - **Windows:**
     ```bash
     .\spitfire_env\Scriptsctivate
     ```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/Spitfire-LMM-Speech-Assistant.git
   cd Spitfire-LMM-Speech-Assistant
   ```

2. **Install dependencies**:
   - Ensure you are in the Python 3.11 environment (e.g., virtual environment).
   - Run the following command to install all required dependencies from `requirements.txt`:
     ```bash
     python3.11 -m pip install -r requirements.txt
     ```

3. **Ensure additional dependencies (Whisper, pyttsx3, etc.) are installed**:
   - **For Whisper and Torch**:
     ```bash
     python3.11 -m pip install whisper torch
     ```
   - **For macOS-specific dependencies (e.g., pyobjc)**:
     ```bash
     python3.11 -m pip install pyobjc
     ```

## OLLAMA Installation (for using LLaMA models)
1. Install OLLAMA from the official website: [OLLAMA Download](https://ollama.com/download).
2. After installation, ensure the `ollama` command-line tool is available:
   ```bash
   ollama --version
   ```

## Running the App

1. **Run the main script**:
   - Once all dependencies are installed, run the application using the following command:
     ```bash
     python3.11 pyttsx3_main.py
     ```

2. **Model download and usage**:
   - The first time you run the app, it may take time as models are downloaded (e.g., LLaMA).
   - You can modify the LLaMA model being used by updating the model call in the `pyttsx3_model_integration.py` file. Look for the line:
     ```python
     command = f"ollama run llama3.2:1b  "{prompt_text}""
     ```
     You can change the model by replacing `llama3.2:1b` with the appropriate model ID.
   
## Notes
- **Whisper** will handle real-time audio processing, and **pyttsx3** will handle text-to-speech conversion.
- On first use, the app may be slower while models are downloaded, but subsequent use will be faster.
