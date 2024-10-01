
# Installation Instructions for the Speech AI Application

## Step 1: Install OLlAMA (Ollama)

OLLAMA is the model serving platform you will use to interact with large language models (like Llama 3.2). To install OLLAMA, follow these steps:

1. Visit the [OLLAMA official website](https://ollama.com) to download the latest version for your operating system (either macOS or Windows).
2. Follow the instructions on the OLLAMA website for installation.
3. Verify the installation by opening your terminal or command prompt and running:

   ```bash
   ollama --version
   ```

   This will confirm that OLLAMA has been installed successfully.

## Step 2: Install Python and Dependencies

1. Ensure you have Python 3.11 installed on your machine. You can download Python from the official Python website: [https://www.python.org/downloads/](https://www.python.org/downloads/).
   
2. Download the project files (including the `requirements.txt` and `setup.py` provided in the setup files).

3. Open a terminal (macOS) or command prompt (Windows) and navigate to the directory where the project files are located.

4. Install dependencies using the following command:

   ```bash
   pip install -r requirements.txt
   ```

## Step 3: Configure the Llama Model in Code

By default, the application uses the Llama 3.2 model served by OLLAMA. If you want to change the model, follow these steps:

1. Open the file `pyttsx3_model_integration.py`.
2. Find the line that specifies the model used in the `process_text_with_llm` function:

   ```python
   command = f"ollama run llama3.2:1b  "{prompt_text}""
   ```

3. Change `"llama3.2:1b"` to the desired model. For example, to use a different model version, you might replace it with `"llama3.1:8b"`.

When you run the code for the first time, OLLAMA will automatically download the model if it hasn’t been downloaded yet. The first-time execution may be slower because the model is being downloaded. Subsequent executions will be faster as the model is cached locally.

## Step 4: Run the Application

To start using the application, open your terminal or command prompt and run:

```bash
python pyttsx3_main.py
```

This will start the speech recognition process and use the OLLAMA-served model for processing.
