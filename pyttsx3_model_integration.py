import subprocess

def process_text_with_llm(prompt_text, emotion=None):
    try:
        # Incorporate the emotion into the prompt subtly, without the model explicitly referring to it
        if emotion:
            prompt_text = f"{prompt_text}\n\nThe user is feeling {emotion}, take this into account when crafting your response, but do not directly acknowledge the emotion or mention it. Keep responses concise unless more detail is requested."

        # Command to run the model
        command = f"ollama run llama3.2:1b \"{prompt_text}\""
        result = subprocess.run(command, shell=True, capture_output=True, text=True)

        if result.returncode != 0:
            raise RuntimeError(f"Error running Ollama: {result.stderr.strip()}")
        
        return result.stdout.strip()

    except Exception as e:
        print(f"An error occurred: {e}")
        return f"An error occurred: {e}"