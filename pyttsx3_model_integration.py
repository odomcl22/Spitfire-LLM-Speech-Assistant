# import subprocess

# def process_text_with_llm(text):
#     # Using subprocess to call Ollama's CLI and process text with Llama 3.1 8B
#     result = subprocess.run(
#         ["ollama", "run", "llama3.1:8b", "--prompt", text],
#         capture_output=True,
#         text=True
#     )
#     return result.stdout.strip()

# #the below code works. 
# import subprocess

# def process_text_with_llm(prompt_text):
#     try:
#         # Command without the --model flag
#         command = f"ollama run llama3.2:1b  \"{prompt_text}\""
#         # Debugging print removed to avoid duplicate output
#         result = subprocess.run(command, shell=True, capture_output=True, text=True)
#         if result.returncode != 0:
#             raise RuntimeError(f"Error running Ollama: {result.stderr.strip()}")
#         return result.stdout.strip()
#     except Exception as e:
#         print(f"An error occurred: {e}")
#         return f"An error occurred: {e}"

import subprocess

def process_text_with_llm(prompt_text):
    try:
        command = f"ollama run llama3.2:1b  \"{prompt_text}\""
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode != 0:
            raise RuntimeError(f"Error running Ollama: {result.stderr.strip()}")
        return result.stdout.strip()
    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"