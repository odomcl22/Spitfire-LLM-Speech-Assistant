
# Installation Guide for Spitfire LMM Speech Assistant

## Prerequisites
1. Python 3.11 (or higher) must be installed. You can download it from [Python Official Website](https://www.python.org/downloads/release/python-311/).
2. Ensure that you have `pip` installed.
3. `Setuptools` is required for packaging and installation purposes.

## Installation on macOS and Windows:
### Step 1: Clone the Repository
Clone the repository to your local machine using:
```bash
git clone https://github.com/your-username/Spitfire-LMM-Speech-Assistant.git
```

### Step 2: Install `setuptools`
Before running the `setup.py`, install `setuptools`:
```bash
pip install setuptools
```

### Step 3: Install Dependencies
Navigate to the project folder and install the dependencies:
```bash
pip install -r requirements.txt
python setup.py install
```

### Step 4: Install Ollama for LLM Support
- Install Ollama via the official website: [https://ollama.com](https://ollama.com)
- By default, this project uses LLaMA 3.2 model. You can modify the model by editing `pyttsx3_main.py`. Look for the section:
```python
# Example usage in pyttsx3_main.py
command = f"ollama run llama3.2:1b  "{prompt_text}""
```
You can change `"llama3.2:1b"` to a different version/model if desired.

### Step 5: Running the Application
After the installation, run the app using:
```bash
python pyttsx3_main.py
```

This will launch the application, with speech-to-text and text-to-speech functionalities.
